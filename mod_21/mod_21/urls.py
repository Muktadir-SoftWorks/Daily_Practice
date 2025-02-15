"""
URL configuration for mod_21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from course import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('home', views.Studentlist.as_view(), name="student_list"),

    path('create', views.create_student, name="create_student"),
    #path('edit/<int:id>/', views.update_student, name="update_student"),
    #path('delete/<int:id>/', views.delete_student, name="delete_student"),


#class based view
    path('update/<int:id>/', views.UpdateStudentData.as_view(), name="UpdateStudentData"),
    path('delete/<int:id>/', views.DeleteStudent.as_view(), name="DeleteStudent"),
    path('create', views.CreateStudent.as_view(), name="create_student"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)