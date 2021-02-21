class CaesarCipher:
    def __init__(self):
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self, plaintext: str, key: int) -> str:
        ciphertext = ''
        for c in plaintext:
            if c.isalpha():
                if c.isupper():
                    ciphertext += self.alphabets[(ord(c) - 65 + key) % 26].upper()
                else:
                    ciphertext += self.alphabets[(ord(c) - 97 + key) % 26]
            else:
                ciphertext += c
        return ciphertext

    def decrypt(self, ciphertext: str, key: int) -> str:
        plaintext = ''
        for c in ciphertext:
            if c.isalpha():
                if c.isupper():
                    plaintext += self.alphabets[(ord(c) - 65 - key) % 26].upper()
                else:
                    plaintext += self.alphabets[(ord(c) - 97 - key) % 26]
            else:
                plaintext += c
        return plaintext

if __name__ == '__main__':
    cipher = CaesarCipher() 
    assert cipher.decrypt(cipher.encrypt('Hello World', 2) , 2) == 'Hello World'