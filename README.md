# NeuralCanvas AI 🎨

NeuralCanvas, hem **Stable Diffusion** tabanlı üretken yapay zekayı hem de gelişmiş geometrik algoritmaları bir araya getiren, Python ile geliştirilmiş kapsamlı bir soyut sanat üretim platformudur.

## 🚀 Özellikler

- **Hibrit Üretim Modu:** İster Stable Diffusion v1.5 kullanarak yüksek kaliteli AI görselleri üretin, ister klasik geometrik algoritmalarla tamamen matematiksel soyut kompozisyonlar oluşturun.
- **Model Eğitimi (Fine-Tuning):** Kendi veri setlerinizi kullanarak Stable Diffusion modellerini eğitebilir ve kişiselleştirilmiş sanat tarzları oluşturabilirsiniz.
- **Görsel Analiz (BLIP):** Referans görsellerden otomatik açıklama (caption) ve renk paleti çıkarımı.
- **Canlı Önizleme:** Üretim aşamasını gerçek zamanlı olarak takip edebileceğiniz interaktif Dashboard.
- **Geri Bildirim Sistemi:** Üretilen görselleri değerlendirerek sistemin evrimine katkıda bulunma.
- **Çoklu Format Desteği:** PNG, JPG ve WEBP formatlarında çıktı alabilme.

## 🛠️ Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/KULLANICI_ADI/NeuralCanvas.git
   cd NeuralCanvas
   ```

2. Sanal ortam oluşturun ve aktif edin:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows için: .venv\Scripts\activate
   ```

3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. `config.py` dosyasına Pixabay API anahtarınızı ekleyin.

## 💻 Kullanım

Uygulamayı başlatmak için:
```bash
python abstract_art_generator.py
```

## 📂 Proje Yapısı

- `abstract_art_generator.py`: Ana Dashboard ve kullanıcı arayüzü.
- `image_generator.py`: AI ve geometrik üretim motoru.
- `models/`: Eğitilmiş AI modellerinin saklandığı dizin.
- `config.py`: API anahtarları ve global ayarlar.
- `examples/`: Referans olarak kullanılan örnek görseller.

## ⚖️ Lisans

Bu proje MIT lisansı ile lisanslanmıştır.

---
*Geleceğin sanatını algoritmalarla keşfedin.*
