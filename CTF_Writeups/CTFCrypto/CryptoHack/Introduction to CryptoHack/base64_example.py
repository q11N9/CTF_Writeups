import base64 
c = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# print(bytes.fromhex(c).decode())
print("Here is your flag: " + base64.b64encode(bytes.fromhex(c)).decode())
# crypto/Base+64+Encoding+is+Web+Safe/