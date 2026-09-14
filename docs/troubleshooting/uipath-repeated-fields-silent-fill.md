# Preenchimento silencioso no campo errado em formulários repetidos

## Contexto

Um workflow UiPath preenche vários destinatários ou registros apresentados como cartões repetidos. A atividade `Type Into` termina sem exceção, mas um campo obrigatório continua vazio ou recebe o valor destinado a outro cartão.

## Sintomas

- O log informa que todos os campos foram preenchidos.
- O portal recusa a operação por ausência de nome, e-mail ou outro valor obrigatório.
- O seletor estrito contém apenas atributos genéricos, como `tag='INPUT'` e `type='text'`.
- Aumentar atrasos não corrige a falha.
- A operação externa não aparece na consulta posterior.

## Causa raiz

O workflow tratava a conclusão da atividade de digitação como confirmação do preenchimento. Em uma página com vários `INPUT` semelhantes, o seletor não identificava de forma única o campo dentro do cartão correto. Também não havia validação prévia dos dados nem pós-condição que confirmasse o valor persistido.

## Solução

1. Valide os valores obrigatórios antes de acessar a interface.
2. Gere erro de negócio descritivo quando um dado obrigatório estiver vazio.
3. Identifique primeiro o cartão pelo seu título ou chave estável.
4. Localize o campo somente dentro desse cartão.
5. Evite seletores baseados apenas em tipo e tag.
6. Limpe e focalize o campo antes de digitar.
7. Leia o valor preenchido ou configure verificação de execução.
8. Após a ação final, consulte um estado observável antes de registrar sucesso.

Exemplo de validação em VB.NET:

```vb
If String.IsNullOrWhiteSpace(recipientName) OrElse
   String.IsNullOrWhiteSpace(recipientEmail) Then
    Throw New BusinessRuleException("Dados obrigatórios do destinatário ausentes")
End If
```

## Validação

- Teste valores válidos, nome vazio e e-mail vazio.
- Teste vários cartões com estrutura idêntica.
- Confirme que cada valor aparece somente no cartão esperado.
- Simule resposta lenta do portal.
- Confirme que o log de sucesso ocorre somente após localizar a operação criada.

## Prevenção

Trate ações de interface como tentativa, não como resultado. Campos repetidos exigem relação explícita entre contêiner e elemento, e toda operação externa deve possuir pós-condição verificável.

## Conhecimento reutilizável

`Type Into` sem exceção comprova que o UiPath executou uma interação. Não comprova que o sistema recebeu o valor no campo correto.

