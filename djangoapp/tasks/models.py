from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

def validate_image_size(image):
    max_size_mb = 8  # Tamanho máximo permitido em MB
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"A imagem não pode exceder {max_size_mb} MB.")

# Modelo das Task
class Task(models.Model):
    title = models.CharField(max_length=255) # Titulo do Job
    created_at = models.DateTimeField(auto_now_add=True) # Data de criação
    description = models.TextField() # Descricao do Job 
    image = models.ImageField(upload_to='job_images/', blank=True, null=True, validators=[validate_image_size])
    due_date = models.DateField(blank=True, null=True) # Prazo de entrega
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos') # Usuario que criou o Job
    priority = models.CharField(max_length=255, default='Normal')  # Prioridade do Job 
    status = models.CharField(max_length=255, default='Todo')  # Status do Job

    def __str__(self):
        return self.title
