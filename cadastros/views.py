from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, Atividade
from django.urls import reverse_lazy


############ CREATE
class CampoCreate(CreateView):
    model = Campo
    fields = ['name', 'description']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')
    
class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['number', 'description', 'points', 'details', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')



############ UPDATE
class CampoUpdate(UpdateView):
    model = Campo
    fields = ['name', 'description']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')
    
class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['number', 'description', 'points', 'details', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')



############ DELETE
class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campo')
    
class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividade')



############ LIST
class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'
    
class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'
    success_url = reverse_lazy('home')