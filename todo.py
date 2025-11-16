from datetime import datetime


while True:

    print("\n - Görev ekle(1)", "\n - Görevleri Listele(2)", "\n - Görev sil(3)", "\n - Görevi tamamladı olarak işaretle(4)", "\n - Çıkış(5)")

    seçim: str = input("Lütfen bir seçim yapınız:").strip().lower()


    try:
        if seçim == "1":
            görev = str(input("lütfen bir görev ekleyiniz:")).strip().lower()
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            satır = "ACTIVE | " + görev + " | " + date + " | -"
            if any(char.isdigit() for char in görev):
                görev = int(görev)
                continue
            with open("görevler.txt", "a", encoding="utf-8") as file:
                file.write(satır + "\n")
            print("görev eklendi.")

        elif seçim == "2":
            with open("görevler.txt", "r", encoding="utf-8") as file:
                görevler = file.readlines()
                if len(görevler) == 0:
                    print("Henüz görev yok.")
                else:
                    print("Tüm görevler:\n")
                    for satır in görevler:
                        satır = satır.strip()
                        parcalar = satır.split(" | ")

                        if len(parcalar) != 4:
                            print("❌", satır)
                            continue

                        durum, metin, olusturma, tamamlama = parcalar

                        ikon = "✅" if durum == "DONE" else "❌"

                        if tamamlama == "-":
                            print(f"{ikon} {metin} (Oluşturma: {olusturma}, Tamamlanma: Yok)")
                        else:
                            print(f"{ikon} {metin} (Oluşturma: {olusturma}, Tamamlanma: {tamamlama})")



        elif seçim == "3":
            with open("görevler.txt", "r", encoding="utf-8") as file:
                görevler = file.readlines()
                sil = input("Lütfen silmek istediğiniz görevi giriniz:").strip().lower()
                if sil + "\n" in görevler:
                    görevler.remove(sil + "\n")
                    with open("görevler.txt", "w", encoding="utf-8") as file:
                        for görev in görevler:
                            file.write(görev)
                        print("Görev silindi.")
                else:
                    print("Bu isimde bir görev yok.")

        elif seçim == "4":
            with open("görevler.txt", "r", encoding="utf-8") as file:
                görevler = file.readlines()
                görev = input("hangi görevi tamamlandı olarak işaretlemek istiyorsun?:").strip().lower()
                if görev + "\n" in görevler:
                    for i in range(len(görevler)):
                        görevler[i] = "✅" + görev + "\n"
                        break
                    with open("görevler.txt", "w", encoding="utf-8") as file:
                        for görev in görevler:
                             file.write(görev)
                             print("Görev tamamlandı olarak işaretlendi.")


        elif seçim == "5":
            print("çıkış")
            break





    except FileNotFoundError:
        print("görevler mevcuttur.")











