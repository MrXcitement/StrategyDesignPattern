import hashlib

def sha1_check(s):
    h = hashlib.sha1()
    h.update(text.encode())
    return h.hexdigest()

def md5_check(s):
    h = hashlib.md5()
    h.update(text.encode())
    return h.hexdigest()

checks = {'len': len,
          'sha1': sha1_check,
          'md5': md5_check}

text = 'this is a secret document'

print(checks['len'](text))
print(checks['sha1'](text))
print(checks['md5'](text))
