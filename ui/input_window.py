import customtkinter as ctk
import cuadrado
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class InputWindow(ctk.CTkToplevel):
    def __init__(self, metodo_numero):
        super().__init__()
        self.title(f"Método {metodo_numero}")
        self.width = 300
        self.height = 250
        self.center_window()

        self.label_semilla = ctk.CTkLabel(self, text="Semilla:")
        self.label_semilla.pack(pady=10)
        self.entry_semilla = ctk.CTkEntry(self)
        self.entry_semilla.pack(pady=5)

        self.label_cantidad = ctk.CTkLabel(self, text="Cantidad de números:")
        self.label_cantidad.pack(pady=10)
        self.entry_cantidad = ctk.CTkEntry(self)
        self.entry_cantidad.pack(pady=5)

        self.button_generar = ctk.CTkButton(self, text="Generar")
        self.button_generar.pack(pady=20)

    def center_window(self):
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()
        x = int((window_width / 2) - (self.width / 2))
        y = int((window_height / 2) - (self.height / 2))
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    # def generar(self,seed,numbers_of_values,):
    #     seed = self.entry_semilla.get()
    #     numbers_of_values = self.entry_cantidad.get()
    #
    #     self.destroy()  # Cierra la ventana después de presionar "Generar"