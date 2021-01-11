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
# # Dataset schema in OpenSAFELY
#
# This notebook provides information about the data schema for tables in the OpenSAFELY-TPP database. 
#
# -


# ### Data sources
# Data sources are listed below, with the table name in the database given in brackets:
#
# * Primary care records, from TPP-SystmOne (`S1`)
# * Positive or negative SARS-CoV2 test, from SGSS (`SGSS`)
# * A&E attendance, from SUS Emergency Care Data (`ECDS`)
# * Hospital admission, from SUS Admitted Patient Care Data (`APCS`)
# * Covid-related ICU admission, from ICNARC (`ICNARC`)
# * Covid-related in-hospital death, from CPNS (`CPNS`)
# * All-cause registered deaths, from ONS (`ONS_Deaths`)
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
from contextlib import contextmanager
from datetime import date, datetime
from IPython.display import display, Markdown

import sys
sys.path.append('../lib/')
from functions import *


# +
# get server credentials from environ.txt

dbconn = os.environ.get('FULL_DATABASE_URL', None).strip('"')

# +
## Import schema data and date

with closing_connection(dbconn) as cnxn:
    table_schema = pd.read_sql("""select * from OpenSAFELYSchemaInformation""", cnxn)

today = date.today()
# -

# ### Notebook run date

display(Markdown(f"""This notebook was run on {today.strftime('%Y-%m-%d')}.  The information below reflects the state of the OpenSAFELY-TPP as at this date."""))

# ## Table names by source
# The table below lists all the data tables available in the OpenSAFELY-TPP database and where the data originate from.

table_names = table_schema[['DataSource', 'TableName']].drop_duplicates().sort_values(['DataSource', 'TableName'])
table_names = table_names[table_names['DataSource']!=""]
display(table_names.reset_index(drop=True).style.set_properties(**{'text-align': 'left'}))

# ## Table Schema
#
# The schema for each table contains the following info:
#
# * `ColumnName`, the column name.
# * `ColumnType`, the column type, for example integer, numeric or date &mdash; see [SQL Server _data types_ documentation](https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql) for more details.
# * `Precision`, `Scale` and `MaxLength` &mdash; see [SQL Server _precision, scale, and length_ documentation](https://docs.microsoft.com/en-us/sql/t-sql/data-types/precision-scale-and-length-transact-sql) for more details.
# * `IsNullable`, are Null values accepted.
#
# The schema for each table is printed below.

# +
pd.set_option('display.max_columns', None)

for source in table_names['DataSource'].unique():
    
    display(Markdown("\n"))
    display(Markdown(f"### {source}"))
    
    for table in table_names.loc[table_names['DataSource']==source, 'TableName']:
        tab = table_schema[table_schema['TableName']==table]
        tab = tab.drop(columns=['TableName', 'DataSource', 'ColumnId', 'CollationName'])
        display(Markdown(f"#### {table}"))
        display(tab.set_index('ColumnName'))
