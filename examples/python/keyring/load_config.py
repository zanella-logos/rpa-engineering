import configparser
from pathlib import Path

import keyring


SERVICE_NAME = "rpa_engineering_example"
SECRET_NAME = "database_password"


def main() -> None:
    config_path = Path(__file__).with_name("config.ini")
    config = configparser.ConfigParser()

    if not config.read(config_path, encoding="utf-8"):
        raise FileNotFoundError("Crie config.ini a partir de config.example.ini.")

    password = keyring.get_password(SERVICE_NAME, SECRET_NAME)
    if password is None:
        raise RuntimeError("Credencial não configurada. Execute setup_credentials.py.")

    print(f"Configuração carregada para {config['database']['server']}.")


if __name__ == "__main__":
    main()

