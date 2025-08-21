# 🎨 Renk Hex Kod Bulucu

Bu uygulama, JPG formatındaki resimlerdeki renkleri hex kodları ile bulmanızı sağlar. OpenCV kullanarak geliştirilmiştir.

## 📋 Özellikler

- Resim yükleme ve görüntüleme
- Fare ile renk seçimi
- Hex ve RGB formatında renk kodları
- Renk önizleme
- Otomatik boyutlandırma

## 🚀 Kurulum

### 1. Projeyi İndirin
```bash
git clone https://github.com/kullaniciadi/hex-color-picker.git
cd hex-color-picker
```

### 2. Python Kurulumu
- Python 3.7 veya üstü yükleyin
- [Python.org](https://python.org) adresinden indirebilirsiniz

### 3. Gerekli Paketleri Yükleyin
```bash
pip install -r requirements.txt
```

## 💻 Kullanım

### 1. Uygulamayı Çalıştırın
```bash
python color_picker.py
```

### 2. Resim Seçimi
- Uygulama otomatik olarak `jeoloji_harita.jpg` dosyasını bulur (varsa)
- "Bu resmi kullanmak istiyor musunuz? (e/h):" sorusuna "e" yazın
- Veya farklı bir resim yolu girebilirsiniz

### 3. Renk Kodlarını Görün
- Resim penceresi açılır
- Fare ile resim üzerinde gezinin
- Her noktada renk kodları görünür:
  - **HEX**: #FF0000 formatında
  - **RGB**: (255,0,0) formatında
  - **Renk önizleme**: Küçük renk kutusu

### 4. Çıkış
- **ESC** tuşu ile uygulamadan çıkın

## 🎯 Kontroller

- **Fare**: Resim üzerinde renk seçimi
- **ESC**: Uygulamadan çıkış

## 📁 Dosya Yapısı

```
hex/
├── color_picker.py      # Ana uygulama
├── requirements.txt     # Python bağımlılıkları
├── jeoloji_harita.jpg  # Jeoloji haritası (örnek resim)
└── README.md           # Bu dosya
```

## 🔧 Gereksinimler

- **Python**: 3.7+
- **OpenCV**: 4.8+
- **NumPy**: 1.24+
- **Pillow**: 10.0+

## ❗ Sorun Giderme

### Resim Yüklenemiyor
- Dosya adında Türkçe karakter olmamalı
- Dosya JPG formatında olmalı
- Dosya yolu doğru olmalı

### Pencere Açılmıyor
- OpenCV kurulumunu kontrol edin
- Python sürümünü kontrol edin
- Hata mesajlarını okuyun

### Paket Kurulum Hatası
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🎨 Örnek Kullanım

1. Projeyi indirin: `git clone https://github.com/kullaniciadi/hex-color-picker.git`
2. Proje klasörüne gidin: `cd hex-color-picker`
3. Paketleri yükleyin: `pip install -r requirements.txt`
4. Uygulamayı çalıştırın: `python color_picker.py`
5. "e" yazarak varsayılan resmi kullanın (varsa)
6. Fare ile resim üzerinde gezinin
7. Hex kodlarını görün
8. ESC ile çıkın

## 📞 Destek

Sorun yaşarsanız:
- Hata mesajlarını kontrol edin
- Python ve paket sürümlerini kontrol edin
- Dosya yollarını kontrol edin
