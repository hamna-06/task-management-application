# 📝 Task Scheduler Application

A modern, feature-rich Python desktop application designed to streamline daily task management. This application provides a secure environment for users to organize, track, and prioritize their work using a graphical interface and a persistent MySQL database.

## ✨ Key Features

- **Interactive UI**: Features a dynamic welcome screen with an animated bubble background.
- **Secure Authentication**: User registration and login with **SHA-256 password encryption**.
- **Task Management (CRUD)**: Create, view, update, and delete tasks with ease.
- **Smart Tracking**: 
    - **Deadlines**: Integrated calendar system (`tkcalendar`) for precise scheduling.
    - **Priority**: Assign Low, Medium, or High priority levels.
    - **Status**: Mark tasks as "Pending" or "Completed".
- **Category System**: Multi-category support to organize tasks by Work, Personal, etc.
- **Audit Logs**: A built-in `TaskHistory` system that tracks every change made to your tasks.
- **Data Persistence**: Powered by a relational MySQL database for reliable storage.

---

## 🛠️ Technology Stack

* **Frontend**: Python (Tkinter & ttk)
* **Database**: MySQL
* **Libraries**: `mysql-connector-python`, `tkcalendar`, `hashlib`

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.x** and **MySQL** (via XAMPP or MySQL Server) installed.

### 2. Install Dependencies
Run the following command to install the required Python libraries:
```bash
pip install mysql-connector-python tkcalendar
