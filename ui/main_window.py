from input_window import InputWindow
import customtkinter as ctk

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Generador de números aleatorios")
        self.geometry("400x400")

        self.label = ctk.CTkLabel(self, text="Seleccioná un método", font=("Arial", 20))
        self.label.pack(pady=30)

        for i in range(1, 5):
            boton = ctk.CTkButton(self, text=f"Método {i}", width=200, command=lambda i=i: self.abrir_ventana(i))
            boton.pack(pady=10)

    def abrir_ventana(self, metodo_numero):
        InputWindow(metodo_numero)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()