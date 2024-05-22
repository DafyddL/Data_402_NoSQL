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
## What ae collections in Mongo?
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
   2. Secondary indexes - Users can create secondary indexes 

## What are replica sets?
## What is sharding?
## Advantages and disadvantages
## Good MongoDB Scenarios
## Bad MongoDB scenarios