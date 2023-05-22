import base64
from src.rsa import *
from src.sha3 import sha3_512 as hash
from src.utility import *
from src.database import *

def sign():
    private_key = None
    # dapatin kunci
    haskey = 'uwu'
    while(private_key == None and haskey != 'keluar'):
        print("ketik keluar untuk keluar dari menu")
        print("apakah kamu punya kunci, nya? (y/n): ", end='')
        haskey = input()

        if(haskey != 'y'):
            generatekey()
        
        else:
            content = openFile()
            hashed_content = hash(content)
            private_key = openPrivateKey()

            encrypted = encrypt(private_key, int(hashed_content, 16))
            saveSignFile(hex(encrypted))

def verify():
      public_key = None
      content = openFile()
      hashed_content = hash(content)
      
      # ambil public key
      print("siapa nama pembuat file ini?: ", end='')
      nama = input()
      data = getdatawithname(nama)

      if(len(data) != 0):
        public_key = stringtokey(data[0].public_keys)
        sign = openSignFile()
        decrypted_sign = decrypt(public_key, int(sign, 16))
        if(decrypted_sign == int(hashed_content,16)):
            print("Sukses!!! Benar punya dia, nya~")
        else:
            print("Gagal!!! Bukan punya dia atau file berubah, nya~")



def generatekey():
    # generate key
            print("membuat key ...")
            public_key, private_key = generate_key_pair(generate_prime_number(), generate_prime_number())
            print("masukkan nama kamu, nya: ", end='')
            name = input()

            # masukin fungsi masukin data baru ke database
            insertdata(name, str(public_key))
            print("ini private key kamu: ")
            print(private_key)
            savePrivateKey(private_key)

command = "ulang"
print("Selamat datang di sisteeeemm\n ~~~DIGISIGN GENSHI DESUUUUU~~~\n")
while command != 'keluar':
    print("Masukkan Command yang anda ingingkan!!\n")
    print("> sign -> melakukan sign pada dokumen, nyaa~")
    print("> verify -> memastikan kebenaran dokumen, nyaa~")
    print("> keluar -> keluar dari sistem, nyaa~")
    print("\n> ", end='')
    command = input()
    if(command == 'sign'):
        sign()
    elif(command == 'verify'):
        verify()
    elif(command == 'keluar'):
         print("Bye byee~~")
    else:
         print("masukan anda salah, nyaa~.\n masukan yang bener dong!!")