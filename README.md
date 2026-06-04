# 💰 SplitBill Pro

> **Full-Stack Expense Splitting SaaS** — Create groups, add expenses, track who owes whom.


---

## 📌 Overview

**SplitBill Pro** is a full-stack web application that simplifies shared expense management. Whether you're splitting rent, travel costs, or dinner bills, SplitBill Pro keeps everyone on the same page with real-time balance tracking and automatic split calculations.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **User Authentication** | JWT-based registration & login with bcrypt password hashing |
| 👥 **Group Management** | Create expense groups and add members by email |
| 💸 **Expense Tracking** | Add expenses with automatic equal-split calculation |
| 📊 **Real-time Balances** | Instantly see who owes whom across each group |
| 🗑️ **Delete Groups** | Remove groups with a confirmation modal to prevent accidents |
| 🎨 **Modern UI** | Responsive single-page app with gradient backgrounds |

---

## 🛠️ Tech Stack

### Backend
- **Python 3.12** — Core language
- **FastAPI** — High-performance async web framework
- **SQLAlchemy** — ORM for database operations
- **SQLite / PostgreSQL** — Database (local / production)
- **JWT** — Token-based authentication
- **bcrypt** — Secure password hashing

### Frontend
- **HTML5** — Semantic markup
- **CSS3** — Flexbox, Grid, animations
- **Vanilla JavaScript** — No frameworks, pure JS

### DevOps
- **Render** — Backend hosting
- **Vercel** — Frontend hosting
- **GitHub** — Version control

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/vigneshsai52/splitbill-pro.git
cd splitbill-pro
```

**2. Create and activate a virtual environment**
```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the backend server**
```bash
python -m uvicorn app.main:app --reload
```

**5. Open the frontend**
```
Open frontend/index.html in your browser
OR use the Live Server extension in VS Code
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./splitbill.db
SECRET_KEY=your-secret-key-here
```

> ⚠️ **Never commit your `.env` file.** Add it to `.gitignore`

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Login (OAuth2 form-based) |
| `GET` | `/auth/me` | Get current authenticated user |

### Groups
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/groups/` | Create a new group |
| `GET` | `/groups/` | Get all groups for current user |
| `DELETE` | `/groups/{id}` | Delete a group by ID |

### Expenses
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/expenses/` | Create a new expense |
| `GET` | `/expenses/group/{id}` | Get all expenses in a group |
| `GET` | `/expenses/balances/{id}` | Get balance summary for a group |

📖 Full interactive docs: [https://splitbill-pro-1.onrender.com/docs](https://splitbill-pro-1.onrender.com/docs)

---

## 🌐 Deployment

| Service | URL | Status |
|---------|-----|--------|
| Frontend | [splitbill-pro-two.vercel.app](https://splitbill-pro-two.vercel.app/) | ✅ Live |
| Backend | [splitbill-pro-1.onrender.com](https://splitbill-pro-1.onrender.com) | ✅ Live |
| Swagger | [splitbill-pro-1.onrender.com/docs](https://splitbill-pro-1.onrender.com/docs) | ✅ Live |

---

## 🗂️ Project Structure

```
splitbill-pro/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic request/response schemas
│   ├── auth.py              # Authentication logic (JWT + bcrypt)
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Auth routes
│       ├── groups.py        # Group routes
│       └── expenses.py      # Expense routes
├── frontend/
│   └── index.html           # Single-page frontend application
├── .env                     # Environment variables (not committed)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🧠 What I Learned

- **JWT Authentication** — Built secure token-based auth with bcrypt hashing and expiry handling
- **Database Relationships** — Used SQLAlchemy many-to-many relationships for group members
- **CORS Issues** — Configured CORS middleware properly for cross-origin Render ↔ Vercel communication
- **OAuth2 Login** — Implemented `OAuth2PasswordRequestForm` for FastAPI-native login
- **Real-time Balances** — Computed balances on-the-fly from raw expense splits (no separate balance table needed)
- **Full-Stack Deployment** — Deployed backend on Render (with PostgreSQL) and frontend on Vercel independently

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
git checkout -b feature/YourFeature
git commit -m "Add YourFeature"
git push origin feature/YourFeature
```

Then open a **Pull Request** on GitHub.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Vignesh Sai**


---

<div align="center">
  Built with ❤️ using <strong>FastAPI</strong> & <strong>Vanilla JS</strong><br/>
  ⭐ Star this repo if you found it helpful!
</div>
