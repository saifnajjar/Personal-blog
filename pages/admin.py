from django.contrib import admin
from .models import Skill
from .models import GeneralSkillText
from .models import Service
from .models import ServiceCategory
from .models import ServiceImage
from .models import Project
from .models import ProjectImage
from .models import Blog
from .models import Comment
from .models import ContactMessage




admin.site.register(Skill)
admin.site.register(GeneralSkillText)
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(ServiceImage)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(ContactMessage)



