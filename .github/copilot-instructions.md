<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# UnderDogsX Platform - Copilot Instructions

## Project Overview
This is a full-stack web application for team coordination with a cyberpunk aesthetic. The platform includes task management, announcements, file sharing, and team collaboration features.

## Technology Stack
- **Frontend**: React + TypeScript + Tailwind CSS
- **Backend**: Python FastAPI + SQLAlchemy
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Authentication**: JWT tokens

## Code Style Guidelines

### Frontend (React/TypeScript)
- Use functional components with hooks
- Implement TypeScript interfaces for all data structures
- Use Tailwind CSS classes for styling
- Follow the cyberpunk design system (dark theme, neon accents)
- Use lucide-react icons
- Implement proper error handling and loading states

### Backend (FastAPI/Python)
- Use Pydantic models for request/response validation
- Implement proper HTTP status codes
- Use SQLAlchemy ORM with declarative models
- Add proper error handling and logging
- Follow RESTful API conventions

## Design System
- **Colors**: Dark backgrounds (#0a0a0a), neon red (#ff0040), neon blue (#00bfff)
- **Typography**: Orbitron for headers, Fira Code for body text
- **Effects**: Glowing borders, pulse animations, cyberpunk aesthetics
- **Components**: Dark cards, neon buttons, glitch effects

## Database Schema
- Users: Authentication and profile data
- Tasks: Project tasks with status/priority
- Announcements: Team communications
- Comments: Task discussions
- Files: Shared documents/links

## Key Features
1. Portal Gate entrance (Moria-style challenge)
2. JWT-based authentication
3. Task management with comments
4. Team announcements with priorities
5. File sharing (uploads and links)
6. Real-time status updates
7. Cyberpunk UI with glowing effects

## Best Practices
- Always validate user input
- Use proper error boundaries
- Implement loading states
- Add TypeScript types for all props
- Use semantic HTML elements
- Ensure responsive design
- Follow accessibility guidelines
- Add proper CORS configuration

## API Endpoints Pattern
- GET /api/{resource} - List resources
- POST /api/{resource} - Create resource
- GET /api/{resource}/{id} - Get specific resource
- PUT /api/{resource}/{id} - Update resource
- DELETE /api/{resource}/{id} - Delete resource

## Component Structure
```
src/
  components/
    PortalGate.tsx
    AuthPage.tsx
    Dashboard.tsx
    TaskList.tsx
    TaskDetail.tsx
    Announcements.tsx
    Files.tsx
    Team.tsx
    Layout.tsx
  contexts/
    AuthContext.tsx
  services/
    api.ts
```

## Security Considerations
- JWT tokens for authentication
- Password hashing with bcrypt
- CORS configuration
- Input validation
- SQL injection prevention
- XSS protection

When writing code for this project, maintain the cyberpunk aesthetic, ensure type safety, and follow the established patterns for consistency.
