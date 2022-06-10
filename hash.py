from hashlib import sha256 as SHA
import codecs


SIZE = 1024*256

def getFileHash(file):
    sha = SHA()
    h = open(file, 'rb')
    content = h.read(SIZE)
    print("\nFile {}의 해쉬값" .format(file))
    while content:
        sha.update(content)
        r = sha.digest()
        print(codecs.encode(r, 'hex_codec'))
        
        content = h.read(SIZE)
    h.close()
    
    hashval = sha.digest()
    return hashval

def hashCheck(f1,f2):
    
    if f1==f2:
        print("=====Two File's Hash is Same=====")
    else:
        print("=====Two File's Hash is Different=====")
        

if __name__ == '__main__':
    f1 = 'plain'
    f2 = 'plain2.txt'
    
    hashval = getFileHash(f1)
    hashval2 = getFileHash(f2)
    
    hashCheck(hashval,hashval2)
    

