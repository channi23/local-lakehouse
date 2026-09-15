# Implementing Snapshot db concept in local-lake house

## Implementation Planning

Get Current Snapshot -> Write new Parquet file -> create new Manifest -> Add the parquert file to the new manifest.json(active files)-> Commit the new Manifest -> Advance the current snapshot pointer


