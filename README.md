# FastAPI C.R.U.D.
## Welcome to my personal project using Python
### Technologies involved: FastAPI, SQLAlchemy, Pydantic, RDS (Relational Data Storage from AWS Cloud) and PostgreSQL

**Goal**: Create a simple CRUD project using FastAPI (for the API) and AWS (for Cloud / Database).

<br>

**Steps followed to create the table**:
<ol>
  <li>Install SQLAlchemy and Dotenv in your virtual environment.</li>
  <li>Create a .env file and fill it with your secret credentials.</li>
  <li>Create the model and setup files.</li>
  <li>The database_model.py file contains the structure of the table you want to create, while the setup_db.py file contains the SQLAlchemy engine configuration to create the table.</li>
</ol>

<br>

**After these steps, I installed ipython3 (or ipython, depending on the Python version installed on your machine) and followed these steps**:
<ol>
  <li>Open the terminal and navigate to the /temp/ folder.</li>
  <li> Run the following commands:</li>
    <ul>
    <li>import database_model, setup_db</li>
    <li>setup_db.create_table() (where setup_db is the file and create_table() is the function that runs the engine to create the table).</li>
      </ul>
</ol>






