from Crypto.Cipher import AES
import base64

MASTER_KEY="bismillah semoga sukses sdfs dfsdf sdf"

def encrypt_val(clear_text):
    enc_secret = AES.new(MASTER_KEY[:16])
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
    return cipher_text

def decrypt_val(cipher_text):
    dec_secret = AES.new(MASTER_KEY[:16])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    clear_val = raw_decrypted.rstrip("\0")
    return clear_val