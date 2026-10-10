-- Smart Registration Portal Database Schema
-- Database Name: registration_portal

CREATE DATABASE IF NOT EXISTS registration_portal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE registration_portal;

-- 1. Students Table
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    dob VARCHAR(20) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    college_name VARCHAR(150) NOT NULL,
    department VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL,
    year_of_study VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. Job Registrations Table
CREATE TABLE IF NOT EXISTS job_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    qualification VARCHAR(100) NOT NULL,
    skills TEXT NOT NULL,
    experience VARCHAR(50) NOT NULL,
    preferred_job_role VARCHAR(100) NOT NULL,
    resume_url VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 3. Event Registrations Table
CREATE TABLE IF NOT EXISTS event_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    event_name VARCHAR(150) NOT NULL,
    event_date VARCHAR(50) NOT NULL,
    organization VARCHAR(150) NOT NULL,
    attendance_type VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 4. Course Registrations Table
CREATE TABLE IF NOT EXISTS course_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    course_name VARCHAR(150) NOT NULL,
    education_level VARCHAR(100) NOT NULL,
    learning_mode VARCHAR(50) NOT NULL,
    preferred_start_date VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 5. Workshop Registrations Table
CREATE TABLE IF NOT EXISTS workshop_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    workshop_name VARCHAR(150) NOT NULL,
    college_or_organization VARCHAR(150) NOT NULL,
    skills TEXT NOT NULL,
    experience_level VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 6. Membership Registrations Table
CREATE TABLE IF NOT EXISTS membership_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    membership_type VARCHAR(50) NOT NULL,
    occupation VARCHAR(100) NOT NULL,
    interests TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 7. Sports Registrations Table
CREATE TABLE IF NOT EXISTS sports_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    dob VARCHAR(20) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    sport_name VARCHAR(100) NOT NULL,
    experience_level VARCHAR(50) NOT NULL,
    team_name VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 8. Volunteer Registrations Table
CREATE TABLE IF NOT EXISTS volunteer_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    areas_of_interest TEXT NOT NULL,
    availability VARCHAR(100) NOT NULL,
    previous_experience TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 9. Internship Registrations Table
CREATE TABLE IF NOT EXISTS internship_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    college_name VARCHAR(150) NOT NULL,
    department VARCHAR(100) NOT NULL,
    skills TEXT NOT NULL,
    internship_domain VARCHAR(100) NOT NULL,
    duration VARCHAR(50) NOT NULL,
    resume_url VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 10. User Registrations Table
CREATE TABLE IF NOT EXISTS user_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 11. Admin Users Table
CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
