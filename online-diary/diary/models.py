from django.db import models

# Create your models here.


class Pessoa(models.Model):
    
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='foto')
    
    def __str__(self):
        return self.nome
    
    
class Diario(models.Model):
    
    titulo = models.CharField(max_length=255)
    tags = models.TextField()
    texto = models.TextField()
    pessoas = models.ManyToManyField(Pessoa, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.titulo

    def get_tags(self):
    # Retorna as tags como uma lista de palavras, separadas por espaços
        return self.tags.split(' ') if self.tags else []

    def set_tags(self, list_tags, reset=False):
        # Remove espaços ao redor de cada palavra da entrada
        list_tags = [tag.strip() for tag in list_tags]

        if not reset:
            # Obtém as tags existentes e adiciona as novas
            existing_tags = self.get_tags()
            list_tags = existing_tags + list_tags  # Combina mantendo ordem

        # Atualiza as tags como uma única string separada por espaços
        self.tags = ' '.join(list_tags)




        