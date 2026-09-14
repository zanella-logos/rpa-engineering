import getpass

import keyring


SERVICE_NAME = "rpa_engineering_example"
SECRET_NAME = "database_password"


def main() -> None:
    password = getpass.getpass("Senha do banco de exemplo: ")
    if not password:
        raise ValueError("A senha não pode ser vazia.")

    keyring.set_password(SERVICE_NAME, SECRET_NAME, password)
    print("Credencial armazenada no cofre do sistema.")


if __name__ == "__main__":
    main()

