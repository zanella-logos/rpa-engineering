# Diálogo nativo bloqueando JavaScript injetado

## Contexto

Uma automação usa JavaScript injetado para acionar um elemento. O clique abre um diálogo nativo bloqueante, mas a atividade de injeção falha antes de devolver o controle ao workflow.

## Sintomas

- O diálogo aparece visualmente.
- A atividade JavaScript termina com erro de comunicação ou falha genérica.
- A próxima atividade, responsável por confirmar o diálogo, não é executada.

## Causa raiz

Chamadas como `alert`, `confirm` e `prompt` bloqueiam a execução da página. Quando abertas antes do retorno da ponte entre navegador e ferramenta de automação, impedem que a atividade conclua seu protocolo de resposta.

## Solução

Agende o clique para ocorrer logo após o término da função injetada, permitindo que a atividade devolva o controle antes da abertura do diálogo. Trate o diálogo em uma atividade separada.

Use essa técnica somente quando o comportamento bloqueante estiver confirmado. Não a aplique como fallback genérico para qualquer falha de clique.

## Validação

- Confirme que a atividade JavaScript termina antes do diálogo.
- Confirme que o diálogo aparece uma única vez.
- Confirme que a etapa seguinte consegue interagir com ele.
- Valide o estado final produzido pela confirmação.

## Prevenção

Identifique previamente ações que abrem diálogos nativos. Separe o acionamento assíncrono da interação com o diálogo.

## Conhecimento reutilizável

Um diálogo visível não comprova que a atividade que o abriu terminou corretamente. Considere o protocolo de retorno entre página e ferramenta de automação.

