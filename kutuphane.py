while True:

    print("\n - kitap ekle(1)", "\n - kitapları listele(2)", "\n - kitap sil(3)", "\n - çıkış(4)")
    # Menüden sonra kitapları listeleyen kısımdır
    try:
        with open("kütüphane.txt", "r", encoding="utf-8") as file:
            kitaplar = file.readlines()
        if kitaplar:
            print("\n 📚 Kütüphanedeki kitaplar:")
            for k in kitaplar:
                print("-", k.strip())
        else:
            print("\nkütüphane şu anda boş.")

    except FileNotFoundError:
        print("\nHenüz kitap eklenmedi.")

    seçim = input("\nBir seçim yapınız:").strip().lower()

    try:
        if seçim == "1":
            kitap = str(input("Bir kitap ekle: "))
            if any(char.isdigit() for char in kitap):
                kitap = int(kitap)
                continue
            with open("kütüphane.txt", "a", encoding="utf-8") as file:
                file.write(kitap + "\n")
            print("Kitap eklendi.")
        elif seçim == "2":
          with open("kütüphane.txt", "r", encoding="utf-8") as file:
              kitaplar = file.readlines()
              if len(kitaplar) == 0:
                  print("Kitap yoktur.")
              else:
                  print("kayıtlı kitaplar")
                  for kitap in kitaplar:
                      print("-",kitap.strip())
        elif seçim == "3":
            with open("kütüphane.txt", "r", encoding="utf-8") as file:
                kitaplar = file.readlines()
            kitap = input("Silmek istediğiniz kitabı giriniz: ").strip()
            if kitap + "\n" in kitaplar:
                kitaplar.remove(kitap + "\n")
                with open("kütüphane.txt", "w", encoding="utf-8") as file:
                    for kitap in kitaplar:
                        print("-", kitap.strip())
                        file.write(kitap)
                print("Kitap silindi.")
            else:
                print("Kitap yoktur.")


        elif seçim == "4":
            print("çıkış")
            break
    except KeyboardInterrupt:
        print("Kitap eklendi.")
