import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Task

# Testes com pytest e pytest-django

@pytest.mark.django_db
def test_create_task():
    # Criando o usuario
    user = User.objects.create_user(
        username='henrique',
        email='henriquesilveira@penseavanti.com.br',
        password='jobber123'
    )
    # Criando o job
    task = Task.objects.create(
        title='Teste criar tarefas',
        description='Teste criar tarefas',
        owner=user
    )
    
    assert task.title == 'Teste criar tarefas'
    assert task.description == 'Teste criar tarefas'
    assert task.owner == user
    assert task.priority == 'Normal'
    assert task.status == 'Todo'
    assert task.created_at is not None
    assert task.due_date is None

@pytest.mark.django_db
def test_default_priority():
    # Criando o usuario
    user = User.objects.create_user(
        username='henrique',
        email='henriquesilveira@penseavanti.com.br',
        password='jobber123'
    )
    
    # Criando o job
    task = Task.objects.create(
        title='Teste criar tarefas',
        description='Teste criar tarefas',
        owner=user
    )
    # Verificando se o default do priority foi corretamente
    assert task.priority == 'Normal'

@pytest.mark.django_db
def test_default_status():
    # Criando o usuario
    user = User.objects.create_user(
        username='henrique',
        email='henriquesilveira@penseavanti.com.br',
        password='jobber123'
    )
    
    # Criando o job
    task = Task.objects.create(
        title='Test Task with Default Status',
        description='This task should have default status.',
        owner=user
    )
    # Verificando se o default do status foi corretamente
    assert task.status == 'Todo'
    
@pytest.mark.django_db
def test_upload_large_image():
    # Cria um usuário
    user = User.objects.create_user(
        username='henrique',
        email='henriquesilveira@penseavanti.com.br',
        password='jobber123'
    )

    # Cria um arquivo de imagem simulado maior que 8MB
    large_image = SimpleUploadedFile(
        "test_image.jpg",  # Nome do arquivo
        b"\x00" * (8 * 1024 * 1024 + 1),  # Conteúdo do arquivo: um pouco maior que 8MB
        content_type="image/jpeg"
    )

    # Tenta criar uma tarefa com a imagem grande e verifica se ocorre um erro de validação
    with pytest.raises(ValidationError, match="A imagem não pode exceder 8 MB."):
        task = Task(
            title='Job com imagem grande',
            description='Testando Job com upload de imagem maior que 8MB',
            owner=user,
            image=large_image
        )
        task.full_clean()  # Valida manualmente o modelo