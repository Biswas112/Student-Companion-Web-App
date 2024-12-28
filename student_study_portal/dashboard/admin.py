from django.contrib import admin
from .models import *

@admin.register(notes)
class admin_notes(admin.ModelAdmin):
    list_display=['id','title','description']
    
@admin.register(homework)
class admin_homework(admin.ModelAdmin):
    list_display=['subject','title','description','due','is_finished']
    
@admin.register(Todo)
class admin_todos(admin.ModelAdmin):
    list_display=['title','is_finished']
    

    
