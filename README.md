============================================================
           💰 SplitBill Pro
     Full-Stack Expense Splitting SaaS
  Create groups, add expenses, track who owes whom
============================================================

Live App    : https://splitbill-pro-two.vercel.app
Backend API : https://splitbill-pro-1.onrender.com
API Docs    : https://splitbill-pro-1.onrender.com/docs

------------------------------------------------------------
📌 OVERVIEW
------------------------------------------------------------
SplitBill Pro is a full-stack web application that simplifies
shared expense management. Whether you're splitting rent,
travel costs, or dinner bills, SplitBill Pro keeps everyone
on the same page with real-time balance tracking and
automatic split calculations.

------------------------------------------------------------
✨ FEATURES
------------------------------------------------------------
🔐 User Authentication
   JWT-based registration & login with bcrypt password hashing

👥 Group Management
   Create expense groups and add members by email

💸 Expense Tracking
   Add expenses with automatic equal-split calculation

📊 Real-time Balances
   Instantly see who owes whom across each group

🗑️ Delete Groups
   Remove groups with a confirmation modal to prevent accidents

🎨 Modern UI
   Responsive single-page app with gradient backgrounds

------------------------------------------------------------
🛠️ TECH STACK
------------------------------------------------------------

BACKEND
-------
  Python 3.12        - Core language
  FastAPI            - High-performance async web framework
  SQLAlchemy         - ORM for database operations
  SQLite / PostgreSQL - Database (local / production)
  JWT                - Token-based authentication
  bcrypt             - Secure password hashing

FRONTEND
--------
  HTML5              - Semantic markup
  CSS3               - Flexbox, Grid, animations
  Vanilla JavaScript - No frameworks, pure JS

DEVOPS
------
  Render             - Backend hosting
  Vercel             - Frontend hosting
  GitHub             - Version control

------------------------------------------------------------
🚀 QUICK START
------------------------------------------------------------

Prerequisites:
  - Python 3.8+
  - pip

Steps:

1. Clone the repository
   git clone https://github.com/vigneshsai52/splitbill-pro.git
   cd splitbill-pro

2. Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate        (macOS/Linux)
   venv\Scripts\activate           (Windows)

3. Install dependencies
   pip install -r requirements.txt

4. Run the backend server
   python -m uvicorn app.main:app --reload

5. Open the frontend
   Open frontend/index.html in your browser
   OR use Live Server extension in VS Code

------------------------------------------------------------
⚙️ ENVIRONMENT VARIABLES
------------------------------------------------------------
Create a .env file in the project root:

   DATABASE_URL=sqlite:///./splitbill.db
   SECRET_KEY=your-secret-key-here

NOTE: Never commit your .env file. Add it to .gitignore

------------------------------------------------------------
📡 API ENDPOINTS
------------------------------------------------------------

AUTHENTICATION
  POST   /auth/register          Register a new user
  POST   /auth/login             Login (OAuth2 form-based)
  GET    /auth/me                Get current authenticated user

GROUPS
  POST   /groups/                Create a new group
  GET    /groups/                Get all groups for current user
  DELETE /groups/{id}            Delete a group by ID

EXPENSES
  POST   /expenses/              Create a new expense
  GET    /expenses/group/{id}    Get all expenses in a group
  GET    /expenses/balances/{id} Get balance summary for a group

Full interactive docs: https://splitbill-pro-1.onrender.com/docs

------------------------------------------------------------
🌐 DEPLOYMENT
------------------------------------------------------------
  Frontend   : https://splitbill-pro-two.vercel.app    ✅ Live
  Backend    : https://splitbill-pro-1.onrender.com    ✅ Live
  Swagger    : https://splitbill-pro-1.onrender.com/docs ✅ Live

------------------------------------------------------------
🗂️ PROJECT STRUCTURE
------------------------------------------------------------
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

------------------------------------------------------------
🧠 WHAT I LEARNED
------------------------------------------------------------
JWT Authentication
  Built secure token-based auth with bcrypt hashing
  and expiry handling

Database Relationships
  Used SQLAlchemy many-to-many relationships for group members

CORS Issues
  Configured CORS middleware properly for cross-origin
  Render <-> Vercel communication

OAuth2 Login
  Implemented OAuth2PasswordRequestForm for FastAPI-native login

Real-time Balances
  Computed balances on-the-fly from raw expense splits
  No separate balance table needed

Full-Stack Deployment
  Deployed backend on Render (with PostgreSQL) and
  frontend on Vercel independently

------------------------------------------------------------
🤝 CONTRIBUTING
------------------------------------------------------------
Contributions, issues, and feature requests are welcome!

  git checkout -b feature/YourFeature
  git commit -m "Add YourFeature"
  git push origin feature/YourFeature
  Open a Pull Request on GitHub

------------------------------------------------------------
📄 LICENSE
------------------------------------------------------------
This project is licensed under the MIT License.

------------------------------------------------------------
👨‍💻 AUTHOR
------------------------------------------------------------
Vignesh Sai

  GitHub   : https://github.com/vigneshsai52
  LinkedIn : https://linkedin.com/in/your-linkedin

------------------------------------------------------------
     Built with ❤️ using FastAPI & Vanilla JS
     ⭐ Star this repo if you found it helpful!
------------------------------------------------------------
