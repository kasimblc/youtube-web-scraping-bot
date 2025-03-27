# YouTube Web Kazıma Aracı
## YouTube Video Bilgisi Kazıyıcı

Bu proje, YouTube'dan video bilgilerini kazımak ve bunları CSV dosyası olarak kaydetmek için tasarlanmış bir web kazıma aracıdır. Bu araç, tarayıcı otomasyonu için Selenium ve veri manipülasyonu ve depolama için çeşitli Python kütüphanelerini kullanır.

Kullanıcılar bir arama terimi girebilir ve program, ilgili tüm videoları kazıyacaktır. Reklamları ve kısa videoları yok sayar. Ayrıca, kaldığı yerden devam etme ve detaylı aramalar yapma özelliklerini destekler.

## Özellikler
- Kullanıcı tarafından sağlanan arama terimlerine dayalı olarak YouTube'dan video meta verilerini kazır.
- Çekilen verileri CSV dosyalarına kaydeder.
- Reklamları ve kısa videoları yok sayar.
- Kaldığı yerden devam etmeyi destekler.
- Daha spesifik sonuçlar için detaylı aramalara izin verir.

## Gereksinimler
- Python 3.x
- Google Chrome tarayıcısı

### Adımlar
1. Depoyu klonlayın:
    ```sh
    git clone https://github.com/kasimblc/youtube-bot
    cd youtube-bot
    ```

2. Gerekli kütüphaneleri yükleyin:
    ```sh
    pip install -r requirements.txt
    ```
    
3. Eğer gerekli kütüphaneler daha önceden yüklü ise, aşağıdaki komutlarla kütüphaneleri en son sürüme güncelleyin:
    - **yt-dlp**: YouTube'dan video bilgisi kazımak için.
    - **selenium**: Tarayıcı otomasyonu için.
    - **webdriver-manager**: ChromeDriver sürüm yönetimi için.

    Güncelleme komutları:
    ```sh
    pip install --upgrade yt-dlp
    pip install --upgrade selenium
    pip install --upgrade webdriver-manager
    ```
    
## Kullanım
1. **Scripti çalıştırın**:
    ```sh
    python YoutubeBot.py
    veya
    python3 YoutubeBot.py
    ```

2. **Arama Yöntemini Seçin**:
   - Script çalıştırıldığında, aşağıdaki arama yöntemlerinden birini seçmeniz istenir:
     - **1: Standart Arama**:  
       - Videoları almak için bir arama terimi girin.  
       - Varsayılan olarak dil veya ülke sınırlamaları olmadan global bir arama yapılır.  
       - Arama terimine uyan tüm videolar alınır.  
     - **2: Özel Arama**:  
       - Gelişmiş arama seçeneklerine izin verir. Belirleyebileceğiniz kriterler:  
         - **Video Sayısı**: Kaç video alınacağını tanımlayın. Tüm videoları almak için `0` girin.  
         - **Arama Dili**: Dili belirtin (ör. İngilizce için `en`, Türkçe için `tr`). Boş bırakılırsa dil filtresi uygulanmaz.  
         - **Arama Ülkesi**: Ülkeyi belirtin (ör. Amerika için `US`, Türkiye için `TR`). Boş bırakılırsa ülke filtresi uygulanmaz.  
       - Bu seçenekler, aramanızı daha spesifik hale getirmenizi sağlar.  
     - **3: Önceki Aramayı Devam Ettir**:  
       - Daha önce başlatılmış bir arama varsa, kaldığı yerden devam etmek için arama terimini girin.  
       - Kayıtlı veri bulunmazsa, yeni bir arama başlatmanız istenir.

3. **Arka Plan İşlemi**:
   - Script tamamen arka planda çalışır. Tarayıcı penceresi veya grafik arayüz açmaz. Tüm işlemler programlama düzeyinde gerçekleştirilir.

4. **Veri Çıktısı**:
   - Kazılan video meta verileri, çalıştırılan dizinde bir **CSV dosyası** olarak kaydedilir. Her satırda video başlıkları, URL'ler ve diğer mevcut meta veriler bulunur.

5. **Hata İşleme**:
   - Belirli video verileri gizlenmişse (ör. kanal sınırlamaları nedeniyle), eksik değerler `Null` olarak görüntülenir.  
   - İşlem sırasında karşılaşılan hatalar terminalde görüntülenir ve çıktı dosyasında `Error` olarak işaretlenir.

6. **Devam Etme Fonksiyonu**:
   - Script kesintiye uğrarsa, kazıma işlemini daha önce toplanmış verileri kaybetmeden kaldığı yerden devam ettirebilir.

## Katkıda Bulunma
Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, sorun bildirimleri veya "pull request"ler göndermekten çekinmeyin.

## Lisans
Bu proje GNU Genel Kamu Lisansı v3.0 altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyin.
