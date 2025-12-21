DROP DATABASE IF EXISTS task_scheduler;
CREATE DATABASE task_scheduler;
USE task_scheduler;

-- Users Table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100),
    password VARCHAR(100)
);

-- Categories Table
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Tasks Table
CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    deadline DATE,
    priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    status ENUM('Pending', 'Completed') DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- TaskCategory Mapping Table (many-to-many)
CREATE TABLE TaskCategory (
    task_id INT,
    category_id INT,
    PRIMARY KEY (task_id, category_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE
);

-- Drop the existing table if already created
DROP TABLE IF EXISTS TaskHistory;

-- Recreate the table with ON DELETE CASCADE
CREATE TABLE TaskHistory (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    task_id INT,
    action ENUM('Created', 'Updated', 'Deleted', 'Completed') NOT NULL,
    action_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE
);

