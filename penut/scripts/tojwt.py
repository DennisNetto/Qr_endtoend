import jwt
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import binascii
key = 'secrete'

qr = b'268156cb2c59c3974990505896b3f9c436942f83d047eaf619b8b5d15932234972c7b01bf3f0dcb4a8479647db8dd50a58850e6fa1' \
     b'40fad2b55b1627d489126f398a6b07b8d55ce655c8fce8261891a1fbe631d7e8b40b3c54c785e21409848c504e9ac22682f65a84580f' \
     b'f30dc879c860c0aeb977e9a8b2c2c05f67ca14639ca31d9eaea2f861a79af54c5a0c440d4fdce3ce7ac058611733f39070ecc93c41de8' \
     b'ea1cf630678bb9cd0df17a086ddde6f4aa99bc8af003ed94a57c35b794a3891a0f6c6f38917c48a8355b7d3293eaf91f0cbc26421c709' \
     b'1ff5ac9f679d894f8fb1e64c8d0640fa5313b03ad1d7a5766563f304fdb34e65bd11708941d71c0ca0aaaff3fcfc549b8f3fc79d4779' \
     b'beabc46777c9c444835f0b3f7ff7019d3d48910acec567ab4fc56a64d8008522d786063458d9c6ce335bb40ac276df62ef44e786bceee0' \
     b'4af6c0b7a54f2276135c5c570cf0fbc012542be160a4d4c29250a342903ba78db0674b28535e7525639a18ac486b233e17124769694d6' \
     b'840760f4d71dd9c9cd06107847b8b5f83baf33fd85922a36a23df8070bf8acb6f86516cc20b1851179b8cdc33e2dcf265e34b34742dc0' \
     b'6cf96d2ae99009ca12112d602b26b38a9c73a26ec427ce7b9be43ca4b3eac670245414f6c27199acb18b1701befb2f68cdb3da6ef1b55' \
     b'5553d90c009e5d4b6c76cf476a40ba01a3aea2fa33c30b437ec6263c46a1cdfefffe6202013eca1e194a3721817172287b540'

ln = len(qr) - 64
data = qr[:ln]
hash = qr[ln:]


result = binascii.unhexlify(data)
with open('test.bin', 'wb') as f:
    f.write(result)

file_in = open("test.bin", "rb")

private_key = RSA.import_key(open("private2.pem").read())

enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
javaweb = (data.decode("utf-8"))

final = jwt.decode(javaweb, key, algorithms="HS256")

print(final)

