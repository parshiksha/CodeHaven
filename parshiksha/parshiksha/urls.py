from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('authentication/', include('authen.urls')),
    path('admin/', admin.site.urls),
    path('profile/', include('userprofile.urls')),
    path('practice/', include('codeditor.urls')),  
    path('problems/', include('problems.urls')),  
]
