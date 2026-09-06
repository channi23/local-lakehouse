# What happens in the system?

first thing we have is input data which is in JSON form, as we are getting the data in json form , i will be also having json-schema for it to
validate the json, the validated json is still considered as raw data, so it does needs to go through transformation: where the system will be
tranforming the raw and validated json into .parquet format with the meta data of each .parquet file. the system also do take snapshots or each
version of change in data, the data in the .parquet as queries using duckDB.

## So i will be rewriting this reasoning in four stages:

i will be having four steps:
- Data Contract
- Data processing
- Data storage
- Query / Consumption

1. Data Contract: (Raw Input is JSON so we will use JSON Schema: validation, store the validation reports with the input data)

2. Data processing: (once we have the validated RAW JSON, we try to transform  the semi-structured JSON to strctured which can used for .parquert)

3. Data storage: (we store the raw JSON irrepective of the validation output, store parquet files with there metadata files and also the catalog metadata file too, also version snapshots)

4. Query/Consumption: (we use duckDB for querying the stored data)



