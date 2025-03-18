import argparse

from keycli.models.password_entry import PasswordEntry
from .core.vault import Vault
from .utils.password_generator import PasswordGenerator
from .encryption.crypto import CryptoManager

class KeyCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="KeyCLI - Password Manager")
        self.vault = Vault()
        self.crypto = CryptoManager("default_secret_key")
        self._setup_parser()

    def _setup_parser(self):
        subparsers = self.parser.add_subparsers(dest="command")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new password entry")
        add_parser.add_argument('service', type=str, help="Service name")
        add_parser.add_argument('username', type=str, help="Username")

        # Get command
        add_parser = subparsers.add_parser("get", help="Get a password entry")
        add_parser.add_argument('service', type=str, help="Service name")

        # Generate command
        add_parser = subparsers.add_parser("generate", help="Generate a new password")

    def run(self):
        args = self.parser.parse_args()
        
        if args.command == 'add':
            password = input("Enter password: ")
            encrypted = self.crypto.encrypt(password)
            entry = PasswordEntry(args.service, args.username, encrypted)
            self.vault.entries.append(entry)
            self.vault.save_entries()
            
        elif args.command == 'get':
            for entry in self.vault.entries:
                if entry.service == args.service:
                    print(f"Password: {self.crypto.decrypt(*entry.encrypted_password)}")
                    
        elif args.command == 'generate':
            print(f"Generated: {PasswordGenerator.generate_password(10)}")

        else:
            self.parser.print_help()

if __name__ == '__main__':
    KeyCLI().run()
