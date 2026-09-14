# Workflow encerrado com falso sucesso

## Contexto

Um workflow termina normalmente e o framework registra sucesso, embora uma etapa obrigatória não tenha sido executada.

## Sintomas

- A execução termina sem exceção.
- Logs da etapa final estão ausentes.
- Parte dos itens foi classificada, mas não entrou na consolidação.
- Um ramo de decisão termina sem próxima atividade.

## Causa raiz

O fluxo possuía uma saída silenciosa. Além disso, um estado desconhecido era tratado como estado conhecido, e controles por item não eram reiniciados corretamente. O framework interpretou o retorno normal como conclusão do processo.

## Solução

1. Enumere todos os estados válidos.
2. Trate valor desconhecido como erro explícito.
3. Reinicie controles no início de cada item.
4. Evite duplicações nas coleções usadas pela decisão final.
5. Faça cada saída convergir para finalização confirmada ou tratamento de erro.
6. Defina a condição de sucesso a partir do resultado consolidado.

## Validação

Cubra combinações de itens processados, já concluídos, desconhecidos e com falha. Verifique que nenhum caminho termina sem finalização ou erro registrado.

## Prevenção

Revise o grafo do workflow procurando ramos sem destino. Use estados explícitos e invariantes para conferir se todos os itens esperados foram contabilizados.

## Conhecimento reutilizável

Retorno normal de uma função ou workflow não prova que o processo atingiu seu estado final obrigatório.

