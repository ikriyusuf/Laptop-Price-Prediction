# Veri Temizleme ve Görselleştirme Projesi

Bu proje, çeşitli veri setleri üzerinde veri temizleme, eksik verileri doldurma ve görselleştirme işlemleri yapmayı amaçlamaktadır. Amaç, veriyi analiz etmek ve görselleştirmek için önceden yapılan temizlik ve dönüşüm işlemlerini içerir.

## Özellikler
- Veri temizleme ve ön işleme
- Eksik verileri doldurma
- Sayısal verilere dönüştürme
- Veri görselleştirmeleri (barplot, histogram, vb.)

## Gereksinimler

- Python 3.10.15
- Pandas
- Seaborn
- Matplotlib

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

## Nasıl Kullanılır

1. Projeyi bilgisayarınıza indirin.
2. Veri dosyasını projeye dahil edin.
3. Projeyi çalıştırarak analize başlayın.