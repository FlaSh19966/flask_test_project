from config import Config
from Crypto.Cipher import AES
from Crypto import Random
import base64


def pad(data):
	length = int(Config.AES_BLOCK_SIZE) - \
	         (len(data) % int(Config.AES_BLOCK_SIZE))
	return data + chr(length) * length

def unpad(data):
	return data[:-ord(data[-1])]

def aes_encrypt(message):
	IV = Random.new().read(int(Config.AES_BLOCK_SIZE))
	aes = AES.new(Config.AES_KEY.encode(), AES.MODE_CBC, IV)
	message = message.decode("utf-8")
	return base64.b64encode(IV + aes.encrypt(pad(message).encode()))

def aes_decrypt(encrypted):
	encrypted = encrypted.replace(" ", "+")
	encrypted = base64.b64decode(encrypted)
	IV = encrypted[:int(Config.AES_BLOCK_SIZE)]
	aes = AES.new(Config.AES_KEY.encode(), AES.MODE_CBC, IV)
	return unpad(aes.decrypt(encrypted[int(Config.AES_BLOCK_SIZE):]).decode())