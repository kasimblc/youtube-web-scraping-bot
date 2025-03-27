import csv
import os
from datetime import datetime
import yt_dlp
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

#Selenium Bot İşlemleri

def setup_driver():
    """
    Chrome WebDriver'ını başlatmak için gerekli ayarları yapar.
    """
    options = Options()
    options.add_argument('--headless')  # Başlatma işlemini gizli modda yapar.
    options.add_argument("--incognito")
    options.add_argument('--no-sandbox')  # Sandbox'ı devre dışı bırakır.
    options.add_argument('--disable-dev-shm-usage')  # /dev/shm kullanımını devre dışı bırakır.
    options.add_argument('--disable-gpu')  # GPU kullanımını devre dışı bırakır.
    #options.add_argument('--ignore-certificate-errors')  # SSL sertifikası hatalarını görmezden gelir.
    options.add_argument('--window-size=1920,1080')  # Pencere boyutunu ayarlar (isteğe bağlı).

    # Çerezleri devre dışı bırakma
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-plugins-discovery')
    options.add_argument('--disable-blink-features=AutomationControlled')
    prefs = {'profile.managed_default_content_settings.cookies': 2}
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

###Video Link Liste İşlemleri

def get_video_links(search_term, num_videos, language=None, country=None):
    """
    Verilen arama terimi için YouTube video linklerini döndürür.
    """
    print("Arama işlemi sürüyor Lütfen bekleyin...")

    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'noplaylist': True,
        'type': 'video',
    }

    #language = "en"

    if language:
        ydl_opts['geo-bypass-language'] = language
    
    if country:
        ydl_opts['geo-bypass-country'] = country

    video_links = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_query = f"ytsearchall:{search_term}"
        result = ydl.extract_info(search_query, download=False)
        entries = result.get('entries', [])
        total_results = len(entries)
        print("")
        print(f"Bulunan toplam video sayısı: {total_results}")
        print(f"Alınan video sayısı: {num_videos if num_videos > 0 else total_results}")
        print("")
        for entry in entries[:num_videos] if num_videos > 0 else entries:
            video_title = entry.get('title')
            video_url = f"https://www.youtube.com/watch?v={entry.get('id')}"
            video_links.append((video_title, video_url))
    return video_links

###Veri Alma İşlemleri

def get_like_count(driver):
    """
    YouTube videosunun beğeni sayısını alır ve ekrana yazdırır.
    """
    try:
        # Beğeni butonunu CSS seçici ile bulma
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.yt-spec-button-shape-next.yt-spec-button-shape-next--tonal.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading.yt-spec-button-shape-next--segmented-start'))
        )
        
        # Beğeni butonunun aria-label özniteliğini alıp yazdırma
        label_text = like_button.get_attribute('aria-label')
        
        # Metin içerisinden sayı değerini çıkarma
        like_count = extract_like_count(label_text)
        return like_count

    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_view_count(driver):
    """
    YouTube videosunun görüntülenme sayısını alır.
    """
    try:
        view_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="interactionCount"][content]'))
        )
        return view_count.get_attribute('content')

    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_upload_date(driver):
    """
    YouTube videosunun yüklenme tarihini alır.
    """
    try:
        upload_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="uploadDate"][content]'))
        )
        return upload_date.get_attribute('content').split('T')[0] if upload_date else None

    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_subscriber_count(driver):
    """
    YouTube videosunun kanal abone sayısını alır.
    """
    try:
        subscriber_count_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#owner-sub-count'))
        )
        subscriber_count_str = subscriber_count_element.get_attribute('aria-label')
        
        # Metindeki tırnak işaretlerini kaldır
        #cleaned_subscriber_count_str = subscriber_count_str.replace('"', '')
        
        return subscriber_count_str
    
    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_duration(driver):
    """
    YouTube videosunun süresini alır.
    """
    try:
        # Önce tüm zaman göstergesi divini bul
        time_display_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ytp-time-display.notranslate'))
        )

        # Daha sonra bu div içinde süreyi içeren span'i bul
        duration_element = time_display_div.find_element(By.CSS_SELECTOR, '.ytp-time-duration')
        
        return duration_element.text

    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_channel_name(driver):
    """
    YouTube videosunun kanal adını alır.
    """
    try:
        channel_name_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ytd-channel-name a'))
        )
        return channel_name_element.text

    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

###Dönüştürme İşlemleri

def extract_like_count(label_text):
    """
    Verilen metin içerisinden sayı değerini çıkarır ve düz bir sayı olarak döndürür.
    """
    match = re.search(r'(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{1,3})?)', label_text)
    if match:
        # Virgül ve noktaları kaldırarak sayıyı döndür
        return int(match.group(0).replace(',', '').replace('.', ''))
    return None

def convert_subscriber_count(subscriber_count_str):
    """
    YouTube kanal abone sayısını metinden sayıya dönüştürür.
    """
    subscriber_count_str = subscriber_count_str.lower().replace(',', '.')

    # Türkçe sayı formatları
    if 'trilyon' in subscriber_count_str:
        number_part = subscriber_count_str.replace(' trilyon abone', '').strip()
        return int(float(number_part) * 1e12)
    elif 'milyar' in subscriber_count_str:
        number_part = subscriber_count_str.replace(' milyar abone', '').strip()
        return int(float(number_part) * 1e9)
    elif 'milyon' in subscriber_count_str:
        number_part = subscriber_count_str.replace(' milyon abone', '').strip()
        return int(float(number_part.replace(' milyon', '')) * 1e6)
    elif 'bin' in subscriber_count_str:
        number_part = subscriber_count_str.replace(' bin abone', '').strip()
        return int(float(number_part) * 1e3)

    # İngilizce sayı formatları
    elif 'billion' in subscriber_count_str or 'b subscribers' in subscriber_count_str:
        number_part = subscriber_count_str.replace(' billion subscribers', '').replace('b subscribers', '').strip()
        return int(float(number_part) * 1e9)
    elif 'million' in subscriber_count_str or 'm subscribers' in subscriber_count_str:
        number_part = subscriber_count_str.replace(' million subscribers', '').replace('m subscribers', '').strip()
        return int(float(number_part) * 1e6)
    elif 'thousand' in subscriber_count_str or 'k subscribers' in subscriber_count_str:
        number_part = subscriber_count_str.replace(' thousand subscribers', '').replace('k subscribers', '').strip()
        return int(float(number_part) * 1e3)

    # Rakam içeren doğrudan ifadeler
    elif 'abone' in subscriber_count_str or 'subscribers' in subscriber_count_str:
        match = re.search(r'\b(\d+)\b', subscriber_count_str)
        if match:
            return int(match.group(1))  # İlk bulunan tam sayıyı döndürür
    else:
        return "Error"  # Dönüşüm yapılamayan durumlar için Hata döndür

###Dosya İşlemleri

def create_csv(search_term):
    """
    Verilen arama terimi ve video bilgilerini CSV dosyasını oluşturur.
    """
    filename = f"{search_term}.csv"
    print(f"{filename} adlı CSV dosyası oluşturuldu.")
    return filename

def save_to_csv(search_term, video_data):
    """
    Verilen arama terimi ve video bilgilerini CSV dosyasına ekler.
    """
    filename = f"{search_term}.csv"
    headers = ['Video Title', 'Video URL', 'Channel Name', 'Upload Date',
            'View Count', 'Like Count', 'Subscriber Count', 'Subscriber Count Text', 'Video Duration']

    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        for video in video_data:
            writer.writerow(video)

    print("Video bilgileri kaydedildi.")

def save_video_links(search_term, video_links):
    """
    Video bağlantılarını dosyaya kaydeder.
    """
    # Ana dosya
    links_filename = create_csv(f"{search_term}_links")
    with open(links_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for video_title, video_url in video_links:
            writer.writerow([video_title, video_url])
    print(f"{links_filename} adlı video bağlantıları dosyası oluşturuldu.")
    
    # Yedek dosya
    backup_links_filename = create_csv(f"{search_term}_links_backup")
    with open(backup_links_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for video_title, video_url in video_links:
            writer.writerow([video_title, video_url])
    print(f"{backup_links_filename} adlı yedek video bağlantıları dosyası oluşturuldu.")

def load_video_links(search_term):
    """
    Video bağlantılarını dosyadan yükler.
    """
    links_filename = f"{search_term}_links.csv"
    video_links = []
    if os.path.exists(links_filename):
        with open(links_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                video_links.append((row[0], row[1]))
    return video_links

def remove_processed_link(search_term, processed_link):
    """
    İşlenen video bağlantısını CSV dosyasından çıkarır.
    """
    links_filename = f"{search_term}_links.csv"
    video_links = load_video_links(search_term)
    with open(links_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for video_title, video_url in video_links:
            if video_url != processed_link:
                writer.writerow([video_title, video_url])
    print(f"{processed_link} adlı video bağlantısı dosyadan çıkarıldı.")

###Choose Search Methods

def choose_search_method():
    print("Arama yöntemini seçin:")
    print("1. Standart arama")
    print("2. Özel arama")
    print("3. Önceki işleme devam et")

    choice = input("Seçiminizi yapın (1/2/3): ").strip().lower()
    return choice

def handle_standard_search():
    search_term = input("Lütfen aramak istediğiniz video için bir terim girin: ").strip()
    if not search_term:
        print("Geçersiz arama terimi.")
        return None, None

    num_videos = 0  # Tüm videoları almak için
    video_links = get_video_links(search_term, num_videos)
    save_video_links(search_term, video_links)
    return search_term, video_links

def handle_custom_search():
    search_term = input("Lütfen aramak istediğiniz video için bir terim girin: ").strip()
    if not search_term:
        print("Geçersiz arama terimi.")
        return None, None
    
    try:
        num_videos = int(input("Kaç video almak istediğinizi girin (0 için tüm videolar): "))
        if num_videos < 0:
            print("Geçersiz video sayısı.")
            return None, None
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")
        return None, None
    
    global_search = input("Global arama mı olsun? (e/h): ").strip().lower()

    if global_search == 'e':
        video_links = get_video_links(search_term, num_videos)
    else:
        language = input("Arama dili (ör. 'en' için İngilizce, 'tr' için Türkçe, boş bırakabilirsiniz): ").strip() or None
        country = input("Arama ülkesi (ör. 'US' için Amerika, 'TR' için Türkiye, boş bırakabilirsiniz): ").strip() or None
        video_links = get_video_links(search_term, num_videos, language, country)
        
    save_video_links(search_term, video_links)
    return search_term, video_links

def handle_previous_search():
    search_term = input("Devam etmek istediğiniz arama terimini girin: ").strip()

    if not search_term:
        print("Geçersiz arama terimi.")
        return None, None

    video_links = load_video_links(search_term)

    if not video_links:
        print("Kayıtlı video bağlantısı bulunamadı, lütfen yeni bir arama başlatın.")
        return None, None

    return search_term, video_links

###Process Videos

def process_videos(driver, search_term, video_links):
    data_num = 1
    for video_title, video_url in video_links:
        try:
            print("▼▼▼▼▼")
            print(f'Sıra: {data_num}')
            data_num += 1

            print(f'Video Başlığı: {video_title}')
            print(f'Video URL: {video_url}')

            print("-*-*-")
            print("Sayfa Yükleniyor ...")

            driver.get(video_url)
            #driver.refresh()
            time.sleep(0.5)

            print("Veriler Alınıyor ...")
            print("-*-*-")

            channel_name = get_channel_name(driver)
            print(f'Kanal Adı: {channel_name}')

            upload_date = get_upload_date(driver) or 'Null'
            print(f'Yükleme Tarihi: {upload_date}')

            view_count = get_view_count(driver) or 'Null'
            print(f'Görüntülenme Sayısı: {view_count}')

            like_count = get_like_count(driver) or 'Null'
            print(f'Beğeni Sayısı: {like_count}')

            subscriber_count_text = get_subscriber_count(driver) or 'Null'
            print(f'Abone Sayısı Metin: {subscriber_count_text}')

            if subscriber_count_text is None or subscriber_count_text == 'Null':
                subscriber_count = 'Null'
            elif subscriber_count_text == 'Error':
                subscriber_count = 'Error'
            else:
                subscriber_count = convert_subscriber_count(subscriber_count_text)
                if subscriber_count is not None and not str(subscriber_count).isdigit():
                    subscriber_count = 'Error'
                elif subscriber_count is None:
                    subscriber_count = 'Null'

            print(f'Abone Sayısı: {subscriber_count}')

            time.sleep(0.5)
            duration = get_duration(driver) or 'Null'
            print(f'Video Süresi: {duration}')

            video_data = [[video_title, video_url, channel_name, upload_date, view_count, like_count, subscriber_count, subscriber_count_text, duration]]

            print("-*-*-")
            save_to_csv(search_term, video_data)
            remove_processed_link(search_term, video_url)

        except Exception as e:
            print(f'Hata: {str(e)}')

        finally:
            time.sleep(0.5)
            driver.get("about:blank")
            time.sleep(0.5)
            print("▲▲▲▲▲")
            print("")

###Main

def main():
    choice = choose_search_method()

    print("Bilgilendirme: Bazı YouTube kanalları belirli verileri gizlemeyi tercih edebilir.")
    print("Bu durumda, gizlenmiş veriler 'Null' olarak gösterilecektir.")
    print("Veri alınırken yaşanan sorunlar ekrana hata mesajı olarak yansıtılacak ve veritabanına 'Error' olarak kaydedilecektir.")


    if choice == '1':
        search_term, video_links = handle_standard_search()
    elif choice == '2':
        search_term, video_links = handle_custom_search()
    elif choice == '3':
        search_term, video_links = handle_previous_search()
    else:
        print("Geçersiz seçim.")
        return

    if not search_term or not video_links:
        return

    try:
        driver = setup_driver()
        print("")
        process_videos(driver, search_term, video_links)
    except Exception as e:
        print(f'Ana hata: {str(e)}')
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()
