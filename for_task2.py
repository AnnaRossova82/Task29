import bcrypt
import uuid
import hashlib
import string

user_login=777
user_password= 'gggsssvvv'

login = input("Please input your login:")
password = input("Please input your password:")
upper_case=any([1 if i in string.ascii_uppercase else 0 for i in password])
lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
special = any([1 if i in string.punctuation else 0 for i in password])
digits = any([1 if i in string.digits else 0 for i in password])
length=len(password)

if length<=10:
    length=True
else:
    length=False
characters=[upper_case, lower_case, special, digits, length]
print(characters)
score=0
for i in range(len(characters)):
    if characters[i]:
        score+=1
print('Password is strong: %s from 5' %score)

hash1=login
print(hash1)
hash2=password
print(hash2)

d=dict()
d['login']=hash1
d['password']=hash2
print(d)

hash_object1 = hashlib.md5(b'gggsssvvv')
print(hash_object1.hexdigest())
hash_object2 = hashlib.md5(user_password.encode())  # password entered by user
if hash_object1.hexdigest() == hashlib.md5(user_password.encode()):
    print("Password is correct")
else:
    raise TypeError("Please enter correct password")
