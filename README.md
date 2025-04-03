# YouTube Web Scraping Tool / YouTube Web Kazıma Aracı

Welcome to the YouTube Web Scraping Tool! / YouTube Web Kazıma Aracına hoş geldiniz!
This tool extracts video information from YouTube and saves it as a CSV file. / Bu araç, YouTube'dan video bilgilerini çıkartır ve CSV dosyası olarak kaydeder.
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

**English:**  
Choose one of the documentations above to get started in your preferred language.  

**Türkçe:**  
Tercih ettiğiniz dilde başlamak için yukarıdaki dokümantasyonlardan birini seçin.  

---

### Bilgilendirme / Information

#### Türkçe:  
Bazı YouTube kanalları, belirli verileri gizlemeyi tercih edebilir. Bu durumda, gizlenmiş veriler "Null" olarak görüntülenecektir. Benzer şekilde, eğer bir videonun yorumları kapalıysa, yorum sayısı alınamayacak ve sistem bunu "Error" olarak bildirecektir.  
Veri alma sürecinde karşılaşılan sorunlar kullanıcıya hata mesajı olarak gösterilecek ve bu durum, "Error" olarak veritabanına kaydedilecektir. Bunun yanı sıra, bazı videolara ait süre bilgileri yanlış olabilir. Video süresindeki bu hataların nedeni, genellikle reklamlardan veya YouTube oynatıcısındaki diğer teknik sorunlardan kaynaklanabilir.  

#### English:  
Some YouTube channels may choose to hide certain data, which will then be displayed as "Null." Similarly, if comments on a video are disabled, the comment count cannot be retrieved and will be recorded as "Error."  
Issues encountered during data collection will be presented as error messages on the screen and logged as "Error" in the database. Additionally, some video duration information may be inaccurate. Causes of incorrect durations often include advertisements or other technical issues within the YouTube player.  
