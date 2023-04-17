Dosya Şifreleme Uygulaması

Bu uygulama, kullanıcıların belirlediği bir şifre kullanarak dosyalarını şifrelemelerine ve şifreli dosyaları çözmelerine olanak tanır.
Kurulum

    Bu projeyi klonlayın:

    bash

git clone https://github.com/kullanici_adi/dosya-sifreleme-uygulamasi.git

Gerekli paketleri yükleyin:

pip install cryptography

Uygulamayı başlatmak için main.py dosyasını çalıştırın:

css

    python main.py

Kullanım

    Uygulama başlatıldığında, şifreleme veya çözme işlemi seçmeniz gereken bir menü görüntülenir.
    Şifreleme işlemi seçilirse, dosyanın tam yolunu ve şifreyi girmeniz istenir.
    Çözme işlemi seçilirse, şifreli dosyanın tam yolunu ve şifreyi girmeniz istenir.
    İşlem tamamlandıktan sonra, şifreli dosya oluşturulur veya çözülmüş dosya görüntülenir.

Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
Katkıda Bulunma

    Bu projeyi fork edin.
    Yeni bir branch oluşturun: git checkout -b my-new-feature
    Yaptığınız değişiklikleri commit edin: git commit -am 'Add some feature'
    Branch'ınıza push yapın: git push origin my-new-feature
    Pull request açın.