import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class InputWindow(ctk.CTkToplevel):
    def __init__(self, master, config):
        super().__init__(master)
        self.config = config
        self.title(config["title"])
        self.geometry("400x250")
        self.focus()
        self.grab_set()
        self.lift()
        self.resizable(False, False)

        self.entries = []

        for label_text in config["labels"]:
            label = ctk.CTkLabel(self, text=label_text)
            label.pack(pady=(8, 0))
            entry = ctk.CTkEntry(self, placeholder_text=label_text)
            entry.pack(pady=(0, 5))
            self.entries.append(entry)

        ctk.CTkButton(self, text="Aceptar",command=self._call_method).pack(pady=10)

    def _call_method(self,):
        method = self.config["method"]
        args = [int(entry.get()) for entry in self.entries]
        result = method(*args)
        print(result)

    def _center_window(self):
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