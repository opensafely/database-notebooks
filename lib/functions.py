import pandas as pd
import numpy as np
import pyodbc
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib.patches as patches
from contextlib import contextmanager



# use this to open connection
@contextmanager
def closing_connection_old(server, database, username, password):
    dsn = (
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + server
        + ";DATABASE="
        + database
        + ";UID="
        + username
        + ";PWD="
        + password
    )
    cnxn = pyodbc.connect(dsn)
    try:
        yield cnxn
    finally:
        cnxn.close()

# use this to open connection
@contextmanager
def closing_connection(dbconn): 
    cnxn = pyodbc.connect(dbconn)
    try: 
        yield cnxn 
    finally: 
        cnxn.close()


def eventcountdf(event_dates, date_range, rule='D', popadjust=False):
    # to calculate the daily count for events recorded in a dataframe
    # where event_dates is a dataframe of date columns
    # set popadjust = 1000, say, to report counts per 1000 population
    
    # initialise dataset
    counts = date_range
    
    
    for col in event_dates:

        # Creates a series of the entry date of the index event
        in_date = event_dates.loc[:, col]

        counts = counts.join(
            pd.DataFrame(in_date, columns=[col]).groupby(col)[col].count().to_frame()
        )

    # convert nan to zero
    counts = counts.fillna(0)
    
    if rule != "D":
        counts = counts.resample(rule).sum()
    
    if popadjust is not False:
        pop = event_dates.shape[0]
        poppern = pop/popadjust
        counts = counts.transform(lambda x: x/poppern)
    
    return(counts)

    


def eventcountseries(event_dates, date_range, rule='D', popadjust=False):
    # to calculate the daily count for events recorded in a series
    # where event_dates is a series
    # set popadjust = 1000, say, to report counts per 1000 population
    
    pop = event_dates.size
    
    counts = event_dates.value_counts().reindex(date_range.index, fill_value=0)
    
    
    if rule != "D":
        counts = counts.resample(rule).sum()
    
    if popadjust is not False:
        pop = event_dates.size
        poppern= pop/popadjust
        counts = counts.transform(lambda x: x/poppern)
    
    return(counts)





def firsteventcountdf(event_dates, date_range,  rule='D', popadjust=False):

    # to calculate the daily number of events in a dataframe, taking first events only
    # subsequent events are excluded, for instance if a patient is admitted to ICU twice only the first admission is observed). 

    # initialise datasets
    counts = date_range

    for idx, col in enumerate(event_dates):

        # Creates a series of the entry date of the index event
        in_date = event_dates.iloc[:, idx]

        counts = counts.join(
            pd.DataFrame(in_date, columns=[col]).groupby(col)[col].count().to_frame()
        )

    # convert nan to zero
    counts = counts.fillna(0)

    if rule != "D":
        counts = counts.resample(rule).sum()
    
    if popadjust is not False:
        pop = event_dates.shape[0]
        poppern= pop/popadjust
        counts = counts.transform(lambda x: x/poppern)

    return(counts)



def eventcountcmldf(event_dates, date_range, rule = "D", popadjust=False):

    # this plots the total number of people on each date who:
    # have experienced a covid-related event on or before that date;
    # have not experienced a 'more advanced' event on or before that date
    # "more advanced" is based on the order Series appear in the event_dates data.frame

    # interpreted as "the most advanced covid-related event you have experienced to date" summed over all patients in the dataset.

    # initialise datasets
    in_counts = date_range
    out_counts = date_range
   

    for idx, col in enumerate(event_dates):

        # Creates a series of the entry date of the index event
        in_date = event_dates.iloc[:, idx]

        # Creates a series of the earliest event date occurring _after_ the index event
        if idx == len(event_dates.columns) - 1:
            # or maximum date + 1 day if on the final column
            out_date = [max(date_range.index) + pd.Timedelta(1, unit='D')] * len(event_dates.index)
        else:
            out_date = np.where(np.isnan(in_date), np.datetime64('NaT'), event_dates.iloc[:, idx + 1:].min(axis=1))

        # removes in dates and out dates where a more advanced event occurs at an earlier date (ie ignores the later event if it is "less advanced")
        in_date2 = np.where(((in_date > out_date) | np.isnan(in_date)), np.datetime64('NaT'), in_date)
        out_date2 = np.where(((in_date > out_date) | np.isnan(in_date)), np.datetime64('NaT'), out_date)

        in_counts = in_counts.join(
            pd.DataFrame(in_date2, columns=[col]).groupby(col)[col].count().to_frame()
        )
        out_counts = out_counts.join(
            pd.DataFrame(out_date2, columns=[col]).groupby(col)[col].count().to_frame()
        )

    # convert nan to zero
    in_counts = in_counts.fillna(0)
    out_counts = out_counts.fillna(0)

    # count total entries/exits up to index date
    in_counts_cml = in_counts.cumsum()
    out_counts_cml = out_counts.cumsum()

    # subtract numbers out from numbers in
    net_counts = in_counts_cml.add(-out_counts_cml)

    if rule != "D":
        net_counts = net_counts.resample(rule).sum()
    
    if popadjust is not False:
        pop = event_dates.shape[0]
        poppern = pop/popadjust
        net_counts = net_counts.transform(lambda x: x/poppern)

    # remove "_date" from column name for better legend
    #net_counts.columns = net_counts.columns.str.replace("_date", "", regex=False)

    return(net_counts)





def eventcounts_strata_plot(df, date_range, date_cols, var, panelheight=5, panelwidth=5, gridcols=1, rule = "D", popadjust=False):
    #### Plot event counts stratified by a categorical variable

    event_dates = df.filter(items=date_cols + [var])
    strata = sorted(event_dates[var].unique())
    
    gridrows = int(np.ceil(len(strata)/gridcols))
    
    figsize = (panelwidth*gridcols, panelheight*gridrows)

    fig, axs = plt.subplots(gridrows, gridcols, figsize=figsize, sharey='all', sharex='all')
     
    for i, strat in enumerate(strata):
          
        col=i % gridcols
        row=np.floor(i / gridcols).astype("int")
            
        events_cat = (event_dates[event_dates[var] == strat]).drop(var, 1)
        count_cat = eventcountdf(events_cat, date_range, rule = "D", popadjust=popadjust)
       
       # axs[row, col] = plt.subplot(gs[i % gridrows, np.floor(i / gridrows).astype("int")])
        for l in date_cols:
            axs[row, col].plot(count_cat.index, count_cat[l], label=l)
            
        axs[row, col].set_title(strat, size=12)
        #axs[row, col].set_ylim([0, maxy])  # set ymax across all subplots 
        if i==0:
            axs[row, col].legend(loc='upper left')
    
    for n, ax in enumerate(axs.flatten()):
        
        ax.xaxis.set_tick_params(labelbottom=True, labelrotation=70)
        ax.yaxis.set_tick_params(labelleft=True)
        if n>=len(strata):
            ax.axis('off')
    plt.subplots_adjust(wspace = 0.2,hspace = 0.5)
    plt.show()


def cmlinc_strata_plot(df, date_cols, var, date_range, panelheight=5, panelwidth=5, gridcols=1, popadjust=False):
    
    #### Plot cumulative event counts stratified by a categorical variable

    event_dates = df.filter(items=date_cols + [var])
    strata = sorted(event_dates[var].unique())
    
    gridrows = int(np.ceil(len(strata)/gridcols))
    
    figsize = (panelwidth*gridcols, panelheight*gridrows)

    
    fig = plt.figure(figsize=figsize)
    gs = gridspec.GridSpec(gridrows,gridcols)  # grid layout for subplots (rows, cols)

        
    if popadjust==False:
        maxy = event_dates.filter(items=date_cols).notna().any(axis=1).groupby(event_dates[var]).sum().max() * 1.05
    else:
        maxy = event_dates.filter(items=date_cols).notna().any(axis=1).groupby(event_dates[var]).mean().max() * 1.05 * popadjust
        
    for i, strat in enumerate(strata):
        events_cat = (event_dates[event_dates[var] == strat]).drop(var, 1)            
        cmlinc_cat = eventcountcmldf(events_cat, date_range, popadjust=popadjust)
       
        ax = plt.subplot(gs[np.floor(i / gridcols).astype("int"), i % gridcols])
        ax.stackplot(cmlinc_cat.index, cmlinc_cat.to_numpy().transpose(), labels=cmlinc_cat.columns)
        ax.set_title(strat, size=12)
        ax.set_ylim([0, maxy])  # set ymax across all subplots 
        ax.xaxis.set_tick_params(labelrotation=70)
        if i==0:
            ax.legend(loc='upper left')

    plt.subplots_adjust(wspace = 0.2,hspace = 0.5)
    plt.show()


    
def plotcounts(date_range, events=None, title="", lookback=30):
    # This function plots event counts over time both overall and for the last X days up to the most recent extracted event.  
    startdate = date_range.index.min()
    enddate = date_range.index.max()
    lastdate = events.max()
    
    
    startdatestring = startdate.strftime('%Y-%m-%d')
    enddatestring = enddate.strftime('%Y-%m-%d')
    lastdatestring = lastdate.strftime('%Y-%m-%d')
        
    def createcounts(date_range, events, lastdate):
        counts = eventcountseries(events, date_range, rule="D")

        lastdaterecent = lastdate - pd.to_timedelta(lookback, unit="D")
        
        lastcounts = counts.loc[(counts.index >= lastdaterecent) & (counts.index <= lastdate)]

        redact = (lastcounts <6) & (lastcounts>0)
        lastcounts = lastcounts.where(~redact, 2.5) #redact small numbers
        
        return counts, lastcounts, redact
    
    counts, lastcounts, redact = createcounts(date_range, events, lastdate)
    
   # xlimlower = mdates.date2num(lastcounts.index[0]+pd.DateOffset(days=-1))
   # xlimupper = mdates.date2num(lastcounts.index[-1]+pd.DateOffset(days=+1))
    
    fig, axs = plt.subplots(1, 2, figsize=(15,5))
    
    axs[1].plot(lastcounts.index, lastcounts, label=events.name, marker='o', markersize=5, color='darkblue', zorder=1)
    axs[1].plot(lastcounts[redact].index, lastcounts[redact], 'o', linestyle = 'None', color='tomato', zorder=2)
    axs[1].xaxis.set_tick_params(labelrotation=70)
    axs[1].xaxis.set_major_locator(ticker.MultipleLocator(2))
    axs[1].set_ylim(bottom=0)
    xlimlower1, xlimupper1 = axs[1].get_xlim()
    ylimlower1, ylimupper1 = axs[1].get_ylim()
    axs[1].set_ylim(bottom=0, top=max([ylimupper1, 7]))
    axs[1].add_patch(patches.Rectangle((xlimlower1,0) ,xlimupper1-xlimlower1, 5.5, linewidth=1,edgecolor='none',facecolor='mistyrose', zorder=3))
    axs[1].grid(True)
    axs[1].spines["left"].set_visible(False)
    axs[1].spines["right"].set_visible(False)
    axs[1].set_title(f"""\n\n Last {str(lookback)} days up to {lastdatestring}""")
    axs[1].set_facecolor('floralwhite')
    
    axs[0].plot(counts.index, counts, color='darkblue', zorder=2)
    axs[0].set_ylabel('event counts')
    axs[0].xaxis.set_tick_params(labelrotation=70)
    axs[0].set_ylim(bottom=0)
    axs[0].grid(True)
    axs[0].spines["left"].set_visible(False)
    axs[0].spines["right"].set_visible(False)
    axs[0].set_title(f"""\n\n From {startdatestring} to {enddatestring}""")
    xlimlower0, xlimupper0 = axs[0].get_xlim()
    ylimlower0, ylimupper0 = axs[0].get_ylim()
    axs[0].add_patch(patches.Rectangle((xlimlower1,0), xlimupper1-xlimlower1, max([ylimupper1, 7]), linewidth=1, edgecolor='orange', linestyle='--', facecolor='floralwhite', zorder=1))
    axs[0].add_patch(patches.Rectangle((xlimlower0,0) ,xlimupper0-xlimlower0, 5, linewidth=1, edgecolor='none', facecolor='mistyrose', zorder=3))
    
    axs[0].annotate("Disclaimer: counts are based on raw event data and should not be used for clinical or epidemiological inference", xy=(0, -0.1), xycords='axes fraction', ha='left')
    
    
    plt.subplots_adjust(top=0.8, wspace = 0.2, hspace = 0.9)
    plt.tight_layout()
    fig.suptitle("\n"+title, y=1, fontsize='x-large')
    plt.show()

    
def plotcounts_history(events=None, title=""):
    # This function plots event counts over time both overall and for the last X days up to the most recent extracted event.  
    startdate = events.min()
    enddate = events.max()
    
    date_range = pd.DataFrame(
        index = pd.date_range(start=startdate, end=enddate, freq="D")
    )
    
    startdatestring = startdate.strftime('%Y-%m-%d')
    enddatestring = enddate.strftime('%Y-%m-%d')
    

    counts_day = eventcountseries(events, date_range, rule="D")
    redact_day = (counts_day <6) & (counts_day>0)
    counts_day = counts_day.where(~redact_day, 2.5) #redact small numbers
    
    counts_week = eventcountseries(events, date_range, rule="W")
    redact_week = (counts_week <6) & (counts_week>0)
    counts_week = counts_week.where(~redact_week, 2.5) #redact small numbers
       
    fig, axs = plt.subplots(1, 1, figsize=(15,5))
    
    axs.plot(counts_day.index, counts_day, color='darkblue', zorder=2)
    axs.plot(counts_week.index - pd.DateOffset(3), counts_week/7, color='orange', zorder=3)
    axs.set_ylabel('event counts')
    axs.xaxis.set_tick_params(labelrotation=70)
    axs.set_ylim(bottom=0)
    axs.grid(True)
    axs.spines["left"].set_visible(False)
    axs.spines["right"].set_visible(False)
    axs.set_title(f"""\n\n From {startdatestring} to {enddatestring}""")
    xlimlower, xlimupper = axs.get_xlim()
    ylimlower, ylimupper = axs.get_ylim()
    axs.add_patch(patches.Rectangle((xlimlower,0) ,xlimupper-xlimlower, 5, linewidth=1, edgecolor='none', facecolor='mistyrose', zorder=4))
       
    plt.subplots_adjust(top=0.8, wspace = 0.2, hspace = 0.9)
    plt.tight_layout()
    fig.suptitle("\n"+title, y=1, fontsize='x-large')
    plt.show()