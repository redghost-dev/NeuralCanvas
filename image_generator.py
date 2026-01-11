import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import random
import colorsys

class ImageGenerator:
    def __init__(self):
        self.formulas = [
            lambda z, c: z**2 + c,
            lambda z, c: z**3 + c,
            lambda z, c: z**4 + c,
            lambda z, c: np.sin(z) + c,
            lambda z, c: np.cos(z**2) + c,
            lambda z, c: z**2 + np.sin(z) + c,
            lambda z, c: z**3 - z + c,
        ]

    def get_color(self, iterations, max_iter):
        if iterations == max_iter:
            return (0, 0, 0)
        
        # Psikedelik renk paleti
        t = iterations / max_iter
        r = np.sin(t * 6.28 * 3) * 127 + 128
        g = np.sin(t * 6.28 * 4 + 2.1) * 127 + 128
        b = np.sin(t * 6.28 * 5 + 4.2) * 127 + 128
        return (int(r), int(g), int(b))

    def compute_fractal(self, width, height):
        max_iter = 100
        formula = random.choice(self.formulas)
        
        # Rastgele kompleks sayı seç
        c = complex(random.uniform(-0.6, 0.6), 
                   random.uniform(-0.6, 0.6))
        
        # Zoom ve pan parametreleri
        zoom = random.uniform(1.5, 3.0)
        x_offset = random.uniform(-0.5, 0.5)
        y_offset = random.uniform(-0.5, 0.5)
        
        result = np.zeros((height, width), dtype=int)
        
        for y in range(height):
            for x in range(width):
                # Piksel koordinatlarını kompleks düzleme dönüştür
                zx = (x - width/2) / (width/4 * zoom) + x_offset
                zy = (y - height/2) / (height/4 * zoom) + y_offset
                z = complex(zx, zy)
                
                # İterasyon
                for i in range(max_iter):
                    if abs(z) > 4.0:
                        result[y, x] = i
                        break
                    z = formula(z, c)
                else:
                    result[y, x] = max_iter
                    
        return result

    def generate(self, width, height):
        # Fraktal hesapla
        fractal = self.compute_fractal(width, height)
        
        # Görüntü oluştur
        image = Image.new('RGB', (width, height))
        pixels = image.load()
        max_iter = np.max(fractal)
        
        # Her piksele renk ata
        for y in range(height):
            for x in range(width):
                pixels[x, y] = self.get_color(fractal[y, x], max_iter)
        
        # Renk efektleri
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(1.5)
        
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.3)
        
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.1)
        
        # Hafif blur efekti
        if random.random() > 0.5:
            image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
            
        return image
