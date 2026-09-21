# This is the first result of the first execution of the pipeline.py script 

The pipeline.py script uses the defined storage helpers which are having different functionalities(writer.py,manifest.py,snapshot.py)



After i wrote the first-version code, to define basic functionalities to them, i wanted to test them using a workflow, as intended, the expectaion was to give a defined input JSON and then call the writer.py function to make it ingest it and convert the JSON data(which is basically in the Python representation for the writer.py(list of dictionaries)), then in the writer.py it uses the PyArrow Table to to convert the semi-structured data into a Table with columns, and we have the arrow table but the job of writer.py is not yet done, then the arrow-table is taken and it is serialized/encoded into Parquet file format, whose physical storage is column-oriented, so basically the writer.py at the end for now returns the file path of the created Parquet file.

Then the pipeline.py takes the parquert file path stores it, and it is also passed the current_manifest_path and the new created parquet path and the new manifest path, where it added the new parquert file in the manifest and return the new manifest path which the pipeline in here stores for the next step.

lastly the pipeline.py uses the functionality of snapshot.py to commit the changes that happened and update the pointer to the latest version.txt, here the snapshot.function is passed the new_manifest path where the new_manifest_path is written to the version.txt file, so basically the latest snapshot points to the latest manifest.json file.


SO at high-level(though it only the frist verison of it) , i have implemented a snapshot-based versioned storage which is also called technically if it gets complete,Multi-Version Concurrency Control (MVCC).

# One thing that needs to be the goal in the next version is

For now the pipeline is like baby-stage, where i need to implement a full MVCC, one thing is as the parquet path in the writer.py is hardcoded, every time a new parquet file is created it is of the same name , so because of that a new manifest will not be created, so i jsut need to solve it by versioning the parquet file too.

## Singning off <SHS>
