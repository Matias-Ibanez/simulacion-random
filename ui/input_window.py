import customtkinter as ctk

ctk.set_appearance_mode("dark")       # Opcional: "light", "dark", "system"
ctk.set_default_color_theme("blue")   # Podés probar otros: "green", "dark-blue", etc.

class InputWindow(ctk.CTkToplevel):
    def __init__(self, metodo_numero):
        super().__init__()
        self.title(f"Método {metodo_numero}")
        self.geometry("300x200")

        self.label_semilla = ctk.CTkLabel(self, text="Semilla:")
        self.label_semilla.pack(pady=10)
        self.entry_semilla = ctk.CTkEntry(self)
        self.entry_semilla.pack(pady=5)

        self.label_cantidad = ctk.CTkLabel(self, text="Cantidad de números:")
        self.label_cantidad.pack(pady=10)
        self.entry_cantidad = ctk.CTkEntry(self)
        self.entry_cantidad.pack(pady=5)

        self.button_generar = ctk.CTkButton(self, text="Generar", command=self.generar)
        self.button_generar.pack(pady=20)

    def generar(self):
        semilla = self.entry_semilla.get()
        cantidad = self.entry_cantidad.get()
        print(f"[Método] Semilla: {semilla}, Cantidad: {cantidad}")
        self.destroy()  # Cierra la ventana después de presionar "Generar"