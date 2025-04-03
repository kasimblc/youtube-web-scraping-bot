# YouTube Web Scraping Tool / YouTube Web Kazıma Aracı

## English

This tool extracts video information from YouTube and saves it as a CSV file.

Select your preferred language to learn more about the project:

- 🌐 [English Documentation](README.en.md)

- 🇹🇷 [Türkçe Dokümantasyon](README.tr.md)

Information

Google Chrome 114 Download Links

For downloading the Google Chrome 114 version, please use one of the links below:

- [Google Chrome and Chromium 114 (Source 1)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)

- [Google Chrome and Chromium 114 (Source 2)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)

- [Google Chrome and Chromium 114 (Source 3)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)

Note: Currently, this bot supports only Google Chrome version 114.xx due to Selenium's compatibility limitations. To ensure smooth operation, please download Chrome 114 using the links above or search for Google Chrome 114 manually and install it on your system.

Disclaimer: The links provided above are sources found online. While I have used them without issues, I cannot guarantee their security. You may also search for Chrome 114 from official sources if you prefer.
---

### Overview
This project allows users to:
- Extract video metadata based on search queries.
- Save metadata into CSV files for easy usage.
- Customize searches by language and region.

### Quick Start
If you prefer to run the Python script, refer to the installation and usage instructions in the README files provided above.

### Search Options
When you run the script, you will be prompted to choose one of the following search methods:

1. **Standard Search:**  
   Enter a search term to perform a global search (without language or country restrictions). All videos matching the search term will be collected.
2. **Advanced Search:**  
   Advanced options will be provided:
   - **Video Count:** Specify the number of videos to retrieve (enter 0 to fetch all available videos).
   - **Search Language:** For example, "en" for English, "tr" for Turkish. Leave blank to disable the language filter.
   - **Search Country:** For example, "US" for the United States, "TR" for Turkey. Leave blank to disable the country filter.
3. **Continue Previous Search:**  
   If a previous search exists, enter the search term to resume from where you left off. If no saved data is available, a new search will be initiated.
4. **Search by Single URL:**  
   Enter a specific YouTube video URL to display metadata for that video only. In this mode, the metadata is shown on-screen and is not saved to the database.

### Features
- **Video Metadata Extraction:** Gathers relevant video information based on the search term.
- **CSV Output:** Saves the collected data into CSV files.
- **Advertisement and Short Video Filtering:** Automatically filters out unwanted content.
- **Resume Capability:** Preserves previously collected data, allowing the process to resume if interrupted.
- **Advanced Search Options:** Enables more specific results by filtering according to language, country, and video count.

### Extracted Data Fields
The tool extracts the following metadata fields from YouTube videos:
- Video Title
- Video URL
- Channel Name
- Upload Date
- Publish Date
- View Count
- Like Count
- Comment Count
- Subscriber Count
- Subscriber Count Text
- Video Duration
- Category

### Additional Information
- Some YouTube channels may choose to hide certain data; in these cases, the hidden information will be displayed as "Null."
- If comments are disabled for a video, the comment count will be recorded as "Error."
- Any issues encountered during data collection will be shown as error messages and logged as "Error" in the database.
- Video duration information may sometimes be inaccurate due to advertisements or other technical issues within the YouTube player.

---

## Türkçe

Bu araç, YouTube'dan video bilgilerini çıkartır ve CSV dosyası olarak kaydeder.

Proje hakkında daha fazla bilgi edinmek için tercih ettiğiniz dili seçin:

- 🌐 [English Documentation](README.en.md)

- 🇹🇷 [Türkçe Dokümantasyon](README.tr.md)

Bilgilendirme

Google Chrome 114 Sürümü İndirme Linkleri

Google Chrome 114 sürümünü indirmek için aşağıdaki linklerden birini kullanabilirsiniz:

- [Google Chrome and Chromium 114 (Source 1)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)

- [Google Chrome and Chromium 114 (Source 2)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)

- [Google Chrome and Chromium 114 (Source 3)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)

Not: Bu bot, şu an Google Chrome 114.xx sürümünü desteklemektedir çünkü Selenium'un mevcut sürümü yalnızca Chrome 114 ile uyumludur. Sorunsuz çalışması için yukarıdaki bağlantılardan Chrome 114 sürümünü indirip yükleyebilir veya Google Chrome 114 araması yaparak manuel olarak sisteminize yükleyebilirsiniz.

Sorumluluk Reddi: Yukarıda verilen bağlantılar internette bulunan kaynaklardır. Ben kullanırken herhangi bir sorun yaşamadım, ancak güvenliklerinden sorumlu değilim. İsterseniz Chrome 114 sürümünü resmi kaynaklardan arayıp indirebilirsiniz.
---

### Genel Bakış
Bu proje kullanıcılara şunları sağlar:
- Arama sorgularına dayalı olarak video meta verilerini çıkartır.
- Meta verilerini kolay kullanım için CSV dosyalarına kaydeder.
- Aramaları dil ve bölgeye göre özelleştirir.

### Hızlı Başlangıç
Eğer Python betiğini çalıştırmayı tercih ediyorsanız, yukarıda verilen README dosyalarından kurulum ve kullanım talimatlarına ulaşabilirsiniz.

### Arama Yöntemleri
Script çalıştırıldığında aşağıdaki seçeneklerden birini seçmeniz istenir:

1. **Standart Arama:**  
   Arama terimi girerek, dil veya ülke sınırlaması olmaksızın global arama yapılır. Arama terimine uyan tüm videolar toplanır.
2. **Özel Arama:**  
   Gelişmiş seçenekler sunulur:
   - **Video Sayısı:** Alınacak video adedini belirtin (tüm videolar için 0 girin).
   - **Arama Dili:** Örneğin, İngilizce için "en", Türkçe için "tr". Boş bırakılırsa dil filtresi uygulanmaz.
   - **Arama Ülkesi:** Örneğin, Amerika için "US", Türkiye için "TR". Boş bırakılırsa ülke filtresi uygulanmaz.
3. **Önceki Aramayı Devam Ettir:**  
   Daha önce başlatılmış bir arama varsa, arama terimini girerek kaldığınız yerden devam edebilirsiniz. Kayıtlı veri yoksa yeni bir arama başlatılır.
4. **Tek Bir URL ile Arama:**  
   Belirli bir YouTube video URL'si girerek sadece o videonun meta verilerini görüntüleyin. Bu modda, veriler yalnızca ekranda gösterilir ve veritabanına kaydedilmez.

### Özellikler
- **Video Meta Verisi Kazıma:** Girilen arama terimlerine göre ilgili video bilgilerini toplar.
- **CSV Çıktısı:** Çekilen verileri CSV dosyaları olarak kaydeder.
- **Reklam ve Kısa Video Filtreleme:** İstenmeyen içerikler otomatik olarak yok sayılır.
- **Devam Ettirme Özelliği:** İşlem kesintiye uğrarsa, daha önce toplanan veriler korunarak kaldığı yerden devam edilebilir.
- **Gelişmiş Arama Seçenekleri:** Arama dili, ülke ve video adedi gibi kriterlerle daha spesifik sonuçlar elde edilebilir.

### Çekilen Veri Alanları
Araç, YouTube videolarından aşağıdaki meta verileri çıkartır:
- Video Başlığı
- Video URL'si
- Kanal Adı
- Yüklenme Tarihi
- Yayınlanma Tarihi
- İzlenme Sayısı
- Beğeni Sayısı
- Yorum Sayısı
- Abone Sayısı
- Abone Sayısı Metni
- Video Süreci
- Kategori
