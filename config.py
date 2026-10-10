import os
import pymysql
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def get_database_uri():
    raw_url = os.environ.get(
        'DATABASE_URL', 
        'mysql+pymysql://root:password@localhost:3306/registration_portal'
    )
    fallback_enabled = os.environ.get('DB_FALLBACK_SQLITE', 'true').lower() in ('true', '1', 't')

    if raw_url.startswith('mysql'):
        try:
            import re
            match = re.match(r'mysql\+pymysql://([^:]+):([^@]+)@([^:/]+):?(\d+)?/(.+)', raw_url)
            if match:
                user, password, host, port, db_name = match.groups()
                port = int(port) if port else 3306
                
                conn = pymysql.connect(
                    host=host,
                    user=user,
                    password=password,
                    port=port,
                    connect_timeout=3
                )
                with conn.cursor() as cursor:
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
                conn.close()
                print(f"[DATABASE] Connected to MySQL Server at {host}:{port} and verified database '{db_name}'.")
                return raw_url
        except Exception as e:
            print(f"[DATABASE WARNING] MySQL Connection Failed: {e}")
            if fallback_enabled:
                sqlite_path = os.path.join(os.path.dirname(__file__), 'registration_portal.db')
                print(f"[DATABASE FALLBACK] Falling back to SQLite database at: {sqlite_path}")
                return f"sqlite:///{sqlite_path}"
            else:
                raise e
    return raw_url


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'smart_registration_portal_secret_key_2026')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'smart_registration_jwt_secret_key_2026')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    SQLALCHEMY_DATABASE_URI = get_database_uri()
