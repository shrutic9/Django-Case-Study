# Case Study on Gas Utility Services using Django 

This project is a Django-based web application developed to assist a gas utility company in handling a high volume of customer service requests efficiently. The system enables customers to submit and track their service requests online.

The solution aims to reduce wait times and streamline customer service operations.

## Features
### 1. For Customers:
Submit Service Requests:

Select the type of service.
Track Service Requests:
View the status of submitted requests.
Check the submission date and resolution date.

### 2. For Customer Support Representatives:
Manage Requests:

Update the status of requests (Pending, In Progress, Resolved).

## Codebase Structure
```
GasUtility/
│
├── gasutility/          # Main project settings
│   ├── settings.py
│   ├── urls.py
|   ├── __init__.py
│   └── ...
│
├── service_requests/   
│   ├── models.py        # Database models
│   ├── views.py         # Application views
│   ├── forms.py         # Form definitions
│   ├── templates/
│   │   └── service_requests/
│   │       ├── submit_request.html
│   │       ├── thanks.html
│   │       ├── track_request.html
|   ├── urls.py          # URL Mapping
|   ├── admin.py         # Manage Admin Interface 
|   ├── apps.py          # Configure app
│   └── ...
│
├── db.sqlite3           # DB
|
└── manage.py            # Django management script
