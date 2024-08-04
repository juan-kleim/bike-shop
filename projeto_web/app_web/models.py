from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    Texto = models.TextField(max_length=3000)


class Comment(models.Model):
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50]  # Retorna os primeiros 50 caracteres do comentário