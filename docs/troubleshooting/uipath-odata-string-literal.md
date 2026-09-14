# Filtro OData inválido por texto livre

## Contexto

Uma automação consulta itens existentes antes de adicionar um novo registro. O filtro usa como referência um texto recebido de sistema externo.

## Sintomas

- A atividade de consulta falha apenas para alguns itens.
- A API informa literal de texto não terminado ou consulta inválida.
- Valores simples funcionam; valores com apóstrofos ou quebras de linha falham.

## Causa raiz

O valor externo foi inserido em um literal OData sem o escape adequado. Um apóstrofo passou a ser interpretado como delimitador da expressão. Espaços e quebras de linha também tornaram a referência inconsistente.

Construtores visuais podem ainda rejeitar expressões complexas aplicadas diretamente no campo do filtro.

## Solução

1. Normalize espaços e quebras de linha em uma etapa anterior.
2. Preserve o conteúdo significativo do identificador.
3. Aplique o escape definido pelo OData: dentro de um literal, represente `'` como `''`.
4. Passe uma variável simples e já preparada para a atividade de consulta.

Remover o apóstrofo indiscriminadamente pode alterar o identificador e criar colisões. Quando possível, use uma chave técnica estável em vez de texto livre.

## Validação

Teste ao menos valores com:

- apóstrofo;
- espaços no início e no fim;
- quebra de linha;
- caracteres acentuados;
- texto vazio;
- texto repetido após normalização.

Confirme que a consulta continua distinguindo referências diferentes.

## Prevenção

Centralize a preparação de valores usados em filtros. Nunca monte expressões OData por concatenação sem conhecer as regras de escape do tipo utilizado.

## Conhecimento reutilizável

Dados válidos para exibição não são necessariamente seguros para uma linguagem de consulta. Normalize e escape conforme o protocolo, sem destruir a identidade do valor.

