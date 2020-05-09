from arvores import no_arvore

class NoArvoreInteiro(no_arvore.NoArvore):
    def __init__(self, valor):
        super().__init__(valor)

    def chave(self):
        return self.valor