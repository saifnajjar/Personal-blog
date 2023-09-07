from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=0, help_text="Proficiency percentage out of 100")

    def __str__(self):
        return self.name

class GeneralSkillText(models.Model):
    text = models.TextField()

    def __str__(self):
        return "General Skill Text"

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.title

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ServiceImage(models.Model):
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return f"Image for {self.service_category.name}"





class Project(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='project_images/')
    main_description = models.TextField()
    secondary_description = models.TextField()
    summary = models.TextField()
    execution_date = models.DateField()

    def __str__(self):
        return self.title



class ProjectComment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment        

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/secondary/')

    def __str__(self):
        return f"Image for {self.project.title}"

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"

from django.db import models
from django.db.models import Count

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    description = models.TextField()
    secondary_description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, related_name='blog_comments')

    def __str__(self):
        return self.title






from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  



   

    




    




















