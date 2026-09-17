'''
this file tests the flow of how the ingestion of the raw file turning to parquert and updating the snapshot pointer whenever update are there in the files.
'''
from .storage import snapshot ,manifest,writer

#writing raw json as the input.

records = [
    {"name":"Hari","age":21},
    {"name":"Vamshi","age":20}
]
# we use the records_to_parquet fucntion in the writer.py to ingest the raw json and convert it into a .parquet file

parquet_file = writer.records_to_parquet(records)

# once we have the .parquet file we send it to the manifest.py to update the manifest by adding the parquet file

# but how do we get the current manifest_path

current_manifest_path = snapshot.get_current_snapshot()
new_manifest_path = manifest.create_updated_manifest(
    current_manifest_path=current_manifest_path,
    new_parquet_path=parquet_file,
    new_manifest_path="data/snapshots/manifest_002.json"
)
# now we have the new manifest path, that we need to serve to snapshot.py

snapshot.commit_snapshot(new_manifest_path)
