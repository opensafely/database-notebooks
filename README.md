This repo contains [four notebooks](https://github.com/opensafely/database-notebooks/tree/master/notebooks) that describe elements of the OpenSAFELY-TPP database. These are run using direct queries to the database on the L2 server, rather than via study definitions. 

* [Database builds](https://github.com/opensafely/database-notebooks/blob/master/notebooks/database-builds.ipynb), describing the build dates for each OpenSAFELY-TPP dataset, and number of events per day in (most of) the linked datasets since Feb 2020 and in the 30 days preceding the last recorded event.
* [Database schema](https://github.com/opensafely/database-notebooks/blob/master/notebooks/database-schema.ipynb) schema for tables in the database &mdash; column names, types, etc.
* [Database history](https://github.com/opensafely/database-notebooks/blob/master/notebooks/database-history.ipynb) similar to database builds, but it provides events per day ever since the first known recorded event.
* [Patient characteristics](https://github.com/opensafely/database-notebooks/blob/master/notebooks/database-patient-characteristics.ipynb) basic counts for patients present in the database.

The first two notebooks are viewable on the [OpenSAFELY reports website](https://reports.opensafely.org/) under the _Databases_ tab.
