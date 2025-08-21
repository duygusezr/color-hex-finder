import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

class ColorPicker:
    def __init__(self):
        self.image = None
        self.original_image = None
        self.window_name = "Renk Hex Kod Bulucu - ESC ile çık"
        self.font = None
        self.try_load_font()
        
    def try_load_font(self):
        """Font yüklemeyi dene"""
        try:
            # Windows için varsayılan font
            self.font = ImageFont.truetype("arial.ttf", 16)
        except:
            try:
                # Linux için varsayılan font
                self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
            except:
                # Font bulunamazsa varsayılan kullan
                self.font = ImageFont.load_default()
    
    def rgb_to_hex(self, r, g, b):
        """RGB değerlerini hex formatına çevir"""
        return f"#{r:02x}{g:02x}{b:02x}".upper()
    
    def mouse_callback(self, event, x, y, flags, param):
        """Fare olaylarını işle"""
        if event == cv2.EVENT_MOUSEMOVE and self.image is not None:
            # Resim sınırları içinde mi kontrol et
            if 0 <= x < self.image.shape[1] and 0 <= y < self.image.shape[0]:
                # BGR formatında renk al (OpenCV BGR kullanır)
                b, g, r = self.image[y, x]
                
                # Hex kodunu hesapla
                hex_code = self.rgb_to_hex(r, g, b)
                
                # Resmin kopyasını oluştur
                display_image = self.image.copy()
                
                # Fare pozisyonunda daire çiz
                cv2.circle(display_image, (x, y), 10, (0, 255, 0), 2)
                
                # Renk bilgilerini resme ekle
                text = f"HEX: {hex_code}"
                text2 = f"RGB: ({r},{g},{b})"
                
                # Arka plan dikdörtgeni
                cv2.rectangle(display_image, (x+15, y-50), (x+200, y+10), (0, 0, 0), -1)
                cv2.rectangle(display_image, (x+15, y-50), (x+200, y+10), (255, 255, 255), 1)
                
                # Metin ekle
                cv2.putText(display_image, text, (x+20, y-30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                cv2.putText(display_image, text2, (x+20, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                # Renk önizleme kutusu
                cv2.rectangle(display_image, (x+180, y-40), (x+195, y-25), (int(b), int(g), int(r)), -1)
                cv2.rectangle(display_image, (x+180, y-40), (x+195, y-25), (255, 255, 255), 1)
                
                # Güncellenmiş resmi göster
                cv2.imshow(self.window_name, display_image)
    
    def load_image(self, image_path):
        """Resmi yükle ve boyutlandır"""
        if not os.path.exists(image_path):
            print(f"Hata: {image_path} dosyası bulunamadı!")
            return False
        
        # Resmi yükle
        self.original_image = cv2.imread(image_path)
        if self.original_image is None:
            print(f"Hata: {image_path} resmi yüklenemedi!")
            return False
        
        # Resmi ekrana sığacak şekilde boyutlandır
        height, width = self.original_image.shape[:2]
        max_width = 1200
        max_height = 800
        
        if width > max_width or height > max_height:
            scale = min(max_width/width, max_height/height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            self.image = cv2.resize(self.original_image, (new_width, new_height))
        else:
            self.image = self.original_image.copy()
        
        return True
    
    def run(self, image_path):
        """Ana uygulama döngüsü"""
        if not self.load_image(image_path):
            return
        
        # Pencere oluştur
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)
        
        # İlk resmi göster
        cv2.imshow(self.window_name, self.image)
        
        print("🎨 Renk Hex Kod Bulucu başlatıldı!")
        print("📋 Kullanım:")
        print("   - Fare ile resim üzerinde gezinin")
        print("   - Renk kodları otomatik görünür")
        print("   - ESC tuşu ile çıkın")
        print(f"📁 Yüklenen resim: {image_path}")
        
        while True:
            key = cv2.waitKey(1) & 0xFF
            
            # ESC tuşu ile çık
            if key == 27:
                break
        
        cv2.destroyAllWindows()
        print("👋 Uygulama kapatıldı!")

def main():
    """Ana fonksiyon"""
    print("🎨 Renk Hex Kod Bulucu")
    print("=" * 40)
    
    # Varsayılan resim yolu
    default_image = "jeoloji_harita.jpg"
    
    if os.path.exists(default_image):
        print(f"📁 Varsayılan resim bulundu: {default_image}")
        use_default = input("Bu resmi kullanmak istiyor musunuz? (e/h): ").lower().strip()
        
        if use_default in ['e', 'evet', 'y', 'yes']:
            image_path = default_image
        else:
            image_path = input("Resim dosyasının yolunu girin: ").strip()
    else:
        image_path = input("Resim dosyasının yolunu girin: ").strip()
    
    if not image_path:
        print("❌ Resim yolu belirtilmedi!")
        return
    
    # ColorPicker'ı başlat
    color_picker = ColorPicker()
    color_picker.run(image_path)

if __name__ == "__main__":
    main()
