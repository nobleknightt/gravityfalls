class RailFenceCipher:
    def encrypt(self, plaintext: str, key: int) -> str:
        ciphertext = ''
        for i in range(key):
            for j in range(i, len(plaintext), key):
                ciphertext += plaintext[j]
        return ciphertext

    def decrypt(self, ciphertext: str, key: int) -> str:
        plaintext = ''
        for i in range(int(len(ciphertext)/key) + 1):
            for j in range(i, len(ciphertext), int(len(ciphertext)/key) + 1):
                plaintext += ciphertext[j]
        return plaintext

if __name__ == '__main__':
    cipher = RailFenceCipher()
    assert cipher.decrypt(cipher.encrypt('Hello World', 3), 3) == 'Hello World'