import sqlite3


con = sqlite3.connect("kütüphane.db")

cursor=con.cursor()


def tablo_olustur ():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,yazar TEXT ,yayınevi TEXT , sayfa INT)")
    con.commit()

def veri_ekle(isim,yazar,yayınevi,sayfa):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa))
    con.commit()
    
def verileri_al_yazara_göre(yazar):
    cursor.execute("Select * From kitaplık where  yazar = ? ",(yazar,))
    liste=cursor.fetchall()
    for i in liste :
        print(i)
def verileri_al_yayınevine_göre(yayınevi):
    cursor.execute("Select * From kitaplık where  yayınevi = ? ",(yayınevi,))
    liste=cursor.fetchall()
    for i in liste :
        print(i)

def veri_güncelle_yayınevi(eski,yeni) :
    cursor.execute("UPDATE kitaplık set yayınevi = ? where yayınevi = ?",(yeni,eski))
    con.commit()

def veri_sil_yazara_göre(yazar):
    cursor.execute("DELETE From kitaplık where yazar= ? ",(yazar,))
    con.commit()
def veri_sil_yayınevine_göre(yayınevi):
    cursor.execute("DELETE From kitaplık where yayınevi= ? ",(yayınevi,))
    con.commit()



tablo_olustur()

veri_ekle('Safahat','Mehmet Akif Ersoy','Dergah',662)
veri_ekle('Sefiller','Victor Hugo','Dünya Klasikleri',871)
veri_ekle('Beyaz Diş','Jack London','Dünya Klasikleri',445)            #Kitaplar veritabanına ekleniyor.
veri_ekle('Siyah İnci','Anna Sewell','İş Bankası',255)
veri_ekle('Körlük','Jose Saramago','Kırmızı Kedi',284)
veri_ekle('1984','George Orwell','Can',352)

veri_güncelle_yayınevi('Dünya Klasikleri','Eski')      # 'Dünya Klasikleri' Yayınevinin yeni adı 'Eski'

#veri_sil_yazara_göre('Jack London')     # Yorum satırını kaldırarak Jack London Kitaplarını veritabanından silebilirsiniz.

verileri_al_yayınevine_göre('Eski')   # 'Eski' yayınevi bünyesindeki kitaplar.



con.close()
