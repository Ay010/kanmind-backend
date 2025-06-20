from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.api.urls')),
    path('api/', include('user_auth.api.urls')),
    path('api/', include('boards.api.urls')),
]
