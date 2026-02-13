Task Management Backend API
===========================

A secure backend for a Task Management System built using Django REST Framework.

This project demonstrates secure authentication, clean REST API design, rate limiting, logging, and production deployment.

🚀 Live Deployment
==================

**Hosted Backend:**[https://task-management-backend-django.onrender.com](https://task-management-backend-django.onrender.com)

**Swagger API Documentation:**[https://task-management-backend-django.onrender.com/api/v1/docs/](https://task-management-backend-django.onrender.com/api/v1/docs/)

## Screenshots
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t1.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t2.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t3.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t4.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t5.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/Screenshot%202026-02-13%20081015.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t6.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t7.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t9.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t10.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t11.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t12.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t13.png)
![image alt](https://github.com/SachinGupta2012/Task_Management_Backend_Django/blob/7b731a72fef265e55742a50d6a994f482a88c9eb/screenshots/t14.png)


🧠 Tech Stack
=============

*   Django 5.x
    
*   Django REST Framework
    
*   JWT Authentication (SimpleJWT)
    
*   OTP-based Authentication
    
*   PostgreSQL (Production)
    
*   SQLite (Local Development)
    
*   drf-spectacular (Swagger Docs)
    
*   Gunicorn
    
*   Render Deployment
    

🔐 Authentication Flow
======================

This system uses **Email-based OTP + JWT authentication**.

> ⚠ For evaluation purposes, OTP is logged in server console instead of being sent via email.

Step 1 — Request OTP
--------------------

### Endpoint

`   POST /api/v1/auth/request-otp/   `

### Request Body

`   {    "email": "user@example.com"  }   `

### What Happens

*   User is created if not exists
    
*   6-digit OTP is generated
    
*   OTP stored with 5-minute expiration
    
*   OTP logged in server console
    
*   Rate limiting applied
    

### Response

`   {    "message": "OTP sent successfully"  }   `

Step 2 — Verify OTP
-------------------

### Endpoint

`   POST /api/v1/auth/verify-otp/   `

### Request Body

`   {    "email": "user@example.com",    "code": "123456"  }   `

### Response

`   {    "access": "jwt_access_token",    "refresh": "jwt_refresh_token"  }   `

If OTP is invalid or expired:

`   400 Bad Request   `

🔑 JWT Configuration
====================

*   Access Token Lifetime: 10 minutes
    
*   Refresh Token Lifetime: 7 days
    
*   Token blacklisting enabled
    

Protected endpoints require:

`Authorization: Bearer` 

📝 Task Management Endpoints
============================

Base URL:

`   /api/v1/tasks/   `

All endpoints require authentication.

Create Task
-----------

`   POST /api/v1/tasks/   `

### Body

`   {    "title": "Complete assignment",    "description": "Finish backend project",    "status": "pending"  }   `

Get All Tasks
-------------

`   GET /api/v1/tasks/   `

Returns only tasks belonging to authenticated user.

Supports:

*   Pagination
    
*   Filtering by status
    
*   Search
    
*   Ordering
    

Get Single Task
---------------

`   GET /api/v1/tasks/{id}/   `

Returns task owned by user.

Update Task
-----------

`   PUT /api/v1/tasks/{id}/   `

or

`   PATCH /api/v1/tasks/{id}/   `

Delete Task
-----------

`   DELETE /api/v1/tasks/{id}/   `

🔒 Authorization
================

*   Users can only access their own tasks.
    
*   Querysets filtered using request.user.
    
*   Unauthorized access returns HTTP 403.
    

⏱ Rate Limiting
===============

To prevent abuse:

*   OTP endpoint: 5 requests per minute
    
*   Authenticated users: 50 requests per minute
    
*   Anonymous users: 10 requests per minute
    

Exceeding limits returns HTTP 429.

📊 Activity Logging
===================

The system logs:

*   OTP requests
    
*   Login success/failure
    
*   Task creation
    
*   Task updates
    
*   Task deletion
    
*   Security-related actions
    

Logs are stored in the database for auditing.

⚙ Environment Variables
=======================

Refer to .env.example.

Required variables include:

*   SECRET\_KEY
    
*   DEBUG
    
*   ALLOWED\_HOSTS
    
*   DATABASE\_URL (Production)
    

Email SMTP variables are optional in this submission since OTP is logged to console.

🛠 Local Setup Instructions
===========================

Clone Repository
----------------

`   git clone   cd Task_Management_Backend_Django   `

Create Virtual Environment
--------------------------

`   python -m venv .venv  .venv\Scripts\activate   `

Install Dependencies
--------------------

`   pip install -r requirements.txt   `

Configure Environment
---------------------
`   cp .env.example .env   `

Update necessary values.

Apply Migrations
----------------
`   python manage.py migrate   `

Run Server
----------

`   python manage.py runserver   `

Open:

`   http://127.0.0.1:8000/api/v1/docs/   `

🌍 Deployment
=============

Deployed on Render using:

*   Gunicorn WSGI server
    
*   PostgreSQL managed database
    
*   Environment-based configuration
    
*   DEBUG=False in production
    

Start command:

`   python manage.py migrate && gunicorn core.wsgi:application   `

