class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def inserir_elemento_posicao(self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao] + [None]
        vetor_inicio[len(vetor_inicio)-1] = elemento
        vetor_final = self.__elementos[posicao:]
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= len(self.__elementos):
            self.__elementos += [None]
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def remover_elemento_posicao(self, posicao):
        vetor_inicio = self.__elementos[:posicao]
        vetor_final = self.__elementos[posicao+1:]
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao -= 1

    def remover_elemento(self, elemento):
        for i, elem in enumerate(self.__elementos):
            if elem == elemento:
                self.remover_elemento_posicao(i)
                break

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]

    @property
    def tamanho_vetor(self):
        return len(self.__elementos)

    def contem(self, elemento):
        for elem in self.__elementos:
            if elemento==elem:
                return True
        return False

    def indice(self, elemento):
        for i, elem in enumerate(self.__elementos):
            if elemento==elem:
                return i
        return -1