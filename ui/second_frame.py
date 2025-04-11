import customtkinter as ctk

class MethodFrame(ctk.CTkFrame):
    def __init__(self, master, method, config, back_callback):
        super().__init__(master)
        self.config = config
        self.method_name = method
        self.back_callback = back_callback
        self.entries = []
        self._load_menu()

    def _load_menu(self):

        self.input_frame = ctk.CTkFrame(master=self, corner_radius=15)
        self.input_frame.pack(side= "left", fill="y", padx=10, pady=10)

        self.result_frame = ctk.CTkFrame(master=self, corner_radius=15, height=150)
        self.result_frame.pack(side= "top", fill= "x", padx=10, pady=10)
        self.result_frame.pack_propagate(False)

        self.test_frame = ctk.CTkFrame(master=self, corner_radius=15)
        self.test_frame.pack(side= "bottom", fill="x", padx=10, pady=10)

        j_title = ctk.CTkLabel(master=self.result_frame, text = self.method_name)
        j_title.pack(side= "top")

        self.results_scroll = ctk.CTkScrollableFrame(master=self.result_frame,
                                                     corner_radius=15,
                                                     orientation="vertical",
                                                     )
        self.results_scroll.pack(side= "top",fill="x", padx=10, pady=10)

        for label_text in self.config["labels"]:
            label = ctk.CTkLabel(self.input_frame, text=label_text)
            label.pack(pady=(10, 0))
            entry = ctk.CTkEntry(self.input_frame, placeholder_text=label_text)
            entry.pack(pady=(0, 5))
            self.entries.append(entry)

        ctk.CTkButton(self.input_frame, text="Generar",command=self._call_method).pack(padx=10 ,pady=15)

        ctk.CTkButton(self.input_frame, text="← Volver", command=self.back_callback).pack(pady=10)


    def _call_method(self):
        method = self.config["method"]
        args = [int(entry.get()) for entry in self.entries]
        result = method(*args)
        for index,result in enumerate(result):
            ctk.CTkLabel(self.results_scroll, text=f"U{index+1} = {result}").pack(pady=10)



