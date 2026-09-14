# Falha ao gerar relatório com ProcessingException ausente

## Contexto

Um workflow consulta itens de fila com estado de falha e gera um relatório concatenando propriedades da exceção de processamento.

## Sintomas

- A consulta da fila termina com sucesso.
- O erro ocorre dentro de `For Each` ou `Multiple Assign`.
- A mensagem informa que uma expressão não pode ser atribuída à string de saída.
- O código acessa diretamente `item.ProcessingException.Reason.ToString`.

## Causa raiz

O código assumia que todo item com estado de falha possuía `ProcessingException` e `Reason`. Itens interrompidos, atualizados por caminhos diferentes ou retornados por determinadas versões da API podem não fornecer uma dessas propriedades.

## Solução

Proteja propriedades opcionais antes de montar o relatório:

```vb
If(
    item.ProcessingException Is Nothing OrElse
    item.ProcessingException.Reason Is Nothing,
    "Falha sem motivo registrado",
    item.ProcessingException.Reason.ToString
)
```

Mantenha paginação e filtros locais independentes dessa propriedade. A ausência do motivo não deve impedir a geração do restante do relatório.

## Validação

- Teste item com exceção e motivo preenchidos.
- Teste item sem `ProcessingException`.
- Teste item com `ProcessingException`, mas sem `Reason`.
- Confirme que todos os itens válidos continuam no relatório.

## Prevenção

Trate metadados de erro recebidos de APIs como opcionais. O relatório deve registrar uma descrição neutra quando o serviço não fornecer o detalhe.

## Conhecimento reutilizável

O estado de falha não garante que o objeto de exceção esteja completo. Relatórios operacionais devem tolerar metadados parciais.

