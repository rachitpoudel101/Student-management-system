from django.contrib import admin
from django.urls import include, path
from student_management_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', views.showDemoPage),  # Added trailing slash
]
