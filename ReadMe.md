## Descrição

Esse projeto tem por finalidade ensinar o desenvolvimento web com python para a turma da disciplina eletiva de pyhton do centro universitário Santa Cruz.

Criamos uma pagina web, que realiza a apresentação da turma, demonstra serviços e página de contato.

Esse projeto utiliza o framework Flask, FastAPI e SQLite para o seu desenvolvimento.

## Estrutura do Projeto
- **main:** Contém os controladores para cada entidade (categoria, estoque, fornecedores, pessoas, funcionários, clientes, vendas);
- **api_app:** Contém os Data Access Objects (DAO) responsáveis pela interação com o banco de dados ou arquivos de dados;
- **create_db:** Contém as classes de modelo para representar as entidades do sistema;
- **Estrutura HTML:** As páginas em HTML estão salvas na pasta templates, onde temos home, serviços e contato.
- **Estrutura CSS:** Estão localizados nos arquivos estáticos na pasta style, onde temos home, serviços e contato.
- **Estrutura de imagens:** Estão localizados nos arquivos estáticos na pasta img. 
- **README.md:** Este arquivo.

## Estrutura de Diretórios

/  
├── Projeto_Flask (pasta principal)  
│   ├── static (pasta de arquivos estáticos)  
│   │   ├── img (pasta de imagens dentro da pasta static)  
│   │   │   ├── 01_servico.jpg  
│   │   │   ├── 02_servico.jpg  
│   │   │   ├── 03_servico.jpg  
│   │   │   ├── lab.jpg  
│   │   │   ├── logo_usc.png  
│   │   │   └── sala.jpg  
│   │   └── style (pasta de arquivos css dentro da pasta static)  
│   │       ├── reset.css   
│   │       ├── style_contact.css  
│   │       ├── style_home.css  
│   │       └── style_services.css  
│   ├── templates (pasta de arquivos html)  
│   │   ├── contact.html  
│   │   ├── home.html  
│   │   └── services.html  
│   ├── ReadMe.md  
│   ├── api_app.py  
│   ├── create_db.py  
│   └── main.py   
   

Pouco a pouco vamos incrementando esse código e deixando mais robustos.

Esse projeto utiliza Python, HTML e CSS, onde utilizamos o framework FLASK, FastAPI, SQLite, Uvicorn e requests.
