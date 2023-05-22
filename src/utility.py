def savePrivateKey(private_key):
    print("\nzzzzzzzzzzzzzzzzzzzzzzzzzzz Save Private Key zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print("masukkan nama file (cth: namefile -> namefile.pri): ", end='')
    file_name = input()
    f = open("private_keys/"+file_name+".pri", 'w')
    f.write(str(private_key))
    f.close()
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")


def openPrivateKey():
    print("\nzzzzzzzzzzzzzzzzzzzzzzzzzzz Load Private Key zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print("masukkan nama file private key \ndi folder private_keys (yang ada .pri nya): ", end='')
    file_name = input()
    try:
        f = open("private_keys/"+file_name, 'r')
        content = f.read()
        f.close()
        return stringtokey(content)
    except:
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")
        print("ngga ada nama file itu di folder private_keys, nyaa~")
    
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")
    
def saveSignFile(content):
    print("\nzzzzzzzzzzzzzzzzzzzzzzzzzzz Save Sign File zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print("masukkan nama file (cth: namefile -> namefile.txt): ", end='')
    file_name = input()
    f = open("file/"+file_name+".txt", 'w')
    f.write(str(content))
    f.close()
    print("file tersimpan pada: ", "file/"+file_name+".txt")
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")

def openSignFile():
    print("\nzzzzzzzzzzzzzzzzzzzzzzzzzzz Load Sign File zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print("masukkan nama file sign \ndi folder file: ", end='')
    file_name = input()
    try:
        f = open("file/"+file_name, 'r')
        content = f.read()
        f.close()
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")
        return content
    except:
        print("ngga ada nama file itu di folder file, nyaa~")
    
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")

def openFile():
    print("\nzzzzzzzzzzzzzzzzzzzzzzzzzzz Load File zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print("masukkan nama file \ndi folder file: ", end='')
    file_name = input()
    try:
        f = open("file/"+file_name, 'rb')
        content = f.read()
        f.close()
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")
        return content
    except:
        print("ngga ada nama file itu di folder file, nyaa~")
    
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n")
    


def stringtokey(stringkey:str):
    '''
    Mengembalikan nilai key dari key yg dalam bentuk string
    '''
    key_temp = (stringkey.replace(')', '')).split('(')[1]
    k = key_temp.split(', ')[0]
    n = key_temp.split(', ')[1].replace("'", '')
    key = int(k), int(n)
    return key