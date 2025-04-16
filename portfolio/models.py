from django.db import models
from django.urls import reverse


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name of the technology (e.g., Python, Django)")
    icon = models.ImageField(upload_to='technology_icons/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Technologies"
    
    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True, help_text="Live website URL")
    technologies = models.ManyToManyField(Technology, blank=True, help_text="Technology used in this project")
    current = models.BooleanField(default=False, help_text="Check if this is a project you're currently working on")
    TYPES = (
        ('DEVOPS', 'DevOps Projects'),
        ('AUTOMATION', 'AI & Automation'),
        ('FIT_WEATHER', 'Fitness & Weather'),
        ('BUSINESS_FINDER', 'Business Finder'),
        ('BLOG', 'Blog'),
        ('WEATHER_APP', 'Weather App'),
        ('MACHINE_LEARNING', 'Machine Learning'),
        ('DATA_VISUALIZATION', 'Data Visualization'),
        ('WEB_DEVELOPMENT', 'Web Development'),
        ('MOBILE_APP', 'Mobile App Development'),
        ('E_COMMERCE', 'E-Commerce'),
        ('OTHER', 'Other')
        )
    
    type = models.CharField(max_length=50,
                  choices=TYPES,
                  default="OTHER")
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)]) 
    
    def __str__(self):
        return self.title

