# Ambiente virtual herdado por subprocesso

## Contexto

Um processo Python executado em ambiente virtual inicia outra automação. A aplicação filha deveria usar dependências próprias, mas recebe o ambiente do processo pai.

## Sintomas

- A automação funciona quando iniciada manualmente.
- Falha apenas quando chamada pelo orquestrador.
- O erro aponta módulo ausente ou versão incompatível.
- O executável Python resolvido não é o esperado.

## Causa raiz

Subprocessos herdam variáveis de ambiente. `PATH`, `VIRTUAL_ENV`, diretório de trabalho e outras configurações podem direcionar a aplicação filha ao interpretador do processo pai.

## Solução

Prefira chamar explicitamente o interpretador pertencente à aplicação filha. Como alternativa temporária para legados, forneça ao subprocesso um ambiente controlado e registre qual executável foi resolvido.

Não dependa apenas de remover `VIRTUAL_ENV`: o `PATH` ainda pode selecionar um Python inesperado.

## Validação

Compare execução manual e execução pelo processo pai. Em ambas, registre com segurança:

- caminho do interpretador;
- versão do Python;
- diretório de trabalho;
- presença das dependências necessárias.

## Prevenção

Cada automação deve declarar seu interpretador e suas dependências. Launchers e agendadores não devem depender do estado global da máquina.

## Conhecimento reutilizável

Quando um comando funciona manualmente e falha por orquestração, compare primeiro o contexto de execução antes de alterar dependências.

