wordlist = ['/.../.../.../.../.../.../.../.../windows/win.ini']

letters = set('/')

for word in wordlist:
    if letters & set(word):
        print word