website = "http://www.morsakademi.com"
kursAdi = "Python Dersleri: Sıfırdan Python Programlama Dersleri."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
a = " Hello world "
print(a.strip())
# 2- 'www.morsakademi.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
print("www.morsakademi.com".strip("www,com"))
# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
print(kursAdi.lower())
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
print(website.count("a"))
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
print(website.startswith("www"))
print(website.endswith("com"))
# 6- 'website' içinde '.com' ifadesi var mı?
print(website.find(".com"))
# sonuc = kursAdi.index('Python')
# sonuc = kursAdi.rindex('Python')
# sonuc = kursAdi.index('React')

# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(kursAdi.isalpha())
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
print("Contents".center(50,'*'))
# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
print(kursAdi.replace(" ","-"))
# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print("Hello World".replace("World","There"))
# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
print(kursAdi.split(" "))