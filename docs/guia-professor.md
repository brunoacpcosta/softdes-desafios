# Guia para Professor

Instruções para professores modificarem a base de dados.

## Adicionando Usuários

Modifique o arquivo csv [Users](https://github.com/brunoacpcosta/softdes-desafios/blob/main/src/users.csv) com o nome e tipo do(s) novo(s) usuário(s) e em seguida rode o script [AddUser](https://github.com/brunoacpcosta/softdes-desafios/blob/main/src/adduser.py) para adicionar as alterações ao banco de dados.

## Adicionando Desafios

Para adicionar um novo desafio é necessário adicioná-lo manualmente no DB. Isso pode ser realizado em um gerenciador de base de dados como o SQLite Studio através do seguinte comando:

```
Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values (#Preencher com parâmetros do desafio);
```

#### Parâmetros:
* numb: Número do desafio (INT)
* release: Data de lançamento (DATE)
* expire: Prazo de entrega (DATETIME)
* problem: Descrição do desafio (TEXT)
* tests: Entradas para os testes (LIST)
* results: Saídas dos testes (LIST)
* diagnosis: Notas possíveis (LIST)

## Documentação

Para mais informações e documentações de Aluno, Professor e/ou Desenvoledor acesse o nosso [Docs](docs)