Task Management Backend API
===========================

A secure and scalable backend for a Task Management System built with Django REST Framework.

This project was developed as part of a backend assignment to demonstrate API design, authentication, security practices, rate limiting, logging, and production deployment.

🚀 Live Deployment
------------------

**Hosted Backend URL:**[https://task-management-backend-django.onrender.com](https://task-management-backend-django.onrender.com)

**Swagger API Documentation:**[https://task-management-backend-django.onrender.com/api/v1/docs/](https://task-management-backend-django.onrender.com/api/v1/docs/)

🧠 Tech Stack
-------------

*   Django 5.x
    
*   Django REST Framework
    
*   JWT Authentication (SimpleJWT)
    
*   Email-based OTP authentication
    
*   PostgreSQL (Production)
    
*   SQLite (Local development)
    
*   drf-spectacular (Swagger docs)
    
*   Gunicorn (WSGI server)
    
*   Render (Deployment)
    

1\. Authentication & Security
=============================

### Email-Based OTP Flow

1.  User submits email.
    
2.  OTP is generated and stored with expiration.
    
3.  OTP is sent via SMTP email.
    
4.  User verifies OTP.
    
5.  JWT access and refresh tokens are issued.
    

### JWT Configuration

*   Access Token Lifetime: 10 minutes
    
*   Refresh Token Lifetime: 7 days
    
*   Token blacklisting enabled
    

### Authorization

*   Strict ownership enforcement.
    
*   Users can only access, modify, or delete their own tasks.
    
*   Querysets filtered by request.user.
    

2\. Core Functionalities
========================

Authenticated users can:

*   Create Task
    
*   View Tasks
    
*   Update Task
    
*   Delete Task
    

Additional features:

*   Pagination
    
*   Filtering
    
*   Search
    
*   Ordering
    

3\. Middleware & Cross-Cutting Concerns
=======================================

Implemented using Django & DRF:

*   JWT Authentication
    
*   Permission Classes (IsAuthenticated)
    
*   Input validation via serializers
    
*   Rate limiting
    
*   Global exception handling
    
*   Activity logging
    

4\. Rate Limiting
=================

*   OTP endpoint: 5 requests per minute
    
*   Authenticated users: 50 requests per minute
    
*   Anonymous users: 10 requests per minute
    

Returns HTTP 429 on abuse.

5\. Activity Logging
====================

All major actions are logged in database:

*   OTP requests
    
*   Login success/failure
    
*   Task creation
    
*   Task update
    
*   Task deletion
    
*   Security events
    

Logs stored for audit and monitoring purposes.

6\. Local Setup Instructions
============================

Step 1 – Clone Repository
-------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone   cd Task_Management_Backend_Django   `

Step 2 – Create Virtual Environment
-----------------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv .venv  .venv\Scripts\activate   # Windows  source .venv/bin/activate  # Mac/Linux   `

Step 3 – Install Dependencies
-----------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

Step 4 – Configure Environment
------------------------------

Copy example file:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cp .env.example .env   `

Update values inside .env.

Step 5 – Apply Migrations
-------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py migrate   `

Step 6 – Run Server
-------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py runserver   `

Open:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://127.0.0.1:8000/api/v1/docs/   `

7\. Deployment
==============

Deployed on Render using:

*   Gunicorn
    
*   PostgreSQL (Render managed database)
    
*   Environment-based configuration
    
*   DEBUG=False in production
    

Production command:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py migrate && gunicorn core.wsgi:application   `

8\. Deliverables
================

*   GitHub Repository
    
*   Hosted Backend URL
    
*   Swagger API Documentation
    
*   README with setup instructions
    
*   .env.example for configuration guidance
    

Design Decisions
================

*   DRF chosen for structured API development.
    
*   JWT used for stateless authentication.
    
*   OTP chosen for passwordless secure login.
    
*   PostgreSQL for production reliability.
    
*   Rate limiting implemented for abuse prevention.
    
*   Centralized exception handling for consistent API responses.
    
*   Activity logging implemented for auditing and traceability.
    

Final Notes
===========

This backend demonstrates:

*   Secure authentication architecture
    
*   Clean RESTful API design
    
*   Production-ready configuration
    
*   Proper separation of concerns
    
*   Defensive programming practices