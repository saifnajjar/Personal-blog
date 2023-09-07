from django.shortcuts import render
from .models import Skill, GeneralSkillText, Service, ServiceCategory, ServiceImage, Project


from django.shortcuts import render, redirect
from .models import Skill, GeneralSkillText, Service, ServiceCategory, ServiceImage, Project
from .forms import ContactForm
from .models import ContactMessage

def index(request):
    skills = Skill.objects.all()
    general_skill_text = GeneralSkillText.objects.first()
    services = Service.objects.all()
    service_categories = ServiceCategory.objects.all()
    projects = Project.objects.all()

    # Create a dictionary to store service images per category
    service_images_per_category = {}
    for category in service_categories:
        images = ServiceImage.objects.filter(service_category=category)
        service_images_per_category[category] = images

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('index')  # توجيه بعد إرسال النموذج
    else:
        contact_form = ContactForm()

    return render(request, 'pages/index.html', {
        'skills': skills,
        'general_skill_text': general_skill_text,
        'services': services,
        'service_categories': service_categories,
        'service_images_per_category': service_images_per_category,
        'projects': projects,
        'contact_form': contact_form,  # إضافة النموذج إلى السياق
    })




from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import ExtractYear
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all().order_by('-publication_date')
    
    
    return render(request, 'pages/all_blogs.html', {'blogs': blogs}) 





from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import CommentForm

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog).order_by('-created_at')
    recent_blogs = Blog.objects.exclude(pk=blog_id).order_by('-publication_date')[:4]

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog

            if request.user.is_authenticated:
                new_comment.user = request.user

            new_comment.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        comment_form = CommentForm()

    return render(request, 'pages/blog_detail.html', {'blog': blog, 'recent_blogs': recent_blogs, 'comments': comments, 'comment_form': comment_form})



from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectComment
from .forms import ProjectCommentForm

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    comments = project.comments.all()  # استرجاع كل التعليقات المرتبطة بالمشروع
    
    if request.method == 'POST':
        form = ProjectCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
    else:
        form = ProjectCommentForm()
    
    context = {
        'project': project,
        'comments': comments,
        'form': form,
    }
    return render(request, 'pages/project_detail.html', context)















  












    






    






