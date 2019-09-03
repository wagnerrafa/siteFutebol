from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
  nome = models.CharField(max_length=255)
  resumo = RichTextField()
  author = models.CharField(max_length=255)
  image = models.ImageField((""), upload_to="")
  created_at = models.DateField(auto_now_add=True)
  def __str__(self):
    return self.nome
