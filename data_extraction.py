from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# CSV dosyasına yazma
def save_to_csv(products, headers):
    with open('notebooks.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Başlıkları yazıyoruz
        for product in products:
            row = []
            for header in headers:
                # Her özellik için değerini alıyoruz, eğer yoksa "N/A" ekliyoruz
                row.append(product.get(header, "N/A"))
            writer.writerow(row)
    print("Data has been saved to notebooks.csv")

# Ürün detaylarını çekme
def get_product_details(driver, product_url):
    driver.get(product_url)  # Ürün sayfasına gidiyoruz
    try:
        # Sayfanın yüklenmesini bekliyoruz
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pr-new-br"))
        )
        
        # Ürün başlığını çekiyoruz
        title_tag = driver.find_element(By.CSS_SELECTOR, ".pr-new-br span")
        title = title_tag.text.strip() if title_tag else "No Title"
        
        # Fiyatı çekiyoruz
        price_tag = driver.find_element(By.CLASS_NAME, "prc-dsc")
        price = price_tag.text.strip() if price_tag else "No Price"
        
        # Tüm özellikleri çekiyoruz
        attributes = driver.find_elements(By.CLASS_NAME, "detail-attr-item")
        product_details = {"Title": title, "Price": price}
        
        for attribute in attributes:
            try:
                # Özellik adı ve değeri
                attribute_name = attribute.find_element(By.CLASS_NAME, "attr-name").text.strip()
                attribute_value = attribute.find_element(By.CLASS_NAME, "attr-value-name-w").text.strip()
                
                # Özellik adını ve değerini saklıyoruz
                product_details[attribute_name] = attribute_value
            except Exception as e:
                print(f"Error occurred while extracting attribute: {e}")

        return product_details
    except Exception as e:
        print(f"Error occurred while extracting product details: {e}")
        return {"Title": "No Title", "Price": "No Price"}

# Ürünleri içeren bağlantıları alıyoruz (ana sayfa)
def get_product_links(driver, url):
    driver.get(url)  # Ana sayfayı açıyoruz
    product_links = []

    # Sayfanın tam yüklenmesini bekliyoruz
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "p-card-wrppr"))
        )
    except Exception as e:
        print(f"Error waiting for page to load: {e}")
        return product_links

    # Ürünleri içeren container'ları buluyoruz
    product_containers = driver.find_elements(By.CLASS_NAME, "p-card-wrppr")

    for container in product_containers:
        try:
            # href etiketi - 'a' tagını alalım
            link_tag = container.find_element(By.TAG_NAME, "a")
            product_url = link_tag.get_attribute("href") if link_tag else None

            if product_url:
                product_links.append(product_url)
        except Exception as e:
            print(f"Error occurred while extracting product link: {e}")
    
    return product_links

# Ürünleri çekme ve CSV dosyasına kaydetme
def scrape_notebooks(base_url):
    all_products = []
    all_headers = set(["Title", "Price"])  # Başlangıçta başlık ve fiyat başlıklarını ekliyoruz
    
    # WebDriver ayarları
    options = Options()
    options.add_argument("--headless")  # Tarayıcıyı görünmeyen modda çalıştırır
    options.add_argument("--disable-gpu")  # Gerekli değil, ama bazı sistemlerde yardımcı olabilir
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Kullanıcı ajanı ekleyin
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Sayfaları 1'den 50'ye kadar gezip ürünleri çekeceğiz
    for page_num in range(1, 51):  # Sayfa numarasını 1'den 50'ye kadar artıracağız
        print(f"Scraping page {page_num}...")
        url = f"{base_url}&pi={page_num}"  # Sayfa numarasını URL'ye ekliyoruz
        
        # Sayfada bulunan tüm ürünlerin bağlantılarını alıyoruz
        product_links = get_product_links(driver, url)

        if not product_links:
            print(f"No products found on page {page_num}.")
            continue

        # Her bir ürünü işliyoruz
        for product_url in product_links:
            try:
                # Ürün sayfasından detayları alıyoruz
                product_details = get_product_details(driver, product_url)

                # En geniş özellik setini almak için tüm başlıkları kaydediyoruz
                all_headers.update(product_details.keys())

                # Ürün bilgilerini kaydediyoruz
                all_products.append(product_details)

                # Kısa bir süre bekleyelim
                time.sleep(1)

            except Exception as e:
                print(f"Error occurred while processing a product: {e}")
    
    # CSV başlıklarını sıralıyoruz ve verileri kaydediyoruz
    all_headers = sorted(all_headers)  # Başlıkları sıralıyoruz (alphabetical order)
    save_to_csv(all_products, all_headers)

    # Tarayıcıyı kapatıyoruz
    driver.quit()

# Ana işlevi çağırıyoruz
if __name__ == "__main__":
    base_url = "https://www.trendyol.com/sr?wc=103108&lc=106084&qt=notebook&st=notebook&os=1"
    
    # Sayfaları çekelim
    scrape_notebooks(base_url)
