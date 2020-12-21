# ImageCrypter

Metni RGB formatında şifreleyerek pixelleri resmin içine entegre eder. Bu sayede metin görselde saklanır.


## Install
```bash
git clone https://github.com/mehmetserifpasa/ImageCrypter
cd ImageCrypter
python3 Encryption.py file.txt
```

## Usage
Şifrelemek istediğiniz metni file.txt dosyasına yazın. Sonra şu komutu çalıştırın.
```bash
python3 Encryption.py file.txt
```
Bu komuttan sonra test.png adlı bir resim dosyası oluşacaktır. Bu resim dosyası metnin şifrelenmiş halidir. Eğer resmi tekrar decryption etmek istiyorsak şu komutu kullanırız:
```bash
python3 Decryption.py test.png 
```

## Image

## Algorithm

*Her karaktere (örnek: a,b,c,&,5 vb.) atanmış bir sayı vardır. Metinde geçen her karakterin sayısal değerini bir listeye ekleriz. Sonra bu sayıları RGB formatına göre şifreliyoruz. Bu şifreleme şöyle çalışmaktadır:

```
0 = (x,Y,x) (0 > x < 255)
1 = (Y,Y,x) (256 > x < 999)
2 = (Y,Y,x) (1000 > x < 9999)
3 = (Y,Y,Yxx) (10.000 > x < 99.999)
4 = (Y,Y,x) + (Y,x,x) (100.000 > x < 999.999)

```
```
x = normal RGB değerini temsil ediyor
Y = algoritmayı temsil ediyor
```
RGB listesi'nin ilk elemanı, metnin karakter sayısıdır. Karakter sayısı fazla olduğunda bunu şifrelemek gerekiyor. Bunu da yukarıdaki formata göre yapıyoruz.

* Eğer karakter sayısı 0 ile 255 arasındaysa, karakter sayısını RGB değerindeki (x,Y,x) orta bölüme koyuyoruz ve 0 sayısını RGB değerindeki (x,x,xxY) son bölümün son sayısına ekliyoruz.

* Eğer karakter sayısı 1000 ile 9999 arasındaysa, karakter sayısını RGB değerindeki (Y,Y,X) baş-orta bölüme koyuyoruz ve 2 sayısını RGB değerindeki (x,x,xxY) son bölümün son sayısına ekliyoruz.

* Eğer karakter sayısı 100.000 ile 999.999 bin arasındaysa bu sefer 2 farklı RGB değeri oluşturuyoruz. Birinci RGB değerini ilk iki bölüme (Y,Y,X), ikinci RGB değerini (Y,x,x) ikinci bölümün birinci bölümüne ekliyoruz.



