import os
import codecs
import ecdsa
import hashlib

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = self.generate_key_pair()

    def generate_key_pair(self):
        # Generate a private key using the SECP256k1 curve
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

        # Derive the public key from the private key
        public_key = private_key.get_verifying_key()

        return private_key, public_key

    def sign(self, message):
        # Sign a message using the private key
        signature = self.private_key.sign(message.encode())
        return codecs.encode(signature, 'hex').decode()

    def verify_signature(self, message, signature):
        # Verify a signature using the public key
        signature_bytes = codecs.decode(signature.encode(), 'hex')
        return self.public_key.verify(signature_bytes, message.encode())

def sha256(message):
    return hashlib.sha256(message.encode()).hexdigest()

if __name__ == '__main__':
    wallet = Wallet()
    message = 'This is a test message'
    signature = wallet.sign(message)

    print(f'Message: {message}')
    print(f'Signature: {signature}')
    print(f'Verified: {wallet.verify_signature(message, signature)}')
