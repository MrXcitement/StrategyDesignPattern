import hashlib

class LenChecker:
    def check(self, text):
        return len(text)

class Sha1Checker:
    def check(self, text):
        h = hashlib.sha1()
        h.update(text.encode())
        return h.hexdigest()

class MD5Checker:
    def check(self, text):
        h = hashlib.md5()
        h.update(text.encode())
        return h.hexdigest()


class Checker():
    def __init__(self, strategy):
        self.strategy = strategy

    def check(self, text):
        return self.strategy.check(text)

text = 'this is a secret document'

c = Checker(LenChecker())
print(c.check(text))

c = Checker(Sha1Checker())
print(c.check(text))

c = Checker(MD5Checker())
print(c.check(text))