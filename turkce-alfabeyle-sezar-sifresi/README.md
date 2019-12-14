# türkçe alfabeyle sezar şifresi
## sezar şifresinin türk alfabesine uygulanmasının basit bir gözterimi.


Sezar şifresiyle ilgili internette çok fazla şey bulmanız mümkün. Binlerce uygulaması var, ancak Türkçe harflerle uygulanması biraz ihmal edilmiş duruyor. Yazımda bu konuya değinerek ufak bir uygulama yapacağım. Klasik yöntem, harfi ascii karaktere çevirmek, bu sayıdan alfabenin ilk harfi a’nın ascii karşılığı olan 97’i çıkarıp, anahtar değeriyle toplamak, bu sayının 26’yla modunu almak (alfabedeki harf sayısı), çıkan sonucu takrar 97 ile toplayıp karaktere dönüştürmektir. Bunu Python koduna uyarlarsak:

```python
print(ord("a"))
harf,anahtar="d",1
sonuc = chr((ord(harf) + anahtar-97) % 26 + 97)
sonuc
çıktı:
97
e
```


Bu yöntem İngiliz alfabesinde işe yarıyor, şöyle ki: d harfinin ascii karşılığı : 100’dür. buna anahtar değerini eklediğimizde (örneğin 1) bu değer 101 olur. 101 sayısının karakter karşılığı ise “e” harfidir.
böylece kaydırma yaparak d harfini e harfi olarak şifreleriz. 

ancak Türkçe alfabede iş biraz karışık, örneğin ç harfinin ascii karşılığı 231, 1 anahtarıyla şifrelemeye çalışırsak sonuçta elde edeceğimiz harf 'è' oluyor. Böylece standart alfabenin dışına çıkmış oluyoruz. 

```python
print(ord ("d"))
print(chr (100+1))
print(ord ("ç"))
print(chr (231+1))
​
100
e
231
è
```

ascii karşılıkları kullanmadan, python sözlüklerle yapılacak bir program, sezar şifresinin uygulanmasındaki bu soruna bir çözüm olabilir. Bunun için öncelikle iki sözlük tanımladım bunlar harften sayıya  ve sayıdan harfe dönüşümü sağlıyorlar:



```python
sayidan_alfabe={0:"a", 1:"b", 2:"c", 3:"ç", 4:"d", 5:"e", 6:"f", 7:"g", 8:"ğ", 9:"h", 10:"ı",
11:"i", 12:"j", 13:"k", 14:"l", 15:"m", 16:"n", 17:"o", 18:"ö", 19:"p", 20:"r",
21:"s", 22:"ş", 23:"t", 24:"u", 25:"ü", 26:"v", 27:"y", 28:"z"}

alfabeden_sayi={"a":0, "b":1, "c":2, "ç":3, "d":4, "e":5, "f":6, "g":7, "ğ":8, "h":9, "ı":10, "i":11,
"j":12, "k":13, "l":14, "m":15, "n":16, "o":17, "ö":18, "p":19, "r":20,
"s":21, "ş":22, "t":23, "u":24, "ü":25, "v":26, "y":27, "z":28 }
```

daha sonra ```sifrele()```  fonksiyonu kullanıcıdan alınan metin ve anahtarı kullanılarak şifrelemeyi uyguluyor. Bunu yaparken izlediği yol kısaca şöyle özetlenebilir:
* metindeki her harf için
    * harfin sayısal karşılığını bul(alfabeden_sayi sözlüğünden)
    * bu karşılığı anahtar değeriyle topla 
    * toplamın 29'dan büyük çıkma ihtimalini önlemek için mod işlemi kullan
    * ortaya çıkan yeni sayıyının harf karşılığını bul (sayidan_alfabe sözlüğünden)
    * yeni elde edilen harfi sonuç değikrnine ekle
    * eğer yabancı bir karakter varsa (x,w,q vs..) şifrelemeden kullan
    
```python    
def sifrele(metin,anahtar):
    sonuc = ""
    for i in metin:
        if i in alfabeden_sayi:
            sayi = alfabeden_sayi[i]
            sayi=(sayi+anahtar)%29
            sonuc=sonuc+sayidan_alfabe[sayi]
        elif i==" ":
            sonuc=sonuc+i
        else:
            sonuc += i
    return sonuc
```


```sifrecoz()``` isimli fonksiyon ise kullanıcıdan aldığı şifreli metne kaba kuvvet uygulayarak tüm olası ihtimalleri deneyerek ekrana yazdırıyor. Bu işlem yalnızca bir for döngüsünden ibaret bu döngü 1-29 arasındaki tüm olası anahtarları şifreli metne uygularken ```sifrele()```  fonksiyonunu kullanıyor. 

```python    
def sifrecoz(metin):
    for i in range(1,29):
        a=sifrele(metin,i)
        print(a)
```



Eğer bu yöntem çok karışık geldiyse, çok daha basit bir yöntem var: Python listeleri kullanmak! index komutunu kullanarak, dizi elemanlarının, sırasına ulaşmamız mümkün.
```python    
dizi.index(dizi-elemanı)
```
yukardaki örneği kullanarak daha basit bir yöntem uygulayabilirsiniz. üstelik çok daha kolayca: tek yapmanız gereken, kullandığımız 2 sözlük yerine tek bir dizi ve bu dizinin indeksini kullanmak.

```python   


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

```




