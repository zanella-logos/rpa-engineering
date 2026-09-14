# Seleção de certificado digital no navegador

Pop-ups de certificado pertencem à interface do navegador ou do sistema operacional, não ao DOM da página. Por isso, a estratégia varia entre navegadores e sistemas.

## Princípios

- Localize o certificado por informação exibida e validada.
- Não dependa de coordenadas fixas.
- Não pressuponha quantidade fixa de teclas direcionais.
- Trate Chrome e Firefox como integrações diferentes.
- Use timeout e erro descritivo quando o certificado não aparecer.
- Nunca registre dados completos do titular em logs públicos.

Uma implementação reutilizável deve separar a descoberta do certificado, a interação com o diálogo e a confirmação de que a navegação prosseguiu.

