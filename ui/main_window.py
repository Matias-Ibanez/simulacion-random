import customtkinter as ctk
from ui.second_frame import  MethodFrame
from methods.cuadrado import _ParteCentralDelCuadrado
from methods.lehmer import _Lehmer

class MainApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.method_configs = {
            "Parte Central del cuadrado": {
                "labels": ["Semilla", "Número de dígitos", "Cantidad a generar",],
                "title": "Método - Cuadrado Medio",
                "method": _ParteCentralDelCuadrado.square_method,
            },
            "Lehmer" :{
                "labels": ["Semilla", "Número", " Cantidad a generar"],
                "title": "Método - Lehmer",
                "method": _Lehmer.lehmer_method,
            },
            "Congruencial Mixto" : {},
            "Congruencial Multiplicativo" : {},
            "Congruencial Aditivo" : {}
        }

        self._set_appearance_mode("Dark")
        self.title("Generador de números aleatorios")
        self.width= 600
        self.height= 400
        self.center_window()
        self.resizable(False, False)

        self.menu_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.menu_frame.pack(fill="both", expand=True, padx=20, pady=20)
        self._load_menu()

        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack_forget()

    def _load_menu(self):
        self.label = ctk.CTkLabel(
            master=self.menu_frame,
            text="Seleccionar método",
            font=("Inter", 20, "bold"),
            fg_color="transparent").pack(pady=30)

        for method in self.method_configs.keys():
             ctk.CTkButton(master=self.menu_frame,
                           text=f"{method}",
                           width=220,
                           corner_radius=32,
                           font=("Inter", 14, "bold"),
                           fg_color="#10B981",
                           hover_color="#059669",
                           command=lambda m=method: self.open_method_frame(m)).pack(pady=10)

    def center_window(self):
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()
        x = int((window_width / 2) - (self.width / 2))
        y = int((window_height / 2) - (self.height / 2))
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def open_method_frame(self, method):
        config = self.method_configs.get(method)
        self.menu_frame.pack_forget()

        for widget in self.main_container.winfo_children():
            widget.destroy()

        method_frame = MethodFrame(master=self.main_container,method=method, config=config, back_callback=self.show_main_menu)
        method_frame.pack(fill="both", expand=True)
        self.main_container.pack(fill="both", expand=True)

    def show_main_menu(self):
        self.main_container.pack_forget()
        self.menu_frame.pack(fill="both", expand=True)
