# Servidor de Desafios


Servidor em Flask para inserir e testar os desafios presentes na materia de Desenvolvimento de Software do Insper



## Dependencies

Python 3.9.x + Bibliotecas

SQLite3

## Installing

Instale as bibliotecas presentes no arquivo requirements.txt

usando :

```
pip install -r requirements.txt
```

Installe o SQLite3 pelo [link](https://www.sqlite.org/index.html)

## Executing program

### Criando Banco

Utilize os scripts [Quiz](src/quiz.sql) e o [User](src/user.sql) para criar seu banco de dados

### Adicionando usuario

Antes de executar o servidor é preciso que crie um usuário no seu banco de dados SQLite3. Para isso utilize o programa [AddUser](src/adduser.py)

### Executando servidor

Assim que tiver inserido o usuário rode o servidor com o comando

```
python softdes.py
```

![alt text](img/terminal.png?raw=true "Terminal")

Isso ira abrir um portal que pode ser acessado pelo link

http://192.168.15.9:80/

![alt text](img/portal.png?raw=true "Portal")

## Documentation

Para mais informações e documentações de Aluno, Professor e/ou Desenvoledor acesse o nosso [Docs](docs)
