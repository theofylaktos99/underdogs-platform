#!/usr/bin/env python3
"""Test registration endpoint"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app, User, get_db, get_password_hash, create_access_token, UserCreate
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from datetime import timedelta

def test_register():
    """Test registration manually"""
    client = TestClient(app)
    
    # Test data
    user_data = {
        "email": "debuguser@example.com",
        "password": "debugpassword123",
        "username": "debuguser",
        "role": "user",
        "department": "",
        "skills": "",
        "location": None,
        "phone": None
    }
    
    print("Testing registration with data:", user_data)
    
    try:
        response = client.post("/api/auth/register", json=user_data)
        print("Status code:", response.status_code)
        print("Response:", response.json())
        
        if response.status_code != 200:
            print("Error response:", response.text)
            
    except Exception as e:
        print("Exception:", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_register()
