---
status: aceita
tecnologias: [Python, Windows]
---

# ADR 001: controlar explicitamente o ambiente de subprocessos

## Contexto

Um orquestrador Python pode iniciar automações com dependências diferentes. A herança implícita do ambiente virtual do processo pai torna a execução dependente do contexto de inicialização.

## Opções consideradas

1. Remover variáveis do ambiente virtual e depender do Python global.
2. Alterar cada launcher para ativar seu próprio ambiente.
3. Chamar explicitamente o interpretador pertencente a cada automação.

## Decisão

Preferir o caminho explícito do interpretador da automação filha. Quando isso ainda não for possível em um legado, fornecer um ambiente controlado ao subprocesso e registrar o interpretador resolvido.

## Consequências

- Execução mais previsível e diagnóstico mais simples.
- Cada automação passa a declarar seu ambiente de execução.
- Projetos legados podem exigir migração gradual.

## Revisão

Reavaliar quando todas as automações forem empacotadas ou executadas em ambientes isolados por outro mecanismo.

