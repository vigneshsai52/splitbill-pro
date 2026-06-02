 SplitBill Pro
Full-stack expense splitting SaaS. Create groups, add expenses, track who owes whom.
🚀 Live Demo: https://splitbill-pro-two.vercel.app
✨ Features
Table
Feature	Description
👤 User Auth	JWT-based registration & login
👥 Groups	Create expense groups with friends
💸 Expenses	Add expenses with automatic splits
📊 Balances	Real-time balance calculation
🗑️ Management	Delete groups with confirmation
🛠️ Tech Stack
Table
Layer	Technology
Backend	Python, FastAPI, SQLAlchemy
Database	SQLite (local) / PostgreSQL (Render)
Auth	JWT tokens + bcrypt
Frontend	HTML5, CSS3, Vanilla JS
Deploy	Render (backend), Vercel (frontend)
🚀 Quick Start
bash
# Clone
git clone https://github.com/vigneshsai52/splitbill-pro.git
cd splitbill-pro

# Backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

# Frontend
# Open frontend/index.html or deploy to Vercel
📸 Screenshots
Register / Login page
Create Group form
Group list with delete
Add Expense form
Expenses & Balances display
🧠 What I Learned
Table
Challenge	Solution
JWT authentication	Implemented secure token-based auth
Database relationships	SQLAlchemy many-to-many for groups
CORS deployment	Configured Render/Vercel integration
Real-time balances	Calculated on-the-fly from expenses
OAuth2 login	Form-based auth for FastAPI
🌐 Live URLs
Frontend: https://splitbill-pro-two.vercel.app
Backend API: https://splitbill-pro-1.onrender.com
Swagger Docs: https://splitbill-pro-1.onrender.com/docs
Built with ❤️ by Vignesh Sai
