# FastAPI + AWS(RDS) C.R.U.D.

## Welcome to my personal project using Python

### Technologies involved:
- FastAPI
- SQLAlchemy
- Pydantic
- RDS (Relational Data Storage from AWS Cloud)
- PostgreSQL

---

## 🎯 Goal

Create a simple CRUD project using FastAPI (for the API) and AWS (for Cloud / Database).

---

## 🛠️ Table Creation Process

To set up the database schema, I followed these steps:

1. Installed **SQLAlchemy** and **python-dotenv** in my virtual environment.
2. Created a `.env` file with my secret credentials (AWS RDS access).
3. Built the `database_model.py` file containing the SQLAlchemy model for the table.
4. Created the `setup_db.py` file to configure the SQLAlchemy engine and trigger table creation.

Then, using **IPython3**(or IPython, depends on the Python version on your machine):

```bash
cd temp/
ipython
```

Within IPython3:

```python
import database_model, setup_db
setup_db.create_table()
```

This process initializes the table on the PostgreSQL database hosted via AWS RDS.

---

## 📁 Application Structure (`server/app`)

The main application logic resides in the `server/app` folder. Here's a breakdown of its components:

- `database.py`: Sets up the database connection using environment variables. Defines the SQLAlchemy engine and session factory, and provides the `get_db` dependency for route-level DB access.
- `database_model.py`: Defines the `Alunos` model class, representing the students table with fields such as `id`, `matricula`, `nome`, `idade`, `sexo`, and `email`.
- `schemas.py`: Defines Pydantic models for data validation. Includes `AlunoBase` (shared fields), `AlunoCreate` (for input), and `Aluno` (for output).
- `services.py`: Contains core CRUD logic for handling students: create, read, update, and delete operations.
- `main.py`: Entry point of the FastAPI application. Exposes REST endpoints (`/alunos/`) and uses dependency injection for database sessions.
- `test_server.py`: A minimal test server that returns a `Hello, World!` message — useful for verifying server setup.
- `requirements.txt`: Contains all necessary Python dependencies for the application.

---

## 🚀 Installation & Execution

Follow the steps below to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/lucasoriental/fastapi_crud.git
cd fastapi_crud
```

### 2. Create and activate a virtual environment

- **Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

- **Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a `.env` file in the root of the project and fill it with your AWS RDS credentials:

```env
DB_AWS_HOST=your_host
DB_AWS_PORT=5432
DB_AWS_NAME=your_database
DB_AWS_USER=your_username
DB_AWS_PASSWORD=your_password
```

### 5. Run the application

```bash
uvicorn server.app.main:app --reload
```

- Access the API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API Docs (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 Available Endpoints

- `GET /alunos/` – Retrieve all students
- `GET /alunos/{id}` – Retrieve a student by ID
- `POST /alunos/` – Add a new student
- `PUT /alunos/{id}` – Update an existing student
- `DELETE /alunos/{id}` – Delete a student

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
