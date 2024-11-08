# Orange Fab Maroc Platform

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Completed Work](#completed-work)
- [To-Do](#to-do)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Project Overview

The **Orange Fab Platform** is a full-fledged web application designed to serve the diverse needs of Orange Fab Maroc. This platform integrates several functional modules, including matchmaking between startups and investors, news management, event scheduling, chatbot interaction, and an internal admin dashboard for effective backend management.

The application is structured to offer a seamless experience for both end-users and administrators. With dedicated sections for news, events, startup portfolios, and a unique notification system that tracks interactions from the chatbot, this platform is engineered to handle complex business processes efficiently.

### Objectives

- **Matchmaking**: Facilitating efficient matchmaking between startups and investors.
- **News Management**: Providing a dynamic platform for managing and displaying news.
- **Event Management**: Streamlining the creation and management of events.
- **Chatbot Interaction**: Enabling interactive user engagements through a custom-built chatbot.
- **Notification System**: Categorizing and displaying notifications in the admin dashboard.
- **Internal Chatbot**: An unfinished project that aims to replicate the functionalities of GPT-based chatbots like ChatGPT, specifically tailored to handle queries and automate responses within the platform.

## Project Structure

The project is divided into two main components: the **Backend** and the **Frontend**. Additionally, there is an unfinished **Internal Chatbot** module designed to handle queries similar to ChatGPT.

### Project Tree Overview

```
FABBOT/
│
├── Backend/
│   ├── Backoffice/
│   │   ├── accounts/
│   │   ├── backoffice/
│   │   ├── content/
│   │   ├── dashboard/
│   │   ├── events/
│   │   ├── internal_chatbot/
│   │   ├── media/
│   │   ├── news/
│   │   ├── node_modules/
│   │   ├── notifications/
│   │   ├── startups/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── venv/
│   │   ├── db.sqlite3
│   │   ├── manage.py
│   │   ├── package-lock.json
│   │   └── package.json
│   └── Scraping/
│
└── Frontend/
    ├── .idea/
    ├── images/
    └── src/
        ├── Accueil.html
        ├── Chatbot.html
        ├── Coming-soon.html
        ├── event.html
        ├── Login.html
        ├── news.html
        └── Portfolio.html
```

### Key Components

- **Backend**:
  - **Backoffice**: The core of the platform, managing everything from user authentication (`accounts`), to event management (`events`), and notification systems (`notifications`).
  - **Internal Chatbot**: A work-in-progress chatbot designed to mimic GPT-3 based responses, assisting users within the platform.
  - **News Management**: Handles all the news-related functionalities, including displaying, filtering, and searching news items.
  - **Events**: Manages the scheduling and organization of events.
  - **Matchmaking**: Facilitates interactions between startups and investors, managing meeting schedules.
  - **Scraping**: A module designed to scrape external data, likely for content aggregation or analysis.

- **Frontend**:
  - **Static Assets**: Contains all the images, CSS, and JavaScript files used across the platform.
  - **HTML Templates**: The main views for the platform, including pages like `Accueil.html`, `Chatbot.html`, and `Portfolio.html`.

## Technologies Used

- **Programming Languages**: Python (Django), JavaScript, HTML, CSS
- **Frameworks**: 
  - **Backend**: Django (v5.0.7)
  - **Frontend**: Bootstrap for styling, jQuery for dynamic content handling.
- **Database**: SQLite for development, PostgreSQL for production.
- **APIs**: Django REST Framework (for RESTful APIs), Axios (for AJAX requests).
- **Tools**: 
  - **Version Control**: Git
  - **Package Management**: npm (for Node.js dependencies)
  - **Deployment**: Render.com
- **Libraries**: Axios for API requests, jQuery for DOM manipulation, and Bootstrap for responsive design.

## Features

### 1. **Matchmaking**
   - Provides a seamless interface for investors to book meetings with startups.
   - Includes an admin dashboard to manage and monitor all bookings.
   - Allows users to cancel or modify their bookings.
   
### 2. **News Management**
   - Highlights weekly and monthly news.
   - Allows filtering and searching of news articles.
   - Admins can easily add, edit, or remove news items.
   
### 3. **Event Management**
   - Enables the creation and management of events.
   - Integrated with the chatbot for user registration.
   - Supports listing of all events with details.

### 4. **Chatbot Integration**
   - Interactive chatbot built with custom logic.
   - Handles user input for propositions and meeting requests.
   - Automatically categorizes and forwards requests to the notification system.

### 5. **Notification System**
   - Displays categorized notifications as `Propositions` and `Rendez-vous`.
   - Provides an admin view for managing and responding to notifications.

### 6. **Internal Chatbot (Unfinished)**
   - An advanced feature aimed at providing GPT-3 like responses.
   - Intended to handle internal queries and automate user interactions within the platform.
   - The chatbot is in the early stages of development, with basic functionalities in place.

### 7. **Admin Dashboard**
   - A comprehensive interface for managing all backend operations.
   - Includes user management, startup portfolios, event management, and news editing.

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- Node.js (for frontend build processes)
- npm (for managing JavaScript packages)
- Git

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/orange-fab-platform.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd FABBOT
   ```

3. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the platform**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`.
   
2. **Interact with the Chatbot**:
   - Visit `http://127.0.0.1:8000/chatbot/` to engage with the chatbot.
   
3. **Admin Dashboard**:
   - Access the admin panel at `http://127.0.0.1:8000/admin/` for backend management.

## Deployment

### Production Deployment

1. **Configure environment variables** for database connections and secret keys.
   
2. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

3. **Deploy on a platform like Render.com**:
   - Follow the platform-specific deployment instructions.
   - Ensure that all necessary environment variables are set for a production environment.

## Completed Work

- [x] **Backend Architecture**: Set up the Django backend with all necessary apps and models.
- [x] **Chatbot Integration**: Developed a custom chatbot for user interaction.
- [x] **Notification System**: Created and integrated the notification system.
- [x] **Matchmaking Module**: Implemented the matchmaking feature for connecting startups with investors.
- [x] **News Management System**: Developed a dynamic system for managing and displaying news.
- [x] **Event Management Module**: Completed the event scheduling and management features.
- [x] **Admin Dashboard**: Built a comprehensive admin panel for backend management.
- [x] **Frontend Development**: Designed and implemented the frontend using Bootstrap and custom CSS.
- [x] **Database Migrations**: Completed all required database migrations.

## To-Do

- [ ] **Complete Backoffice Features**: Finish the development of the Events, Notiffications, and Landing Page sections.
- [ ] **Complete Backoffice Frontend**: Finish the development of the Frontend of the Backoffice following the figma design.
- [ ] **Complete Internal Chatbot**: Finish the development of the GPT-4 like internal chatbot.
- [ ] **User Authentication**: Implement a more robust authentication system with role-based access controls.
- [ ] **Unit Testing**: Develop unit and integration tests for all major components.
- [ ] **Advanced Search and Filter Options**: Enhance filtering options in the news and notification modules.
- [ ] **Optimize Performance**: Review and optimize the platform for better speed and scalability
- [ ] **Deploy Project**: Deploy the project on the given VPS.


## Contributing

If you would like to contribute to this project, please follow these steps:

1. **Fork the repository**.
2. **Create a feature branch** (`git checkout -b feature/your-feature-name`).
3. **Commit your changes** (`git commit -m 'Add some feature'`).
4. **Push to the branch** (`git push origin feature/your-feature-name`).
5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
