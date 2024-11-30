# Django Case Study on Gas Utility Services

This project is a Django-based web application developed to assist a gas utility company in handling a high volume of customer service requests efficiently. The system enables customers to submit and track their service requests online.

The solution aims to reduce wait times and streamline customer service operations.

## Features
### For Customers:
Submit Service Requests:

Select the type of service.
Track Service Requests:
View the status of submitted requests.
Check the submission date and resolution date.

### For Customer Support Representatives:
Manage Requests:

Update the status of requests (Pending, In Progress, Resolved).
Admin Dashboard:

GasUtilityApp/
│
├── gasutility/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── service_requests/    # Core app for service requests
│   ├── models.py        # Database models
│   ├── views.py         # Application views
│   ├── forms.py         # Form definitions
│   ├── templates/
│   │   └── service_requests/
│   │       ├── submit_request.html
│   │       ├── thanks.html
│   │       ├── track_request.html
│   └── ...
│
└── manage.py            # Django management script
