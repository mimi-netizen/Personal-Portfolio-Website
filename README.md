# Portfolio Website

A modern, responsive portfolio website built with Django and Bootstrap. This website showcases my professional work, skills, and experience as a DevOps Engineer and Full-Stack Developer.

## About
A modern portfolio website with integrated Content Management System (CMS) built with Django and Bootstrap. This platform combines professional portfolio presentation with powerful content management capabilities, allowing dynamic updates to projects and content through an administrative interface.

### CMS Features
- Secure admin dashboard for content management
- Dynamic project creation and editing
- Integrated media management system
- Role-based access control
- Persistent storage for content and media
- SEO-friendly content structure

## Features

- Responsive design using Bootstrap 5
- Dynamic project showcase
- Contact form
- Smooth scroll navigation
- Dark theme with green accents
- Social media integration

## Technologies Used

- Django 
- Python
- Bootstrap 5
- HTML/CSS
- JavaScript
- SQLite (Database)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/mimi-netizen/Django_portfolio_site.git
cd Django_portfolio_site
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
Django_portfolio_site/
├── portfolio/           # Main app directory
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   ├── models.py       # Database models
│   └── views.py        # View functions
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Contact

- Email: celynekydd@gmail.com
- LinkedIn: [Celyne Kydd](https://linkedin.com/in/celyne-kydd)

## License

© 2025 Celyne Kydd. All rights reserved.
