# Architecture of local-lakehouse

## 1. Overall Flow

The system is a local analytical data platform built to understand the core ideas behind modern data platforms like Snowflake and Databricks,
also in  the process this project will be helping personally to level my DBMS conceptual and execution part including the design principles.

The overall flow is:

Raw JSON event -> Ingestion+CDC(Change Data Capture) -> Strcutured Records -> Partitioned Parquet Files -> Metadata catalog + statistics -> Query Engine(DuckDB) -> Query Optimization + Data Skipping ->  Query Execution -> Parallel / Distributed Simulation -> Lakehouse Transaction Log -> Versioned Table State

## 2. Raw Data and CDC

The input layer consists of raw JSON events.

Each event represents a data change and contains information such as the operation type, record ID, event time, and payload.

CDC events are append only and represent INSERT,UPDATE,DELETE style changes

The ingestion layer reads these events and converts the raw, semi-structured JSON into strctured records.

## 3. Metadata Catalog

The system maintains a relational metadata catalog

The catalog describes:
- schema
- tables
- columns
- partitions
- files
- permissions

The catalog itself is normalized using  relational database design principles such as functional dependencies, keys, 3NF and BCNF

The catalog stores information about the data rather than the data itself or records

## 4. Parquet Storage

Strcutured records are written into compressed Parquert files

Parquet uses columnar storage

A Parquet file contains multiple row groups, each row group is an independent chunk of columnar data.

Conceptually:

Parquet file -> row groups -> column chunks -> Encoded / compressed column data

The data is partitioned using directory layouts such as:

data/year=2026/month=09/day=02/

the catalog records the partitions and the file belongs to them

## 5. Statistics and Metadata

File-level and row-group level statistics are collected

these include:

- min value
- max value
- null count
- row count

The statistics allow the system to determine whether a file or row group can satisfy a query predicate

for example if  row group has:

max_salary = 50,000

then a predicate :

salary>90,000

cannot match the row group, so it can be skipped.

partition metadata allows partition pruning, while file and row groups allows data skipping

## 6. Query Engine

DuckDB is used as the local analytical SQL Engine

A Query conceptually passes through:

SQL -> Logical Plan -> Optimization -> Physical Operations -> Execution -> Result

Optimization can use partition pruning, predicate pushdown, projection pushdown, statistics and data skipping to reduce unnecessary work.

## 7. Parallel / Distributed Simulation

The project simulates a distributed execution environment

Records are deterministically assigned to shards using a hash of user_id

The system contains:

Coordinator -> Workers -> Shards 

The coordinator recieves the Query and delegates the work to the workers.

Each worker processes its assigned shard and produces a partial result.

The coordinator merged the partial result into a unified result.

(This is basically for understanding distributed execution and is used to understand concepts such as sharding, data locality, coordinators, workers, parallel scans, aggregation and data skew)

## 8. Lakehouse Layer

The lakelayer combines the parquet data files with a transaction log.

The transaction logs record table state changes such as:

ADD file
REMOVE file

By reading the transaction log in order, the system can determine which files are active for paticular table version

Therefore the lakehouse provides a versioned table abstraction over the underlying Parquet files

for example:

Version 1:
ADD A
ADD B

Active files : A,B

Version 2:

ADD C
REMOVE A

Active files : C,A

This allows the system to reconstruct different table versions and demonstrate time travel










