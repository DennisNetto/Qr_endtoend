import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import qrcode
import jwt
import hashlib
import binascii


def cryupt(a, b, c, d):
    secret = 'secrete'
    a1 = bytes(a, "utf-8")
    encoded = jwt.encode({"id_number": a, "First_name": b, "Last_name": c, "DOB": d}, secret, algorithm="HS256")

    directoryname = "tmp" + a
    f1 = "./"
    path = os.path.join(f1, directoryname)
    os.mkdir(path)
    w3 = (directoryname + "/" + a + "private.pem")
    w4 = (directoryname + "/" + a + "receiver.pem")
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open(w3, "wb")
    file_out.write(private_key)
    file_out.close()
    public_key = key.publickey().export_key()
    file_out = open(w4, "wb")
    file_out.write(public_key)
    file_out.close()

    hash = hashlib.sha256()
    hash.update(a1)
    hash1 = (hash.hexdigest())
    h = str(hash1)

    data = encoded.encode("utf-8")

    file_ent = open(a + "encrypted_data.bin", "wb")
    recipient_key = RSA.import_key(open(w4).read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_ent.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
    file_ent.close()

    with open(a + "encrypted_data.bin", 'rb') as f:
        content = f.read()
    result = binascii.hexlify(content)
    h = bytes(h, 'utf-8')
    result = result + h
    print(result)
    qr = qrcode.make(result)
    qr.save(directoryname + "/" + a + 'qr.png')
    os.remove(a + "encrypted_data.bin")

a = "27461501745267184763129482"
b = "Larry"
c = "Parker"
d = "1991-03-12"
cryupt(a, b, c, d)
