import os  # Dosya işlemleri için kullanılan kütüphaneyi ekleme işlemi


DOSYA_ADI = "gorevler.txt" # Görevlerin kaydedileceği dosya adı
gorevler = []  # Görevleri saklayacağımız liste

# Görevleri dosyadan okuma fonksiyonu
def gorevleri_yukle():
    if os.path.exists(DOSYA_ADI):  # Dosya varsa
        try:
            with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    gorevler.append(satir.strip())  # Satır sonundaki boşlukları silerek listeye ekle
            print("To-Do List Uygulamasına Hoş Geldiniz!\nGörevler başarıyla yüklendi.")
        except:
            print("To-Do List Uygulamasına Hoş Geldiniz!\nGörev dosyası okunamadı. Yeni bir liste oluşturuldu.")
    else:
        # Dosya yoksa kullanıcıyı bilgilendir
        print("To-Do List Uygulamasına Hoş Geldiniz!\nGörev dosyası bulunamadı. Yeni bir liste oluşturuldu.")

# Görevleri dosyaya yazdırma fonksiyonu
def gorevleri_kaydet():
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")  # Her görevi ayrı satıra yazdırıyor
    except:
        print("Görevler kaydedilirken bir hata oluştu.")

# Görev listesini ekrana yazdırma fonksiyonu
def gorevleri_listele():
    if not gorevler:
        print("Henüz görev bulunmamaktadır.")
    else:
        print("\n--- GÖREV LİSTESİ ---")
        for i, gorev in enumerate(gorevler, 1):  # Görevleri numaralandırarak sıralıyor
            print(f"{i}. {gorev}")
        print("--------------------")

# Yeni görev ekleme fonksiyonu
def yeni_gorev_ekle():
    gorev = input("Yeni görev: ").strip()
    if gorev:
        gorevler.append(gorev)  # Görevi listeye ekle
        print(f"'{gorev}' görevi eklendi.")
        gorevleri_kaydet()  # Değişiklikleri kaydet
    else:
        print("Boş görev eklenemez.")

# Mevcut görevi düzenleme fonksiyonu
def gorev_duzenle():
    gorevleri_listele()  # Önce görevleri göster
    try:
        no = int(input("Düzenlemek istediğiniz görevin numarası: "))
        if 1 <= no <= len(gorevler):
            yeni_metin = input(f"Yeni görev metni ({gorevler[no-1]}): ").strip()
            if yeni_metin:
                gorevler[no-1] = yeni_metin  # Görevi güncelle
                print("Görev başarıyla güncellendi.")
                gorevleri_kaydet()
            else:
                print("Boş görev girilemez.")
        else:
            print("Geçersiz görev numarası!")
    except ValueError:
        print("Lütfen bir sayı girin!")

# Görev silme fonksiyonu
def gorev_sil():
    gorevleri_listele()  # Önce görevleri göster
    try:
        no = int(input("Silmek istediğiniz görevin numarası: "))
        if 1 <= no <= len(gorevler):
            silinen = gorevler.pop(no-1)  # İlgili görevi listeden çıkarma
            print(f"'{silinen}' görevi silindi.")
            gorevleri_kaydet()
        else:
            print("Geçersiz görev numarası!")
    except ValueError:
        print("Lütfen bir sayı girin!")

# Ana menü döngüsü
def ana_menu():
    while True:
        print("\n--- TO-DO LIST UYGULAMASI ---")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle")
        print("4. Görev Sil")
        print("5. Çıkış")

        secim = input("Seçiminiz (1-5): ")

        if secim == "1":
            gorevleri_listele()
        elif secim == "2":
            yeni_gorev_ekle()
        elif secim == "3":
            gorev_duzenle()
        elif secim == "4":
            gorev_sil()
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break  # Döngüden çık ve programı bitir
        else:
            print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir sayı giriniz.")

gorevleri_yukle()
ana_menu()
