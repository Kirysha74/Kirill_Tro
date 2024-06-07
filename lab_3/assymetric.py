from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


class Assymetric:
    """
    A class that implements an assymmetric encryption algorithm
    """

    def __init__(self):
        """
        The constructor does nothing
        """
        pass

    @staticmethod
    def generate_keys():
        """
        Static method for generating keys for an asymmetric algorithm
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
        """
        enc_symmetric = public_key.encrypt(symmetric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        return enc_symmetric

    @staticmethod
    def decrypt_key(enc_symmetric: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
        Static method for key decryption.
        """
        symmetric_key = private_key.decrypt(enc_symmetric, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        return symmetric_key
     