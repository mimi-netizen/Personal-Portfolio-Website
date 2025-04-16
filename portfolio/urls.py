from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio' # needed for namespacing

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('send-email/', views.send_email, name='send_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
