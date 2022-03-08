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
# # Characteristics of patients included in the OpenSAFELY-TPP database
#
# This notebook provides information about the characteristics of patients available in the OpenSAFELY-TPP database. 
#
# The database includes patients registered, or recently registered, at GP practices using TPP's SystmOne Clinical Information System.
#


# +
## Import libraries

# %load_ext autoreload
# %autoreload 2

import os
import pandas as pd
import numpy as np
from datetime import date, datetime
from IPython.display import display, Markdown

# -


# get data extraction date
extract_date = pd.to_datetime(os.path.getmtime("../output/input.csv"), unit='s')
# get notebook run date
run_date = date.today()

display(Markdown(f"""This notebook was run on {run_date.strftime('%Y-%m-%d')}. The information below is based on data extracted from the OpenSAFELY-TPP database on {extract_date.strftime('%Y-%m-%d')}."""))

# +
# import data

categories = [
    "sex",
    "region",
    "stp",
    "care_home_type", 
    #"ethnicity",
    "imd"
]

dfdtype={field: "category" for field in categories}

df = pd.read_csv(
    '../output/input.csv',
    dtype = dfdtype
)

for column in categories: 
    df[column] = df[column].cat.add_categories("(Missing)").fillna("(Missing)")
    
df_adult = df[df['age']>=18]
# -

# ## registered patients
#

# +
tabledata = {
    ' ':[
        
        "All available patients &mdash; see <a href='"+"https://docs.opensafely.org/en/latest/dataset-intro/#opensafely-tpp-database-builds"+"' target='_blank'>"+"inclusion criteria"+"</a>",
        'Patients actively registered at a TPP practice on '+extract_date.strftime('%Y-%m-%d'),
        'Patients actively registered at the same TPP practice for at least one year up to '+extract_date.strftime('%Y-%m-%d'),   
        'Unique practice IDs',
        'Unique STPs',
    ],
    'All ages':[
        len(df.index),
        df.registered.sum(axis=0),
        df.registered_one_year.sum(axis=0),
        df.practice_id.nunique(),
        df.stp.nunique(),        
    ],
    '18+ only':[
        len(df_adult.index),
        df_adult.registered.sum(axis=0),
        df_adult.registered_one_year.sum(axis=0),
        df_adult.practice_id.nunique(),
        df_adult.stp.nunique(),        
    ],
}

tabledata = pd.DataFrame(tabledata)

tabledata

# use styling - https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
styles = [dict(selector="th", props=[("text-align", "left")])]

tabledata.style.set_properties(subset=[" "], **{'text-align':'left', 'index':False}).set_table_styles(styles).hide_index()
