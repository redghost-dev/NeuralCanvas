import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import threading
import queue
from image_generator import ImageGenerator

class AbstractArtDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Soyut Sanat Üretici")
        self.root.geometry("800x600")
        
        self.is_generating = False
        self.image_queue = queue.Queue()
        self.generator = ImageGenerator()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Format seçimi
        self.format_frame = ttk.LabelFrame(self.root, text="Görsel Formatı")
        self.format_frame.pack(padx=10, pady=5, fill="x")
        
        self.format_var = tk.StringVar(value="PNG")
        formats = ["PNG", "JPG", "WEBP"]
        for fmt in formats:
            ttk.Radiobutton(self.format_frame, text=fmt, variable=self.format_var, value=fmt).pack(side="left", padx=5)
        
        # Boyut seçimi
        self.size_frame = ttk.LabelFrame(self.root, text="Boyut Seçimi")
        self.size_frame.pack(padx=10, pady=5, fill="x")
        
        self.preset_sizes = {
            "Instagram Post": (1080, 1080),
            "Instagram Story": (1080, 1920),
            "Twitter Post": (1200, 675),
            "Facebook Post": (1200, 630),
            "LinkedIn Post": (1200, 627)
        }
        
        self.size_var = tk.StringVar(value="Instagram Post")
        self.size_combo = ttk.Combobox(self.size_frame, textvariable=self.size_var, values=list(self.preset_sizes.keys()))
        self.size_combo.pack(side="left", padx=5)
        
        # Önizleme alanı
        self.preview_frame = ttk.LabelFrame(self.root, text="Önizleme")
        self.preview_frame.pack(padx=10, pady=5, expand=True, fill="both")
        
        self.preview_label = ttk.Label(self.preview_frame)
        self.preview_label.pack(expand=True)
        
        # Kontrol butonları
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=5, fill="x")
        
        self.start_button = ttk.Button(self.button_frame, text="Başlat", command=self.start_generation)
        self.start_button.pack(side="left", padx=5)
        
        self.stop_button = ttk.Button(self.button_frame, text="Durdur", command=self.stop_generation, state="disabled")
        self.stop_button.pack(side="left", padx=5)
        
        self.save_button = ttk.Button(self.button_frame, text="Kaydet", command=self.save_image, state="disabled")
        self.save_button.pack(side="left", padx=5)

    def start_generation(self):
        if not self.is_generating:
            self.is_generating = True
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            
            size = self.preset_sizes[self.size_var.get()]
            format_type = self.format_var.get()
            
            thread = threading.Thread(target=self.generate_images, args=(size, format_type))
            thread.daemon = True
            thread.start()
            
            self.check_queue()

    def stop_generation(self):
        self.is_generating = False
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

    def generate_images(self, size, format_type):
        while self.is_generating:
            image = self.generator.generate(size[0], size[1])
            self.image_queue.put(image)

    def check_queue(self):
        try:
            image = self.image_queue.get_nowait()
            self.display_preview(image)
            self.save_button.configure(state="normal")
        except queue.Empty:
            pass
        
        if self.is_generating:
            self.root.after(100, self.check_queue)

    def display_preview(self, image):
        # Önizleme boyutunu ayarla
        preview_width = 400
        ratio = preview_width / image.width
        preview_height = int(image.height * ratio)
        
        preview = image.copy()
        preview.thumbnail((preview_width, preview_height))
        
        photo = ImageTk.PhotoImage(preview)
        self.preview_label.configure(image=photo)
        self.preview_label.image = photo
        self.current_image = image

    def save_image(self):
        if hasattr(self, 'current_image'):
            file_format = self.format_var.get().lower()
            filetypes = [(f"{file_format.upper()} files", f"*.{file_format}")]
            filename = filedialog.asksaveasfilename(
                defaultextension=f".{file_format}",
                filetypes=filetypes
            )
            if filename:
                self.current_image.save(filename)

if __name__ == "__main__":
    root = tk.Tk()
    app = AbstractArtDashboard(root)
    root.mainloop()
