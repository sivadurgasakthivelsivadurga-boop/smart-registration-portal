from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

def utc_now():
    return datetime.now(timezone.utc)

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    college_name = db.Column(db.String(150), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    year_of_study = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "student",
            "type_name": "Student Registration",
            "full_name": self.full_name,
            "dob": self.dob,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "college_name": self.college_name,
            "department": self.department,
            "course": self.course,
            "year_of_study": self.year_of_study,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class JobRegistration(db.Model):
    __tablename__ = 'job_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    qualification = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.Text, nullable=False)
    experience = db.Column(db.String(50), nullable=False)
    preferred_job_role = db.Column(db.String(100), nullable=False)
    resume_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "job",
            "type_name": "Job Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "qualification": self.qualification,
            "skills": self.skills,
            "experience": self.experience,
            "preferred_job_role": self.preferred_job_role,
            "resume_url": self.resume_url,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class EventRegistration(db.Model):
    __tablename__ = 'event_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    event_name = db.Column(db.String(150), nullable=False)
    event_date = db.Column(db.String(50), nullable=False)
    organization = db.Column(db.String(150), nullable=False)
    attendance_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "event",
            "type_name": "Event Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "event_name": self.event_name,
            "event_date": self.event_date,
            "organization": self.organization,
            "attendance_type": self.attendance_type,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class CourseRegistration(db.Model):
    __tablename__ = 'course_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(150), nullable=False)
    education_level = db.Column(db.String(100), nullable=False)
    learning_mode = db.Column(db.String(50), nullable=False)
    preferred_start_date = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "course",
            "type_name": "Course Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "course_name": self.course_name,
            "education_level": self.education_level,
            "learning_mode": self.learning_mode,
            "preferred_start_date": self.preferred_start_date,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class WorkshopRegistration(db.Model):
    __tablename__ = 'workshop_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    workshop_name = db.Column(db.String(150), nullable=False)
    college_or_organization = db.Column(db.String(150), nullable=False)
    skills = db.Column(db.Text, nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "workshop",
            "type_name": "Workshop Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "workshop_name": self.workshop_name,
            "college_or_organization": self.college_or_organization,
            "skills": self.skills,
            "experience_level": self.experience_level,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class MembershipRegistration(db.Model):
    __tablename__ = 'membership_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    membership_type = db.Column(db.String(50), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    interests = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "membership",
            "type_name": "Membership Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "membership_type": self.membership_type,
            "occupation": self.occupation,
            "interests": self.interests,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class SportsRegistration(db.Model):
    __tablename__ = 'sports_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    sport_name = db.Column(db.String(100), nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    team_name = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "sports",
            "type_name": "Sports Registration",
            "full_name": self.full_name,
            "dob": self.dob,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "sport_name": self.sport_name,
            "experience_level": self.experience_level,
            "team_name": self.team_name,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class VolunteerRegistration(db.Model):
    __tablename__ = 'volunteer_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    areas_of_interest = db.Column(db.Text, nullable=False)
    availability = db.Column(db.String(100), nullable=False)
    previous_experience = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "volunteer",
            "type_name": "Volunteer Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "areas_of_interest": self.areas_of_interest,
            "availability": self.availability,
            "previous_experience": self.previous_experience,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class InternshipRegistration(db.Model):
    __tablename__ = 'internship_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    college_name = db.Column(db.String(150), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.Text, nullable=False)
    internship_domain = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    resume_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "internship",
            "type_name": "Internship Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "college_name": self.college_name,
            "department": self.department,
            "skills": self.skills,
            "internship_domain": self.internship_domain,
            "duration": self.duration,
            "resume_url": self.resume_url,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class UserRegistration(db.Model):
    __tablename__ = 'user_registrations'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "user",
            "type_name": "General User Registration",
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "username": self.username,
            "address": self.address,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class AdminUser(db.Model):
    __tablename__ = 'admin_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


MODEL_MAP = {
    'student': Student,
    'job': JobRegistration,
    'event': EventRegistration,
    'course': CourseRegistration,
    'workshop': WorkshopRegistration,
    'membership': MembershipRegistration,
    'sports': SportsRegistration,
    'volunteer': VolunteerRegistration,
    'internship': InternshipRegistration,
    'user': UserRegistration
}
