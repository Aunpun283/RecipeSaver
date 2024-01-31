"""
URL configuration for Backend project.

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
from django.urls import path
from . import routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_recipe', routes.add_recipe),
    path("fetch_recipe_using_ownerid",routes.fetch_recipe_list_with_ownerid),
    path("fetch_recipe",routes.fetch_recipe),
    path('add_ingredient',routes.add_ingredient),
    path("add_instruction",routes.add_instruction),
    path("del_recipe",routes.del_recipe)
]
