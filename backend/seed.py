import os
import sys
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Base, User, Task, Announcement, Comment, File, TaskStatus, Priority, UserStatus

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Database setup
DATABASE_URL = "sqlite:///./underdogsx.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_database():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Create users
        users_data = [
            {
                "username": "admin",
                "email": "admin@underdogsx.com",
                "hashed_password": main.get_password_hash("admin123"),
                "role": "admin",
                "department": "Management",
                "status": main.UserStatus.online,
                "skills": "Leadership,Strategy,Project Management",
                "location": "New York, NY",
                "phone": "+1 (555) 000-0001",
                "joined_at": datetime.utcnow(),
                "last_active": datetime.utcnow(),
                "is_active": True
            },
            {
                "username": "john_doe",
                "email": "john@underdogsx.com",
                "hashed_password": main.get_password_hash("password123"),
                "role": "Lead Developer",
                "department": "Engineering",
                "status": main.UserStatus.online,
                "skills": "React,Node.js,TypeScript,AWS",
                "location": "San Francisco, CA",
                "phone": "+1 (555) 123-4567",
                "joined_at": datetime.utcnow() - timedelta(days=30),
                "last_active": datetime.utcnow(),
                "is_active": True
            },
            {
                "username": "jane_smith",
                "email": "jane@underdogsx.com",
                "hashed_password": main.get_password_hash("password123"),
                "role": "UI/UX Designer",
                "department": "Design",
                "status": main.UserStatus.away,
                "skills": "Figma,Adobe XD,Sketch,Prototyping",
                "location": "Austin, TX",
                "phone": "+1 (555) 234-5678",
                "joined_at": datetime.utcnow() - timedelta(days=25),
                "last_active": datetime.utcnow() - timedelta(hours=2),
                "is_active": True
            },
            {
                "username": "mike_johnson",
                "email": "mike@underdogsx.com",
                "hashed_password": main.get_password_hash("password123"),
                "role": "Backend Developer",
                "department": "Engineering",
                "status": main.UserStatus.busy,
                "skills": "Python,FastAPI,PostgreSQL,Docker",
                "location": "Chicago, IL",
                "phone": "+1 (555) 345-6789",
                "joined_at": datetime.utcnow() - timedelta(days=20),
                "last_active": datetime.utcnow() - timedelta(minutes=30),
                "is_active": True
            },
            {
                "username": "sarah_wilson",
                "email": "sarah@underdogsx.com",
                "hashed_password": main.get_password_hash("password123"),
                "role": "QA Engineer",
                "department": "Quality Assurance",
                "status": main.UserStatus.online,
                "skills": "Selenium,Jest,Cypress,Manual Testing",
                "location": "Remote",
                "phone": "+1 (555) 456-7890",
                "joined_at": datetime.utcnow() - timedelta(days=15),
                "last_active": datetime.utcnow(),
                "is_active": True
            }
        ]
        
        # Create users
        created_users = []
        for user_data in users_data:
            user = UserModel(**user_data)
            db.add(user)
            created_users.append(user)
        
        db.commit()
        
        # Create tasks
        tasks_data = [
            {
                "title": "API Development",
                "description": "Build REST API for user authentication. This includes implementing JWT tokens, user registration, login, logout, and password reset functionality.",
                "status": TaskStatus.in_progress,
                "priority": Priority.high,
                "assignee_id": created_users[1].id,
                "creator_id": created_users[0].id,
                "due_date": datetime.utcnow() + timedelta(days=5),
                "tags": "backend,api,auth"
            },
            {
                "title": "UI/UX Design",
                "description": "Create wireframes and mockups for the dashboard. Focus on cyberpunk aesthetic with dark theme and neon accents.",
                "status": TaskStatus.completed,
                "priority": Priority.medium,
                "assignee_id": created_users[2].id,
                "creator_id": created_users[0].id,
                "due_date": datetime.utcnow() + timedelta(days=3),
                "tags": "design,ui,dashboard"
            },
            {
                "title": "Database Schema",
                "description": "Design and implement the database schema for the application. Include tables for users, tasks, announcements, and files.",
                "status": TaskStatus.pending,
                "priority": Priority.urgent,
                "assignee_id": created_users[3].id,
                "creator_id": created_users[0].id,
                "due_date": datetime.utcnow() + timedelta(days=2),
                "tags": "database,schema,backend"
            },
            {
                "title": "Testing Framework",
                "description": "Set up automated testing pipeline with unit tests, integration tests, and end-to-end tests.",
                "status": TaskStatus.in_progress,
                "priority": Priority.medium,
                "assignee_id": created_users[4].id,
                "creator_id": created_users[0].id,
                "due_date": datetime.utcnow() + timedelta(days=7),
                "tags": "testing,automation,ci-cd"
            },
            {
                "title": "Deployment Setup",
                "description": "Configure production deployment pipeline using Docker and cloud services.",
                "status": TaskStatus.pending,
                "priority": Priority.low,
                "assignee_id": created_users[1].id,
                "creator_id": created_users[0].id,
                "due_date": datetime.utcnow() + timedelta(days=10),
                "tags": "deployment,docker,cloud"
            }
        ]
        
        # Create tasks
        created_tasks = []
        for task_data in tasks_data:
            task = TaskModel(**task_data)
            db.add(task)
            created_tasks.append(task)
        
        db.commit()
        
        # Create announcements
        announcements_data = [
            {
                "title": "Welcome to UnderDogsX Platform",
                "content": "Welcome to the UnderDogsX coordination platform! This is our new internal tool for managing projects, tasks, and team collaboration. Please explore the features and let us know if you have any feedback.",
                "author_id": created_users[0].id,
                "priority": Priority.high,
                "pinned": True
            },
            {
                "title": "Team Meeting Tomorrow",
                "content": "We will have our weekly team meeting tomorrow at 2 PM. Please prepare your progress reports and any blockers you're facing. The meeting will be held in the main conference room.",
                "author_id": created_users[0].id,
                "priority": Priority.medium,
                "pinned": False
            },
            {
                "title": "New Security Guidelines",
                "content": "Please review the updated security guidelines in the shared drive. All team members must complete the security training by end of the week. Contact IT if you have any questions.",
                "author_id": created_users[0].id,
                "priority": Priority.urgent,
                "pinned": False
            },
            {
                "title": "Code Review Process",
                "content": "We're implementing a new code review process. All pull requests must be reviewed by at least one senior developer before merging. Please follow the new guidelines in the documentation.",
                "author_id": created_users[1].id,
                "priority": Priority.medium,
                "pinned": False
            }
        ]
        
        # Create announcements
        for announcement_data in announcements_data:
            announcement = AnnouncementModel(**announcement_data)
            db.add(announcement)
        
        db.commit()
        
        # Create comments
        comments_data = [
            {
                "content": "I've started working on the JWT implementation. Should have the basic structure ready by tomorrow.",
                "author_id": created_users[1].id,
                "task_id": created_tasks[0].id
            },
            {
                "content": "Great! Don't forget to implement rate limiting for the login endpoint.",
                "author_id": created_users[3].id,
                "task_id": created_tasks[0].id
            },
            {
                "content": "I've completed the wireframes. They're available in the shared Figma workspace.",
                "author_id": created_users[2].id,
                "task_id": created_tasks[1].id
            },
            {
                "content": "The database schema is ready for review. I've created the ER diagram and SQL scripts.",
                "author_id": created_users[3].id,
                "task_id": created_tasks[2].id
            }
        ]
        
        # Create comments
        for comment_data in comments_data:
            comment = CommentModel(**comment_data)
            db.add(comment)
        
        db.commit()
        
        # Create files
        files_data = [
            {
                "name": "Project Requirements.pdf",
                "file_type": "pdf",
                "size": 2048576,
                "uploader_id": created_users[0].id,
                "description": "Initial project requirements and specifications"
            },
            {
                "name": "API Documentation",
                "file_type": "link",
                "url": "https://api-docs.underdogsx.com",
                "uploader_id": created_users[1].id,
                "description": "Complete API documentation with examples"
            },
            {
                "name": "Design Mockups",
                "file_type": "folder",
                "uploader_id": created_users[2].id,
                "description": "UI/UX design mockups and wireframes"
            },
            {
                "name": "database-schema.sql",
                "file_type": "sql",
                "size": 4096,
                "uploader_id": created_users[3].id,
                "description": "Database schema and migration scripts"
            },
            {
                "name": "test-plan.docx",
                "file_type": "docx",
                "size": 1024000,
                "uploader_id": created_users[4].id,
                "description": "Comprehensive testing plan and procedures"
            }
        ]
        
        # Create files
        for file_data in files_data:
            file = FileModel(**file_data)
            db.add(file)
        
        db.commit()
        
        print("Database seeded successfully!")
        print("Login credentials:")
        print("Admin: admin@underdogsx.com / admin123")
        print("User: john@underdogsx.com / password123")
        print("User: jane@underdogsx.com / password123")
        print("User: mike@underdogsx.com / password123")
        print("User: sarah@underdogsx.com / password123")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
