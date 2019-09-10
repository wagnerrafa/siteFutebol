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

class Marcar_Jogo(models.Model):
  
  LUGAR = (
        ( "G" , "Gramado" ),
        ( "S" , "Society" ),
        ( "F" , "Futsal" ),
        ( "T" , "Taqueada" ),
    )

  name = models.CharField(max_length=255)
  time = models.CharField(max_length=255)
  end = models.CharField(max_length=255)
  tel = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  date = models.CharField(max_length=255)
  lugar = models.CharField(max_length = 255, choices = LUGAR)
  msg = models.CharField(max_length=255)
  criado = models.DateField(auto_now_add=True)
  placarCasa = models.IntegerField(null=True)
  placarFora = models.IntegerField(null=True)
  def __str__(self):
    return self.name
   
  

  
