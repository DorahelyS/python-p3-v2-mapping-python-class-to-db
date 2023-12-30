'''

Introduction
Object-Relational Mapping (ORM) is a programming technique that provides a mapping between an object-oriented 
data model and a relational database model.

We equate a Python class with a database table and an instance of a class (i.e. an object) to a table row.

Why map classes to tables? To persist data stored in Python objects efficiently and in an organized manner, 
we need to map a Python class to a database table by writing methods that encapsulate table creation and deletion, 
along with methods to save, update, delete, and query object state within a database table.

As an example, assume we want to create a database to store data about the departments and employees within a 
company. It is convention to pluralize the name of the class to create the name of the table. Therefore, 
the Department class maps to the "departments" table and the Employee class maps to the "employees" table.

create_table (cls)	None	Create a table to store data about instances of a class.
drop_table (cls)	None	Drop the table.
save (self)	        None	Save the attributes of an object as a new table row.
create(cls, attributes)	an object that is an instance of cls	Create a new object that is an instance of cls and save its attributes as a new table row.
update(self)	    None	Update an object's corresponding table row
delete (self)	    None	Delete the table row for the specified object

Mapping a Department class to a database table:
*** Remember to run pipenv install to install the dependencies and pipenv shell to enter your virtual environment 
before running your code.

The starter code for the Department class is in lib/department.py. The Department class is defined with attributes for id, name and location.

The __init__ method assigns a default value of None to the id attribute. The id will be assigned a value after 
saving the object attributes as a new table row (id will be assigned the value of the new row's primary key). 
We'll see how to assign the id attribute later in the lesson.

Creating the Database
First we need to create our database, then we will create a "departments" table.

Whose responsibility is it to create the database? It is not the responsibility of the Department class. 
Remember, classes are mapped to tables inside a database, not to the database as a whole. Accordingly, 
you'll see that Python packages have modules solely for configuration of reused (constant) variables. 
We'll put the database initialization in the file lib/__init__.py.

CONN is a constant equal to a hash that contains a connection to the database.
CURSOR is a constant that allows us to interact with the database and execute SQL statements.

We can access the constants within lib/department.py by adding the import statement before the class declaration:
from __init__ import CURSOR, CONN

Creating (and dropping) the "departments" table:
