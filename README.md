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
Below are examples of NoSQL schema based off of an SQL equivalent:
![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*1_soKFBUMCpC8tnGQ3Y-2A.png)
![](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*dWftD3BKJSvnhVjOrIh-aA.png)
## Scalability of NoSQL
SQL and NoSQL servers emphasize different scaling strengths due to their designs.
SQL systems typically rely on vertical scaling, which involves improving and adding resources to the same server to handle increased load. 
Horizontal scaling, typically seen in NoSQL systems, is achieved by adding more servers or nodes to a distributed system, which then helps increase capacity.

In NoSQL systems, the nodes communicate with each other and distribute the load, so adding more nodes helps increase the overall capacity of the system. 
This is a more scalable and cost-effective solution for managing a growing database and increased database traffic.

The major disadvantage of NoSQL here is that the disk space required is much higher than SQL. 
## Types of NoSQL database
There are numerous NoSQL database categories, this includes
- Key-value pair 
  - data stored as a pair, where key is like a title/reference and value is the value
- Document-oriented
  - Stores information in flexible documents that store variable amounts of data
- Column-oriented
- Graph-based
- Time series

## Disadvantages of NoSQL
- Relatively large - they are fast but relatively inefficient in disk storage
- Newer and less mature - stability can sometimes be an issue
- No Universal Query Language - You often have to interact with specific APIs, which the general expertise in specific ones is not there in the same way as SQL
- No joins
- Potential data retrieval inconsistencies
- Lack of data integrity safeguards
- Each NoSQL implementation has its own syntax

# MongoDB
## What is MongoDB?
MongoDB is an opensource NoSQL database management program. 
It is a tool that can manage, store, or retrieve document-oriented information.
## What are collections in Mongo?
MongoDB stores data records as BSON documents which are gathered in collections.
So simply a collection is **a collection of documents**.
A database stores one or more collections of documents.
## What are Documents?
MongoDB stores data records as BSON documents. 
BSON is a binary representation of JSON documents, though it contains more data types than JSON.
Documents are composed of field-and-value pairs and have structure as follows:
```
{
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}
```

Documents can hold any of the supported BSON data types, including other documents, arrays, and even arrays of documents.
```
var mydoc = {
               _id: ObjectId("5099803df3f4948bd2f98391"),
               name: { first: "Alan", last: "Turing" },
               birth: new Date('Jun 23, 1912'),
               death: new Date('Jun 07, 1954'),
               contribs: [ "Turing machine", "Turing test", "Turingery" ],
               views : NumberLong(1250000)
            }
```

## MongoDB Architecture - How does it work?
1. So firstly, a user submits a JSON document to mongo where they are installed internally as BSON. 
   1. Documents can be large, so Mongo will sometimes compress them.
2. Users then create collections to hold documents, which have some important fields.
   1. _id index - a primary key to uniquely identify the document even across machines and shards.
   2. Secondary indexes - Users can create secondary indexes which points back to the BSON document. This allows fast traversal using different fields, not just _id.



## What are replica sets?
A replica set in MongoDB is a group of mongod processes that maintain the same data set.
Replica sets provide redundancy and high availability, and are the basis for all production deployments.

## What is sharding?
Sharding is a method for distributing data across multiple machines. 
MongoDB uses sharding to support deployments with very large data sets and high throughput operations.
Essentially, **sharding is MongoDBs implementation of horizontal scaling**

MongoDB uses a shard key to distribute the collection's documents across shards. 
The shard key consists of a field or multiple fields in the documents.
## Advantages and disadvantages

### Advantages
- Schema-less
  - MongoDB doesn't require predefined schemas
- Document-oriented
  - Documents map to native data types in several programming languages
- Scalability
  - Horizontal scalability is useful for big data applications
  - Sharding lets the user distribute data across a cluster of machines
- Third-party support
  - Supports several storage engines and supports pluggable storage APIs
- Aggregation
  - Built-in aggregation functions
  - Run MapReduce code directly on the database

### Disadvantages
- Continuity
    - Automatic failover means that when the master node fails, another takes over but takes up to a minute
- Write limits
  - The single master node limits how fast data can be written, as all writes must be recorded on the master
- Data consistency
  - No full referential integrity through foreign-key restraints
- Security
  - User authentication is not enabled by default

## Good MongoDB Scenarios
### Integrating large amounts of diverse data
If you are bringing together tens or hundreds of data sources, the flexibility and power of the document model can create a single unified view in ways that other databases cannot.

Example: Healthcare Data Integration
### Describing complex data structures that evolve
Document databases allow embedding of documents to describe nested structures and easily tolerate variations in data in generations of documents.
Specialized data formats like geospatial are efficiently supported.

Example: Content Management System
### Delivering data in high-performance applications
MongoDB’s scale-out architecture can support huge numbers of transactions on humongous databases. 
Unlike other databases that either cannot support such scale or can only do so with massive amounts of engineering and additional components, MongoDB has a clear path to scalability because of the way it was designed.
MongoDB is scalable out of the box.

Example: Online Gaming Platforms
### Supporting hybrid and multi-cloud applications
MongoDB can be deployed and run on a desktop, a massive cluster of computers in a data center, or in a public cloud, either as installed software or through MongoDB Atlas, a database-as-a-service product.

Example: E-Commerce Platforms
### Supporting agile development and collaboration
Document databases put developers in charge of the data. 
Data becomes like code that is friendly to developers. 
This is far different from making developers use a strange system that requires a specialist. 
Document databases also allow the evolution of the structure of the data as needs are better understood. 
Collaboration and governance can allow one team to control one part of a document and another team to control another part.

Example: Startups and Rapid Prototyping
## Bad MongoDB Scenarios
### Complex transactions
Although mongodb supports multi-document ACID transactions, they are not as robust as RDBMS systems like PostgeSQL or MySQL.

Example: Banking systems or financial applications that require complex, multi-step transactions and stringent consistency.

### Heavy joins and Relationships
MongoDB's design does not handle complex joins and relationships between data as efficiently as RDBMS.

Example: Applications that rely heavily on complex joins, such as enterprise resource planning (ERP) systems, where multiple tables need to be joined to retrieve meaningful information.
### Highly Structured Data with Fixed Schema
MongoDB is schema-flexible, which can be a downside for applications where a rigid schema is beneficial for data integrity.

Example: Applications requiring highly structured data with fixed relationships, like accounting software.
### High Consistency and Data Integrity Requirements
While MongoDB can be configured for strong consistency, its default behavior is eventual consistency, which might not be suitable for applications needing immediate consistency.

Example: Stock trading platforms where accurate, real-time data is critical.

### Write-Heavy Applications with High Concurrency
MongoDB can face performance issues under high write loads with high concurrency, especially if the data needs to be written to a single shard or replica set.

Example: Real-time analytics applications that require frequent and simultaneous writes.

