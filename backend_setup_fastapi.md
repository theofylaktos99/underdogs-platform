Build the backend of the UnderDogs platform using Python FastAPI.

🎯 PURPOSE:
Provide authentication, task management, announcements, and team tracking for the internal coordination app.

📂 STRUCTURE:
- `/app/main.py` – FastAPI instance + routers
- `/app/models/` – Pydantic + ORM schemas
- `/app/routes/` – All endpoints: auth, tasks, announcements, users
- `/app/services/` – Business logic (e.g., auth validation, task assignment)
- `/app/utils/` – helper functions

🔐 AUTH:
- JWT with roles: admin, member, guest
- Register/Login/Logout
- Auth middleware

📦 DATABASE:
- Use SQLModel or Tortoise ORM
- Seed data (users, tasks)

📘 BONUS:
- Endpoint: `/api/system/lore` returns the full “Speak, friend and enter” passage from Tolkien as a fun JSON Easter egg.

Final output: fully structured backend with example data and working endpoints.
