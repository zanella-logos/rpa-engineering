# Fundamentos de RPA confiável

Uma automação confiável precisa comprovar o resultado de cada ação relevante. Uma atividade terminar sem exceção significa apenas que a ferramenta executou a tentativa; isso não confirma que o sistema aceitou a operação.

## Ciclo recomendado

1. Localizar o elemento ou recurso correto.
2. Inspecionar o estado atual.
3. Executar a ação.
4. Verificar o efeito esperado.
5. Registrar evidência suficiente para diagnóstico.
6. Encerrar ou encaminhar a falha de forma explícita.

## Estado técnico e estado de negócio

Um clique pode ocorrer sem que um pedido seja enviado. Uma chamada pode responder sem que o registro fique disponível. Um workflow pode terminar sem exceção e ainda deixar o processo incompleto.

Defina uma condição observável para o resultado esperado, como:

- mensagem de confirmação;
- mudança de status;
- desaparecimento do formulário;
- criação de registro;
- presença de arquivo ou item de fila;
- resposta de API com conteúdo validado.

## Falhas explícitas

Estados desconhecidos não devem cair automaticamente no ramo de sucesso ou no estado oposto. Se os valores válidos são `ATIVO` e `INATIVO`, texto vazio ou inesperado deve gerar diagnóstico próprio.

## Retomada

Uma execução retomada não deve pressupor que o trabalho anterior está completo. Reconcilie o estado esperado com o estado existente e processe somente o que falta, preservando idempotência.

