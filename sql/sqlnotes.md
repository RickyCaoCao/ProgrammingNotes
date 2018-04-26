# SQL Notes

## DB Problems

Missing Index
Bad Schema
Slow Connection
Elastic Search

‘EXPLAIN Command’
  - key, ????

ISNULL is function and functions cannot be used on column fields in MySQL


Making temp tables are slow, try getting ID and then searching by ID
When are temp tables made?
	- UNION

1. Avoid temp table
2. Limit data that gets copied to table
3. Avoid TEXT columns

## Migration
- Typically can use `ALTER` in `SQL` but that can't be done in real-time
- Percona Toolkit to change schema in real-time (ptosc)
	- Ruby gem
	- only suitable for small tables

## Distributing Database Load
- load balancer = higher latency

### Primary and Foreign Keys

Foreign key is a field that points to primary key in another table
 - Primary Key Constraint - will make sure the row will have a unique id
   - if two columns are both unique id, then indexes can be duplicated but the combination of both columns must be unique

 foreign key constraint prevents destroying links between tables

