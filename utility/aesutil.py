#-*- coding:utf-8 -*-
import binascii
from Crypto.Cipher import AES
import base64

pcks5_pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
pcks5_unpad = lambda s : s[0:-ord(s[-1])]

key_hex = '3C3890A29C4ADF3714BF27AA3C10EBF2A298E68F08C7CF0DED1635343D586634'
key = binascii.a2b_hex(key_hex)
aes_obj = AES.new(key, AES.MODE_ECB)

data_hex = '30317C3132333435363738393130313233343536373839313031323334353637383931303132'
data = binascii.a2b_hex(data_hex)
print data

data_padding = pcks5_pad(data)
print binascii.b2a_hex(data_padding)

encrypted_data = aes_obj.encrypt(data_padding)
print binascii.b2a_hex(encrypted_data)

data_hex = '686A9401953B0BD808B9048E59FACBDE67C4C37F0D6F9F24AAB20F0BB335B3CF0B0BECFB4E3CA4C64511099263D9F6D8'
data = binascii.a2b_hex(data_hex)
# print data


decrypted_buf = aes_obj.decrypt(data)

print binascii.b2a_hex(decrypted_buf)


# key = '63773872966244281889471329228128'
# cardno = '4580601024530920'
# cardno_padding = pcks5_pad(cardno)
# print cardno_padding
# print binascii.b2a_hex(cardno_padding)
# aes_obj = AES.new(key, AES.MODE_ECB)
# encrypted_cardno = aes_obj.encrypt(cardno_padding)
# print base64.b64encode(encrypted_cardno)
# 
# encrypted_text = 'w1RrCOvHkx3VOTCblVh0HPCzdrjF6xijvijWmjUM89o='
# encrypted_buf = base64.b64decode(encrypted_text)
# decrypted_text = aes_obj.decrypt(encrypted_buf)
# print binascii.b2a_hex(decrypted_text)
# print decrypted_text
# print len(decrypted_text)
# cardno2 = pcks5_unpad(decrypted_text)
# print cardno
# print len(cardno)



