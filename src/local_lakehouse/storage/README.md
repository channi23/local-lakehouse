# What exactly contains in this directory?

The Storage Package here i define contains scripts that help in different applications, one that i am currently(initially) implementing is
Snapshot-DB concept :

Which is implemented using these script files:

writer.py -> creates .parquet files
manifest.py -> creates/reads manifest(the .json file(basically like metadata, tells which parquet file contains in which snapshots))
snapshot.py -> manages snapshot verison/commits

(this is initail,basic impplementation of the concept)

