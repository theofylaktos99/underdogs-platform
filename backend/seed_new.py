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
                "hashed_password": get_password_hash("admin123"),
                "role": "admin",
                "department": "Management",
                "status": UserStatus.online,
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
                "hashed_password": get_password_hash("password123"),
                "role": "Lead Developer",
                "department": "Engineering",
                "status": UserStatus.online,
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
                "hashed_password": get_password_hash("password123"),
                "role": "UI/UX Designer",
                "department": "Design",
                "status": UserStatus.away,
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
                "hashed_password": get_password_hash("password123"),
                "role": "Backend Developer",
                "department": "Engineering",
                "status": UserStatus.busy,
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
                "hashed_password": get_password_hash("password123"),
                "role": "QA Engineer",
                "department": "Quality Assurance",
                "status": UserStatus.online,
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
            user = User(**user_data)
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
                "description": "Set up automated testing framework with Jest and Cypress. Include unit tests and integration tests.",
                "status": TaskStatus.in_progress,
                "priority": Priority.medium,
                "assignee_id": created_users[4].id,
                "creator_id": created_users[0].id,
                "due_date": datetime.utcnow() + timedelta(days=7),
                "tags": "testing,qa,automation"
            }
        ]
        
        # Create tasks
        created_tasks = []
        for task_data in tasks_data:
            task = Task(**task_data)
            db.add(task)
            created_tasks.append(task)
        
        db.commit()
        
        # Create announcements
        announcements_data = [
            {
                "title": "Welcome to UnderDogsX Platform!",
                "content": "Welcome to our new team coordination platform! This cyberpunk-themed platform will help us stay organized and connected. Please take some time to explore the features and update your profile.",
                "priority": Priority.high,
                "author_id": created_users[0].id
            },
            {
                "title": "New Project Kickoff",
                "content": "We're starting a new project this week. All team members should review the project requirements and check their assigned tasks.",
                "priority": Priority.medium,
                "author_id": created_users[0].id
            },
            {
                "title": "Team Meeting Tomorrow",
                "content": "Don't forget about our team meeting tomorrow at 2 PM. We'll discuss project progress and upcoming deadlines.",
                "priority": Priority.urgent,
                "author_id": created_users[0].id
            }
        ]
        
        # Create announcements
        for announcement_data in announcements_data:
            announcement = Announcement(**announcement_data)
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
                "content": "Great! Let me know if you need any help with the authentication flow.",
                "author_id": created_users[0].id,
                "task_id": created_tasks[0].id
            },
            {
                "content": "The wireframes are complete. I'll start working on the high-fidelity mockups next.",
                "author_id": created_users[2].id,
                "task_id": created_tasks[1].id
            },
            {
                "content": "Looking good! The cyberpunk theme is really coming together nicely.",
                "author_id": created_users[0].id,
                "task_id": created_tasks[1].id
            }
        ]
        
        # Create comments
        for comment_data in comments_data:
            comment = Comment(**comment_data)
            db.add(comment)
        
        db.commit()
        
        # Create files
        files_data = [
            {
                "name": "project_requirements.pdf",
                "file_type": "application/pdf",
                "size": 2048000,
                "url": "/files/project_requirements.pdf",
                "uploader_id": created_users[0].id,
                "description": "Complete project requirements document"
            },
            {
                "name": "api_documentation.md",
                "file_type": "text/markdown",
                "size": 512000,
                "url": "/files/api_documentation.md",
                "uploader_id": created_users[1].id,
                "description": "API endpoints and usage documentation"
            },
            {
                "name": "design_system.sketch",
                "file_type": "application/sketch",
                "size": 10240000,
                "url": "/files/design_system.sketch",
                "uploader_id": created_users[2].id,
                "description": "Complete design system with components and styles"
            }
        ]
        
        # Create files
        for file_data in files_data:
            file = File(**file_data)
            db.add(file)
        
        db.commit()
        
        print("Database seeded successfully!")
        print(f"Created {len(created_users)} users")
        print(f"Created {len(created_tasks)} tasks")
        print(f"Created {len(announcements_data)} announcements")
        print(f"Created {len(comments_data)} comments")
        print(f"Created {len(files_data)} files")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
