from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView
from stf.views import *


urlpatterns = [
    path('api/v1/', include(('base.routers', 'base'), namespace='api')),
    path('admin/', admin.site.urls),
    path('', include('stf.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', auth_views.LogoutView.as_view(template_name='registration/signup.html'), name='signup'),
    path('accounts/profile/', update_profile, name="profile"),
    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),
    ]
