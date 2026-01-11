from PIL import Image, ImageDraw, ImageFilter

def main():
    # 1. Yeni bir görüntü oluşturma
    img = Image.new('RGB', (400, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Şekiller çizme
    draw.rectangle([50, 50, 350, 250], fill='blue', outline='red', width=2)
    draw.ellipse([100, 100, 300, 200], fill='yellow')
    draw.line([0, 0, 400, 300], fill='green', width=3)

    # Görüntüyü kaydetme
    img.save('temel_sekiller.png')

    # 2. Varolan bir görüntüyü açma (örnek olarak az önce oluşturduğumuz dosyayı kullanalım)
    img2 = Image.open('temel_sekiller.png')

    # 3. Görüntü işleme örnekleri
    # Döndürme
    rotated = img2.rotate(45)
    rotated.save('dondurulmus.png')

    # Yeniden boyutlandırma
    resized = img2.resize((200, 150))
    resized.save('kucultulmus.png')

    # Bulanıklaştırma filtresi
    blurred = img2.filter(ImageFilter.BLUR)
    blurred.save('bulanik.png')

    # Görüntüyü gri tonlamaya çevirme
    grayscale = img2.convert('L')
    grayscale.save('gri_tonlama.png')

    print("Tüm işlemler tamamlandı! Oluşturulan dosyalar:")
    print("- temel_sekiller.png")
    print("- dondurulmus.png")
    print("- kucultulmus.png")
    print("- bulanik.png")
    print("- gri_tonlama.png")

if __name__ == "__main__":
    main()
