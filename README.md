# Skill Swap Platform

A modern, responsive web application for skill exchange and barter-style learning, built with Django and Bootstrap 5.

## 🚀 Features
- **User Profiles:** Name, location, profile photo, privacy, and multi-block availability
- **Skill Listings:** Offer and want skills, each with description, experience level, and category
- **Skill Search:** Find users by skill, category, location, and availability
- **Swap Requests:** Send, accept, reject, cancel, and delete swap requests with message and preferred time
- **Feedback & Ratings:** Leave and view feedback after swaps
- **Admin Panel:** Custom dashboard for user/skill moderation, analytics, platform-wide messages, and CSV exports
- **Responsive UI:** Beautiful, mobile-friendly design with Bootstrap 5 and icons

## 🛠️ Tech Stack
- **Backend:** Django 5
- **Frontend:** Bootstrap 5, Bootstrap Icons
- **Database:** SQLite (default, easy to switch to PostgreSQL)

## 📦 Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Pratham0086/Skill-Swap-Platform...-.git
   cd Skill-Swap-Platform...-
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser (admin):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
7. **Access the app:**
   - User site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin panel: [http://127.0.0.1:8000/adminpanel/](http://127.0.0.1:8000/adminpanel/)

## ✨ Contribution
- Fork the repo and create a feature branch
- Submit a pull request with a clear description
- For major changes, open an issue first to discuss

## 📄 License
MIT

---

**Skill Swap Platform** &copy; {{ now|date:'Y' }} | [GitHub Repo](https://github.com/Pratham0086/Skill-Swap-Platform...-.git)
