# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown]
# # Latest coverage for data sources in OpenSAFELY
#
# This notebook provides information about data import dates and recent activity in the OpenSAFELY-TPP database. 
#
# This notebook can be used to:
#
# * Obtain the most recent import date for each data source
# * Obtain the frequency of historical import dates for each external data source
# * Obtain the most recent event date for each data source amongst TPP patients
# * Understand event activity amongst TPP patients from 1 February 2020 onwards
# * Estimate the latest reliable date for events recorded in each data source, i.e., a cut-off beyond which the data may be incomplete.
#
# This notebook can not be used to:
#
# * Obtain future import dates
# * Understand patient activity over time at a national level
# * Estimate the earliest reliable date for events recorded in each data source
#
# -


# ### Data sources
# Data sources are listed below, with the table name in the database given in brackets:
#
# * Positive or negative SARS-CoV2 test, first tests only, from SGSS (`SGSS_Positive` and `SGSS_Negative`)
# * Positive or negative SARS-CoV2 test, any test, from SGSS (`SGSS_AllTests_Positive` and `SGSS_AllTests_Negative`)
# * A&E attendance, from SUS Emergency Care Data (`EC`)
# * Hospital admission, from SUS Admitted Patient Care Data (`APCS`)
# * Covid-related ICU admission, from ICNARC (`ICNARC`)
# * Covid-related in-hospital death, from CPNS (`CPNS`)
# * All-cause registered deaths, from ONS (`ONS_Deaths`)
#
# For primary care data in SystmOne (`S1`), the delay from events occurring in reality to being available in OpenSAFELY is 2 - 9 days.
# Reducing this to one day is possible for urgent queries where necessary.
#
# Note that currently only the `SGSS_Negative` and `SGSS_Positive` tables are queriable with a study definition. 
# These tables only provide the first known test for any person (with a few unexplained exceptions), so there won't be multiple positive tests per patient in SGSS data. Data for negative test results is unreliable. 
# Support for `SGSS_AllTests_Positive` and `SGSS_AllTests_Negative` will be added later. 
#
# Additional data sources include:
# * High cost drugs (`HighCostDrugs`)
# * Unique Property Reference Number, used for deriving household variables (`UPRN`)
# * Master Patient Index (`MPI`)

# +
## Import libraries

# %load_ext autoreload
# %autoreload 2

import pyodbc
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as patches
import matplotlib.dates as mdates
from contextlib import contextmanager
from datetime import date, datetime
from IPython.display import display, Markdown

import sys
sys.path.append('../lib/')
from functions import *


# +
# get server credentials from environment variable

dbconn = os.environ.get('FULL_DATABASE_URL', None).strip('"')

# +
## Import libraries

with closing_connection(dbconn) as cnxn:
    DBbuild = pd.read_sql("""select * from LatestBuildTime""", cnxn)
    latestbuilds = pd.read_sql(
    """
        select BuildDesc as dataset, max(BuildDate) as latest_import from BuildInfo
        group by BuildDesc
    """, cnxn)
    allbuilds = pd.read_sql("""select * from BuildInfo""", cnxn)

# select start and end dates
start_date = pd.to_datetime("2020-02-01", format='%Y-%m-%d')
#start_date = pd.to_datetime("2020-02-01", format='%Y-%m-%d')
end_date = pd.to_datetime(latestbuilds['latest_import'].max(), format='%Y-%m-%d')
run_date = date.today()
run_datetime = datetime.now()
# -

# ### Notebook run date

display(Markdown(f"""This notebook was run on {run_date.strftime('%Y-%m-%d')}.  The information below reflects the state of the OpenSAFELY-TPP as at this date."""))

# ## Latest dataset import dates
# TPP create a snapshot of the primary care information captured in the SystmOne database which is processed (for example unstructured free-text is removed and other OpensAFELY-specific tables are created) before being imported into the OpenSAFELY-TPP database. 
# TPP also receive (or "ingest") external datasets from SUS, ONS, etc., which are processed and imported into OpenSAFELY-TPP. 
# Each imported dataset over-writes previously-imported data.
#
# Once a dataset has been imported, it can be queried immediately in the secure environment. 
# SystmOne data is imported approximately weekly. 
# External datasets are imported shortly after they have been received (usually within a few days). Each external dataset is sent at different times.
#
# The dates in the table below reflect when the datasets were last imported into the OpenSAFELY-TPP database.
# They do not reflect when the data were received by TPP nor when the latest events described in each dataset occurred.

latestbuilds

# The figure below shows all dataset import dates for SystmOne (`S1`) data and for external datasets, up until the date this notebook was run (the vertical black line).

# +
fig, ax = plt.subplots(figsize=(10,5))

sources = allbuilds['BuildDesc'].unique()

for source in allbuilds['BuildDesc'].unique():
    dat = allbuilds[(allbuilds['BuildDesc']==source)]
    x = dat['BuildDate']
    y = dat['BuildDesc']
    ax.scatter(x, y, marker='.', s=60)

ax.xaxis.set_tick_params(labelrotation=70)
ax.grid(True, axis='x')
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.axvline(run_datetime, color='black')
ax.set_title(f"""Latest dataset import dates as at {run_date.strftime('%Y-%m-%d')}""")
# -

# ## Event activity in external datasets
#
# Event activity (i.e., counts of patient events such as hospital admissions and deaths) is reported for each external dataset from 1 February up to the notebook run date, and for the latest 30 days of activity. 
#
# The OpenSAFELY-TPP database only includes patients recently (< 5 years) or actively registered at a GP practice using TPP's SystmOne clinical information system (roughly 40% of English residents). 
# Event activity therefore reflects these patients only.
#
# All recorded events are extracted.

# Make a dataframe with consecutive dates
date_range = pd.DataFrame(
    index = pd.date_range(start=start_date, end=end_date, freq="D")
)


# +
def datequery(table, var_table, var_df, from_date):
    query = (
      "SELECT " + var_table + " AS " + var_df
    + " FROM " + table
    + " WHERE " + var_table + " >= CONVERT(date, '" + from_date + "')"
    )
    return query

start_date_text = start_date.strftime('%Y-%m-%d')
#CodedEvent_query = datequery("CodedEvent", "ConsultationDate", "consultation_date", start_date_text)
#Appointment_query = datequery("Appointment", "SeenDate", "appointment_date", start_date_text)
APCS_query = datequery("APCS", "Admission_Date", "hosp_admission_date", start_date_text)
CPNS_query = datequery("CPNS", "DateOfDeath", "cpns_death_date", start_date_text)
EC_query = datequery("EC", "Arrival_Date", "ed_attendance_date", start_date_text)
ICNARC_query = datequery("ICNARC", "CONVERT(date, IcuAdmissionDateTime)", "icu_admission_date", start_date_text)
ONS_query = datequery("ONS_Deaths", "dod", "ons_death_date", start_date_text)
SGSS_query = datequery("""( 
         SELECT Earliest_Specimen_Date FROM SGSS_Positive 
         UNION ALL
         SELECT Earliest_Specimen_Date FROM SGSS_Negative
         )  AS a""", 
        "Earliest_Specimen_Date", "specimen_date", start_date_text)
SGSSpos_query = datequery("SGSS_Positive", "Earliest_Specimen_Date", "specimen_date", start_date_text)
SGSS_AllTests_query = datequery("""( 
         SELECT Specimen_Date FROM SGSS_AllTests_Positive 
         UNION ALL
         SELECT Specimen_Date FROM SGSS_AllTests_Negative
         )  AS a""", 
        "Specimen_Date", "specimen_date", start_date_text)
SGSSpos_AllTests_query = datequery("SGSS_AllTests_Positive", "Specimen_Date", "specimen_date", start_date_text)

with closing_connection(dbconn) as cnxn:
    #CodedEvent_df = pd.read_sql(CodedEvent_query, cnxn, parse_dates=['coded_event_date'])
    #Appointment_df = pd.read_sql(Appointment_query, cnxn, parse_dates=['appointment_date'])
    APCS_df = pd.read_sql(APCS_query, cnxn, parse_dates=['hosp_admission_date'])
    CPNS_df = pd.read_sql(CPNS_query, cnxn, parse_dates=['cpns_death_date'])
    EC_df = pd.read_sql(EC_query, cnxn, parse_dates=['ed_attendance_date'])
    ICNARC_df = pd.read_sql(ICNARC_query, cnxn, parse_dates=['icu_admission_date'])
    ONS_df = pd.read_sql(ONS_query, cnxn, parse_dates=['ons_death_date'])
    SGSS_df = pd.read_sql(SGSS_query, cnxn, parse_dates=['specimen_date'])
    SGSSpos_df = pd.read_sql(SGSSpos_query, cnxn, parse_dates=['specimen_date'])
    SGSS_all_df = pd.read_sql(SGSS_AllTests_query, cnxn, parse_dates=['specimen_date'])
    SGSSpos_all_df = pd.read_sql(SGSSpos_AllTests_query, cnxn, parse_dates=['specimen_date'])
    
# Note that CodedEvent and Appointment extracts take a long time to run.
# -

# The plots below show activity for 1 Feb 2020 onwards (left plot) and for the last 30 days up to the most recent event date (right plot). 
# Counts less than five are redacted. 
#

#plotcounts(date_range, CodedEvent_df['coded_event_date'], title="Any coded event in Primary Care, from SystmOne")
plotcounts(date_range, SGSS_df['specimen_date'], title="First-only SARS-CoV2 test, in TPP-registered patients (SGSS)")
plotcounts(date_range, SGSSpos_df['specimen_date'], title="First-only Positive SARS-CoV2 test, in TPP-registered patients (SGSS)")
plotcounts(date_range, SGSS_all_df['specimen_date'], title="Any SARS-CoV2 test, in TPP-registered patients (SGSS)")
plotcounts(date_range, SGSSpos_all_df['specimen_date'], title="Positive SARS-CoV2 test, in TPP-registered patients (SGSS)")
plotcounts(date_range, EC_df['ed_attendance_date'], title="A&E attendance, in TPP-registered patients (SUS EC)")
plotcounts(date_range, APCS_df['hosp_admission_date'], title="Hospital admission, in TPP-registered patients (SUS APCS)")
plotcounts(date_range, ICNARC_df['icu_admission_date'], title="Covid-related ICU admission, in TPP-registered patients (ICNARC)")
plotcounts(date_range, CPNS_df['cpns_death_date'], title="Covid-related in-hospital death, in TPP-registered patients (CPNS)")
plotcounts(date_range, ONS_df['ons_death_date'], title="Registered death, in TPP-registered patients (ONS)")


# +
### number of visits per patient

def recurrentquery(table, id_table, date_table, from_date, head=5):
    query = (
    f"""
    SELECT a.*, b.patients_with_exactly_X_events 
    FROM (
        SELECT X, COUNT(X) AS patients_with_at_least_X_events 
        FROM
        (
            SELECT {id_table}, ROW_NUMBER() OVER(PARTITION BY {id_table} ORDER BY {id_table})  AS X
            FROM {table}
            WHERE {date_table} >= CONVERT(date, '{from_date}')
        ) AS a
        GROUP BY X
    ) AS a
    LEFT JOIN
    (
        SELECT X, COUNT(X) AS patients_with_exactly_X_events 
        FROM
        (
            select count(*) AS X
            FROM {table}
            WHERE {date_table} >= CONVERT(date, '{from_date}')
            GROUP BY {id_table}
        ) AS a
        GROUP BY X
    ) AS b
    ON a.X=b.X
    ORDER BY a.X
    """
    )
    
    display(Markdown(f"### Repeat events in {table}"))
    display(pd.read_sql(f"select count(*) as total_events from {table} where {date_table} >= CONVERT(date, '{from_date}')", cnxn))
    display(pd.read_sql(query, cnxn).fillna(0).astype(int).head(head).set_index("X"))
    print(" ")


# -

# ## Recurrent events / repeat patient IDs
# Some datasets may have multiple rows per patient, for instance if the patient was admitted to hospital more than once. 
# Currently a study definition can return either the first event, the last event, or the count of events occurring during the period of interest. 
# The tables below count recurrent events for each dataset from 1 February onwards, up to 5 events. 
#
# `patients_with_at_least_1_events` is the number of unique patients in the dataset. 
# This is the number of events that can be returned by a study variable that takes the first event or the last event, from 1 February onwards. 

with closing_connection(dbconn) as cnxn:
    recurrentquery("APCS", "Patient_ID", "Admission_Date", start_date_text, 5)
    recurrentquery("CPNS", "Patient_ID", "DateOfDeath", start_date_text, 5)
    recurrentquery("EC", "Patient_ID", "Arrival_Date", start_date_text, 5)
    recurrentquery("ICNARC", "Patient_ID", "IcuAdmissionDateTime", start_date_text, 5)
    #recurrentquery("SGSS", "Patient_ID", "Earliest_Specimen_Date", start_date_text, 5)
    recurrentquery("SGSS_Positive", "Patient_ID", "Earliest_Specimen_Date", start_date_text, 5)
    recurrentquery("SGSS_AllTests_Positive", "Patient_ID", "Specimen_Date", start_date_text, 5)
    recurrentquery("ONS_Deaths", "Patient_ID", "dod", start_date_text, 5)

