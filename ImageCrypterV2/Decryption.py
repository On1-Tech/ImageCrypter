from PIL import Image
import time
import sys

""" Resimdeki pixellerin RGB değerlerini tutar. """
RGB_CHARACTER_LIST = []



""" Encryption edilmiş metini buraya yazıyoruz."""
OUTPUT = open('output.txt', 'w')



image = Image.open(sys.argv[1])
px = image.load()



""" Bu fonksiyon: eğer metin kaç karakterliyse ona göre pixel değerlerini alır.
 Örnek: 20 karakterliyse sadece resmin 20 pixelini alır.
 """
x1 = 5
y1 = 0

def YERLESTIR():
    global px
    global x1
    global y1

    RGB_CHARACTER_LIST.append(px[x1,y1])
    x1 += 5

    if x1 == 2560:
        y1 += 1
        x1 =  0




""" RGB değerinin (x,y,z) z kısmının son sayısını alır. """
CHECK_SPLIT = list(str(px[0,0][2]))[-1]

""" RGB değerinin (x,y,z) x kısmını alır. """
RGB_ZERO = px[0,0][0]

""" RGB değerinin (x,y,z) y kısmını alır. """
RGB_ONE  = px[0,0][1]

RGB_ONE_SPLIT  = list(str(px[0,0][1]))

""" RGB değerinin (x,y,z) z kısmını alır. """
RGB_TWO  = px[0,0][2]

""" RGB değerinin (x,y,z) z kısmının ilk harfini alır. """
CHECK_SPLIT_TWO = list(str(px[0,0][2]))[0]

""" RGB değerinin (x,y,z) x kısmının ilk harfini alır. Yukarıdan farkı ise bu 2 pixeli döndürür. """
RGB_SECTION_TWO = list(str(px[5,0][0]))[0]

RGB_SECTION_TWO_ONE = list(str(px[5,0][0]))

RGB_SECTION_TWO_ = int(px[5,0][0])



"""
0 = (x,Y,x) (0 > x < 255)
1 = (Y,Y,x) (256 > x < 999)
2 = (Y,Y,x) (1000 > x < 9999)
3 = (Y,Y,Yxx) (10.000 > x < 99.999)
4 = (Y,Y,x) + (Y,x,x) (100.000 > x < 999.999)

Not: Bu kısım şifreleme mantığını anlatır. Github'da Readme kısmında anlattım.
"""
if int(CHECK_SPLIT) == 0:
    for i in range(int(RGB_ONE)):
        YERLESTIR()



if int(CHECK_SPLIT) == 1:
    for i in range(int(str(RGB_ZERO) + str(RGB_ONE))):
        YERLESTIR()



if int(CHECK_SPLIT) == 2:
    if len(RGB_ONE_SPLIT) == 1:
        if int(RGB_ONE) == 0:
            for i in range(int(str(RGB_ZERO) + str(RGB_ONE) + "0")):
                YERLESTIR()
    else:
        for i in range(int(str(RGB_ZERO) + str(RGB_ONE))):
            YERLESTIR()



if int(CHECK_SPLIT) == 3:
    if len(RGB_ONE_SPLIT) == 1:
        if int(RGB_ONE) == 0:
            for i in range(int(str(RGB_ZERO) + str(RGB_ONE) + "0" + str(CHECK_SPLIT_TWO))):
                YERLESTIR()
    else:
        for i in range(int(str(RGB_ZERO) + str(RGB_ONE) + str(CHECK_SPLIT_TWO))):
            YERLESTIR()



if int(CHECK_SPLIT) == 4:
    if len(RGB_SECTION_TWO_ONE) == 1:
        if int(RGB_SECTION_TWO_ONE[0]) == 0:
            for i in range(int(str(RGB_ZERO) + str(RGB_ONE) + str(RGB_SECTION_TWO) + "0")):
                YERLESTIR()
    else:
        for i in range(int(str(RGB_ZERO) + str(RGB_ONE) + str(RGB_SECTION_TWO_))):
            YERLESTIR()


# ------------------------------------ Decryption -------------------------------------

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
parantezlistesagg = "]"

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



for tx in RGB_CHARACTER_LIST:
    if tx[1] == a:
        OUTPUT.write(aa)
    if tx[1] == b:
        OUTPUT.write(bb)
    if tx[1] == c:
        OUTPUT.write(cc)
    if tx[1] == ç:
        OUTPUT.write(çç)
    if tx[1] == d:
        OUTPUT.write(dd)
    if tx[1] == e:
        OUTPUT.write(ee)
    if tx[1] == f:
        OUTPUT.write(ff)
    if tx[1] == g:
        OUTPUT.write(gg)
    if tx[1] == ğ:
        OUTPUT.write(ğğ)
    if tx[1] == h:
        OUTPUT.write(hh)
    if tx[1] == ı:
        OUTPUT.write(ıı)
    if tx[1] == i:
        OUTPUT.write(ii)
    if tx[1] == j:
        OUTPUT.write(jj)
    if tx[1] == k:
        OUTPUT.write(kk)
    if tx[1] == l:
        OUTPUT.write(ll)
    if tx[1] == m:
        OUTPUT.write(mm)
    if tx[1] == n:
        OUTPUT.write(nn)
    if tx[1] == o:
        OUTPUT.write(oo)
    if tx[1] == ö:
        OUTPUT.write(öö)
    if tx[1] == p:
        OUTPUT.write(pp)
    if tx[1] == r:
        OUTPUT.write(rr)
    if tx[1] == s:
        OUTPUT.write(ss)
    if tx[1] == ş:
        OUTPUT.write(şş)
    if tx[1] == t:
        OUTPUT.write(tt)
    if tx[1] == u:
        OUTPUT.write(uu)
    if tx[1] == ü:
        OUTPUT.write(üü)
    if tx[1] == v:
        OUTPUT.write(vv)
    if tx[1] == y:
        OUTPUT.write(yy)
    if tx[1] == z:
        OUTPUT.write(zz)
    if tx[1] == x:
        OUTPUT.write(xx)
    if tx[1] == nokta:
        OUTPUT.write(noktaa)
    if tx[1] == virgul:
        OUTPUT.write(virgull)
    if tx[1] == unlem:
        OUTPUT.write(unlemm)
    if tx[1] == bosluk:
        OUTPUT.write(boslukk)
    if tx[1] == dolar:
        OUTPUT.write(dolarr)
    if tx[1] == yüzde:
        OUTPUT.write(yüzdee)
    if tx[1] == ve:
        OUTPUT.write(vee)

    if tx[1] == tekNokta:
        OUTPUT.write(tekNoktaa)
    if tx[1] == parantezSol:
        OUTPUT.write(parantezSoll)
    if tx[1] == parantezSag:
        OUTPUT.write(parantezSagg)
    if tx[1] == yildiz:
        OUTPUT.write(yildizz)
    if tx[1] == tire:
        OUTPUT.write(tiree)
    if tx[1] == slash:
        OUTPUT.write(slashh)
    if tx[1] == ikinokta:
        OUTPUT.write(ikinoktaa)

    if tx[1] == noktaliVirgul:
        OUTPUT.write(noktaliVirgull)
    if tx[1] == kucuktur:
        OUTPUT.write(kucukturr)
    if tx[1] == buyuktur:
        OUTPUT.write(buyukturr)
    if tx[1] == esittir:
        OUTPUT.write(esittirr)
    if tx[1] == mail:
        OUTPUT.write(maill)
    if tx[1] == soruisareti:
        OUTPUT.write(soruisaretii)
    if tx[1] == kares:
        OUTPUT.write(karess)

    if tx[1] == ciftnoktaAy:
        OUTPUT.write(ciftnoktaAyy)
    if tx[1] == carp:
        OUTPUT.write(carpp)
    if tx[1] == susluparantezsol:
        OUTPUT.write(susluparantezsoll)
    if tx[1] == susluparantezsag:
        OUTPUT.write(susluparantezsagg)
    if tx[1] == parantezlistesol:
        OUTPUT.write(parantezlistesoll)
    if tx[1] == parantezlistesag:
        OUTPUT.write(parantezlistesagg)
    if tx[1] == alttire:
        OUTPUT.write(alttiree)
    if tx[1] == tersslash:
        OUTPUT.write(tersslashh)

    if tx[1] == sifir:
        OUTPUT.write(sifirr)
    if tx[1] == bir:
        OUTPUT.write(birr)
    if tx[1] == iki:
        OUTPUT.write(ikii)

    if tx[1] == uc:
        OUTPUT.write(ucc)
    if tx[1] == dort:
        OUTPUT.write(dortt)
    if tx[1] == bes:
        OUTPUT.write(bess)
    if tx[1] == alti:
        OUTPUT.write(altii)
    if tx[1] == yedi:
        OUTPUT.write(yedii)

    if tx[1] == sekiz:
        OUTPUT.write(sekizz)
    if tx[1] == dokuz:
        OUTPUT.write(dokuzz)

print("Finish => output.txt")



