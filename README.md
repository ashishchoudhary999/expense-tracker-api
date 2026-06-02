# 💰 Expense Tracker API

A production-ready REST API for tracking personal expenses, built with **FastAPI** and **PostgreSQL**. Features secure JWT authentication, user-specific data isolation, and analytical reporting endpoints — fully deployed to the cloud.

🔗 **Live API Docs:** [https://expense-tracker-api-llc1.onrender.com/docs](https://expense-tracker-api-llc1.onrender.com/docs)

> ⚠️ Hosted on a free tier — the first request after inactivity may take ~50 seconds to wake the server.

---

## ✨ Features

- 🔐 **JWT Authentication** — secure register & login with hashed passwords (bcrypt)
- 👤 **User-Specific Data** — every user can only access their own expenses
- 📝 **Full CRUD** — create, read, update, and delete expenses
- 📊 **Analytical Reports**
  - Total spending grouped by **category**
  - Total spending grouped by **month**
  - Overall **stats** (highest, average, count, most-used category)
- 🛡️ **Protected Routes** — endpoints secured via OAuth2 bearer tokens
- ☁️ **Cloud Deployed** — running on Render with a managed Neon PostgreSQL database

---

## 🛠️ Tech Stack

| Layer            | Technology                          |
|------------------|-------------------------------------|
| Language         | Python                              |
| Framework        | FastAPI                             |
| Database         | PostgreSQL (Neon)                   |
| ORM              | SQLAlchemy                          |
| Validation       | Pydantic                            |
| Auth             | JWT (python-jose), Passlib + Bcrypt |
| Server           | Uvicorn                             |
| Deployment       | Render                              |

---

## 📚 API Endpoints

### Authentication
| Method | Endpoint           | Description                  | Auth Required |
|--------|--------------------|------------------------------|---------------|
| POST   | `/users/register`  | Register a new user          | No            |
| POST   | `/users/login`     | Login and receive JWT token  | No            |

### Expenses
| Method | Endpoint                  | Description              | Auth Required |
|--------|---------------------------|-------------------------|---------------|
| POST   | `/expense`                | Create an expense       | Yes           |
| GET    | `/expenses`               | List all your expenses  | Yes           |
| GET    | `/expense/{id}`           | Get a single expense    | Yes           |
| PUT    | `/expense/{id}`           | Update an expense       | Yes           |
| DELETE | `/expense/{id}`           | Delete an expense       | Yes           |

### Reports
| Method | Endpoint                          | Description                          | Auth Required |
|--------|-----------------------------------|--------------------------------------|---------------|
| GET    | `/expenses/summary/category`      | Total spending per category          | Yes           |
| GET    | `/expenses/summary/monthly`       | Total spending per month             | Yes           |
| GET    | `/expenses/stats`                 | Highest, average, count, top category| Yes           |

---

## 🏗️ Project Structure

```
expense_tracker_api/
├── app/
│   ├── main.py          # FastAPI app entry point + Swagger auth config
│   ├── database.py      # DB engine, session, connection pooling
│   ├── models.py        # SQLAlchemy models (User, Expense)
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── crud.py          # Database operations & reporting queries
│   ├── auth.py          # Password hashing, JWT, current-user dependency
│   └── routes/
│       ├── user.py      # Register & login endpoints
│       └── expense.py   # Expense CRUD + reporting endpoints
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/ashishchoudhary999/expense-tracker-api.git
cd expense-tracker-api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql://user:password@host/dbname
SECRET_KEY=your_long_random_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> 💡 Generate a strong `SECRET_KEY` with:
> ```bash
> python -c "import secrets; print(secrets.token_hex(32))"
> ```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

Visit **http://127.0.0.1:8000/docs** to explore the interactive API.

---

## 🔑 Environment Variables

| Variable                      | Description                          |
|-------------------------------|--------------------------------------|
| `DATABASE_URL`                | Full PostgreSQL connection string    |
| `SECRET_KEY`                  | Secret used to sign JWT tokens       |
| `ALGORITHM`                   | JWT signing algorithm (e.g. `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime in minutes            |

---

## 🧠 How Authentication Works

1. User **registers** → password is hashed with bcrypt and stored (never in plain text).
2. User **logs in** → server verifies the password and returns a signed **JWT access token**.
3. For protected routes, the client sends the token in the header:
   `Authorization: Bearer <token>`
4. The server **decodes and verifies** the token, identifies the user, and returns only that user's data.

---

## 👤 Author

**Ashish Choudhary**
GitHub: [@ashishchoudhary999](https://github.com/ashishchoudhary999)

---

## 📄 License

This project is licensed under the **MIT License** — see below.

```
MIT License

Copyright (c) 2026 Ashish Choudhary

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
