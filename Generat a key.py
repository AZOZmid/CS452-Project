import cryptography

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()