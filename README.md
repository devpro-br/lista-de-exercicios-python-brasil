# Projeto de resolução de exercício Python Brasil

Objetivo desse repositório é ajudar alunos aprendendo lógica de programação imperativa com Python a praticarem a validarem seu conhecimento.
Esse repositório contém testes para os [exercícios da wiki da Python Brasil](https://wiki.python.org.br/ListaDeExercicios)

# Instruções para quem vai apenas resolver os exercícios
## Como o projeto está organizado?

Os pacotes do projeto possuem o mesmo nome de cada uma das sessões da lista de exercícios.
Dentro de cada se encontra um arquivo python com um doctest que valida a correta implementação do problema.

## Como fazer os exercícios?

Você deve forkar esse repositório e resolver cada exercício. Ao enviar para o seu repositório, o servidor de integração do Github (Github Action) vai corrigir seu exercício, informando se há falhas.
Assim você consegue evoluir com a certeza de entender os conceitos ;)

# Instruções para quem quer acrescentar exercícios no projeto
## Como contribuir para o projeto?

1. Forke o esse projeto;
2. Crie um script para cada exercício, dentro da pasta referente a seção de exercícios da Python Brasil. Use o arquivo [secao_01_estrutura_sequencial/ex_01_alo_mundo.py](secao_01_estrutura_sequencial/ex_01_alo_mundo.py) como modelo.
3. Use o padrão de nomenclatura para os scritps `ex_dd_nome_do_arquivo`. Ou seja, comece sempre com o sufixo "ex_" seguindo do número do exercício. Assim a ordem alfabética dos arquivos ficará na mesma sequência que os exercícios da lista.
4. Crie um doctest para o exercício;
5. Crie uma entrada no [.github/workflows/corretor_de_exercícios.yml](.github/workflows/corretor_de_exercícios.yml) para executar o teste do exercício.
6. Envie um pull request de volta para o projeto original [https://github.com/confraria-devpro/lista-de-exercicios-python-brasil](https://github.com/confraria-devpro/lista-de-exercicios-python-brasil).

Exemplo de código para testar o exercício alo_mundo.py:

```
    - name: Correção do Exercício 01 da seção de Estrutura Sequencial
      if: always()
      run: |
        python -m doctest -f secao_01_estrutura_sequencial/ex_01_alo_mundo.py
```
A seção nome é um texto livre. Já o final da última linha aponta para o endereço completo do script, incluindo o pacote (pasta) em que ele se encontra.






