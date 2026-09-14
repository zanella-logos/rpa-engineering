# Seleção incorreta em listas de cards dinâmicos

## Contexto

Uma página mostra vários cards com a mesma estrutura e os mesmos botões. Um seletor genérico encontra múltiplas correspondências ou aciona o item errado.

## Sintomas

- O seletor encontra vários elementos semelhantes.
- A primeira tentativa funciona após aplicar filtros, mas falha depois de atualizar a página.
- O botão existe, porém pertence a outro card.
- Esperas maiores não corrigem o comportamento.

## Causa raiz

A busca localizou o botão globalmente, sem limitar o escopo ao item atual. Após atualizar a página, filtros e resultados ainda não estavam restaurados ou foram perdidos.

## Solução

1. Localize o card por identificador de negócio fictício ou chave técnica.
2. Exija correspondência única.
3. Busque o botão somente dentro desse card.
4. Após navegação ou atualização, restaure os filtros.
5. Aguarde o card correto, não apenas o carregamento geral da página.
6. Interrompa o fluxo quando houver zero ou múltiplas correspondências.

## Validação

Teste listas com um item, vários itens semelhantes, item ausente, resultado duplicado e atualização da página. Confirme que somente o card esperado muda de estado.

## Prevenção

Modele seletores repetidos como relação entre contêiner e ação: primeiro identifique o item; depois localize a ação dentro dele.

## Conhecimento reutilizável

Esperar mais tempo não recupera filtros perdidos nem corrige seletor sem contexto.

