class AtbashCipher:

    def __init__(self) -> None:
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

class CaesarCipher:

    def __init__(self) -> None:
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

class KeywordCipher:

    def __init__(self) -> None:
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

class RailFenceCipher:

    def __init__(self) -> None:
        pass

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

class VigenereCipher:

    def __init__(self) -> None:
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

class MorseCode:

    def __init__(self) -> None:
        self.morse_code = {'a': '·-', 'b': '-···', 'c': '-·-·', 'd': '-··', 'e': '·', 'f': '··-·', 'g': '--·', 'h': '····', 'i': '··', 'j': '·---', 'k': '-·-·', 'l': '·-·-', 'm': '--', 'n': '-·', 'o': '---', 'p': '·--·', 'q': '--·-', 'r': '·-·', 's': '···', 't': '-', 'u': '··-', 'v': '···-', 'w': '·--', 'x': '-··-', 'y': '-·--', 'z': '--··'}

    def encode(self, message: str) -> str:
        return '   '.join([' '.join([self.morse_code[letter] for letter in word]) for word in message.lower().split()])
        # letters are seperated by single space and words are seperated by triple space

    def decode(self, message: str) -> str:
        self.morse_code = dict(zip(self.morse_code.values(), self.morse_code.keys()))
        return ' '.join([''.join([self.morse_code[code] for code in word.split(' ')]) for word in message.split('   ')])