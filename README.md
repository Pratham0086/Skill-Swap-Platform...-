# 🔁 Skill Swap Platform - Odoo Hackathon Project

A mini-application built on **Odoo** that enables users to **offer their skills** and **request skills from others**, fostering a barter-based knowledge and service exchange community.

---

## 📌 Overview

The Skill Swap Platform allows users to:

- Create a personalized profile
- List skills they **offer** and **want**
- Specify their **availability**
- Browse other users by skills
- **Request**, **Accept/Reject**, or **Delete** skill swap offers
- Leave **ratings and feedback** after a swap
- Control profile visibility (Public/Private)

---

## ⚙️ Tech Stack

- **Odoo 16/17** (Community Edition)
- Python (Odoo ORM)
- XML (Views, Menus)
- PostgreSQL (Odoo backend DB)
- Odoo Studio *(if used)*

---

## 🚀 Features

### 👤 User Profile
- Name, optional location and profile photo
- Skills Offered (One2many list)
- Skills Wanted (One2many list)
- Availability (e.g., weekends, evenings)
- Public/Private profile toggle

### 🔍 Search and Discover
- Filter users by skill
- View available swap opportunities
- Profile visibility rules respected

### 🔁 Swap Requests
- Send requests by selecting a skill offered and skill requested
- Accept or reject swap requests
- Cancel (delete) pending requests

### ⭐ Feedback System
- After swap completion, users can rate each other
- Optional written feedback
- Builds a trust-based reputation system

---

## 🧱 Core Models

- `skill.profile` – Extends user profile
- `skill.line` – Represents individual skill (offered/wanted)
- `skill.swap.request` – Handles request workflow
- `skill.rating` – Feedback and ratings for completed swaps

---

## 📂 Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/skill-swap-platform.git
