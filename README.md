# Veri Temizleme ve Görselleştirme Projesi

Bu proje, çeşitli veri setleri üzerinde veri temizleme, eksik verileri doldurma, görselleştirme işlemleri ve **çoklu lineer regresyon** analizi yapmayı amaçlamaktadır. Proje, veriyi analiz etmek, görselleştirmek ve çoklu lineer regresyon modeli ile tahminlerde bulunmak için gereken temizlik, dönüşüm ve eğitim işlemlerini içerir.

## Özellikler
- Veri temizleme ve ön işleme
- Eksik verileri doldurma
- Sayısal verilere dönüştürme
- Veri görselleştirmeleri (barplot, histogram, vb.)
- Çoklu lineer regresyon analizi

## Gereksinimler

- Python 3.10.15
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn

## Yapılan İşlemler

1. **Veri Temizliği**:
   - Eksik değerler dolduruldu.
   - Gereksiz ve eksik veriler temizlendi.
   - `'Belirtilmemiş'` gibi değerler boşlukla değiştirildi.

2. **Veri Dönüştürme**:
   - Sayısal verilere dönüştürülmesi gereken sütunlar (örneğin, `Ekran Kartı Hafızası`, `İşlemci Hızı`) sayısal verilere dönüştürüldü.

3. **Eksik Verilerin Doldurulması**:
   - En sık tekrar eden değerler (mode) veya ortalama değer ile eksik veriler dolduruldu.

4. **Görselleştirme**:
   - Ekran Tipi, İşlemci Hızı gibi verilerle ilgili barplot ve diğer grafikler oluşturuldu.

5. **Çoklu Lineer Regresyon**:
   - Modelin amacı: **Bağımlı değişken** olarak `Satış Fiyatı` (veya başka bir hedef) kullanıldı ve **bağımsız değişkenler** olarak `Ekran Kartı Hafızası`, `İşlemci Hızı`, `RAM`, vb. gibi sayısal özellikler kullanıldı.
   - **Veri Ayrımı**: Veri seti, eğitim ve test verileri olarak %70 eğitim, %30 test oranında bölündü.
   - **Model Eğitimi**: `scikit-learn` kütüphanesinin **LinearRegression** sınıfı kullanılarak eğitim yapıldı.
   - **Model Performansı**: Modelin doğruluğu **R² skoru**, **Mean Squared Error (MSE)** veya **Root Mean Squared Error (RMSE)** gibi metriklerle ölçüldü.
   - Model, eğitim verileri üzerinden eğitildikten sonra, test verileri üzerinde tahminler yapıldı ve gerçek ile tahmin edilen değerler karşılaştırıldı.

6. **Sonuçların Görselleştirilmesi**:
   - Gerçek ve tahmin edilen değerlerin karşılaştırılması için **scatter plot** veya **line plot** grafiklerinden yararlanıldı.
   - Modelin sonuçları, görsel olarak modelin doğruluğunu ve tahmin performansını ortaya koymak için grafiklerle desteklendi.

## Modelin Performansı
Modelin başarısını ölçmek için kullanılan metrikler:
- **R² Skoru**: Modelin ne kadar doğru tahminler yaptığı hakkında genel bir fikir verir. (Örneğin, %80 R², modelin %80 doğrulukla tahmin yaptığı anlamına gelir.)
- **Mean Squared Error (MSE)**: Modelin tahminleriyle gerçek değerler arasındaki ortalama karesel farkı ölçer.
- **Root Mean Squared Error (RMSE)**: MSE'nin karekökü alınarak daha anlaşılır bir sonuç sağlanır.
