"""
URL configuration for projeto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from django.contrib import admin
#from django.http import HttpResponse
from django.urls import path, include
from .views import CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList

#def my_view(request):
#    return HttpResponse('Uma linda String')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    
    # path('editar/campo/<tipo:name>/')
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    
    # path('editar/campo/<tipo:name>/')
    path('deletar/campo/<int:pk>/', CampoDelete.as_view(), name='deletar-campo'),
    path('deletar/atividade/<int:pk>/', AtividadeDelete.as_view(), name='deletar-atividade'),
    
    # path('editar/campo/<tipo:name>/')
    path('listar/campo/', CampoList.as_view(), name='listar-campo'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade'),
]
