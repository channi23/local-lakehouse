'''
manifest.py is the file which handles(or basically has the functionality to decide what file (parquet) is added by the writer, so it can create a new manifest file
with the updated contents.
)
'''
import json

def create_updated_manifest(current_manifest_path, new_parquet_path,new_manifest_path):
    with open(current_manifest_path,"r") as file:
        manifest = json.load(file)
    manifest["files"].append(new_parquet_path)
    with open(new_manifest_path,"w") as file:
        json.dump(manifest,file,indent=4)
    return new_manifest_path

