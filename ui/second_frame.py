import customtkinter as ctk

def only_numbers(valor):
    return valor.isdigit() or valor == ""

class MethodFrame(ctk.CTkFrame):
    def __init__(self, master, method, config, back_callback):
        super().__init__(master)
        self.config = config
        self.method_name = method
        self.back_callback = back_callback
        self.entries = []
        self._load_menu()

    def _load_menu(self):
        self.input_frame = ctk.CTkFrame(master=self, corner_radius=15, fg_color = "#292840",
                                        width=450, border_width=3, border_color="#8449BF")
        self.input_frame.pack(side= "left", fill="y", padx=10, pady=10)

        self.result_frame = ctk.CTkFrame(master=self, corner_radius=15, height=300, fg_color = "#059669",)
        self.result_frame.pack(side= "top", fill= "x", padx=10, pady=10)
        self.result_frame.pack_propagate(False)

        self.test_frame = ctk.CTkFrame(master=self, corner_radius=15)
        self.test_frame.pack(fill="both", padx=10, pady=10)

        j_title = ctk.CTkLabel(master=self.result_frame, text = self.method_name, font=("Inter", 25, "bold"))
        j_title.pack(side= "top")

        self.results_scroll = ctk.CTkScrollableFrame(master=self.result_frame,
                                                     corner_radius=15,
                                                     orientation="vertical",
                                                     )
        self.results_scroll.pack(side= "top",fill="x", padx=10, pady=10)

        validate_numbers = self.register(only_numbers)

        for label_text in self.config["labels"]:

            label = ctk.CTkLabel(
                self.input_frame,
                text=label_text,
                font=("Inter", 18, "bold")
            )
            label.pack(fill="x", padx=20, pady=(10, 10))

            entry = ctk.CTkEntry(
                self.input_frame,
                placeholder_text="Solo números",
                border_color="#059669",
                width=180,
                validate="key",
                validatecommand=(validate_numbers, "%P")
            )
            entry.pack(fill = "x", padx = 20,  pady=(0, 5))
            self.entries.append(entry)

        ctk.CTkButton(
            self.input_frame,
            text="Generar",
            command=self._call_method,
            fg_color="#8449BF",
            hover_color="#059669",
            font=("Inter", 18, "bold")
        ).pack(padx=10, pady=15)

        ctk.CTkButton(
            self.input_frame,
            text="← Volver",
            command=self.back_callback,
            fg_color="#8449BF",
            hover_color="#059669",
            font=("Inter", 18, "bold")
        ).pack(pady=10)

    def _call_method(self):
        for widget in self.results_scroll.winfo_children():
            widget.destroy()
        try:
            method = self.config["method"]
            args = [int(entry.get()) for entry in self.entries]
            result = method(*args)

            for index, value in enumerate(result):
                ctk.CTkLabel(
                    self.results_scroll,
                    text=f"U{index + 1} = {value}",
                    font=("Inter", 18)
                ).pack(pady=10)


        except ValueError:
            self.error_label = ctk.CTkLabel(
                self,
                text="¡Error! Campos vacíos",
                font=("Inter", 15),
            )
            self.error_label.pack(pady=10)
            self.after(2000, self.error_label.destroy)












