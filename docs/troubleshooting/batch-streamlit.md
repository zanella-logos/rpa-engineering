# Scripts Batch e inicialização do Streamlit

Quando um launcher `.bat` falha apenas em determinada máquina, investigue codificação, terminações de linha, expansão de variáveis e comandos dentro de blocos entre parênteses.

## Diagnóstico

- Confirme que o arquivo é realmente executado pelo `cmd.exe`.
- Compare codificação e terminações de linha com um script mínimo funcional.
- Execute cada comando separadamente.
- Reduza blocos condicionais complexos.
- Verifique qual Python e ambiente virtual foram resolvidos.

Arquivos Batch são tradicionalmente distribuídos com CRLF para máxima compatibilidade no Windows, mas LF isoladamente não deve ser tratado como causa universal. Reproduza o comportamento na versão real do Windows antes de concluir a causa raiz.

Aplicações Streamlit também podem solicitar configuração inicial em contexto interativo. Para execução automatizada, defina previamente as opções suportadas pela versão utilizada e valide que o processo inicia sem esperar entrada no terminal.

