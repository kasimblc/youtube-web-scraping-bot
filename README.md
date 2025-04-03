# YouTube Web Scraping Tool / YouTube Web Kazıma Aracı

Welcome to the YouTube Web Scraping Tool! / YouTube Web Kazıma Aracına hoş geldiniz!
This tool extracts video information from YouTube and saves it as a CSV file. / 

Bu araç, YouTube'dan video bilgilerini çıkartır ve CSV dosyası olarak kaydeder.
Select your preferred language to learn more about the project: / Proje hakkında daha fazla bilgi edinmek için tercih ettiğiniz dili seçin:

- 🌐 [English Documentation](README.en.md) / 🌐 [İngilizce Dokümantasyon](README.en.md)
- 🇹🇷 [Türkçe Dokümantasyon](README.tr.md) / 🇹🇷 [Türkçe Dokümantasyon](README.tr.md)

---

## Overview / Genel Bakış

**English:**  
This project allows users to:  
- Extract video metadata based on search queries.  
- Save metadata into CSV files for easy usage.  
- Customize searches by language and region.  

**Türkçe:**  
Bu proje kullanıcılara şunları sağlar:  
- Arama sorgularına dayalı olarak video meta verilerini çıkartır.  
- Meta verilerini kolay kullanım için CSV dosyalarına kaydeder.  
- Aramaları dil ve bölgeye göre özelleştirir.  

---

## Quick Start / Hızlı Başlangıç


## Quick Start / Hızlı Başlangıç

## Pre-compiled Executable / Derlenmiş Çalıştırılabilir Versiyon

**English:**  
A pre-compiled executable (exe) version is now included, which is ready to run immediately without any additional setup. However, to use this executable, you need to have one of the Google Chrome 114.x versions installed on your system. You can download it from the links provided below or search for it on Google.

**Türkçe:**  
Kullanıma hazır derlenmiş bir exe versiyonu eklenmiştir. Ekstra kurulum gerektirmeden doğrudan çalıştırılabilir. Ancak, bu exe dosyasını kullanabilmek için sisteminizde Google Chrome'un 114.x sürümlerinden birinin yüklü olması gerekmektedir. Aşağıdaki linklerden birinden indirebilir veya Google'da aratarak bulabilirsiniz.

**English:**  
If you prefer to run the Python script instead of the executable, you can refer to the installation and usage instructions in the README files provided above.

**Türkçe:**  
Eğer exe yerine Python betiğini çalıştırmayı tercih ediyorsanız, yukarıda verilen README dosyalarından kurulum ve kullanım talimatlarına ulaşabilirsiniz.

---

### Bilgilendirme / Information

### Google Chrome 114 Sürümü İndirme Linkleri / Google Chrome 114 Download Links
Google Chrome 114 sürümünü indirmek için aşağıdaki linklerden birini kullanabilirsiniz:  
For downloading the Google Chrome 114 version, please use one of the links below:
- [Google Chrome ve Chromium 114 (Kaynak 1)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)  
- [Google Chrome ve Chromium 114 (Kaynak 2)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)  
- [Google Chrome ve Chromium 114 (Kaynak 3)](https://www.getgnu.org/internet/google-chrome-ve-chromium-114-0-5735-90-ve-91-surumleri-duyuruldu.html)

## Search Options / Arama Yöntemleri
When you run the script, you will be prompted to choose one of the following search methods:

**English:**
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

**Türkçe:**
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

---

## Features / Özellikler
**English:**
- **Video Metadata Extraction:** Gathers relevant video information based on the search term.
- **CSV Output:** Saves the collected data into CSV files.
- **Advertisement and Short Video Filtering:** Automatically filters out unwanted content.
- **Resume Capability:** Preserves previously collected data, allowing the process to resume if interrupted.
- **Advanced Search Options:** Enables more specific results by filtering according to language, country, and video count.

**Türkçe:**
- **Video Meta Verisi Kazıma:** Girilen arama terimlerine göre ilgili video bilgilerini toplar.
- **CSV Çıktısı:** Çekilen verileri CSV dosyaları olarak kaydeder.
- **Reklam ve Kısa Video Filtreleme:** İstenmeyen içerikler otomatik olarak yok sayılır.
- **Devam Ettirme Özelliği:** İşlem kesintiye uğrarsa, daha önce toplanan veriler korunarak kaldığı yerden devam edilebilir.
- **Gelişmiş Arama Seçenekleri:** Arama dili, ülke ve video adedi gibi kriterlerle daha spesifik sonuçlar elde edilebilir.

---

## Extracted Data Fields / Çekilen Veri Alanları
The tool extracts the following metadata fields from YouTube videos:

**English:**
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

**Türkçe:**
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
- Video Süresi
- Kategori

---

## Additional Information / Ek Bilgiler
**English:**
- Some YouTube channels may choose to hide certain data; in these cases, the hidden information will be displayed as "Null."
- If comments are disabled for a video, the comment count will be recorded as "Error."
- Any issues encountered during data collection will be shown as error messages and logged as "Error" in the database.
- Video duration information may sometimes be inaccurate due to advertisements or other technical issues within the YouTube player.

**Türkçe:**
- Bazı YouTube kanalları, belirli verileri gizlemeyi tercih edebilir. Bu durumda, gizlenen veriler "Null" olarak görüntülenir.
- Eğer bir videonun yorumları kapalıysa, yorum sayısı "Error" olarak kaydedilir.
- Veri toplama sırasında karşılaşılan sorunlar, ekranda hata mesajı olarak gösterilir ve veritabanına "Error" olarak kaydedilir.
- Video süresi bilgisi, reklamlardan veya YouTube oynatıcısındaki teknik sorunlardan dolayı bazen hatalı olabilir.
