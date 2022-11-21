from django.contrib import admin
from django.urls import path
import blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog.site.urls)
]
