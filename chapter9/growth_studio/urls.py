"""growth_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from blog.api import BlogSet
from blog.views import blog_detail
from blog.views import blog_list
from homepage.views import index

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blog', BlogSet)

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', blog_list),
    url(r'^blog/(?P<slug>[^\.]+).html', blog_detail, name='blog_view'),
    url(r'^api/', include(apiRouter.urls)),
    url(r'^about-us/$', TemplateView.as_view(template_name='pages/about-us.html')),
    url(r'^api-token-auth/', obtain_jwt_token),
]

urlpatterns += staticfiles_urlpatterns()

