setup_db and database_model are the responsible for setting up the table in the database!

To run the function and create the table, the following steps are requireds:

1. First install the ipython or ipython3;

2. Run: "ipython" or "ipython3" in the terminal (ipython3 for my case);

3. You must import the Models and the "Engine" to create the table using SQLAlchemy;
3.1: Run the following commands: "import setup_db, database_model"

4. Then, you can run the function from setup_db, by the folllowing command: "setup_db.create_table()"

5. You can check out via pgadmin4 or whatever, you will see your table created successfully!

Notes:

- SQLAlchemy is required!

- For my case, as I'm using an database from AWS, I prefered to use .env to protect my data, such as hosts, user, pass and others!

- In my case, the commands is for Postgres database environments;