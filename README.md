# NeuralCanvas AI 🎨

NeuralCanvas is a high-performance abstract art generation platform developed with Python. It seamlessly bridges the gap between state-of-the-art **Generative AI (Stable Diffusion)** and classical **high-fidelity geometric algorithms**.

## 🌟 Key Features

### 1. Hybrid Art Generation Engine
- **AI Mode:** Leveraging **Stable Diffusion v1.5**, the system generates complex, high-quality abstract textures and compositions.
- **Algorithm Mode:** For a more mathematical touch, the system uses custom Pillow-based algorithms to draw shapes (ellipses, polygons, lines) based on color density maps extracted from reference images.

### 2. Intelligent Image Analysis
- **Auto-Captioning (BLIP):** Powered by the Salesforce BLIP model, the system "sees" and describes reference images to generate relevant prompts automatically.
- **Palette Extraction:** Automatically extracts dominant color schemes from any image to ensure color harmony in new creations.

### 3. Model Fine-Tuning & Customization
- **On-Device Training:** Train and fine-tune your own Stable Diffusion models directly through the Dashboard.
- **Model Management:** Easily switch between different fine-tuned models saved in your local directory.

### 4. Interactive Dashboard
- **Live Progress:** Watch your art being created block-by-block or step-by-step with real-time progress bars and status animations.
- **Social Media Presets:** One-click sizing for Instagram (Posts/Stories), Twitter, LinkedIn, and Facebook.

## 🧠 Important: Model Information

**NeuralCanvas handles heavy model weights smartly:**
- **Initial Run:** On the first execution, the application will automatically download the **Stable Diffusion v1.5** weights and **BLIP** models from Hugging Face. 
- **Storage:** Please ensure you have at least **10GB+ of free disk space**.
- **Hardware:** A GPU with at least 8GB VRAM is highly recommended for AI-based generation and mandatory for model training.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/redghost-dev/NeuralCanvas.git
   cd NeuralCanvas
   ```

2. **Environment Setup:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration:**
   Open `config.py` and add your [Pixabay API Key](https://pixabay.com/api/docs/) to enable automated image dataset collection.

## 💻 Usage

Launch the visual dashboard with:
```bash
python abstract_art_generator.py
```

## 📂 Project Architecture

- `abstract_art_generator.py`: The heart of the application. Manages the Tkinter UI, threading, and training loops.
- `image_generator.py`: The backend engine. Contains logic for both AI diffusion and the geometric shape-rendering algorithm.
- `config.py`: Centralized configuration for API keys and global constants.
- `models/`: (Local only) This is where your custom fine-tuned models are stored.
- `examples/`: Reference images used by the engine to "inspire" new abstract works.

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.

---
*Transforming algorithms into aesthetics.*
