# Backend

## CRUD
o Django utiliza o ORM (Object-Relational Mapping) para interagir com o banco de dados. O Django ORM permite que você defina seus modelos de dados como classes Python e, a partir dessas classes, o Django cuida da criação das tabelas no banco de dados e das operações CRUD (Create, Read, Update, Delete) de forma automática.

Vantagens da ORM: Abstração, Integração, Performace e Portabilidade.

_Como eu não possuo necessidades específicas que exigem controle mais fino sobre o SQL, optei por usar o ORM._

## Pillow
No modelo de tarefas (Task) e no modelo de usuários (User), estou utilizando __ImageField__ para armazenar imagens, como fotos de perfil e imagens relacionadas a tarefas. O ImageField exige o Pillow para:

- **Upload de Imagens**: Permite que você faça o upload de arquivos de imagem nos campos definidos.
- **Validação de Imagens**: Verifica se o arquivo enviado é uma imagem válida.
- **Redimensionamento e Manipulação**: Facilita o redimensionamento, corte ou aplicação de outras manipulações básicas de imagens, caso você precise implementar isso no futuro.

_Nota: Se o seu backend não usasse Pillow, o Django não conseguiria lidar com campos de imagem corretamente, e você veria erros ao tentar executar operações relacionadas a imagens, como uploads e validações._