# lista-de-exercicios-python-brasil

Objetivo desse repositório e ajudar alunos aprendendo lógica de programação imperativa com Python a praticarem a validarem seu conhecimento.
Esse repositório contém testes para os [exercícios da wiki da Python Brasil](https://wiki.python.org.br/ListaDeExercicios)

## Como o projeto está organizado?

Os pacotes do projeto possuem o mesmo nome de cada uma das sessões da lista de exerícios.
Dentro de cada se encontra um arquivo python com um doctest que valida a correta implementação do problema.



## Como fazer os exercícios?

Você deve clonar esse repositório e resolver cada exercício. Ao enviar para o seu repositório, o servidor de integração do Github (Github Action) vai corrigir seu exercício, informando se há falhas.
Assim você consegue evoluir com a certeza de entender os conceitos ;)

## Como contribuir para o projeto?

1. Forke o esse projeto;
2. Crie um script para cada exercício, dentro da pasta referente a seção de exercícios da Python Brasil. Use o arquivo [estrutura_sequencial_01/alo_mundo_01.py](estrutura_sequencial_01/alo_mundo_01.py) como modelo.
3. Crie um doctest para o exercício;
4. Crie uma entrada no [.github/workflows/corretor_de_exercícios.yml](.github/workflows/corretor_de_exercícios.yml) para executar o teste do exercício.
5. Envie um pull request de volta para o projeto original [https://github.com/confraria-devpro/lista-de-exercicios-python-brasil](https://github.com/confraria-devpro/lista-de-exercicios-python-brasil).

Exemplo de código para testar o exerício alo_mundo.py:

```
    - name: Correção do Exercício 01 da sessão de Estrutura Sequencial
      run: |
        python -m doctest -f estrutura_sequencial_01/alo_mundo_01.py
```
A sessão nome é um texto livre. Já o final da última linha aponta para o endereço completo do script, incluindo o pacote (pasta) em que ele se encontra.






