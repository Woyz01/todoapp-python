Basit Python Görev Takip Uygulaması (To-Do App)

Bu proje, tamamen terminal üzerinden çalışan basit bir **Görev Takip (To-Do)** uygulamasıdır.  
Kullanıcı görev ekleyebilir, listeleyebilir, silebilir ve görevleri *tamamlandı* olarak işaretleyebilir.  
Tüm görevler, tarih bilgileriyle birlikte bir `.txt` dosyasında saklanır.

---

 Özellikler

- Görev ekleme  
- Görevleri listeleme  
- Görev silme  
- Görevi **tamamlandı** olarak işaretleme  
- Her görev için:
  - Oluşturulma zamanı
  - Tamamlanma zamanı (varsa)
- Veriler kalıcı olarak `görevler.txt` dosyasında saklanır.

Görev satırları şu formatta tutulur:

```text
DURUM | GÖREV_METNİ | OLUŞTURULMA_ZAMANI | TAMAMLANMA_ZAMANI



Örnek olarak;
- ACTIVE | kahve iç | 13/11/2025 18:18:58 | -                         #ACTIVE = Görev aktif
- DONE   | spor yap | 13/11/2025 17:59:35 | 13/11/2025 18:05:12       #DONE = Görev tamamlandı
                                                                      # - henüz tamamlanma zamanı yok


Kullanılan Teknolojiler:

- Python 3
- Standart kütüphaneler(datatime, os)
- Dosya işlemleri(open, readlines, write, append)

Proje Dosya Yapısı

- todo.py → Görev takip (To-Do) uygulamasının ana dosyası
- görevler.txt → Görevlerin saklandığı veri dosyası
- kutuphane.py / kütüphane.txt → Daha önce yapılan basit kütüphane (kitap takip) çalışması
- gif_maker.py, output.gif → GIF oluşturma denemesi
- recoreder_core.py → Ses kaydedici çalışması
- .idea/ → PyCharm proje ayarları
