
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


app_name = 'users'
urlpatterns = [
    path('signup/', views.register,name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('profile/', views.profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)$', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
