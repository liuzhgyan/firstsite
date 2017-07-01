#-*- coding:utf-8 -*-
import binascii
import rsa
import hashlib
import base64

key_hex = '30317C3132333435363738393130313233343536373839313031323334353637383931303132'
key = binascii.a2b_hex(key_hex)
print key

private_key_hex = '308204A30201000282010100CD0D2EA2CF306F7A6A7B63A11814400FDF610B8A3BECE7218A680BA2CEAD7F86B640D9BB108B8F9E4948E4AAD5F7ECF016AC0E974D7B01E84EC82E96805B05B090512DA5D0F4E27CEF0CB4F5B95F400C9FD2AC7E5DB934784C503DFDAD96FDFF5F8E973AEE6803D3563BB9425F44F4EDD64418F5DCB8DACD6833C7E4DC3DFDB2F02AE02C59FC67C9B5763F5CA7F248D7496B9E3F1806919F76D50A912FBBE7EDB75C9CA8D24552D076E800463CA7F3CF8076513404660E26F24F69B11C0C04D289C8E1CA52E1EE5A7962F298778791599C83972F0880BD571543EA6F8E8BE4B20A0A166D39281AAC6EACAF54156B88F2E418304FF82A605E7419B017D6D04AE102030100010282010019909802116DDB003AB00E9057A05D5FA7E72C03FC8BABECBE6FA6BFBCCA87234456C52E9C40A2291C699BA4D6FA204ECB57814188EB44A61CD3101D3B27335D90E8A615CDD3079286FAA1171FC39F3329114AE893067E6309DF593DE6FB73C877E149BBE85C61D9B7F47343B1FD616CC3B188212321E2EF081BA898EBD7F368B76C1D40BDA474C5764CDCA57EF342A838B2F0543878D3D7E28A5C049CFCCD69051BDBA3D01F32B7951F1E10F92245383486C0C5C7BB5F4A56FD46C6DB6F6C73F4FD53918523094721E5B9A417867335B01D9EF4ECF262F3AC11BF27D6418234CD978726BDFC964C5836D8F9DC62C76A3FDDDE9620C79B0F17554442B5BFC86F02818100F2E398B41570A443770EE2F3BCF6CC71D4B4A331DAAC9B334E58E0E72C775D0356EB94AE875D257D5D6463180C1FBEEA54CB46E9CBCC4F63E43AD4C20A048840A3428B9DA66EDFA8AAF4620C118899B689687CFA744A8DCA78681C692D6F35AE10DBC49654D53EB08BA571D64C45B9F0B211B767B3C6B503B8E831CAD24B8C0302818100D81EB892E85687AB4E58A5C53F47DCB951564C35A5ABEA1BA57E3A9013668E3B532A8F5FD14CFBF588EA5E4FE137206FD56BA8A407F85BD54136CEC6EDC7EE1747355ACFA2996CC1574E3D86F264D523268D7E9FF6AE27B6F608C5F861E51A8DF20EF5D1321E59A38C7F21F08F813A67AC3A5A4404D11504619B5F9638DCC24B0281807D3087FD91EB6C0F05E79B5C8BB21D3032B5244446F49E4DF47CE4F6E23967AC97F976B9FA352D648F657599E86DD866496C38D1BA64452B34708A46B5091EFD49E8BBB3771C40955BFFF8254648450A0B8ADA97F0A698AC9A20F73BD2DA362DD0ACA587E293C2EB161F212C96457E102C87EB233D4B16F3A333B2AE5A73EBE702818052C7418F136AC1403E1BFA3298D05F9CA3A8D83BDC1F02E65FF6FF5B5BF2F61B86F9503D351FB58A104D249E97F6D377C2592018E3EC9ED009D08256F39096835804F9A979F02615CFE8E9EC1C3FBEDB5DD2E86340CAE7EF4E418202670CA7A522C7D423B27CA97CD93D80B47162E00A018FC02F39611419BF811195AA65F40D028181008D4B963A5B3C64C7FE0BAF5D18EABA992D8CA7F195D9791C670E2B96964E89DD863683AE7E4565F5A42F275E0EC2692C5BDD2521AE3B5324D4FF3C8EAA0E2BEF840E3F9A211419F9BD3CD736CB80829F27978223B6954DE4FD6D60F3EA05325D5E507174C36FC10B9427092B45F428E5CF3CB5ED0015F17BADB25F3A1834CEA7'

public_key_hex = '3082010A0282010100CD0D2EA2CF306F7A6A7B63A11814400FDF610B8A3BECE7218A680BA2CEAD7F86B640D9BB108B8F9E4948E4AAD5F7ECF016AC0E974D7B01E84EC82E96805B05B090512DA5D0F4E27CEF0CB4F5B95F400C9FD2AC7E5DB934784C503DFDAD96FDFF5F8E973AEE6803D3563BB9425F44F4EDD64418F5DCB8DACD6833C7E4DC3DFDB2F02AE02C59FC67C9B5763F5CA7F248D7496B9E3F1806919F76D50A912FBBE7EDB75C9CA8D24552D076E800463CA7F3CF8076513404660E26F24F69B11C0C04D289C8E1CA52E1EE5A7962F298778791599C83972F0880BD571543EA6F8E8BE4B20A0A166D39281AAC6EACAF54156B88F2E418304FF82A605E7419B017D6D04AE10203010001'

private_key = binascii.a2b_hex(private_key_hex)
public_key = binascii.a2b_hex(public_key_hex)

print len(private_key)
print len(public_key)

encrypted_data_hex = '6B448BC864DBB90B2A530760182C40D6E6A3DD296C670ACCF773A166AB4104826D264ACD77EBB2ADCF81B4E725A05A0CEF062E71E2CEC282180F4751A99A5CB7359448FE1FD41107C5993D0545A2CC90EA40FCA475655F37625DABA9D529D8B59BB0382F49150549AC4E3F0ED4BD284C89F9EED75EC7EB3BDB653F2FB5A8E860C8B88E48C0C6EFA64D48366F9F1B1DB488582CE25566275F91FB2C5AC0338A3E6F107DA48AD56711F62F8D6B27D3899D618CC056258FE8CA43685121D9037D6729585C12D5F796AC8D44E65DE5C279A6E40279BCF245C87B44A3A6AD2FFA9D14F0AE6B1EBD6E5CA9D56E354984E0EC72D93D28D4B617D14C551BAD007C2EFEF2'
encrypted_data = binascii.a2b_hex(encrypted_data_hex)

rsa_pubkey = rsa.PublicKey._load_pkcs1_der(public_key)
print rsa_pubkey

rsa_prikey = rsa.PrivateKey._load_pkcs1_der(private_key)
print rsa_prikey

decrypted_data = rsa.decrypt(encrypted_data, rsa_prikey)
print decrypted_data
print len(decrypted_data)

encrypted_key = rsa.encrypt(key, rsa_pubkey)
print binascii.b2a_hex(encrypted_key)

decrypted_key2 = rsa.decrypt(encrypted_key, rsa_prikey)
print decrypted_key2

sha256_util = hashlib.sha256()

msg_hex = '3C726F6F743E0D0A093C4D73674865616465723E0D0A09093C44743E323031362D31322D33305431313A30303A30303C2F44743E0D0A09093C54703E455043432E3130312E3030312E30313C2F54703E0D0A09093C49643E5A323030373933333030303031303C2F49643E0D0A09093C447263743E31313C2F447263743E0D0A09093C5369676E4E623E4E6F313233343536373839303C2F5369676E4E623E0D0A09093C4E637270746E534E3E4E6F323233343536373839303C2F4E637270746E534E3E0D0A09093C4467746C456E766C703EE695B0E5AD97E8AF81E4B9A6E5AF86E696873C2F4467746C456E766C703E0D0A093C2F4D73674865616465723E0D0A093C4D7367426F64793E0D0A09093C53676E496E663E0D0A0909093C4163637449643E5A323030373933333030303031303C2F4163637449643E0D0A0909093C7454703E30303C2F7454703E0D0A0909093C7449643E363232323838303130373635313236373C2F7449643E0D0A0909093C53676E4E6D3EE5BCA0E5B08FE99BA8E79A84E5AF86E69687E5BDA2E5BC8F3C2F53676E4E6D3E0D0A0909093C494454703E30313C2F494454703E0D0A0909093C49444E6F3E3133303032373139393030393031313130313C2F49444E6F3E0D0A0909093C4D6F623E31333832303938353633383C2F4D6F623E0D0A09093C2F53676E496E663E0D0A09093C496E663E0D0A0909093C437467793E303230323C2F437467793E3E0D0A0909093C727849643E323031363131323230393837363534333231313032303130333C2F727849643E0D0A0909093C72784474546D3E323031362D31312D32325431393A32303A33363C2F72784474546D3E0D0A0909093C74684D73673E3132333435363C2F74684D73673E0D0A09093C2F547278496E663E0D0A09093C496E737467496E663E0D0A0909093C496749643E5A323030373934343030303031303C2F496749643E0D0A0909093C49416363743E323031313036303631323332E5AF86E69687E5BDA2E5BC8F3C2F49416363743E0D0A09093C2F496E737467496E663E0D0A093C2F4D7367426F64793E0D0A3C2F726F6F743E'
msg = binascii.a2b_hex(msg_hex)
# print msg
sha256_util.update(msg)
msg_sha256_hex = sha256_util.hexdigest()
print msg_sha256_hex

msg_sha256_b64 = base64.b64encode(sha256_util.digest())
print msg_sha256_b64

msg_sign = rsa.sign(msg, rsa_prikey, 'SHA-256')
print binascii.b2a_hex(msg_sign)
print base64.b64encode(msg_sign)

msg_sign_b64 = 'MTJw8liMhUEu+q6l58lXMXHkR15aoiKCNGDgUEKWNLVhtqhEOUp8ev78X5od/YwOAjHspOY3yvYHjeh/MW2CxkQlbRrmbxVamdVEu7eXH1tvkLvZlKXD/Q3aQQMe3lGpQOeyeNWNS3hDgsXjXpx0wnWRireFMDsel9bhJ1d31AEuM6cuSFaTLKp0iiD4T/y1W9a+PJ7qoDjOb3YZeX+m0J7Byo+JU4uu1obPaQlcUUbnSc1bvfDKOnuQ3Dm4Uo1qz3yGaYZ6zEwSUiG7Kzr8kfVU66pvFzIXiTA2hF1w8HFGj/ewOhgiQtHcgaMdYzbu828ENOqUXLcyNmSdgelcIA=='
msg_sign2 = base64.b64decode(msg_sign_b64)
print rsa.verify(msg, msg_sign, rsa_pubkey)
print rsa.verify(msg, msg_sign2, rsa_pubkey)


