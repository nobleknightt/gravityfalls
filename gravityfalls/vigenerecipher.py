class VigenereCipher:
    def __init__(self):
        self.mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    def generate_key(self, key: str, length: int) -> str:
        key = key.lower()
        return key * int(length/len(key)) + key[:length % len(key)]

    def encrypt(self, plaintext: str, key: str) -> str:
        key = self.generate_key(key, len(plaintext))
        ciphertext = ''
        for c, k in zip(plaintext, key):
            if c.isalpha():
                if c.isupper():
                    ciphertext += chr(65 + (self.mapping[c.lower()] + self.mapping[k]) % 26).upper()
                else:
                    ciphertext += chr(97 + (self.mapping[c] + self.mapping[k]) % 26)
            else:
                ciphertext += c
        return ciphertext

    def decrypt(self, ciphertext: str, key: str) -> str:
        key = self.generate_key(key, len(ciphertext))
        plaintext = ''
        for c, k in zip(ciphertext, key):
            if c.isalpha():
                if c.isupper():
                    plaintext += chr(65 + (self.mapping[c.lower()] - self.mapping[k]) % 26).upper()
                else:
                    plaintext += chr(97 + (self.mapping[c] - self.mapping[k]) % 26)
            else:
                plaintext += c
        return plaintext

if __name__ == '__main__':
    cipher = VigenereCipher()
    assert cipher.decrypt(cipher.encrypt('Hello World', 'great'), 'great') == 'Hello World'