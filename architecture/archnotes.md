# Architecture Notes/Ideas
Some general notes about architectural ideas.

### Asynchronous vs Synchronous Slaves (for failovers)
- Synchronous = better guarantee that data is not lost
- Synchronous = no scalability as databases have to be in same data center or super high latency


### Hard Dependencies
- will reduce availability

### AWS Failing
- have Disaster Recovery environments (Linode, etc.)
- cross-DC systems

### Multi-Tenancy
- prone to hard failures

### Security
- getting hacked = losing customers

### Multiple DNS Providers
- prevents impact of DDoS attacks on one specific DNS provider (see DDoS on Dyn in 2016 - <https://dyn.com/blog/dyn-analysis-summary-of-friday-october-21-attack/>)

### Database Pipelines
- **Kafka > Cassandra**