import random


class simuladordedado:
    def __init__(self):
        self.mens = "Você gostaria de gerar um novo valor para o dado (d6)? "
        self.valor_minimo = 1
        self.valor_maximo = 6

    def iniciar(self):
        resposta = input(str(self.mens))
        try:
            if resposta == 'sim' or resposta == 's':
                self.gerarvalordodado()
            elif resposta == 'não' or resposta == 'n':
                print('OK! encerrando...')
            else:
                print('Por Favor, digite apenas Sim ou Não')
        except:
            print('Ocorreu um ero ao receber sua resposta')

    def gerarvalordodado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simular = simuladordedado()
simular.iniciar()
