# Isolamento de ambiente em subprocessos Python

Um processo Python iniciado dentro de um ambiente virtual herda variáveis como `PATH` e `VIRTUAL_ENV`. Se ele iniciar outra automação que deveria usar um interpretador diferente, essa herança pode selecionar dependências erradas.

## Sintoma típico

- O comando funciona quando executado manualmente.
- O mesmo comando falha quando iniciado pelo orquestrador.
- O erro indica módulo ausente ou incompatibilidade de versão.

## Diagnóstico

Compare, nos dois contextos:

- executável Python resolvido;
- valor de `VIRTUAL_ENV`;
- início do `PATH`;
- diretório de trabalho;
- usuário responsável pela execução.

## Opções

1. Chamar diretamente o interpretador do ambiente pertencente à automação filha.
2. Fornecer um ambiente explícito e mínimo ao subprocesso.
3. Padronizar um ambiente virtual por automação.

A primeira opção costuma ser a mais previsível. Remover `VIRTUAL_ENV` sem controlar qual executável será resolvido pelo `PATH` pode apenas trocar um comportamento implícito por outro.

## Validação

Registre o caminho do interpretador no início da execução e teste tanto a chamada manual quanto a chamada pelo processo pai.

