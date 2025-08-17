import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.deactivate_automatic_dpi_awareness()
class Screen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("DataAnalyzerCLI")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        title_label = ctk.CTkLabel(self, text="📊 Data Analyzer CLI", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=15)

        subtitle_label = ctk.CTkLabel(self, text="Selecione um arquivo para análise",font=("Helvetica", 13))
        subtitle_label.pack(pady=5)

        choose_btn = ctk.CTkButton(self, text="📂 Escolher Arquivo",command=self.choose_file)
        choose_btn.pack(pady=10)

        self.file_label = ctk.CTkLabel(self, text="Nenhum arquivo selecionado",font=("Helvetica", 11))
        self.file_label.pack(pady=5)

        send_btn = ctk.CTkButton(self, text="🚀 Enviar Arquivo",command=self.send_file, fg_color="green")
        send_btn.pack(pady=15)

    def choose_file(self):
        filepath = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
        )
        if filepath:
            self.file_label.configure(text=f"Selecionado: {filepath.split('/')[-1]}")
            self.selected_file = filepath
        else:
            self.file_label.configure(text="Nenhum arquivo selecionado")
            self.selected_file = None

    def send_file(self):
        if hasattr(self, "selected_file") and self.selected_file:
            messagebox.showinfo("Sucesso", f"Arquivo enviado:\n{self.selected_file}")
            self.quit()
            self.destroy()
        else:
            messagebox.showwarning("Atenção", "Nenhum arquivo selecionado!")

if __name__ == "__main__":
    app = Screen()
    app.mainloop()
