from django.contrib import admin
from .models import Consultation, Estimate, reviews,Project

admin.site.register(reviews)
admin.site.register(Consultation)
admin.site.register(Estimate)





@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    
    



