from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists,
)

# Important Dates
export_date="2021-01-18"

# Import Codelists
from codelists import *

# Specifiy study defeinition
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "index_date"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # extract everyone
    population=patients.all(),

    index_date = export_date,

    registered=patients.registered_as_of(
        "index_date",
        return_expectations={"incidence": 0.98},
    ),
    registered_one_year=patients.registered_with_one_practice_between(
        start_date="index_date - 1 year",
        end_date="index_date",
        return_expectations={"incidence": 0.98},
    ),
    died=patients.died_from_any_cause(
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),

    ################################################
    ###### DEMOGRAPHICS ##
    ################################################

    age=patients.age_as_of(
        "index_date",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
    
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),

    # ETHNICITY IN 6 CATEGORIES
    # ethnicity=patients.with_these_clinical_events(
    #     ethnicity_codes,
    #     returning="category",
    #     find_last_match_in_period=True,
    #     include_date_of_match=False,
    #     return_expectations={
    #         "category": {"ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5": 0.2}},
    #         "incidence": 0.75,
    #     },
    # ),

    ################################################
    ###### PRACTICE AND PATIENT ADDRESS VARIABLES ##
    ################################################
    # practice pseudo id
    practice_id=patients.registered_practice_as_of(
        "index_date", 
        returning="pseudo_id",
        return_expectations={
            "int": {"distribution": "normal", "mean": 1000, "stddev": 100},
            "incidence": 1,
        },
    ),

    # stp is an NHS administration region based on geography
    stp=patients.registered_practice_as_of(
        "index_date",
        returning="stp_code",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "STP1": 0.1,
                    "STP2": 0.1,
                    "STP3": 0.1,
                    "STP4": 0.1,
                    "STP5": 0.1,
                    "STP6": 0.1,
                    "STP7": 0.1,
                    "STP8": 0.1,
                    "STP9": 0.1,
                    "STP10": 0.1,
                }
            },
        },
    ),
    # NHS administrative region
    region=patients.registered_practice_as_of(
        "index_date",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.2,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.1,
                    "South East": 0.2,
                },
            },
        },
    ),

    # IMD - quintile
    imd=patients.categorised_as(
        {
            "0": "DEFAULT",
            "1": """index_of_multiple_deprivation >=1 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 AND index_of_multiple_deprivation < 32844""",
        },
        index_of_multiple_deprivation=patients.address_as_of(
            "index_date",
            returning="index_of_multiple_deprivation",
            round_to_nearest=100,
        ),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.05,
                    "1": 0.19,
                    "2": 0.19,
                    "3": 0.19,
                    "4": 0.19,
                    "5": 0.19,
                }
            },
        },
    ),

    # CAREHOME STATUS
    care_home_type=patients.care_home_status_as_of(
        "index_date",
        categorised_as={
            "PC": """
              IsPotentialCareHome
              AND LocationDoesNotRequireNursing='Y'
              AND LocationRequiresNursing='N'
            """,
            "PN": """
              IsPotentialCareHome
              AND LocationDoesNotRequireNursing='N'
              AND LocationRequiresNursing='Y'
            """,
            "PS": "IsPotentialCareHome",
            "": "DEFAULT",  # use empty string
        },
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"PC": 0.05, "PN": 0.05, "PS": 0.05, "": 0.85, }, },
        },
    ),
)