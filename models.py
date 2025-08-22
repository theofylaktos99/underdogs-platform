"""
Separate module to import SQLAlchemy models correctly
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

# Create Base class for SQLAlchemy models
Base = declarative_base()

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class Priority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"

class UserStatus(str, enum.Enum):
    online = "online"
    away = "away"
    busy = "busy"
    offline = "offline"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    department = Column(String, default="")
    status = Column(Enum(UserStatus), default=UserStatus.offline)
    avatar = Column(String, nullable=True)
    joined_at = Column(DateTime, default=datetime.utcnow)
    last_active = Column(DateTime, default=datetime.utcnow)
    skills = Column(Text, default="")
    location = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    tasks_assigned = relationship("Task", back_populates="assignee", foreign_keys="Task.assignee_id")
    tasks_created = relationship("Task", back_populates="creator", foreign_keys="Task.creator_id")
    announcements = relationship("Announcement", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    files = relationship("File", back_populates="uploader")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    priority = Column(Enum(Priority), default=Priority.medium)
    assignee_id = Column(Integer, ForeignKey("users.id"))
    creator_id = Column(Integer, ForeignKey("users.id"))
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tags = Column(Text, default="")
    
    # Relationships
    assignee = relationship("User", back_populates="tasks_assigned", foreign_keys=[assignee_id])
    creator = relationship("User", back_populates="tasks_created", foreign_keys=[creator_id])
    comments = relationship("Comment", back_populates="task")

class Announcement(Base):
    __tablename__ = "announcements"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    priority = Column(Enum(Priority), default=Priority.medium)
    pinned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    author = relationship("User", back_populates="announcements")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    author = relationship("User", back_populates="comments")
    task = relationship("Task", back_populates="comments")

class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    file_type = Column(String)
    size = Column(Integer, nullable=True)
    url = Column(String, nullable=True)
    uploader_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text, nullable=True)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    uploader = relationship("User", back_populates="files")
