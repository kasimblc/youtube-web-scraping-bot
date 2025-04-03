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


# Programın bulunduğu ana dizini al
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# "data" klasörünü oluştur (eğer yoksa)
os.makedirs(DATA_DIR, exist_ok=True)


### Selenium Bot İşlemleri
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


### Video Link Liste İşlemleri
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


### Veri Alma İşlemleri
def get_like_count(driver):
    """
    YouTube videosunun beğeni sayısını alır ve ekrana yazdırır.
    """
    try:
        # Beğeni butonunu CSS seçici ile bulma
        like_button = WebDriverWait(driver, 5).until(
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
    Video görüntülenme sayısını alır. Hem "interactionCount" hem de "userInteractionCount" meta etiketlerini kontrol eder.
    """
    selectors = [
        'meta[itemprop="userInteractionCount"][content]',
        'meta[itemprop="interactionCount"][content]' 
    ]
    for sel in selectors:
        try:
            view_meta = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, sel))
            )
            if view_meta:
                return view_meta.get_attribute('content')
        except Exception:
            continue
    print("get_view_count: Uygun meta etiket bulunamadı")
    return "Error"

def get_comment_count(driver):
    """
    YouTube videosunun yorum sayısını alır. Yorumlar henüz yüklenmemişse,
    sayfayı kademeli olarak kaydırır ve belirli sayıda denemeden sonra hata verir.
    """
    max_scroll_attempts = 3  # Maksimum kaydırma denemesi
    attempt = 0
    comment_count_element = None

    # İlk olarak CSS seçici yöntemi ile deniyoruz
    while attempt < max_scroll_attempts:
        try:
            comment_count_element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#count yt-formatted-string span:first-of-type")
                )
            )
            if comment_count_element:
                break
        except Exception as e:
            # Bulunamadıysa sayfayı biraz kaydırıyoruz
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1.5)  # Kaydırma sonrası elementin yüklenmesi için bekleme
            attempt += 1

    # Eğer CSS seçici ile bulunamazsa, XPath yöntemiyle deniyoruz
    if not comment_count_element:
        try:
            comment_count_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//yt-formatted-string[@class='count-text style-scope ytd-comments-header-renderer']//span)[1]")
                )
            )
        except Exception as e:
            print(f"Yorum sayısı alınırken hata oluştu: {str(e)}")
            return "Error"

    # Gelen metni temizleyerek sayı formatına çeviriyoruz
    comment_text = comment_count_element.text.strip().replace('.', '').replace(',', '')
    return comment_text

def get_upload_date(driver):
    """
    YouTube videosunun yüklenme tarihini alır.
    """
    try:
        upload_date = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="uploadDate"][content]'))
        )
        return upload_date.get_attribute('content').split('T')[0] if upload_date else None
    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_publish_date(driver):
    """
    YouTube videosunun yayınlanma tarihini alır.
    """
    try:
        publish_date = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="datePublished"][content]'))
        )
        return publish_date.get_attribute('content').split('T')[0] if publish_date else None
    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_video_category(driver):
    """
    YouTube videosunun kategori bilgisini alır.
    """
    try:
        category = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="genre"][content]'))
        )
        return category.get_attribute('content') if category else None
    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"

def get_subscriber_count(driver):
    """
    YouTube videosunun kanal abone sayısını alır.
    """
    try:
        subscriber_count_element = WebDriverWait(driver, 5).until(
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
    Video süresini öncelikle meta etiketinden alır.
    Eğer meta etiketinde (itemprop="duration") bulunamazsa, oynatıcı üzerindeki süre göstergesinden okumaya çalışır.
    """
    try:
        # İlk öncelik meta etiketi: <meta itemprop="duration" content="...">
        duration_meta = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="duration"][content]'))
        )
        if duration_meta:
            # Meta etiketindeki süre bilgisini al, ve parse_duration ile düzenleyerek döndür.
            meta_content = duration_meta.get_attribute('content')
            return parse_duration(meta_content)
    except Exception as e:
        print("Meta etiket ile duration alınamadı:", str(e))
    
    # Eğer meta etiketten alınamazsa, oynatıcıdaki süreyi deniyoruz:
    selectors = [
        '.ytp-time-display.notranslate.ytp-time-display-allow-autohide',  # En spesifik
        '.ytp-time-display.notranslate',  # Orta seviye
        '.ytp-time-display'  # En genel
    ]
    
    duration_element = None
    
    for selector in selectors:
        try:
            time_display_div = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            # Süreyi içeren span'ı almayı dene:
            duration_element = time_display_div.find_element(By.CSS_SELECTOR, '.ytp-time-duration')
            if duration_element:
                return duration_element.text
        except Exception:
            continue
    
    print("get_duration: Süre alınamadı")
    return "Error"

def get_channel_name(driver):
    """
    YouTube videosunun kanal adını alır.
    Öncelikle meta etiketinden okumaya çalışır, eğer bulunamazsa alternatif yöntemi dener.
    """
    try:
        # İlk öncelik meta etiketi: <link itemprop="name" content="Kanal Adı">
        channel_meta = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[itemprop="author"] link[itemprop="name"][content]'))
        )
        if channel_meta:
            return channel_meta.get_attribute('content')
    except Exception as e:
        print("Meta etiket ile kanal adı alınamadı:", str(e))

    # Alternatif yöntem: Kanal isminin geçtiği element
    try:
        channel_name_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ytd-channel-name a'))
        )
        return channel_name_element.text
    except Exception as e:
        print(f"Hata: {str(e)}")
        return "Error"


### Dönüştürme İşlemleri
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

def parse_duration(duration_str):
    """
    ISO 8601 formatındaki (örneğin 'PT81M24S', 'pt81m24s', 'PT1H5M3S', 'PT45S') video süresini
    "HH:MM:SS" ya da "MM:SS" formatına çevirir. Küçük/büyük harf duyarlılığına dikkat etmez.
    """
    # Gelen string'i büyük harfe çeviriyoruz
    duration_str = duration_str.upper()
    
    # ISO 8601 süresini parçalara ayıran regex deseni:
    pattern = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'
    match = re.match(pattern, duration_str)
    if not match:
        return "Error: Geçersiz süre formatı"
    
    h, m, s = match.groups()
    h = int(h) if h else 0
    m = int(m) if m else 0
    s = int(s) if s else 0

    # Toplam saniyeyi hesaplıyoruz
    total_seconds = h * 3600 + m * 60 + s
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Eğer süre 1 saatten uzun ise HH:MM:SS formatında, değilse MM:SS formatında döndürür
    if hours > 0:
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes}:{seconds:02}"

### Dosya İşlemleri
def get_save_path(search_term):
    """
    Belirtilen arama terimi için data klasörü altında bir dizin oluşturur.
    Dosya kaydedilecek dizinin yolunu döndürür.
    """
    search_dir = os.path.join(DATA_DIR, search_term)
    os.makedirs(search_dir, exist_ok=True)
    return search_dir

def create_csv(search_term):
    """
    Verilen arama terimi için CSV dosyasını oluşturur ve yolunu döndürür.
    """
    save_path = get_save_path(search_term)
    filename = os.path.join(save_path, f"{search_term}.csv")
    return filename

def save_to_csv(search_term, video_data):
    """
    Verilen arama terimi için video bilgilerini CSV dosyasına ekler.
    """
    filename = create_csv(search_term)
    headers = ['Video Title', 'Video URL', 'Channel Name', 'Upload Date', 'Publish Date',
               'View Count', 'Like Count', 'Comment Count', 'Subscriber Count', 'Subscriber Count Text',
               'Video Duration', 'Category']
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerows(video_data)
    
    print(f"Video bilgileri {filename} dosyasına kaydedildi.")

def save_video_links(search_term, video_links):
    """
    Video bağlantılarını dosyaya kaydeder (ana ve yedek).
    """
    save_path = get_save_path(search_term)
    links_filename = os.path.join(save_path, f"{search_term}_links.csv")
    backup_links_filename = os.path.join(save_path, f"{search_term}_links_backup.csv")
    
    for filename in [links_filename, backup_links_filename]:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(video_links)
        print(f"{filename} adlı video bağlantıları dosyası oluşturuldu.")

def load_video_links(search_term):
    """
    Video bağlantılarını dosyadan yükler.
    """
    save_path = get_save_path(search_term)
    links_filename = os.path.join(save_path, f"{search_term}_links.csv")
    video_links = []
    
    if os.path.exists(links_filename):
        with open(links_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            video_links = [(row[0], row[1]) for row in reader]
    
    return video_links

def remove_processed_link(search_term, processed_link):
    """
    İşlenen video bağlantısını CSV dosyasından çıkarır.
    """
    save_path = get_save_path(search_term)
    links_filename = os.path.join(save_path, f"{search_term}_links.csv")
    video_links = load_video_links(search_term)
    
    with open(links_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for video_title, video_url in video_links:
            if video_url != processed_link:
                writer.writerow([video_title, video_url])
    
    print(f"{processed_link} adlı video bağlantısı {links_filename} dosyasından çıkarıldı.")

### Choose Search Methods
def choose_search_method(): 
    print("Arama yöntemini seçin:")
    print("1. Standart arama")
    print("2. Özel arama")
    print("3. Önceki işleme devam et")
    print("4. Tek Url")

    choice = input("Seçiminizi yapın (1/2/3/4): ").strip().lower()
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

def handle_single_url():
    video_url = input("Lütfen tek bir video URL'si girin: ").strip()
    if not video_url:
        print("Geçersiz URL.")
        return None, None

    video_title = "URL"
    video_links = [(video_title, video_url)]
    return "URL", video_links


### Process Videos
def process_videos(driver, search_term, video_links, choice):
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
            time.sleep(0.5)

            print("Veriler Alınıyor ...")
            print("-*-*-")

            channel_name = get_channel_name(driver)
            print(f'Kanal Adı: {channel_name}')

            upload_date = get_upload_date(driver) or 'Null'
            print(f'Yükleme Tarihi: {upload_date}')

            publish_date = get_publish_date(driver) or 'Null'
            print(f'Yayınlama Tarihi: {publish_date}')

            view_count = get_view_count(driver) or 'Null'
            print(f'Görüntülenme Sayısı: {view_count}')

            like_count = get_like_count(driver) or 'Null'
            print(f'Beğeni Sayısı: {like_count}')

            comment_count = get_comment_count(driver) or 'Null'
            print(f'Yorum Sayısı: {comment_count}')

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

            duration = get_duration(driver) or 'Null'
            print(f'Video Süresi: {duration}')

            video_category = get_video_category(driver) or 'Null'
            print(f'Kategori: {video_category}')

            print("-*-*-")

            # Eğer seçim '4' (Tek URL) değilse CSV'ye kaydet
            if choice != '4':
                video_data = [[video_title, video_url, channel_name, upload_date, publish_date, view_count, like_count,
                               comment_count, subscriber_count, subscriber_count_text, duration, video_category]]
                save_to_csv(search_term, video_data)
                remove_processed_link(search_term, video_url)

        except Exception as e:
            print(f'Hata: {str(e)}')

        finally:
            driver.get("about:blank")
            time.sleep(0.5)
            print("▲▲▲▲▲")
            print("")

### Main
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
    elif choice == '4':
        search_term, video_links = handle_single_url()
    else:
        print("Geçersiz seçim.")
        return

    if not search_term or not video_links:
        return

    try:
        driver = setup_driver()
        print("")
        process_videos(driver, search_term, video_links, choice)  # choice parametresi eklendi

        print("Tarama işlemleri bitti!!!!!!")
    except Exception as e:
        print(f'Ana hata: {str(e)}')
    finally:
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    main()
