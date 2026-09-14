# Configurações e credenciais em Python no Windows

Automações não devem guardar senhas ou tokens no código-fonte. Uma opção para aplicações desktop no Windows é separar configurações operacionais de segredos protegidos pelo cofre do usuário.

## Separação

| Dado | Armazenamento sugerido |
|---|---|
| Identificador da automação, ambiente lógico e opções não sensíveis | Arquivo de configuração local ou variável de ambiente |
| Senha, token e chave de API | Windows Credential Manager por meio de `keyring` |

Hosts, nomes de banco e usuários também podem revelar a infraestrutura. Mesmo quando não concedem acesso isoladamente, evite colocá-los em exemplos públicos.

## Cuidados

- O cofre pertence ao usuário do Windows. Configure o segredo com a mesma conta que executa a automação agendada.
- Falhe com mensagem clara quando um segredo obrigatório estiver ausente.
- Nunca substitua silenciosamente senha ausente por string vazia.
- Não registre o valor recuperado.
- Para contêineres e servidores, avalie um gerenciador de segredos próprio do ambiente.

Veja o [exemplo seguro](../../examples/python/keyring/README.md).

