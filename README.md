# NeuralCanvas AI 🎨

NeuralCanvas is a comprehensive abstract art generation platform developed with Python, combining both **Stable Diffusion**-based generative AI and advanced geometric algorithms.

## 🚀 Features

- **Hybrid Generation Mode:** Produce high-quality AI images using Stable Diffusion v1.5 or create purely mathematical abstract compositions with classic geometric algorithms.
- **Model Training (Fine-Tuning):** Train Stable Diffusion models using your own datasets to create personalized art styles.
- **Image Analysis (BLIP):** Automatic prompt (caption) generation and color palette extraction from reference images.
- **Live Preview:** An interactive Dashboard where you can follow the production stage in real-time.
- **Feedback System:** Contribute to the evolution of the system by rating the generated images.
- **Multi-Format Support:** Export in PNG, JPG, and WEBP formats.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/redghost-dev/NeuralCanvas.git
   cd NeuralCanvas
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Pixabay API key to the `config.py` file.

## 💻 Usage

To start the application:
```bash
python abstract_art_generator.py
```

## 📂 Project Structure

- `abstract_art_generator.py`: Main Dashboard and user interface.
- `image_generator.py`: AI and geometric generation engine.
- `models/`: Directory where trained AI models are stored.
- `config.py`: API keys and global settings.
- `examples/`: Reference images used as examples.

## ⚖️ License

This project is licensed under the MIT License.

---
*Explore the art of the future with algorithms.*
