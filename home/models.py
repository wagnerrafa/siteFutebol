from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Post(models.Model):
  nome = models.CharField(max_length=255)
  resumo = RichTextField()
  content = RichTextUploadingField()
  author = models.CharField(max_length=255)
  image = CloudinaryField('imagem')
  created_at = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.nome
