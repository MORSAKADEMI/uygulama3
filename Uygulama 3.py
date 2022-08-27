website = "http://www.morsakademi.com"
kursAdi = "Python Dersleri: Sıfırdan Python Programlama Dersleri."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
cozum = " Hello World ".strip()

# 2- 'www.morsakademi.com' içindeki morsakademi bilgisi haricindeki her karakteri silin.
cozum2 = "www.morsakademi.com".lstrip("w.").rstrip(".com")
#morsakademinin içinde m ve o olduğu için .strip("w.com") olmuyor!

# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
cozum3 = kursAdi.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
cozum4 = website.count("a")

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
cozum5 = website.startswith("www"),website.endswith("com")

# 6- 'website' içinde '.com' ifadesi var mı?
cozum6 = website.find(".com")

# sonuc = kursAdi.index('Python')
# sonuc = kursAdi.rindex('Python')
# sonuc = kursAdi.index('React')

# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
cozum7 = kursAdi.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
cozum8 = "Contents".center(50,"*")

# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
cozum9 = kursAdi.replace(" ","-")

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
cozum10 = "Hello World".replace("World","There")

# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
cozum11 = kursAdi.split()
