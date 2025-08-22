# Underdogs Platform 🏰

A full-stack medieval castle portal application with React frontend and FastAPI backend.

## 🌟 Features

- **Medieval Castle Gate Portal** - Interactive castle door with authentication
- **JWT Authentication** - Secure user registration and login
- **Real-time Dashboard** - Task management and team collaboration
- **Responsive Design** - Works on all devices

## 🚀 Live Demo

- **Frontend**: https://famous-moonbeam-1630fd.netlify.app
- **Backend**: (Deploy in progress...)

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

**Built with ❤️ by the UnderDogsX team**

*"You have my sword. And you have my bow. And my axe!"*
