# Automação orientada ao estado da interface

Portais com sessão persistente podem abrir em etapas diferentes. Um fluxo de login que sempre espera usuário, depois senha, falha quando a sessão reconhecida abre diretamente na senha.

## Padrão

1. Detecte o estado atual.
2. Execute apenas as etapas necessárias para aquele estado.
3. Faça os ramos convergirem em uma etapa comum.
4. Valide o efeito produzido pela ação anterior.

Ao substituir um elemento após mudança de interface, valide também o contrato com a próxima etapa. Se a próxima atividade espera uma janela de arquivos, o comando anterior precisa iniciar upload local, não abrir uma tela visualmente semelhante.

