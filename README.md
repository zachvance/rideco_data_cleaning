# RideCo Data Cleaning

A script for cleaning the CSV reports downloaded from the RideCo. dashboard.

This script likely will not have much of a use case outside of my organization, as our requirements were quite specific, but I've made it available on the off chance a snippet may help someone.

## What this script does

### To the 'rides' report:

- Filters out the columns that are not required.
- Cleans the strings 'Payment Method' column to remove redundant information.
- Applies a map to the categorical values in the 'Fleet' column to group these values (via the 'FLEET_GROUPS' dictionary in config.py).
- Applies a map to the categorical values in the 'Passenger Types' column to group these values (via the 'PASSENGER_GROUPS' dictionary in config.py).
- Applies a map to the categorical values in the 'Passenger Groups' column to group these values (via the 'AMBULATORY_STATUS' dictionary in config.py).
- Filters the dataframe and resaves into five separate CSVs - 'payment_methods.csv', 'passenger_types.csv', 'statuses.csv', 'distance_in_km.csv', and     'ambulatory_statuses.csv'.

### To the 'vehicle_hours' report:

- Filters out the columns that are not required.
- Converts the time in 'Online Time (minutes)', 'Offline Time (minutes)', and Working Time (minutes)' into separate hours columns.
- Filters the dataframe and resaves into two separate CSVs - 'hours.csv', and 'accepted_ignored.csv'.

## Reasoning

The summary of data that our department wanted went beyond what was offered at face value from the reports generated from the dashboard, and required multiple steps to clean the raw data on a monthly basis - including cleaning of string variables and grouping of various categorical values - the steps of which are outlined above.

This script is meant to ease that workload and prepare the CSVs for importing into a report template XLSX file before further pivoting. The pivoting *could* be done via python with a pd.groupby (see: the commented-out lines in main.py), but by using a pivot table within Excel allows the department using the report greater descretion over filtering.
