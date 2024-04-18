from django.urls import path
from . import views

app_name = 'auth_page'

urlpatterns = [
    path('login', views.login_page.as_view(), name='login'),
    path('logout', views.logout_page.as_view(), name="logout"),
    path('register', views.register_page.as_view(), name="register"),
    path('blog', views.blog_page.as_view(), name='blog'),
    path('create', views.create_blog.as_view(), name='create'),
]