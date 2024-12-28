from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api import NotesViewSet
router=DefaultRouter()
router.register(r'notes_api',NotesViewSet,basename="notes_api")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path("notes",views.nots,name='notes'),
    path('homework',views.home_work,name='homework'),
    path('youtube',views.tube,name='youtube'),
    path('to_do',views.to_do,name="to_do"),
    path('books',views.books,name="books"),
    path('dic',views.dic,name='dic'),
    path('wiki',views.wiki,name='wiki'),
    path('conv',views.conv,name='conv'),
    path('login',views.log_in,name='login'),
    path('profile',views.profile,name='profile'),
    path('Notes_det/<int:id>',views.notes_det,name='Notes_det'),
    path('delete/<int:pk>',views.delete_note,name='delete'),
    path('delete_homework/<int:pk>',views.home_del,name='delete_homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update_homework'),
    path('delete_pro/<int:pk>',views.delete_pro,name='delete_pro'),
    path('update_todo/<int:pk>',views.update_todo,name='update_todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete_todo'),
    path('delete_pro1/<int:pk>',views.delete_pro1,name='delete_pro1'),
    path('register',views.register,name='register'),
    path('logout',views.log_out,name='logout'),
    path('chat',views.chat,name="chat"),

   
    
]
urlpatterns+=router.urls