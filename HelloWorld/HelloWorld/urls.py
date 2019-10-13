"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from book import views
from . import view
urlpatterns = [
   url(r'login_user',views.login_user),
   url(r'admin', views.jinru),
   url(r'html', view.html),
   url(r'updown', view.kugou),
   url(r'insert', views.insert),
   url(r'truncate', views.truncate),
   url(r'update', views.update),
   url(r'test',views.test),
   url(r'mohuselect', views.get),
   url(r'qqmusic', views.qqmusic),
   
    
]
