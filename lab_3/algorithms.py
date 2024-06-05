import os

from cryptography.hazmat.primitives.padding import ANSIX923
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


class Symmetric:
    """
    A class that implements a symmetric encryption algorithm

    Attributes:
        None

    Methods:
        generate_key(key_length):
          Generate key for a symmetric algorithm
        encrypt_text(text, symmetric_key):
          Encrypts the text using a symmetric key
        decrypt_text(encrypted_text, symmetric_key):
          Decrypts the text using a symmetric key
    """

    def __init__(self):
        """
        The constructor does nothing

        Parameters:
            None

        Returns:
            None
        """
        pass
    
    @staticmethod
    def generate_key(key_length: int) -> bytes:
        """
        Static method for generating key for a symmetric algorithm.

        Parameters:
            key_length: int
              Key length for the symmetric algorithm

        Returns:
            symmetric_key: bytes
              Key for a symmetric algorithm
        """
        symmetric_key = os.urandom(key_length)
        return symmetric_key
    
    @staticmethod
    def encrypt_text(text: str, symmetric_key: bytes) -> bytes:
        """
        Static method for text encryption.

        Parameters:
            text: str
              The source text
            symmetric_key: bytes
              Key for a symmetric algorithm

        Returns:
            encrypted_text: bytes
              Encrypted text
        """
        padder = ANSIX923(128).padder()
        b_text = bytes(text, 'UTF-8')
        padded_text = padder.update(b_text)+padder.finalize()
        iv = os.urandom(8)
        cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        return encrypted_text
    
    @staticmethod
    def decrypt_text(encrypted_text: bytes, symmetric_key: bytes) -> str:
        """
        Static method for text decryption.

        Parameters:
            encrypted_text: bytes
              The encrypted text
            symmetric_key: bytes
              Key for a symmetric algorithm

        Returns:
            final_text: str
              Decrypted text
        """
        iv = os.urandom(8)
        cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(
            encrypted_text) + decryptor.finalize()
        unpadder = ANSIX923(128).unpadder()
        unpadded_decrypted_text = unpadder.update(
            decrypted_text) + unpadder.finalize()
        final_text = unpadded_decrypted_text.decode('utf-8', errors='ignore')
        return final_text

class Assymetric:
    """
    A class that implements an assymmetric encryption algorithm

    Attributes:
        None

    Methods:
        generate_keys():
          Generates keys for an asymmetric algorithm
        encrypt_key(symmetric_key, public_key):
          Encrypts the key using an assymmetric algorithm
        decrypt_text(enc_symmetric, private_key):
          Decrypts the key using an assymmetric algorithm
    """

    def __init__(self):
        """
        The constructor does nothing

        Parameters:
            None

        Returns:
            None
        """
        pass

    @staticmethod
    def generate_keys():
        """
        Static method for generating keys for an asymmetric algorithm

        Parameters:
            None

        Returns:
            (private_key, public_key): Tuple[rsa.RSAPrivateKey,rsa.RSAPublicKey]
              A tuple of keys(private key, public key)
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        return private_key, public_key
    
    @staticmethod
    def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
        Static method for key encryption.

        Parameters:
            symmetric_key: bytes
              The source symmetric key
            public_key: rsa.RSAPublicKey
              The public key of the asymmetric algorithm

        Returns:
            enc_symmetric: bytes
              Encrypted symmetric key
        """
        enc_symmetric = public_key.encrypt(symmetric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        return enc_symmetric

    @staticmethod
    def decrypt_key(enc_symmetric: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
        Static method for key decryption.

        Parameters:
            enc_symmetric: bytes
              Encrypted symmetric key
            private_key: rsa.RSAPrivateKey
              The private key of the asymmetric algorithm

        Returns:
            symmetric_key: bytes
              Decrypted symmetric key
        """
        symmetric_key = private_key.decrypt(enc_symmetric, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        return symmetric_key
     