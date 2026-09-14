# Configuração e credenciais com `keyring`

Este exemplo separa opções não sensíveis, armazenadas em `config.example.ini`, de uma senha guardada pelo cofre do Windows.

## Preparação

```powershell
python -m pip install keyring
python setup_credentials.py
python load_config.py
```

Copie `config.example.ini` para `config.ini` e mantenha `config.ini` fora do controle de versão caso ele receba valores específicos do ambiente.

O exemplo retorna erro quando a credencial não existe e nunca imprime seu valor.

