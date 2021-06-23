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
    def check(self, strategy, text):
        if strategy == 'len':
            c = LenChecker()
        elif strategy == 'sha1':
            c = Sha1Checker()
        elif strategy == 'md5':
            c = MD5Checker()
        else:
            raise ValueError(f'No strategy {strategy} known')

        return c.check(text)

text = 'this is a secret document'

c = Checker()
print(c.check('len', text))

c = Checker()
print(c.check('sha1', text))

c = Checker()
print(c.check('md5', text))