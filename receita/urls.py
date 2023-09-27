from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome-da-url')
    path('', IndexView.as_view(), name='home'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]

