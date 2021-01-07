# Dataset schema in OpenSAFELY

This notebook provides information about the data schema for tables in the OpenSAFELY-TPP database. 


### Data sources
Data sources are listed below, with the table name in the database given in brackets:

* Positive or negative SARS-CoV2 test, first tests only, from SGSS (`SGSS_Positive` and `SGSS_Negative`)
* Positive or negative SARS-CoV2 test, any test, from SGSS (`SGSS_AllTests_Positive` and `SGSS_AllTests_Negative`)
* A&E attendance, from SUS Emergency Care Data (`EC`)
* Hospital admission, from SUS Admitted Patient Care Data (`APCS`)
* Covid-related ICU admission, from ICNARC (`ICNARC`)
* Covid-related in-hospital death, from CPNS (`CPNS`)
* All-cause registered deaths, from ONS (`ONS_Deaths`)

Additional data sources include:
* High cost drugs (`HighCostDrugs`)
* Unique Property Reference Number, used for deriving household variables (`UPRN`)
* Master Patient Index (`MPI`)


```python
## Import libraries

%load_ext autoreload
%autoreload 2

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
```


```python
# get server credentials from environ.txt

dbconn = os.environ.get('FULL_DATABASE_URL', None).strip('"')
```


```python
## Import schema data and date

with closing_connection(dbconn) as cnxn:
    table_schema = pd.read_sql("""select * from OpenSAFELYSchemaInformation""", cnxn)

today = date.today()
```

### Notebook run date


```python
display(Markdown(f"""This notebook was run on {today.strftime('%Y-%m-%d')}.  The information below reflects the state of the OpenSAFELY-TPP as at this date."""))
```


This notebook was run on 2021-01-06.  The information below reflects the state of the OpenSAFELY-TPP as at this date.


## Table Schema

The schema for each table contains the following info:

* `ColumnName`, the column name.
* `ColumnType`, the column type, for example integer, numeric or date &mdash; see [here](https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql) for more details.
* `Precision`, `Scale` and `MaxLength` &mdash; see [here](https://docs.microsoft.com/en-us/sql/t-sql/data-types/precision-scale-and-length-transact-sql) for more details.
* `IsNullable`, are Null values accepted.


```python
display(table_schema[['TableName']].drop_duplicates().reset_index(drop=True).style.set_properties(**{'text-align': 'left'}))
```


<style  type="text/css" >
    #T_41f2fde0_5000_11eb_bb06_0242ac110004row0_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row1_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row2_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row3_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row4_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row5_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row6_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row7_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row8_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row9_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row10_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row11_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row12_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row13_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row14_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row15_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row16_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row17_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row18_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row19_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row20_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row21_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row22_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row23_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row24_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row25_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row26_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row27_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row28_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row29_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row30_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row31_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row32_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row33_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row34_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row35_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row36_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row37_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row38_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row39_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row40_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row41_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row42_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row43_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row44_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row45_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row46_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row47_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row48_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row49_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row50_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row51_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row52_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row53_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row54_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row55_col0 {
            text-align:  left;
        }    #T_41f2fde0_5000_11eb_bb06_0242ac110004row56_col0 {
            text-align:  left;
        }</style><table id="T_41f2fde0_5000_11eb_bb06_0242ac110004" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >TableName</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row0_col0" class="data row0 col0" >ECDS</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row1_col0" class="data row1 col0" >ECDS_EC_Diagnoses</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row2_col0" class="data row2 col0" >HighCostDrugs</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row3_col0" class="data row3 col0" >Household</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row4_col0" class="data row4 col0" >HouseholdMember</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row5_col0" class="data row5 col0" >ICD10Dictionary</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row6_col0" class="data row6 col0" >ICNARC</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row7_col0" class="data row7 col0" >LatestBuildTime</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row8" class="row_heading level0 row8" >8</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row8_col0" class="data row8 col0" >MedicationDictionary</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row9" class="row_heading level0 row9" >9</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row9_col0" class="data row9 col0" >MedicationIssue</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row10" class="row_heading level0 row10" >10</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row10_col0" class="data row10 col0" >MedicationRepeat</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row11" class="row_heading level0 row11" >11</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row11_col0" class="data row11 col0" >MedicationSensitivity</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row12" class="row_heading level0 row12" >12</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row12_col0" class="data row12 col0" >MPI</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row13" class="row_heading level0 row13" >13</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row13_col0" class="data row13 col0" >MSOA_PopulationEstimates_2019</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row14" class="row_heading level0 row14" >14</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row14_col0" class="data row14 col0" >ONS_Deaths</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row15" class="row_heading level0 row15" >15</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row15_col0" class="data row15 col0" >ONS_Deaths_TmpJRC</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row16" class="row_heading level0 row16" >16</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row16_col0" class="data row16 col0" >ONS_Deaths_Without_Final_Codes_20200612</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row17" class="row_heading level0 row17" >17</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row17_col0" class="data row17 col0" >OPA</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row18" class="row_heading level0 row18" >18</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row18_col0" class="data row18 col0" >OPA_Cost</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row19" class="row_heading level0 row19" >19</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row19_col0" class="data row19 col0" >OPA_Diag</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row20" class="row_heading level0 row20" >20</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row20_col0" class="data row20 col0" >OPA_Proc</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row21" class="row_heading level0 row21" >21</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row21_col0" class="data row21 col0" >OpenSAFELYSchemaInformation</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row22" class="row_heading level0 row22" >22</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row22_col0" class="data row22 col0" >Organisation</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row23" class="row_heading level0 row23" >23</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row23_col0" class="data row23 col0" >Patient</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row24" class="row_heading level0 row24" >24</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row24_col0" class="data row24 col0" >PatientAddress</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row25" class="row_heading level0 row25" >25</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row25_col0" class="data row25 col0" >PotentialCareHomeAddress</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row26" class="row_heading level0 row26" >26</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row26_col0" class="data row26 col0" >QOFClusterReference</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row27" class="row_heading level0 row27" >27</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row27_col0" class="data row27 col0" >RegistrationHistory</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row28" class="row_heading level0 row28" >28</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row28_col0" class="data row28 col0" >SGSS_AllTests_Negative</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row29" class="row_heading level0 row29" >29</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row29_col0" class="data row29 col0" >SGSS_AllTests_Positive</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row30" class="row_heading level0 row30" >30</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row30_col0" class="data row30 col0" >SGSS_Negative</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row31" class="row_heading level0 row31" >31</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row31_col0" class="data row31 col0" >SGSS_Positive</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row32" class="row_heading level0 row32" >32</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row32_col0" class="data row32 col0" >UnitDictionary</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row33" class="row_heading level0 row33" >33</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row33_col0" class="data row33 col0" >UPRN</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row34" class="row_heading level0 row34" >34</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row34_col0" class="data row34 col0" >Vaccination</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row35" class="row_heading level0 row35" >35</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row35_col0" class="data row35 col0" >VaccinationReference</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row36" class="row_heading level0 row36" >36</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row36_col0" class="data row36 col0" >APCS</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row37" class="row_heading level0 row37" >37</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row37_col0" class="data row37 col0" >APCS_Cost</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row38" class="row_heading level0 row38" >38</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row38_col0" class="data row38 col0" >APCS_Der</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row39" class="row_heading level0 row39" >39</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row39_col0" class="data row39 col0" >Appointment</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row40" class="row_heading level0 row40" >40</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row40_col0" class="data row40 col0" >BuildInfo</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row41" class="row_heading level0 row41" >41</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row41_col0" class="data row41 col0" >CodeCountIndicator</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row42" class="row_heading level0 row42" >42</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row42_col0" class="data row42 col0" >CodedEvent</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row43" class="row_heading level0 row43" >43</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row43_col0" class="data row43 col0" >CodedEventRange</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row44" class="row_heading level0 row44" >44</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row44_col0" class="data row44 col0" >Consultation</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row45" class="row_heading level0 row45" >45</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row45_col0" class="data row45 col0" >CPNS</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row46" class="row_heading level0 row46" >46</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row46_col0" class="data row46 col0" >CTV3Dictionary</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row47" class="row_heading level0 row47" >47</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row47_col0" class="data row47 col0" >CTV3Hierarchy</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row48" class="row_heading level0 row48" >48</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row48_col0" class="data row48 col0" >DataDictionary</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row49" class="row_heading level0 row49" >49</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row49_col0" class="data row49 col0" >EC</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row50" class="row_heading level0 row50" >50</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row50_col0" class="data row50 col0" >EC_AlcoholDrugInvolvement</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row51" class="row_heading level0 row51" >51</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row51_col0" class="data row51 col0" >EC_Comorbidities</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row52" class="row_heading level0 row52" >52</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row52_col0" class="data row52 col0" >EC_Cost</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row53" class="row_heading level0 row53" >53</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row53_col0" class="data row53 col0" >EC_Diagnosis</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row54" class="row_heading level0 row54" >54</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row54_col0" class="data row54 col0" >EC_Investigation</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row55" class="row_heading level0 row55" >55</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row55_col0" class="data row55 col0" >EC_PatientMentalHealth</td>
            </tr>
            <tr>
                        <th id="T_41f2fde0_5000_11eb_bb06_0242ac110004level0_row56" class="row_heading level0 row56" >56</th>
                        <td id="T_41f2fde0_5000_11eb_bb06_0242ac110004row56_col0" class="data row56 col0" >EC_Treatment</td>
            </tr>
    </tbody></table>



```python
pd.set_option('display.max_columns', None)

for table in table_schema['TableName'].unique():
    tab = table_schema[table_schema['TableName']==table]
    tab = tab.drop(columns=['TableName', 'ColumnId', 'CollationName'])
    display(Markdown(f"## {table}"))
    display(tab.set_index('ColumnName'))
```


## ECDS



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Der_Number_EC_Treatment</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_AEA_Diagnosis_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_EC_Diagnosis_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_AEA_Investigation_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_EC_Investigation_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Der_Number_AEA_Diagnosis</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Number_EC_Diagnosis</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Number_AEA_Investigation</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Number_EC_Investigation</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Number_AEA_Treatment</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>143 rows × 5 columns</p>
</div>



## ECDS_EC_Diagnoses



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Ordinal</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>DiagnosisCode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## HighCostDrugs



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>FinancialMonth</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FinancialYear</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PersonAge</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PersonGender</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ActivityTreatmentFunctionCode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TherapeuticIndicationCode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HighCostTariffExcludedDrugCode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DrugName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RouteOfAdministration</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DrugStrength</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DrugVolume</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DrugPackSize</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DrugQuanitityOrWeightProportion</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>UnitOfMeasurement</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DispensingRoute</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HomeDeliveryCharge</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TotalCost</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DerivedSNOMEDFromName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DerivedVTM</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DerivedVTMName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Household



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Household_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MSOA</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>NFA_Unknown</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>CareHome</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Prison</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HouseholdSize</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MatchesUprnCount</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MixedSoftwareHousehold</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TppPercentage</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## HouseholdMember



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HouseholdMember_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Household_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## ICD10Dictionary



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CodeDescription</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ParentCode</th>
      <td>char</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ParentCodeDescription</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## ICNARC



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ICNARC_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>CalculatedAge</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EstimatedAge</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>OriginalHospitalAdmissionDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HospitalAdmissionDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>IcuAdmissionDateTime</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TransferredIn</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>OriginalIcuAdmissionDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HighestLevelFirst24Hours</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Ventilator</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AP2score</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>IMscore</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>pfratio</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>BasicDays_RespiratorySupport</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AdvancedDays_RespiratorySupport</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>BasicDays_CardiovascularSupport</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AdvancedDays_CardiovascularSupport</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SupportDays_Renal</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SupportDays_Neurological</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SupportDays_Gastrointestinal</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SupportDays_Dermatological</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SupportDays_Liver</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Level3days</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Level2days</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Level1days</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Level0days</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HRG</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>yusurv</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>IcuDischargeDateTime</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TransferredOut</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ausurv</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>UltimateIcuDischargeDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>yhsurv</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HospitalDischargeDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ahsurv</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>UltimateHospitalDischargeDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateOfDeath</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## LatestBuildTime



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>DtLatestBuild</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## MedicationDictionary



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MultilexDrug_ID</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ProductId</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>FullName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RootName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PackDescription</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Form</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Strength</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>CompanyName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DMD_ID</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## MedicationIssue



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Consultation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MedicationIssue_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>RepeatMedication_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MultilexDrug_ID</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Dose</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Quantity</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>StartDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EndDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MedicationStatus</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ConsultationDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## MedicationRepeat



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Consultation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MedicationRepeat_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MultilexDrug_ID</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Dose</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Quantity</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>StartDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EndDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MedicationStatus</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ConsultationDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## MedicationSensitivity



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Consultation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MedicationSensitivity_ID</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MultilexDrug_ID</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>StartDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>FormulationSpecific</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Ended</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ConsultationDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## MPI



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Gender</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Birth_Month</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Death_Month</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RP_of_Death</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateFrom</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateTo</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Date_Added</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Original_Posting_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Data_Source</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Latest_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Care_Home_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ServiceType</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Living_Alone_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Living_with_young_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Living_with_elderly_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>OS_Property_Classification</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Rural_Urban_Classification</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>property_type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>private_outdoor_space</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>private_outdoor_space_area</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Pseudo_uprn</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Pseudo_parent_uprn</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## MSOA_PopulationEstimates_2019



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSOA_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>LA_Code_2019</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>LA_Code_2020</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Age_All</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Age_0</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Age_86</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Age_87</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Age_88</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Age_89</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Age_90_Plus</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>95 rows × 5 columns</p>
</div>



## ONS_Deaths



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ageinyrs</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>dod</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10UND</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>icd10u</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10001</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10002</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10003</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10004</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10005</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10006</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10007</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10008</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10009</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10010</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10011</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10012</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10013</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10014</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10015</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN1</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN2</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN3</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN4</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN5</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN6</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN7</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN8</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN9</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## ONS_Deaths_TmpJRC



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ageinyrs</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>dod</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10UND</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>icd10u</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10001</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10002</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10003</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10004</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10005</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10006</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10007</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10008</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10009</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10010</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10011</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10012</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10013</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10014</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10015</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN1</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN2</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN3</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN4</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN5</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN6</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN7</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN8</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN9</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>FIC10MEN15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## ONS_Deaths_Without_Final_Codes_20200612



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ageinyrs</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>dod</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>icd10u</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10001</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10002</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10003</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10004</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10005</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10006</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10007</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10008</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10009</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10010</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10011</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10012</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10013</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10014</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ICD10015</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## OPA



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>OPA_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Ethnic_Category</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Main_Specialty_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Treatment_Function_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MultiProf_Ind_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Administrative_Category</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Attendance_Status</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>First_Attendance</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Medical_Staff_Type_Seeing_Patient</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Operation_Status</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Outcome_of_Attendance</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Appointment_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Consultation_Medium_Used</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Activity_Location_Type_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Clinic_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Provider_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Provider_Code_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Priority_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>OPA_Referral_Source</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Referral_Request_Received_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HRG_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HRG_Version_No</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Activity_Month</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Financial_Year</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## OPA_Cost



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>OPA_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Tariff_OPP</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Tariff_Total_Payment</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Grand_Total_Payment_MFF</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## OPA_Diag



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>OPA_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Primary_Diagnosis_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Secondary_Diagnosis_Code_1</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Primary_Diagnosis_Code_Read</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Secondary_Diagnosis_Code_1_Read</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## OPA_Proc



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>OPA_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Primary_Procedure_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Procedure_Code_2</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Primary_Procedure_Code_Read</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Procedure_Code_2_Read</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## OpenSAFELYSchemaInformation



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>TableName</th>
      <td>nvarchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>TableName</th>
      <td>sysname</td>
      <td>256</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ColumnId</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ColumnName</th>
      <td>nvarchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ColumnName</th>
      <td>sysname</td>
      <td>256</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ColumnType</th>
      <td>nvarchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ColumnType</th>
      <td>sysname</td>
      <td>256</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MaxLength</th>
      <td>smallint</td>
      <td>2</td>
      <td>5</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Precision</th>
      <td>tinyint</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Scale</th>
      <td>tinyint</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CollationName</th>
      <td>nvarchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>CollationName</th>
      <td>sysname</td>
      <td>256</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>IsNullable</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Organisation



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Organisation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>GoLiveDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>STPCode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MSOACode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Region</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## Patient



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>DateOfBirth</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateOfDeath</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Sex</th>
      <td>char</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## PatientAddress



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>PatientAddress_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>StartDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EndDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>AddressType</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>RuralUrbanClassificationCode</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ImdRankRounded</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MSOACode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## PotentialCareHomeAddress



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>PatientAddress_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>LocationRequiresNursing</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>LocationDoesNotRequireNursing</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## QOFClusterReference



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ClusterType</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ClusterName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CTV3Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## RegistrationHistory



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Registration_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Organisation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>StartDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EndDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## SGSS_AllTests_Negative



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Organism_Species_Name</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Specimen_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Report_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Age_In_Years</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Patient_Sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>County_Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PostCode_Source</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Symptomatic</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Ethnic_Category_Desc</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Pillar</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>LFT_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## SGSS_AllTests_Positive



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Organism_Species_Name</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Specimen_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Report_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Age_In_Years</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Patient_Sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>County_Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PostCode_Source</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Symptomatic</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Ethnic_Category_Desc</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Pillar</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>LFT_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## SGSS_Negative



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Organism_Species_Name</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Earliest_Specimen_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Report_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Age_In_Years</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Patient_Sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>County_Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PostCode_Source</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## SGSS_Positive



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Organism_Species_Name</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Earliest_Specimen_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Report_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Age_In_Years</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Patient_Sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>County_Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PostCode_Source</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lab_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## UnitDictionary



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>UnitDictionary_ID</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CTV3Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Units</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Minimum</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Maximum</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>LowerNormalBound</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>UpperNormalBound</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>DecimalPlaces</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## UPRN



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Pseudo_uprn</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Pseudo_parent_uprn</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>class</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Total_Pop</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_0to4</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_5to9</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_10to14</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_15to19</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_20to24</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_25to29</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_30to34</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_40to44</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_45to49</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_50to54</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_55to59</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_60to64</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_65to69</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_70to74</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_75to79</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_80to84</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>_85Plus</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Care_Home_Flag</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ServiceType</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Rural_Urban_Classification</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>property_type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>private_outdoor_space</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>private_outdoor_space_area</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Vaccination



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Vaccination_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>VaccinationDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>VaccinationName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>VaccinationName_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>VaccinationSchedulePart</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## VaccinationReference



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>VaccinationName_ID</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>VaccinationName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>VaccinationContent</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## APCS



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>APCS_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Carer_Support_Indicator</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Ethnic_Group</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Administrative_Category</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Patient_Classification</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Admission_Method</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Discharge_Destination</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Discharge_Method</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Source_of_Admission</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Admission_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Discharge_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Provider_Org_Code_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Duration_of_Elective_Wait</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_Core_HRG_SUS</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_HRG_Version_No_SUS</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Hospital_Spell_Duration</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Spell_LoS</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Diagnosis_Count</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Procedure_Count</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Diagnosis_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Procedure_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Admit_Treatment_Function_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Dischg_Treatment_Function_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Pseudo_Patient_Pathway_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Activity_Month</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Financial_Year</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## APCS_Cost



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>APCS_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Tariff_Initial_Amount</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Tariff_Total_Payment</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Grand_Total_Payment_MFF</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## APCS_Der



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>APCS_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Spell_Dominant_Procedure</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_Primary_Diagnosis</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_Secondary_Diagnosis</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_Treatment_Function_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_Main_Specialty_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_LoS</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_PbR_CC_Day</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_PbR_Rehab_Days</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_RE30_Indicator</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Spell_RE30_Admit_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Appointment



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Appointment_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Organisation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>BookedDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>StartDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EndDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ArrivedDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>SeenDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>FinishedDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Status</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## BuildInfo



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BuildDesc</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>BuildDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>BuildNumber</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## CodeCountIndicator



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CTV3Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CodeCountIndicator</th>
      <td>float</td>
      <td>8</td>
      <td>53</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## CodedEvent



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Consultation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CodedEvent_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CTV3Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>NumericValue</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ConsultationDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## CodedEventRange



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CodedEvent_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>CodedEventRange_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Consultation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>LowerBound</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>UpperBound</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Comparator</th>
      <td>tinyint</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## Consultation



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Consultation_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Registration_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ConsultationDate</th>
      <td>datetime</td>
      <td>8</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## CPNS



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Id</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>LocationOfDeath</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Sex</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateOfAdmission</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateOfSwabbed</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateOfResult</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RelativesAware</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TravelHistory</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RegionCode</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RegionName</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>OrganisationTypeLot</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RegionApproved</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>RegionalApprovedDate</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>NationalApproved</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>NationalApprovedDate</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PreExistingCondition</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DateOfDeath</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>HadLearningDisability</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>ReceivedTreatmentForMentalHealth</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Ethnic_Category_Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Latest_SUS_Attendance_Date_For_Ethnicity</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Source_Dataset_For_Ethnicty</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>snapDate</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>OnDeathCertificateNotice</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>CovidTestResult</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>NHSworker</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>PreExistingConditionList</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>LearningDisabilityType</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TransferredFromLearningDisabilityAutismSetting</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>TransferredFromAMentalHealthSetting</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DetainedUnderMHAct</th>
      <td>bit</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## CTV3Dictionary



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CTV3Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## CTV3Hierarchy



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ParentCTV3Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ParentCTV3Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ChildCTV3Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ChildCTV3Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ChildToParentDistance</th>
      <td>int</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## DataDictionary



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Table</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Description</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## EC



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Ethnic_Category</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Department_Type</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Arrival_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Arrival_Time</th>
      <td>time</td>
      <td>5</td>
      <td>16</td>
      <td>7</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Arrival_Mode_SNOMED_CT</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_AttendanceCategory</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Attendance_Source_SNOMED_CT</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Decision_To_Admit_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Decision_To_Admit_Treatment_Function_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Discharge_Destination_SNOMED_CT</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Chief_Complaint_SNOMED_CT</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Injury_Date</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SUS_HRG_Code</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SUS_Tariff</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>SUS_Final_Price</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DQ_Chief_Complaint_Expected</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DQ_Chief_Complaint_Completed</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DQ_Chief_Complaint_Valid</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DQ_Primary_Diagnosis_Expected</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DQ_Primary_Diagnosis_Completed</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>DQ_Primary_Diagnosis_Valid</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_EC_Diagnosis_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_EC_Investigation_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_EC_Treatment_All</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Activity_Month</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Der_Financial_Year</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## EC_AlcoholDrugInvolvement



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Alcohol_Drug_Involvement_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Is_Code_Approved_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## EC_Comorbidities



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Comorbidity_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_16</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_17</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_18</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_19</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_20</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_21</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_22</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_23</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Comorbidity_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## EC_Cost



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Tariff_Total_Payment</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Grand_Total_Payment_MFF</th>
      <td>real</td>
      <td>4</td>
      <td>24</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## EC_Diagnosis



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Chief_Complaint_SNOMED_CT</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_16</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_17</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_18</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_19</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_20</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_21</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_22</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_23</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Diagnosis_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_16</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_17</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_18</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_19</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_20</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_21</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_22</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_23</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Diagnosis_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## EC_Investigation



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Investigation_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_16</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_17</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_18</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_19</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_20</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_21</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_22</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_23</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Investigation_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_16</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_17</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_18</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_19</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_20</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_21</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_22</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_23</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Investigation_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## EC_PatientMentalHealth



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>MH_Classification_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MH_Start_Date_01</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MH_Expiry_Date_01</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>MH_Start_Date_23</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MH_Expiry_Date_23</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MH_Classification_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MH_Start_Date_24</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>MH_Expiry_Date_24</th>
      <td>date</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>74 rows × 5 columns</p>
</div>



## EC_Treatment



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ColumnType</th>
      <th>MaxLength</th>
      <th>Precision</th>
      <th>Scale</th>
      <th>IsNullable</th>
    </tr>
    <tr>
      <th>ColumnName</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Ident</th>
      <td>bigint</td>
      <td>8</td>
      <td>19</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>EC_Treatment_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_16</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_17</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_18</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_19</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_20</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_21</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_22</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_23</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>EC_Treatment_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_01</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_02</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_03</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_04</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_05</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_06</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_07</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_08</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_09</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_10</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_11</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_12</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_13</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_14</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_15</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_16</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_17</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_18</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_19</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_20</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_21</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_22</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_23</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>AEA_Treatment_24</th>
      <td>varchar</td>
      <td>8000</td>
      <td>0</td>
      <td>0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



```python

```
