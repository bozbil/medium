def sifrele(metin,anahtar):
    sonuc = ""
    for i in metin:
      harf = i    
      if (harf.isupper()):
         sonuc += chr((ord(harf) + anahtar-65) % 26 + 65)
      else:
         sonuc += chr((ord(harf) + anahtar - 97) % 26 + 97)
    return sonuc

def sifrecoz(metin):
    for i in range(27):
        a=sifrele(metin,i)
        print(a)

             
def main(): 
    a = int(input(":Sezar şifresi programı - lütfen seçiniz:\n"
						"1. Şifreleme \n2. Şifre çözme\n")) 
    if (a == 1):
        metin = (input("lütfen şifrelenecek metni giriniz:\n"))
        anahtar = int(input("lütfen şifrelenecek metni giriniz:\n"))
        sonuc=sifrele(metin,anahtar)
        print(sonuc)
	   
		
    elif (a == 2):
        metin = (input("lütfen şifresi çözülecek metni giriniz:\n"))
        sonuc=sifrecoz(metin) 
    else:
        print("yanlış giriş - yalnızca 1 veya 2 girebilirsiniz") 
    	
# Driver Code 
if __name__ == '__main__' : 
	main() 
