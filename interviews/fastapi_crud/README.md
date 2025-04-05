# CRUD Implementation challenge

I was asked to implement a CRUD REST API in a language and framework of my choice. The challenge was to create an API that could interact with a database, handling basic operations like creating, updating, retrieving, and deleting records.
 I was asked to implement a CRUD REST API in a language and framework of my choice. 
 Here are the requirements given to me:
  - Create: Implement an idempotent method to create a new record.
  - Get By ID: Retrieve a single record based on its unique identifier.
  - Get All: Fetch all records from the database and return them as a CSV file.
  - Update: Modify an existing record by its ID.
  - Delete: Remove a record by its ID.
  
They also emphasized the importance of handling HTTP headers properly (e.g., Content-Type, Authorization), as well as managing HTTP status codes for each operation.

# Installation
```console
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
# Testing
```console
uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```
You also can check out http://127.0.0.1:8000/docs for built-in API documentation.
