from tkinter import filedialog


class ReadCSV:
    def __init__(self):
        self.caminho = ''

    def localizar_csv(self, leiaute='Lista de CNPJs'):
        self.caminho = filedialog.askopenfilename(title=f'Arquivo CSV {leiaute}',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

    def get_caminho(self):
        return self.caminho
