<div align="center">
💰 SplitBill Pro
Full-Stack Expense Splitting SaaS
Create groups, add expenses, track who owes whom — all in real-time.
https://splitbill-pro-two.vercel.app
https://splitbill-pro-1.onrender.com
https://splitbill-pro-1.onrender.com/docs
</div>
✨ Features
Table
Feature	Description
🔐 User Auth	JWT-based registration & login with bcrypt hashing
👥 Group Management	Create expense groups, add members by email
💸 Expense Tracking	Add expenses with automatic split calculation
📊 Real-time Balances	See who owes whom at a glance
🗑️ Delete Groups	Remove groups with confirmation modal
🎨 Modern UI	Responsive design with gradient backgrounds
🛠️ Tech Stack
Backend
Python 3.12
FastAPI — High-performance async web framework
SQLAlchemy — ORM for database operations
SQLite (local) / PostgreSQL (production)
JWT — Token-based authentication
bcrypt — Secure password hashing
Frontend
HTML5 — Semantic markup
CSS3 — Flexbox, Grid, animations
Vanilla JavaScript — No frameworks, pure JS
DevOps
Render — Backend hosting
Vercel — Frontend hosting
GitHub — Version control
🚀 Quick Start
Prerequisites
Python 3.8+
pip
Local Setup
bash
# 1. Clone the repository
git clone https://github.com/vigneshsai52/splitbill-pro.git
cd splitbill-pro

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the backend
python -m uvicorn app.main:app --reload

# 5. Open frontend
# Simply open frontend/index.html in your browser
# Or use Live Server extension in VS Code
Environment Variables
Create a .env file in the root:
env
DATABASE_URL=sqlite:///./splitbill.db
SECRET_KEY=your-secret-key-here
📡 API Endpoints
Table
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Login user (OAuth2)
GET	/auth/me	Get current user
POST	/groups/	Create new group
GET	/groups/	Get my groups
DELETE	/groups/{id}	Delete group
POST	/expenses/	Create expense
GET	/expenses/group/{id}	Get group expenses
GET	/expenses/balances/{id}	Get group balances
Full API Documentation: https://splitbill-pro-1.onrender.com/docs
🌐 Live Deployment
Table
Component	URL	Status
Frontend	https://splitbill-pro-two.vercel.app	✅ Live
Backend API	https://splitbill-pro-1.onrender.com	✅ Live
Swagger Docs	https://splitbill-pro-1.onrender.com/docs	✅ Live
📸 Screenshots
Authentication
Clean login/register interface
Form validation with error messages
Dashboard
Create groups with name and description
View all groups in card layout
Click group to view details
Group Details
Add expenses with description, amount, payer
View all expenses in list
Real-time balance calculation
🧠 What I Learned
Table
Challenge	Solution
JWT Authentication	Implemented secure token-based auth with refresh
Database Relationships	Used SQLAlchemy many-to-many for group members
CORS Issues	Configured proper CORS for Render/Vercel
OAuth2 Login	Implemented form-based auth for FastAPI
Real-time Balances	Calculated on-the-fly from expense splits
Deployment	Deployed full-stack on Render + Vercel
🗂️ Project Structure
plain
splitbill-pro/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database config
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── auth.py              # Authentication logic
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Auth routes
│       ├── groups.py        # Group routes
│       └── expenses.py      # Expense routes
├── frontend/
│   └── index.html           # Single-page frontend
├── requirements.txt         # Python dependencies
└── README.md               # This file
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
📄 License
This project is licensed under the MIT License.
👨‍💻 Author
Vignesh Sai
GitHub: @vigneshsai52
LinkedIn: Your LinkedIn
<div align="center">
Built with ❤️ using FastAPI & Vanilla JS
</div>
