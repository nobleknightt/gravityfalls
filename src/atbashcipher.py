class AtbashCipher:
    def __init__(self):
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ''
        for c in plaintext:
            if c.isalpha():
                if c.isupper():
                    ciphertext += self.alphabets[25 - (ord(c) - 65)].upper()
                else:
                    ciphertext += self.alphabets[25 - (ord(c) - 97)]
            else:
                ciphertext += c
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ''
        for c in ciphertext:
            if c.isalpha():
                if c.isupper():
                    plaintext += self.alphabets[25 - (ord(c) - 65)].upper()
                else:
                    plaintext += self.alphabets[25 - (ord(c) - 97)]
            else:
                plaintext += c
        return plaintext

if __name__ == '__main__':
    cipher = AtbashCipher()
    assert cipher.decrypt(cipher.encrypt('Hello World')) == 'Hello World'