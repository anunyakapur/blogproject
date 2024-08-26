"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from blog.views import custom_logout, create_post, post_list, post_detail, edit_post, delete_post
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('create_post/', create_post, name='create_post'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('post/<int:id>/edit/', edit_post, name='edit_post'),
    path('post/<int:id>/delete/', delete_post, name='delete_post'),
    path('', post_list, name='post_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##edit your OWN posts[DONE]
##comment on ANYONE's posts[DONE]
##username displayed with post[DONE]
##post anonymously[DONE]
##allow users to include images in their posts[DONE]

##users can upvote/downvote on different posts
##adding functionality to the search bar