from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='uploads/produtos/')
    preco_unitario = models.IntegerField(default=0)
    estoque = models.IntegerField(default=0)
    

    @staticmethod
    def get_all_produtos():
        return Produtos.objects.all()
    @staticmethod
    def get_produtos_by_id(ids):
        return Produtos.objects.filter (id__in=ids)