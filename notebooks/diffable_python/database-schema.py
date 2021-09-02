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
# # Dataset schema in OpenSAFELY-TPP
#
# This notebook displays the schema of the OpenSAFELY-TPP database. It is part of the technical documentation of the OpenSAFELY platform to help users understand the underlying data and guide analyses. 
#
# The schema information is read from the `OpenSAFELYSchemaInformation` table, which is refreshed at the same time as the core `S1` SystemOne tables. There are some non-automated steps required to update the schema information when a new table is added to the database &mdash; if you can't see a table that you are expecting to see, speak to TPP.
#
# If you would like to apply to use the OpenSAFELY platform please read our [documentation](https://docs.opensafely.org/), the [principles of the platform](https://www.opensafely.org/about/), and information about our [pilot programme for onboarding external users](https://www.opensafely.org/onboarding-new-users/).
#
# If you want to see the Python code used to create this notebook, you can [view it on GitHub](https://github.com/opensafely/database-notebooks/blob/master/notebooks/database-schema.ipynb).
# -


# ### Data sources
# The core SystmOne primary care datasets are held in the `S1` tables in the OpenSAFELY-TPP database. Other externally-linked data sources are listed below, with the table name given in brackets:
#
# * All positive or negative SARS-CoV2 tests, from SGSS (`SGSS_AllTests_Positive` and `SGSS_AllTests_Negative`)
# * First-ever positive or negative SARS-CoV2 test, from SGSS (`SGSS_Positive` and `SGSS_Negative`)
# * A&E attendances, from SUS Emergency Care data (`EC`)
# * In-patient hospital admissions, from SUS Admitted Patient Care Spells data (`APCS`)
# * Out-patient hospital appointments, from SUS (`OPA`)
# * Covid-related ICU admissions, from ICNARC (`ICNARC`)
# * Covid-related in-hospital deaths, from CPNS (`CPNS`)
# * COVID-19 Infection Survey, from ONS (`ONS_CIS`)
# * All-cause registered deaths, from ONS (`ONS_Deaths`)
# * High cost drugs (`HighCostDrugs`)
# * Unique Property Reference Number, used for deriving household variables (`UPRN`)
# * Master Patient Index (`MPI`)
# * Health and Social Care Worker identification, collected at the point of vaccination (`HealthCareWorker`)
#
# Some of these tables are accompanied by additional tables with further data. For instance, `OPA` contains the core out-patient appointment event data, and is supplemented by the `OPA_Cost`, `OPA_Diag`, `OPA_Proc` tables. See the [data schema notebook](https://github.com/opensafely/database-notebooks/blob/master/notebooks/database-schema.ipynb) for more information. 

# +
## Import libraries

# %load_ext autoreload
# %autoreload 2

import pyodbc
import os
import pandas as pd
import numpy as np
from datetime import date, datetime
from IPython.display import display, Markdown

import sys
sys.path.append('../lib/')
from functions import *


# +
# get the server credentials from environ.txt

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
