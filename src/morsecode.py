class MorseCode:
    def __init__(self):
        self.morse_code = {'a': '·-', 'b': '-···', 'c': '-·-·', 'd': '-··', 'e': '·', 'f': '··-·', 'g': '--·', 'h': '····', 'i': '··', 'j': '·---', 'k': '-·-·', 'l': '·-·-', 'm': '--', 'n': '-·', 'o': '---', 'p': '·--·', 'q': '--·-', 'r': '·-·', 's': '···', 't': '-', 'u': '··-', 'v': '···-', 'w': '·--', 'x': '-··-', 'y': '-·--', 'z': '--··'}

    def encode(self, message: str) -> str:
        # letters are seperated by single space and words are seperated by triple space
        return '   '.join([' '.join([self.morse_code[letter] for letter in word]) for word in message.lower().split()])

    def decode(self, message: str) -> str:
        self.morse_code = dict(zip(self.morse_code.values(), self.morse_code.keys()))
        return ' '.join([''.join([self.morse_code[code] for code in word.split(' ')]) for word in message.split('   ')])

if __name__ == '__main__':
    morsecode = MorseCode()
    assert morsecode.decode(morsecode.encode('this is a message')) == 'this is a message'