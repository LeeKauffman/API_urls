API de URLs

Esta é uma API simples para gerenciar URLs em um banco de dados PostgreSQL. A API oferece operações básicas de CRUD (Create, Read, Update, Delete) para manipular URLs.

Configuração antes de executar a aplicação, certifique-se de ter o Docker e o Docker Compose instalados em sua máquina. 
Isso garantirá que você possa facilmente configurar e executar o banco de dados PostgreSQL necessário para a aplicação.

Instalação e Execução 
Clone este repositório em sua máquina local: 
git clone https://github.com/LeeKauffman/API_urls.git

Navegue até o diretório clonado: 
cd urls-api

Execute o comando Docker Compose para construir e iniciar o contêiner do banco de dados PostgreSQL: 
docker-compose up -d

Após o banco de dados estar em execução, você pode iniciar a aplicação Flask. Certifique-se de ter o Python e as dependências do projeto instaladas. 
Você pode instalar as dependências executando: 
pip install -r requirements.txt

Com as dependências instaladas, você pode iniciar a aplicação Flask: python app/main.py A aplicação será executada em http://localhost:5000/.

Uso da API A API oferece os seguintes endpoints:

POST /urls: Cria uma nova URL. 
GET /urls: Retorna todas as URLs armazenadas no banco de dados. 
PUT /urls/<url_id>: Atualiza a URL com o ID especificado. 
DELETE /urls/<url_id>: Exclui a URL com o ID especificado.
