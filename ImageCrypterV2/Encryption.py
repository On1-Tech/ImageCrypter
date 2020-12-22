from PIL import Image
import sys
import random
from PIL import ImageFile


image = Image.open(sys.argv[1])
px = image.load()


""" 
Karakterlerimize hem numara atıyoruz hem de string değerlerini yazıyoruz.
"""
a = 1
aa = "a"

b = 2
bb = "b"

c = 3
cc = "c"

ç = 4
çç = "ç"

d = 5
dd = "d"

e = 6
ee = "e"

f = 7
ff = "f"

g = 8
gg = "g"

ğ = 9
ğğ = "ğ"

h = 10
hh = "h"

ı = 11
ıı = "ı"

i = 12
ii = "i"

j = 13
jj = "j"

k = 14
kk = "k"

l = 15
ll = "l"

m = 16
mm = "m"

n = 17
nn = "n"

o = 18
oo = "o"

ö = 19
öö = "ö"


p = 20
pp = "p"

r = 21
rr = "r"

s = 22
ss = "s"

ş = 23
şş = "ş"

t = 24
tt = "t"

u = 25
uu = "u"

ü = 26
üü = "ü"


v = 27
vv = "v"

y = 28
yy = "y"

z = 29
zz = "z"

nokta = 30
noktaa = "."

unlem = 31
unlemm = "!"

virgul = 32
virgull = ","

x = 33
xx = "33"

bosluk = 34
boslukk = " "

dolar = 35
dolarr = "$"

yüzde = 36
yüzdee = "%"

ve = 37
vee = "&"

tekNokta = 38
tekNoktaa = "'"

parantezSol = 39
parantezSoll = "("

parantezSag = 40
parantezSagg = ")"

yildiz = 41
yildizz = "*"

tire = 42
tiree = "-"

slash = 43
slashh = "/"

ikinokta = 44
ikinoktaa = ":"

noktaliVirgul = 45
noktaliVirgull = ";"

kucuktur = 46
kucukturr = "<"

buyuktur = 47
buyukturr = ">"

esittir = 48
esittirr = "="

mail = 49
maill = "@"

soruisareti = 51
soruisaretii = "?"

kares = 52
karess = "#"

ciftnoktaAy = 53
ciftnoktaAyy = '"'

carp = 54
carpp = "*"

susluparantezsol = 55
susluparantezsoll = "{"

susluparantezsag = 56
susluparantezsagg = "}"

parantezlistesol = 57
parantezlistesoll = "["

parantezlistesag = 58
parantezlistesag = "]"

alttire = 59
alttiree = "_"

tersslash = 60
tersslashh = "\\"

bir = 61
birr = "1"

iki = 62
ikii = "2"

uc = 63
ucc = "3"

dort = 64
dortt = "4"

bes = 65
bess = "5"

alti = 66
altii = "6"

yedi = 67
yedii = "7"

sekiz = 68
sekizz = "8"

dokuz = 69
dokuzz = "9"

sifir = 70
sifirr = "0"




""" Kullanıcıdan şifrelenecek yazıyı txt formatında alıyoruz."""
TEXT = open(sys.argv[1], "r")



""" Şifrelenecek yazının her karakterini yukarıdaki numara indeksine göre ekliyor """
sifre = []



""" Örnek: Eğer a varsa a'nın bulunduğu değişkene git ve numara sırasını al. Bunu sifre listesine ekle """
for tx in TEXT.read().lower():
    if tx == aa:
        sifre.append(a)
    if tx == bb:
        sifre.append(b)
    if tx == cc:
        sifre.append(c)
    if tx == çç:
        sifre.append(ç)
    if tx == dd:
        sifre.append(d)
    if tx == ee:
        sifre.append(e)
    if tx == ff:
        sifre.append(f)
    if tx == gg:
        sifre.append(g)
    if tx == ğğ:
        sifre.append(ğ)
    if tx == hh:
        sifre.append(h)
    if tx == ıı:
        sifre.append(ı)
    if tx == ii:
        sifre.append(i)
    if tx == jj:
        sifre.append(j)
    if tx == kk:
        sifre.append(k)
    if tx == ll:
        sifre.append(l)
    if tx == mm:
        sifre.append(m)
    if tx == nn:
        sifre.append(n)
    if tx == oo:
        sifre.append(o)
    if tx == öö:
        sifre.append(ö)
    if tx == pp:
        sifre.append(p)
    if tx == rr:
        sifre.append(r)
    if tx == ss:
        sifre.append(s)
    if tx == şş:
        sifre.append(ş)
    if tx == tt:
        sifre.append(t)
    if tx == uu:
        sifre.append(u)
    if tx == üü:
        sifre.append(ü)
    if tx == vv:
        sifre.append(v)
    if tx == yy:
        sifre.append(y)
    if tx == zz:
        sifre.append(z)
    if tx == xx:
        sifre.append(x)

    if tx == noktaa:
        sifre.append(nokta)

    if tx == virgull:
        sifre.append(virgul)

    if tx == unlemm:
        sifre.append(unlem)

    if tx == boslukk:
        sifre.append(bosluk)

    if tx == dolarr:
        sifre.append(dolar)

    if tx == yüzdee:
        sifre.append(yüzde)

    if tx == vee:
        sifre.append(ve)

    if tx == tekNoktaa:
        sifre.append(tekNokta)

    if tx == parantezSoll:
        sifre.append(parantezSol)

    if tx == parantezSagg:
        sifre.append(parantezSag)

    if tx == yildizz:
        sifre.append(yildiz)
    if tx == tiree:
        sifre.append(tire)

    if tx == slashh:
        sifre.append(slash)

    if tx == ikinoktaa:
        sifre.append(ikinokta)

    if tx == noktaliVirgull:
        sifre.append(noktaliVirgul)

    if tx == kucukturr:
        sifre.append(kucuktur)

    if tx == buyukturr:
        sifre.append(buyuktur)

    if tx == esittirr:
        sifre.append(esittir)

    if tx == maill:
        sifre.append(mail)

    if tx == soruisaretii:
        sifre.append(soruisareti)

    if tx == karess:
        sifre.append(kares)

    if tx == ciftnoktaAyy:
        sifre.append(ciftnoktaAy)

    if tx == carpp:
        sifre.append(carp)

    if tx == susluparantezsoll:
        sifre.append(susluparantezsol)

    if tx == susluparantezsagg:
        sifre.append(susluparantezsag)

    if tx == alttiree:
        sifre.append(alttire)

    if tx == tersslashh:
        sifre.append(tersslash)

    if tx == sifirr:
        sifre.append(sifir)

    if tx == birr:
        sifre.append(bir)

    if tx == ikii:
        sifre.append(iki)

    if tx == ucc:
        sifre.append(uc)

    if tx == dortt:
        sifre.append(dort)

    if tx == bess:
        sifre.append(bes)

    if tx == altii:
        sifre.append(alti)

    if tx == yedii:
        sifre.append(yedi)

    if tx == sekizz:
        sifre.append(sekiz)

    if tx == dokuzz:
        sifre.append(dokuz)




""" Şifreli color renkleri [RGB] """
COLOR_KEY = []


print("Karakter Sayısı: " + str(len(sifre)))
print("Finish => output.png")


"""
0 = (x,Y,x) (0 > x < 255)
1 = (Y,Y,x) (256 > x < 999)
2 = (Y,Y,x) (1000 > x < 9999)
3 = (Y,Y,Yxx) (10.000 > x < 99.999)
4 = (Y,Y,x) + (Y,x,x) (100.000 > x < 999.999)

Not: Bu kısım şifreleme mantığını anlatır. Github'da Readme kısmında anlattım.
"""

if len(sifre) <= 255:
    px[0,0] = (
        (random.randint(1,255),
         len(sifre),
         int(str(random.randint(10,24)) + "0"))
    )


if len(sifre) > 255 and len(sifre) <= 999:

    SPLIT_INT = list(str(len(sifre)))

    px[0,0] = (
        (int(SPLIT_INT[0] + SPLIT_INT[1]),
         int(SPLIT_INT[2]),
         int(str(random.randint(10,25)) +  "1"))
    )



if len(sifre) >= 1000 and len(sifre) <= 9999:

    SPLIT_INT = list(str(len(sifre)))

    px[0,0] = (
        (int(SPLIT_INT[0] + SPLIT_INT[1]),
         int(SPLIT_INT[2] + SPLIT_INT[3]),
         int(str(random.randint(10, 25)) + "2"))
    )


if len(sifre) >= 10000 and len(sifre) <= 99999:

    SPLIT_INT = list(str(len(sifre)))

    px[0,0] =(
        (int(SPLIT_INT[0] + SPLIT_INT[1]),
         int(SPLIT_INT[2] + SPLIT_INT[3]),
         int(str(SPLIT_INT[4]) + "3"))
    )


if len(sifre) >= 100000 and len(sifre) <= 999999:

    SPLIT_INT = list(str(len(sifre)))

    px[0,0] =(
        (int(SPLIT_INT[0] + SPLIT_INT[1]),
         int(SPLIT_INT[2] + SPLIT_INT[3]),
         int(str(random.randint(10,25)) + "4"))
    )

    px[5,0] =(
        (int(SPLIT_INT[4] + SPLIT_INT[5]), random.randint(1,255), random.randint(1,255))
    )



""":arg
Verdiğimiz metindeki bütün karakterleri RGB değerinde listeye ekliyor
"""
for i in sifre:
    COLOR_KEY.append(
        (random.randint(0,255), int(i) ,random.randint(0,255))
    )




""":arg
Bu fonksiyonda resimde 0 pixelden başlayarak sonuna kadar RGB değerlerimizi ekliyoruz.
"""

if len(sifre) >= 100000 and len(sifre) <= 999999:
    x1 = 10
    y1 = 0

else:
    x1 = 5
    y1 = 0

def YERLESTIR(x):
    global px
    global x1
    global y1

    px[x1,y1] = x
    x1 += 5

    if x1 == 2560:
        y1 += 1
        x1 =  0

for i in COLOR_KEY:
    YERLESTIR(i)


image.save('output.png')


















