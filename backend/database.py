import sqlite3
import logging
from datetime import datetime, timezone
from backend.config import DATABASE_PATH

logger = logging.getLogger("backend.database")

def get_connection():
    """Create and return a SQLite database connection with Row factory."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize SQLite database table schema if it does not exist."""
    conn = get_connection()
    try:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS enquiries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    work_email TEXT NOT NULL,
                    company TEXT,
                    phone TEXT,
                    service TEXT,
                    message TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
        logger.info("Database initialized at %s", DATABASE_PATH)
    except Exception as e:
        logger.error("Failed to initialize database: %s", e)
        raise
    finally:
        conn.close()

def save_enquiry(name, work_email, company="", phone="", service="", message=""):
    """Insert a new contact enquiry into the database and return the saved record."""
    conn = get_connection()
    try:
        created_at_str = datetime.now(timezone.utc).isoformat()
        with conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO enquiries (name, work_email, company, phone, service, message, created_at)
                VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
            """, (name, work_email, company, phone, service, message))
            enquiry_id = cursor.lastrowid
            
        return {
            "id": enquiry_id,
            "name": name,
            "work_email": work_email,
            "company": company,
            "phone": phone,
            "service": service,
            "message": message,
            "created_at": created_at_str
        }
    except Exception as e:
        logger.error("Database insert error: %s", e)
        raise
    finally:
        conn.close()

def get_enquiries(limit=100):
    """Retrieve recent enquiries from database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM enquiries ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()
