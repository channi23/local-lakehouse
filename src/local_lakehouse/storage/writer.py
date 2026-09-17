'''
okay, JSON file contains keys and values which is the same structure of a python dictionary, assuming i am getting the input data as a python dictionary
i need to make the K,V data-structure into a table format using PyArrow library.
'''

'''
getting into the work here, first i would like convert the key-value paired .json input into a  strcutured table by using pyarrow
'''

import pyarrow as pa
import pyarrow.parquet as pq

#function should return the parquet file which is created, basicall the path
def records_to_parquet(records):
    table = pa.Table.from_pylist(records)
    #table is now column oriented internally
    pq.write_table(
        table,
        "data.parquet",
        compression="snappy"
    )
    return "data.parquet"



