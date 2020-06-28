from django.contrib import admin
from .models import skillSummary, Education, WorkExperience, AchieveAccomplish, memberships, Projects

admin.site.register(skillSummary)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(AchieveAccomplish)
admin.site.register(memberships)
admin.site.register(Projects)