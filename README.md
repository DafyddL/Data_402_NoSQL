# NoSQL

## What is NoSQL?
NoSQL (Not only SQL) databases are non-tabular databases and store data differently than relational tables.
NoSQL databases store data in a format other than relational databases.
## Comparison of SQL and NoSQL
| SQL                              |              | NoSQL                             |
|----------------------------------|--------------|-----------------------------------|
| Relational                       | Model        | None-relational                   |
| Structured tables                | Data         | Semi-structured                   |
| Strict schema                    | Flexibility  | Dynamic schema                    |
| ACID                             | Transactions | Mostly BASE, some ACID*           |
| Strong                           | Consistency  | Eventual to Strong                |
| Consistency prioritised          | Availability | Basic Availability                |
| Vertically by upgrading hardware | Scale        | Horizontally by data partitioning |

*Atomicity, Consistency, Isolation, Durability; Basically Available, Soft state, Eventually consistent
## What languages can be used?
They can be written in any language (Java, Python, Ruby) and are mainly written as JSON, XML, etc. files
## Examples of NoSQL schema design
![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*1_soKFBUMCpC8tnGQ3Y-2A.png)
![](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*dWftD3BKJSvnhVjOrIh-aA.png)
## Scalability of NoSQL
SQL and NoSQL servers emphasize different scaling strengths due to their designs.
SQL systems typically rely on vertical scaling, which involves improving and adding resources to the same server to handle increased load. 
Horizontal scaling, typically seen in NoSQL systems, is achieved by adding more servers or nodes to a distributed system, which then helps increase capacity.

In NoSQL systems, the nodes communicate with each other and distribute the load, so adding more nodes helps increase the overall capacity of the system. 
This is a more scalable and cost-effective solution for managing a growing database and increased database traffic.
## Types of NoSQL database
There are numerous NoSQL database categories, this includes
- Key-value pair 
- Document-oriented
- Column-oriented
- Graph-based
- Time series