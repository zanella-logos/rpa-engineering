# Interagir e verificar o resultado

Interfaces web podem aceitar um clique tecnicamente sem executar o efeito esperado. O padrão abaixo reduz sucessos falsos.

## Fluxo

1. Execute a interação nativa com seletor estável.
2. Aguarde uma condição relacionada ao resultado, não apenas um intervalo fixo.
3. Verifique o estado esperado.
4. Quando apropriado, use um fallback no mesmo alvo.
5. Verifique novamente.
6. Sem confirmação, encerre com erro descritivo.

## Fallback com JavaScript

JavaScript pode ajudar quando o elemento está presente no DOM, mas a camada de automação não consegue interagir com ele. O fallback não deve contornar autorização, validação ou regra de negócio.

Operações que abrem `alert`, `confirm` ou `prompt` podem bloquear o retorno da ponte de automação. Quando a ferramenta precisa retornar antes da abertura do diálogo, agende a interação e trate a confirmação na etapa seguinte.

## Listas e cards

Em páginas com itens repetidos, limite a busca pelo identificador do item atual antes de localizar o botão de ação. Após atualizar a página, confirme que filtros e resultados foram restaurados.

