# YouTube Web Kazıma Aracı
## YouTube Video Bilgisi Kazıyıcı

---

Bu proje, YouTube’dan video bilgilerini kazıyarak bunları CSV formatında saklamak için geliştirilmiş bir araçtır. Selenium ile tarayıcı otomasyonu sağlanırken, veri işleme ve depolama işlemleri için çeşitli Python kütüphaneleri kullanılır. Proje; reklamlar ve kısa videoları filtrelemek, kaldığı yerden devam etmek ve gelişmiş arama seçenekleri sunmak gibi özellikler içerir.

### Özellikler
- **Video Meta Verisi Kazıma:** Girilen arama terimlerine göre ilgili video bilgilerini toplar.
- **CSV Çıktısı:** Çekilen verileri CSV dosyaları olarak kaydeder.
- **Reklam ve Kısa Video Filtreleme:** İstenmeyen içerikler otomatik olarak yok sayılır.
- **Devam Ettirme Özelliği:** İşlem kesintiye uğrarsa, daha önce toplanan veriler korunarak kaldığı yerden devam edilebilir.
- **Gelişmiş Arama Seçenekleri:** Arama dili, ülke ve video adedi gibi kriterlerle daha spesifik sonuçlar elde edilebilir.

---

## Gereksinimler

### 1. Python Sürümü
- **Python 3.x:** En güncel 3.x sürümünün kurulu olduğundan emin olun.

### 2. Google Chrome Tarayıcısı ve ChromeDriver
- **Google Chrome:** Projede kullanılacak tarayıcıdır.
- **ChromeDriver:** Selenium’un otomasyonu gerçekleştirebilmesi için gereklidir.
  - **Önemli:**  
    - Program, en güncel ChromeDriver sürümünü otomatik olarak indirir. Kullanıcının yalnızca kendi Chrome tarayıcı sürümünü uygun hale getirmesi gerekmektedir.
    - Yanlış sürüm kombinasyonu otomasyon sürecinde hatalara yol açabilir.
    - Yeni Chrome sürümleri çıktığında, uyumluluğu kontrol etmek için aşağıdaki komut kullanılabilir.
  - **Chrome Sürümünü Kontrol Etme:**
    ```sh
    chrome --version  # veya Windows için "chrome.exe --version"
    ```
  - Eğer Chrome sürümünüz mevcut ChromeDriver sürümüyle uyumlu değilse, uygun Chrome sürümünü yükleyin.

### 3. Kütüphanelerin Güncellenmesi
- Projede kullanılan kütüphanelerin en güncel sürümleriyle çalışması önemlidir. Güncel kütüphane sürümleri, hata düzeltmeleri ve yeni özellikler içerir.
- **Gerekli kütüphaneler:**
  - **yt-dlp:** YouTube’dan video bilgisi kazımak için.
  - **selenium:** Tarayıcı otomasyonu için.
  - **webdriver-manager:** ChromeDriver sürüm yönetimi için.
- Kurulum ve güncelleme adımları sırasında aşağıdaki komutları kullanın:
    ```sh
    pip install -r requirements.txt
    pip install --upgrade yt-dlp selenium webdriver-manager
    ```

---

## Kurulum Adımları

1. **Depoyu Klonlayın:**
    ```sh
    git clone https://github.com/kasimblc/youtube-bot
    cd youtube-bot
    ```

2. **Gerekli Kütüphaneleri Yükleyin:**
    ```sh
    pip install -r requirements.txt
    ```

3. **(Opsiyonel) Kütüphane Güncellemeleri:**
    Eğer kütüphaneler önceden yüklenmişse, aşağıdaki komutlarla güncellemeyi yapabilirsiniz:
    ```sh
    pip install --upgrade yt-dlp
    pip install --upgrade selenium
    pip install --upgrade webdriver-manager
    ```

---

## Kullanım

### Çalıştırma Adımları

1. **Scripti Başlatın:**
    ```sh
    python YoutubeBot.py
    ```
    veya
    ```sh
    python3 YoutubeBot.py
    ```

2. **Arama Yöntemini Seçin:**
   Script çalıştırıldığında, aşağıdaki seçeneklerden birini seçmeniz istenir:
   - **1: Standart Arama**  
     - Bir arama terimi girerek, global (dil veya ülke sınırlaması olmadan) arama yapılır.
     - Arama terimine uyan tüm videolar toplanır.
   
   - **2: Özel Arama**  
     - Gelişmiş arama seçenekleri sunulur:
       - **Video Sayısı:** Alınacak video adedini belirtin. Tüm videolar için `0` girin.
       - **Arama Dili:** Örneğin İngilizce için `en`, Türkçe için `tr`. Boş bırakılırsa dil filtresi uygulanmaz.
       - **Arama Ülkesi:** Örneğin Amerika için `US`, Türkiye için `TR`. Boş bırakılırsa ülke filtresi uygulanmaz.
   
   - **3: Önceki Aramayı Devam Ettir**  
     - Daha önce başlatılmış bir arama varsa, arama terimini girerek kaldığınız yerden devam edebilirsiniz.  
     - Kayıtlı veri yoksa, yeni bir arama başlatmanız istenir.
   
   - **4: Tek Bir URL ile Arama**  
     - Belirli bir YouTube video URL’si girerek sadece o videonun meta verilerini görüntüleyin.
     - Bu seçim, meta verileri yalnızca ekranda gösterir; veritabanına kayıt yapılmaz.

---

## Ek Bilgilendirme

### Arka Plan İşlemi
- Script, tamamen arka planda çalışır. Tarayıcı penceresi veya grafik arayüz açılmadan tüm işlemler programatik olarak gerçekleştirilir.

### Veri Çıktısı
- Kazıma işlemi sonunda, video meta verileri scriptin çalıştırıldığı dizinde bir **CSV dosyası** olarak kaydedilir.
- Her satır; video başlığı, URL ve diğer mevcut meta verileri içerir.

### Hata İşleme
- Eğer bazı video verileri gizlenmişse (örneğin, kanal sınırlamaları nedeniyle), eksik değerler `Null` olarak görüntülenir.
- İşlem sırasında oluşan hatalar terminalde görüntülenir ve çıktı dosyasında `Error` olarak işaretlenir.

### Devam Ettirme Fonksiyonu
- Script kesintiye uğrarsa, daha önce toplanan veriler kaybolmadan kaldığı yerden devam ettirilebilir.

---

## Katkıda Bulunma
Hata bildirimleri, iyileştirme önerileri veya katkılarınız için lütfen "pull request" gönderin veya sorun bildirimi oluşturun.

---

## Lisans
Bu proje, GNU Genel Kamu Lisansı v3.0 kapsamında lisanslanmıştır. Detaylar için lütfen LICENSE dosyasına bakınız.
