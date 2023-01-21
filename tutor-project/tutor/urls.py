from django.contrib import admin
from django.urls import path
from account import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
    path('login/', views.loginuser, name='login'),

    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('addpupil/', views.add_pupil, name='add_pupil'),
    path('addcours/', views.add_cours, name='add_course'),
    path('editpupil/', views.edit_pupil, name='edit_pupil'),
    path('editcours/', views.edit_cours, name='edit_cours'),

    path('pupil/<int:pk>', views.PupilDetailView.as_view(), name='pupil_detail'),
    path('cours/<int:pk>', views.CoursDetailView.as_view(), name='cours_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
