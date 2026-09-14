# Ação de interface sem confirmação do resultado

## Contexto

Uma automação aciona um botão e registra sucesso porque a atividade terminou sem exceção. Posteriormente, descobre-se que o formulário permaneceu aberto e a operação não foi concluída.

## Sintomas

- O log informa sucesso, mas o efeito esperado não existe.
- A interface permanece no mesmo estado.
- Reexecutar o clique manualmente conclui a ação.
- A falha ocorre de forma intermitente sob lentidão ou atualização assíncrona.

## Causa raiz

O fluxo confundiu sucesso técnico da tentativa com sucesso da operação. A atividade comprovou apenas que enviou a interação ao elemento.

## Solução

1. Execute a interação nativa.
2. Aguarde uma condição ligada ao resultado.
3. Verifique mensagem, status, desaparecimento do formulário ou outro efeito observável.
4. Quando seguro, tente um fallback no mesmo alvo.
5. Verifique novamente.
6. Sem confirmação, encerre com erro descritivo.

Antes de repetir uma ação, confirme que ela é idempotente ou que não foi processada silenciosamente.

## Validação

Teste o caminho normal, resposta lenta, clique sem efeito e resultado incerto. O log de sucesso deve aparecer somente após a confirmação do estado final.

## Prevenção

Defina uma pós-condição para toda ação que produza efeito externo. A validação deve fazer parte da operação, não ser uma etapa opcional de observação.

## Conhecimento reutilizável

Ausência de exceção não comprova resultado de negócio. Automação confiável trabalha com pós-condições explícitas.

