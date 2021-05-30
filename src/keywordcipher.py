class KeywordCipher:
    def __init__(self):
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def generate_key(self, keyword: str) -> str:
        key = keyword.lower()
        for c in self.alphabets:
            if c not in key:
                key += c
        return key

    def encrypt(self, plaintext: str, keyword: str) -> str:
        mapping = dict(zip(self.alphabets, self.generate_key(keyword)))
        ciphertext = ''
        for c in plaintext:
            if c.isalpha():
                if c.isupper():
                    ciphertext += mapping[c.lower()].upper()
                else:
                    ciphertext += mapping[c]
            else:
                ciphertext += c
        return ciphertext

    def decrypt(self, ciphertext: str, keyword: str) -> str:
        mapping = dict(zip(self.generate_key(keyword), self.alphabets))
        plaintext = ''
        for c in ciphertext:
            if c.isalpha():
                if c.isupper():
                    plaintext += mapping[c.lower()].upper()
                else:
                    plaintext += mapping[c]
            else:
                plaintext += c
        return plaintext

if __name__ == '__main__':
    cipher = KeywordCipher()
    assert cipher.decrypt(cipher.encrypt('Hello World', 'great'), 'great') == 'Hello World'