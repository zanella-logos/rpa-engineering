# Filtros OData com texto livre no UiPath

Valores externos usados em filtros OData podem conter apóstrofos, quebras de linha e espaços inesperados. Concatenar esses valores diretamente pode produzir consulta inválida ou alterar seu significado.

## Abordagem

1. Normalize o valor antes de configurar a atividade.
2. Aplique o escape exigido pelo OData. Em literais, um apóstrofo é normalmente representado por dois apóstrofos (`'` → `''`).
3. Passe uma variável simples ao construtor de filtros.
4. Registre a estrutura do erro sem registrar dados pessoais do item.

Remover o caractere pode alterar o identificador e gerar colisões. Prefira escape correto ou uma chave técnica que não dependa de texto livre.

Filtros de data também devem ser verificados contra a versão da atividade e o endpoint usados. Se uma opção for rejeitada, confirme a consulta gerada antes de mover o filtro para memória, pois filtragem local pode aumentar paginação, tráfego e uso de memória.

