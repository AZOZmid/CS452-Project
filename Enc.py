from cryptography.fernet import Fernet
key = None
with open('key.key','rb') as f :
    key = f.read()
    key = key
    print(key)
     
input_file = 'test.txt'
output_file ='testEnc.txt'

with open(input_file, 'rb') as f:
    data = f.read()
    

fernet = Fernet(key)
encrypted = fernet.encrypt(data)
print(encrypted)

with open(output_file, 'wb') as f:
    f.write(encrypted)

# You can delete input_file if you want