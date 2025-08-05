import random
import string
chars= " " + string.ascii_letters + string.digits + string.punctuation

chars=list(chars)
key=chars.copy()

random.shuffle(key)

print(f"org :{chars}")
print(f"changed: {key}")

org_msg=input("Enter your Text: ")

length=len(org_msg)
encrip=""
discrip=""
for x in org_msg:
    ind=chars.index(x)
    encrip+=key[ind]

print(f"the encripted value is {encrip}")
for x in encrip:
    ind=key.index(x)
    discrip+=chars[ind]

print(f"Descripted value is {discrip}")
