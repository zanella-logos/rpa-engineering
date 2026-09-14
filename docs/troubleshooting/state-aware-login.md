# Login iniciado em etapa inesperada

## Contexto

Uma automação assume que o login sempre começa pelo campo de usuário. Em sessões reconhecidas, o sistema abre diretamente na senha ou em outra etapa intermediária.

## Sintomas

- O seletor do usuário encontra múltiplos elementos ou nenhum elemento.
- O campo de senha já está visível quando o fluxo tenta preencher o usuário.
- A autenticação funciona após limpar a sessão, mas falha em reutilização normal.

## Causa raiz

O fluxo foi construído como sequência fixa, embora a autenticação seja uma máquina de estados. Sessão persistente, redirecionamento e autenticação parcial podem omitir etapas.

## Solução

1. Detecte a tela apresentada.
2. Execute somente as ações exigidas pelo estado atual.
3. Faça os ramos convergirem antes da próxima etapa comum.
4. Evite preencher o mesmo campo duas vezes.
5. Confirme que a autenticação chegou ao estado esperado.

## Validação

Teste sessão nova, sessão reconhecida, autenticação expirada, erro de credencial e redirecionamento lento.

## Prevenção

Modele autenticações por estados observáveis. Não presuma que todas as telas aparecem em ordem fixa.

## Conhecimento reutilizável

Automação resiliente reage à tela existente, não à tela que deveria existir segundo o caminho ideal.

