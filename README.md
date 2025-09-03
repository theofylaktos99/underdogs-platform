
> **Note:** This project is a first attempt at building a platform/app for use with my collaborators. It was created during my third month of programming, and I am aware of its weak points. The only reason I did not further develop or improve them was to see how quickly I could build something similar from scratch. The total time invested in this project is approximately 40-50 hours max!

# Underdogs Platform 🏰

A full-stack medieval castle portal application with React frontend and FastAPI backend.

## 🌟 Features

- **Medieval Castle Gate Portal** - Interactive castle door with authentication
- **JWT Authentication** - Secure user registration and login
- **Real-time Dashboard** - Task management and team collaboration
- **Responsive Design** - Works on all devices

## 🚀 Live Demo

- **Frontend**: https://famous-moonbeam-1630fd.netlify.app
- **Backend**: https://underdogs-platform.onrender.com
- **API Docs**: https://underdogs-platform.onrender.com/docs

## 🛠️ Tech Stack

### Frontend
- React 19 with TypeScript
- Tailwind CSS for styling
- Axios for API calls
- React Router for navigation

### Backend
- FastAPI with Python
- SQLAlchemy ORM
- JWT authentication
- SQLite database

## 📦 Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Server runs on: http://localhost:8000

### Frontend
```bash
cd frontend
npm install
npm start
```
App runs on: http://localhost:3000

## 🌐 Deployment

### Backend (Railway)
1. Connect this repo to Railway
2. Select `backend` folder
3. Auto-deploys on push

### Frontend (Netlify)
1. Build: `npm run build`
2. Deploy `build/` folder to Netlify
3. Set environment variables

## 🎨 Portal Features

- Medieval castle gate design
- "Speak friend and enter" title
- Password hint: "mellon" displayed on ground
- Smooth animations and effects
- Dark theme with red accents

## 📁 Project Structure

```
underdogsx/
├── backend/           # FastAPI backend
│   ├── main.py       # Main application
│   ├── models.py     # Database models
│   └── requirements.txt
├── frontend/         # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── contexts/
│   │   └── services/
│   └── public/
└── README.md
```

## 🔐 Environment Variables

### Backend (.env)
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./underdogs.db
```

### Frontend (.env)
```
REACT_APP_API_URL=your-backend-url
```

## 📝 License

MIT License - Feel free to use this project!

---

Made with ❤️ for the Underdogs platform

A dark-themed internal web application for coordinating teams of developers, designers, and project collaborators. Built with a cyberpunk aesthetic inspired by brutalism and Greek mythology.

## 🎯 Features

- **Portal Gate Authentication**: Moria-style challenge entrance
- **Task Management**: Create, assign, and track project tasks
- **Team Collaboration**: Member profiles and status tracking
- **Announcements**: Team bulletin board with priority levels
- **File Sharing**: Upload and share documents and links
- **Real-time Updates**: Live status updates and notifications
- **Dark Cyberpunk Theme**: Neon accents, glowing effects, and modern UI

## 🧱 Tech Stack

### Frontend
- **React** with TypeScript
- **Tailwind CSS** for styling
- **React Router** for navigation
- **Axios** for HTTP requests
- **Lucide React** for icons

### Backend
- **FastAPI** (Python)
- **SQLAlchemy** ORM
- **JWT Authentication**
- **SQLite** (development) / **PostgreSQL** (production)
- **Pydantic** for data validation

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd underdogsx
   ```

2. **Backend Setup**
   ```bash
   cd backend
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\\Scripts\\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Set up environment variables
   cp .env.example .env
   # Edit .env with your configuration
   
   # Seed the database with test data
   python seed.py
   
   # Start the backend server
   python main.py
   ```
   
   The backend will be available at `http://localhost:8000`

3. **Frontend Setup**
   ```bash
   cd ../frontend
   
   # Install dependencies
   npm install
   
   # Start the development server
   npm start
   ```
   
   The frontend will be available at `http://localhost:3000`

## 🎮 Usage

### Portal Gate Entry
1. Navigate to `http://localhost:3000`
2. Answer the Moria-style challenge: "FRIEND"
3. You'll be redirected to the authentication page

### Authentication
Use these test credentials:
- **Admin**: `admin@underdogsx.com` / `admin123`
- **Developer**: `john@underdogsx.com` / `password123`
- **Designer**: `jane@underdogsx.com` / `password123`
- **Backend Dev**: `mike@underdogsx.com` / `password123`
- **QA Engineer**: `sarah@underdogsx.com` / `password123`

### Navigation
- **Dashboard**: Overview of tasks, announcements, and team activity
- **Tasks**: View and manage project tasks with filtering
- **Announcements**: Team bulletin board with priority levels
- **Files**: Shared documents and links
- **Team**: Member profiles and status tracking

## 🛠️ Development

### Backend API Endpoints

- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user
- `GET /api/tasks` - List tasks
- `POST /api/tasks` - Create task
- `GET /api/tasks/{id}` - Get task details
- `PUT /api/tasks/{id}` - Update task
- `GET /api/announcements` - List announcements
- `POST /api/announcements` - Create announcement
- `GET /api/files` - List files
- `POST /api/files` - Upload file
- `GET /api/users` - List users
- `GET /api/comments/{task_id}` - Get task comments
- `POST /api/comments` - Create comment

### Frontend Components

- `PortalGate` - Moria-style entrance challenge
- `AuthPage` - Login/registration interface
- `Dashboard` - Main dashboard with stats and activity
- `TaskList` - Task management interface
- `TaskDetail` - Individual task view with comments
- `Announcements` - Team bulletin board
- `Files` - File sharing interface
- `Team` - Member profiles and status
- `Layout` - Main application layout with sidebar

### Database Schema

- **Users**: Authentication and profile information
- **Tasks**: Project tasks with status and priority
- **Announcements**: Team communications
- **Comments**: Task-specific discussions
- **Files**: Shared documents and links

## 🎨 Design System

### Colors
- **Background**: `#0a0a0a` (dark-bg)
- **Cards**: `#1a1a1a` (dark-card)  
- **Borders**: `#333333` (dark-border)
- **Neon Red**: `#ff0040` (primary accent)
- **Neon Blue**: `#00bfff` (secondary accent)
- **Neon Green**: `#00ff41` (success accent)

### Typography
- **Headers**: Orbitron (cyberpunk font)
- **Body**: Fira Code (monospace)
- **Accents**: Glowing text effects

### Effects
- Neon glow shadows
- Glitch text animations
- Pulse animations
- Cyberpunk aesthetic elements

## 📦 Deployment

### Production Setup

1. **Environment Variables**
   ```bash
   # Backend (.env)
   DATABASE_URL=postgresql://user:password@localhost/underdogsx
   SECRET_KEY=your-super-secret-key
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   
   # Frontend
   REACT_APP_API_URL=https://your-api-domain.com
   ```

2. **Database Migration**
   ```bash
   # Set up PostgreSQL database
   # Update DATABASE_URL in .env
   python seed.py
   ```

3. **Build and Deploy**
   ```bash
   # Frontend
   npm run build
   
   # Backend
   pip install -r requirements.txt
   python main.py
   ```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🎵 Bonus Features

- **Ambient Music Toggle**: Optional cyberpunk background music
- **Markdown Support**: Rich text editing for announcements
- **Real-time Notifications**: Live updates for team activities
- **Mobile Responsive**: Works on all device sizes
- **Dark Mode Only**: Fully embraces the cyberpunk aesthetic

## 🔧 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check DATABASE_URL in .env
   - Ensure database service is running
   - Run `python seed.py` to initialize

2. **CORS Issues**
   - Verify frontend URL in backend CORS settings
   - Check API_URL in frontend environment

3. **Authentication Errors**
   - Verify JWT secret key is set
   - Check token expiration settings
   - Clear browser localStorage if needed

### Support

For issues and questions:
- Check the troubleshooting guide
- Review API documentation at `http://localhost:8000/docs`
- Create an issue in the repository

---

## 🔍 Current Implementation Status

### ✅ Completed Features

#### Core Infrastructure
- ✅ **Frontend-Backend Architecture**: Full React + FastAPI setup with TypeScript
- ✅ **Authentication System**: JWT-based auth with bcrypt password hashing
- ✅ **Database Layer**: SQLAlchemy ORM with SQLite (dev ready for PostgreSQL)
- ✅ **CORS Configuration**: Proper cross-origin setup for production deployment
- ✅ **Environment Management**: Configurable environment variables for different stages

#### UI/UX Components
- ✅ **Portal Gate**: Unique LOTR-inspired authentication portal with "mellon" challenge
- ✅ **Dashboard**: Comprehensive overview with stats, recent activity, and team metrics
- ✅ **Task Management**: Full CRUD operations with filtering, priority levels, and status tracking
- ✅ **Team Directory**: Member profiles with skills, departments, and online status
- ✅ **Announcements**: Priority-based team bulletin board with pinning capabilities
- ✅ **File Sharing**: Upload and link sharing with categorization
- ✅ **Responsive Design**: Mobile-first approach with cyberpunk aesthetic

#### Technical Features
- ✅ **Cold Start Handling**: Intelligent retry mechanisms for cloud deployment
- ✅ **Error Boundaries**: Comprehensive error handling and user feedback
- ✅ **Loading States**: Proper loading indicators throughout the application
- ✅ **Internationalization**: English/Greek language support with context-based translation
- ✅ **API Integration**: Axios interceptors with token management and retry logic

### 🚧 Partially Implemented

#### Database Relationships
- ⚠️ **Model Relationships**: Some relationships commented out in main.py but fully implemented in models.py
- ⚠️ **Data Consistency**: API endpoints use basic queries without leveraging full relationship capabilities

#### API Coverage
- ⚠️ **Complete CRUD**: Some endpoints missing (DELETE operations for tasks, announcements)
- ⚠️ **Advanced Filtering**: Limited filtering capabilities in current API endpoints
- ⚠️ **File Upload**: File management system exists but actual file upload implementation missing

### ❌ Missing Features & Weaknesses

#### 🔴 Critical Missing Features

1. **Testing Framework**
   - No unit tests implemented
   - No integration tests
   - No end-to-end testing
   - Only basic manual testing scripts exist

2. **Real-time Features**
   - No WebSocket implementation despite having websockets dependency
   - No real-time notifications
   - No live status updates
   - Static data refresh only

3. **Production Scalability**
   - No containerization (Docker missing)
   - No CI/CD pipeline
   - No database migrations system
   - No monitoring/logging infrastructure

4. **Security Enhancements**
   - No rate limiting
   - No input sanitization beyond basic validation
   - No XSS protection headers
   - No CSRF protection
   - Missing file upload security

5. **Performance Optimization**
   - No caching layer (Redis missing)
   - No API response caching
   - No image optimization
   - No lazy loading for large datasets

#### 🟡 Medium Priority Missing Features

1. **User Experience**
   - No advanced search functionality
   - No drag-and-drop interfaces
   - No keyboard shortcuts
   - No dark/light theme toggle (fixed dark mode only)
   - No accessibility features (ARIA labels, screen reader support)

2. **Data Management**
   - No data export functionality
   - No backup/restore capabilities
   - No audit logging
   - No data archiving system

3. **Communication Features**
   - No email notifications
   - No push notifications
   - No in-app messaging system
   - No comment threading for tasks

4. **Advanced Task Management**
   - No task dependencies
   - No time tracking
   - No task templates
   - No bulk operations
   - No task history/changelog

5. **Admin Panel**
   - No user management interface
   - No system configuration UI
   - No analytics dashboard
   - No role-based permissions beyond basic auth

#### 🟢 Nice-to-Have Features

1. **Integration Capabilities**
   - No third-party integrations (GitHub, Slack, etc.)
   - No API documentation (Swagger UI not exposed)
   - No webhook support
   - No OAuth providers integration

2. **Advanced Analytics**
   - No reporting system
   - No data visualization charts
   - No performance metrics
   - No user activity analytics

3. **Mobile Experience**
   - No PWA implementation
   - No mobile push notifications
   - No offline capabilities
   - No mobile-specific UI optimizations

---

## 🛠️ Technical Debt & Code Quality Issues

### Code Organization
- **Duplicate Models**: Models defined in both main.py and models.py
- **Commented Code**: Relationship definitions commented out in main.py
- **Mock Data**: Dashboard and components using hardcoded mock data instead of API calls
- **Type Inconsistencies**: Some API responses not properly typed

### Database Issues
- **Relationship Utilization**: Not leveraging SQLAlchemy relationships for efficient queries
- **Migration System**: No Alembic migrations implemented
- **Connection Pooling**: No connection pool configuration for production
- **Index Optimization**: Missing database indexes for performance

### API Design
- **Consistency**: Some endpoints don't follow RESTful conventions
- **Error Handling**: Inconsistent error response formats
- **Validation**: Limited Pydantic validation on some endpoints
- **Documentation**: Missing comprehensive API documentation

### Frontend Architecture
- **State Management**: Using Context API for everything (may need Redux for complex state)
- **Component Coupling**: Some components tightly coupled to mock data
- **Bundle Optimization**: No code splitting for large components
- **Memory Leaks**: Potential memory leaks in useEffect hooks without cleanup

---

## 📋 Priority Roadmap for Future Development

### Phase 1: Foundation Strengthening (Immediate - 2 weeks)
1. **Testing Implementation**
   - Unit tests for all components and API endpoints
   - Integration tests for authentication flow
   - E2E tests for critical user journeys
   - Testing documentation and guidelines

2. **Code Quality**
   - Resolve duplicate model definitions
   - Implement proper database relationships
   - Remove hardcoded mock data
   - Add comprehensive TypeScript types

3. **Security Hardening**
   - Implement rate limiting
   - Add input sanitization
   - Configure security headers
   - Audit authentication system

### Phase 2: Production Readiness (1-2 months)
1. **DevOps & Deployment**
   - Docker containerization
   - CI/CD pipeline setup
   - Database migration system
   - Monitoring and logging infrastructure

2. **Performance Optimization**
   - Implement Redis caching
   - API response optimization
   - Frontend bundle optimization
   - Database query optimization

3. **Real-time Features**
   - WebSocket implementation
   - Real-time notifications
   - Live status updates
   - Real-time collaboration features

### Phase 3: Feature Enhancement (2-3 months)
1. **Advanced User Features**
   - Advanced search and filtering
   - Drag-and-drop interfaces
   - Bulk operations
   - Data export functionality

2. **Communication System**
   - Email notifications
   - Push notifications
   - In-app messaging
   - Comment threading

3. **Analytics & Reporting**
   - User activity analytics
   - Performance dashboards
   - Custom reports
   - Data visualization

### Phase 4: Scale & Integrations (3+ months)
1. **Third-party Integrations**
   - GitHub integration
   - Slack notifications
   - OAuth providers
   - Webhook system

2. **Mobile & PWA**
   - Progressive Web App
   - Mobile optimizations
   - Offline capabilities
   - Mobile push notifications

3. **Enterprise Features**
   - Multi-tenancy support
   - Advanced role management
   - API rate limiting tiers
   - Enterprise SSO

---

**Built with ❤️ by the UnderDogsX team**

*"You have my sword. And you have my bow. And my axe!"*

---

## 📊 Project Health Metrics

- **Code Coverage**: 0% (No tests implemented)
- **Technical Debt**: Medium-High (Duplicate code, mock data dependencies)
- **Security Score**: 6/10 (Basic auth, missing security headers)
- **Performance Score**: 7/10 (Good frontend, needs backend optimization)
- **Maintainability**: 7/10 (Good structure, needs cleanup)
- **Scalability**: 5/10 (Needs infrastructure improvements)

**Overall Project Status: 70% MVP Complete - Ready for Beta Testing with Production Hardening Required**
