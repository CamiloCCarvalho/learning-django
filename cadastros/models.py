from django.db import models

# Create your models here.
class Campo(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    description = models.CharField(max_length=150, verbose_name='Descrição')
    
    def __str__(self):
        return "{} ({})".format(self.name, self.description)
    
class Atividade(models.Model):
    number = models.IntegerField(verbose_name='Número', unique=True)
    description = models.CharField(max_length=150, verbose_name='Descrição')
    points = models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Pontos')
    details = models.CharField(max_length=100, verbose_name='Detalhes', null=True, blank=True, default='Sem detalhes')
    
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{} ({}) - [{}]".format(self.number, self.description, self.campo.name)
    
    
    