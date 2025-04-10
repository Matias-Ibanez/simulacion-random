import customtkinter as ctk
from ui.input_window import  InputWindow
from methods.cuadrado import _ParteCentralDelCuadrado

class MainApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.methods = ["Parte Central del cuadrado", "Lehmer",
                        "Congruencial Mixto", "Congrencial Multiplicativo",
                        "Congruencial Aditivo"]
        self.buttons = {}
        self.method_configs = {
            "Parte Central del cuadrado": {
                "labels": ["Semilla", "Número de dígitos", "Cantidad de números"],
                "title": "Método - Cuadrado Medio",
                "method": _ParteCentralDelCuadrado.square_method,
            }

        }

        self.title("Generador de números aleatorios")
        self.width= 400
        self.height= 400
        self.center_window()
        self.resizable(False, False)

        frame = ctk.CTkFrame(
            master= self,
            fg_color="#2D2D2D",
            border_width=2,
            border_color="#A78BFA",
            corner_radius=15,
            width = 300,
            height = 300
        )
        frame.pack(expand =True)
        frame.pack_propagate(False)

        self.label = ctk.CTkLabel(
            master=frame,
            text="Seleccionar método",
            font=("Inter", 20, "bold"),
            fg_color = "transparent")
        self.label.pack(pady=30)

        for method in self.method_configs.keys():
            button = ctk.CTkButton(master=frame,
                                   text=f"{method}",
                                   width=220,
                                   corner_radius=32,
                                   font= ("Inter", 14, "bold"),
                                   fg_color="#10B981",
                                   hover_color="#059669",
                                   command=lambda m=method: self.open_popup(m))
            button.pack(pady=10)
            self.buttons[method] = button

    def center_window(self):
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()
        x = int((window_width / 2) - (self.width / 2))
        y = int((window_height / 2) - (self.height / 2))
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def open_popup(self, method):
        config = self.method_configs.get(method)
        if config:
            InputWindow(
                master=self,
                config=config,
            )



    # @staticmethod
    # def handle_button_click(method):
    #    second_window = m_window.InputWindow(method)
    #    second_window.focus()
    #    second_window.grab_set()
    #    second_window.lift()




        # optionmenu = ctk.CTkOptionMenu(self, values=["option 1", "option 2"],
        #                                          )
        # optionmenu.grid(row=1, column = 1)
        # optionmenu.set("option 2")
