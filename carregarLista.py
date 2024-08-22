

class LoadList:
    def __init__(self, caminho):
        self.array = []
        self.caminho = caminho

    def loadCaminho(self):
        arq_open = open(self.caminho, 'r')
        linhas_arq = arq_open.readlines()
        for linha in linhas_arq:
            self.array.append(linha)
        return self.array
