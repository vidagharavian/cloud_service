

<!-- ABOUT THE PROJECT -->
## About The Project
The purpose of this project is to implement a system for managing a cloud resource leasing organization. 
In a cloud resource distribution system, users can rent the resources they need for processing, storage, server hosting, etc. for a while. Depending on the capabilities of this distribution system, users can create their own resources with different configurations. The choice of users in the configuration is limited to the options provided by the system. Each resource in this system has its own operating system, RAM capacity, number of cores and CPU frequency, storage capacity and network bandwidth. The user can only create resources whose operating system is available in the system, and the amount of RAM,
CPU, storage space and bandwidth less than or equal to the capacities listed for that source in the system
### Built With

this project is fully in python. Also for data storage we have used postgreSQL and we have used PyQt5 to manage user interface.




<!-- GETTING STARTED -->
## Getting Started

After cloning the project. there few steps before running the project.,

### Prerequisites
please change configuration of  postgreSQL database  to connect properly .
this configuration is in data_base_connection.py.
* database connection
 ```
conn = psycopg2.connect(host="localhost", port = 5432, database="CloudManagement", user="postgres", password="1235698")
```
- host: your database host
- port : your postgreSQL database port.
- database : name of your database
- user : user of your database
- password : the password that you have set for your database 


<!-- USAGE EXAMPLES -->
## Usage

this project is an python-base ORM which can manage select,update,delete,insert and even complex join queries.All you need to do is to rewrite cloud_management.py to be matched with your own tables and queries that you need for your project. Also, in athentication.py you have find a user name and password athentication service which could be helpfull in any project.

some of the set ups queries like creating your tables and indexing them to search faster through their rows are available in sql directory.


