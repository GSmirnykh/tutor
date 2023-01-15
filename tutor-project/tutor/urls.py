from django.contrib import admin
from django.urls import path
from account import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('addpupil/', views.add_pupil, name='add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
