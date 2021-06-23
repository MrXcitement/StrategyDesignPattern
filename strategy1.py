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


lc = LenChecker()
sc = Sha1Checker()
md = MD5Checker()

text = 'this is a secret document'
print(lc.check(text))
print(sc.check(text))
print(md.check(text))