# Filtro de data rejeitado em consulta OData

## Contexto

Uma atividade busca itens recentes usando parâmetros de data. Após atualização de pacote, mudança de endpoint ou alteração de configuração, a consulta passa a ser rejeitada.

## Sintomas

- A consulta funciona sem intervalo de datas.
- Ao preencher data inicial ou final, a API retorna opções de consulta inválidas.
- O erro ocorre antes do processamento dos resultados.

## Causa raiz

A atividade gerou uma expressão de data incompatível com o endpoint ou com a versão da API utilizada. Formato, fuso horário, precisão ou combinação de parâmetros podem alterar a expressão final.

## Solução

1. Capture a estrutura da requisição sem registrar dados dos itens.
2. Confirme formato, fuso horário e operador aceitos pelo endpoint.
3. Teste os parâmetros de data isoladamente.
4. Atualize a atividade ou ajuste o filtro conforme a documentação da versão em uso.
5. Se o endpoint não aceitar o filtro, consulte um intervalo controlado e filtre em memória.

Filtragem em memória é contingência, não correção universal. Ela pode aumentar paginação, tráfego e consumo de memória.

## Validação

- Teste data inicial, data final e intervalo completo.
- Inclua registros exatamente nos limites.
- Verifique conversão entre horário local e UTC.
- Confirme paginação e volume máximo esperado.

## Prevenção

Trate filtros de data como contratos de integração versionados. Após atualizar pacote ou API, valide a consulta gerada antes de liberar a automação.

## Conhecimento reutilizável

Uma expressão válida em uma versão ou endpoint pode ser rejeitada em outro. Diagnostique a consulta efetivamente enviada, não apenas os valores mostrados no editor visual.

