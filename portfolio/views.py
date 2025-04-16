from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    current_projects = Project.objects.filter(current=True)
    completed_projects = Project.objects.filter(current=False)[:3]  # Limit to 3 projects
    context = {
        'current_projects': current_projects,
        'completed_projects': completed_projects,
        'is_homepage': True,  # Flag to identify homepage view
    }
    return render(request, 'portfolio/index.html', context) # Renders the index.html template and pass the projects to the template


def project_redirect(request, pk):
    project = get_object_or_404(Project, pk=pk)  # Get the specific project

    
    return redirect('home') # Or another appropriate view


def about(request):
    return render(request, 'portfolio/about.html') # Renders the index.html template and pass the projects to the template


def projects(request):
    current_projects = Project.objects.filter(current=True)
    completed_projects = Project.objects.filter(current=False)  # No limit
    context = {
        'current_projects': current_projects,
        'completed_projects': completed_projects,
        'is_homepage': False,  # Flag to identify projects page
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def send_email(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            # Email content
            subject = f'Portfolio Contact: Message from {name}'
            email_body = f"""
You have received a new message from your portfolio contact form.

Sender Details:
- Name: {name}
- Email: {email}

Message:
{message}

---
This email was sent from your portfolio contact form.
"""
            
            send_mail(
                subject=subject,
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,  
                recipient_list=['celynekydd@gmail.com'],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            
        except Exception as e:
            print(f"Email error: {str(e)}")  # For debugging
            messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
    
    return redirect('portfolio:home')

