import tkinter as tk

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Basit Arayüz Tasarımı")  # Pencere başlığı
root.geometry("300x200")  # Pencere boyutu

# Etiket oluştur
label = tk.Label(root, text="Merhaba! Bir şeyler yazın:")
label.pack(pady=10)

# Giriş kutusu oluştur
entry = tk.Entry(root)
entry.pack(pady=10)

# Buton tıklandığında çalışacak fonksiyon
def button_click():
    entered_text = entry.get()  # Giriş kutusundaki metni al
    label.config(text=f"Yazdığınız metin: {entered_text}")  # Etiketi güncelle

# Buton oluştur
button = tk.Button(root, text="Gönder", command=button_click)
button.pack(pady=10)

# Pencereyi çalıştır
root.mainloop()
