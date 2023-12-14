# Python - Object Relational Mappers.

When developing an application with a need for persistent
storage, the use of a database becomes more pronounced and necessary.

Relational databases (DBs) have found notable use in the world of web
and application development. The traditional way of interacting with
DBs involve the use of Structure Query Language (SQL) queries and stored procedures
to interact with the database. This works! And keeps working.

On a new paradigm of engineering principles, most programming languages
have implemented an object oriented approach which majorly aims to model real life
objects with codes. A typical object will contain several properties about the object,
as well as methods (which are functions that manipulate the object's properties).

What Object Relational Mapping or Object Relational Mappers (ORMs) seek to implement
is to bridge the two worlds of relational databases and objects.
This is implemented in such a way that a typical class and class definition can represent
an entity in the relational database (an entity such as a table) and an object can represent
an instance of such entity, in the case of a table, an object will represent a single record
from the table.

This particular relationship or conversion is not exactly perfect but it gives a typical
way to do all of the programming in a framework.


Thus in this directory, we will be exploring this behaviour, right from using a database 
connector to using an ORM (SQLAlchemy in this case), and then to querying and then handling sessions.

Shal, we?
