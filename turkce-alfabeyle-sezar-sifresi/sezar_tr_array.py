alfabe=["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı",
        "i","j", "k", "l", "m", "n", "o", "ö", "p", "r","s", "ş", "t", "u", "ü", "v", "y", "z"]

def sifrele(metin,anahtar):
    sonuc = ""
    for i in metin:
        if i in alfabe:
            sayi = alfabe.index(i)
            sayi=(sayi+anahtar)%29
            sonuc=sonuc+alfabe[sayi]
        elif i==" ":
            sonuc=sonuc+i
        else:
            sonuc += i
    return sonuc
      
      

def sifrecoz(metin):
    for i in range(1,29):
        a=sifrele(metin,i)
        print(a)


def main():

    bayrak=True
    while bayrak:
        a = (input(":Sezar şifresi programı - lütfen seçiniz:\n"
                                                    "1. Şifreleme \n2. Şifre çözme\n"))
        try:
            if (int(a) == 1):
                bayrak=False
                
                metin = (input("lütfen şifrelenecek metni giriniz:\n"))
                metin=metin.lower()
                anahtar = int(input("lütfen şifreleyecek anahtarı giriniz:\n"))
                sonuc=sifrele(metin,anahtar)
                print(sonuc)
                   
                        
            elif (int(a) == 2):
                bayrak=False
                metin = (input("lütfen şifresi çözülecek metni giriniz:\n"))
                sonuc=sifrecoz(metin) 
        except :
            bayrak=True
            print("yanlış giriş") 
            
if __name__ == '__main__' : 
	main() 
