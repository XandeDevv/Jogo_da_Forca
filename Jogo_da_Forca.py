from random import choice


class Forca:
    def __init__(self):
        self.erro = 0
        self.chutes = []
        self.sorteada = choice(lista)
        self.sorteada_oculta = []
        for c in self.sorteada:
            self.sorteada_oculta.append('_')

    def cabeçalho(self,txt,tam=42):
        print('-'*tam)
        print(txt.center(tam))
        print('-'*tam)

    def titulo(self):
        self.cabeçalho('Jogo da Forca')
        print(f'A palavra tem {len(self.sorteada)} letras')
        print('O jogo acaba com 7 erros')
        print('Digite as palavras sem acentuação')

    def chute(self,lista):
        while True:
            for c in self.sorteada_oculta:
                print(c,end=' ')
            print('')
            self.chute = input('Qual o seu chute:').upper().strip()[0]
            if self.chute.isalpha()==False:
                print(f'\033[31mDigite Apenas Letras\033[m')
                continue
            elif self.chute in self.chutes:
                print(f'\033[31mVocê já escolheu essa letra!\033[m')
                continue
            self.chutes.append(self.chute)
            self.acertouErrou()
            print(f'Seus chutes foram ',end='')
            for c in self.chutes:
                print(c,end=', ')
            print()

    def acertouErrou(self):
        if self.chute in self.sorteada:
            for c,v in enumerate(self.sorteada):
                if self.chute==v:
                    self.sorteada_oculta[c]=v
                    print(f'Você achou a letra {v} na {c+1}ª posição')
        else:
            self.erro+=1
            if self.erro<3:
                print(f'Você Errou {self.erro} vezes')
            elif self.erro<5:
                print(f'\033[33mVocê Errou {self.erro} vezes\033[m')
            else:
                print(f'\033[31mVocê Errou {self.erro} vezes\033[m')
        self.ganhouPerdeu()

    def ganhouPerdeu(self):
        if '_' not in self.sorteada_oculta:
            self.cabeçalho(f'A palavra era {self.sorteada}')
            self.cabeçalho('Parábens! Você Ganhou!!!')
            exit()
        elif self.erro==7:
            self.cabeçalho(f'A palavra era {self.sorteada}')
            self.cabeçalho('Você Perdeu!')
            exit()


lista=['NAVIO','BANANA','PERNAMBUCO','AZEITONA','TRATOR','BARRIGA','BISCOITO','COMPUTADOR','GARRAFA','MOCHILA'
       'LIVRARIA','TABUADA','CELULAR','CACHORRO','TRAVESSEIRO','PORTA','VESTIDO','PERFUME','PYTHON','FUTEBOL',
       'GAFANHOTO','COXINHA','PIZZARIA','UNIVERSIDADE','CASTELO','ELEFANTE','BASQUETE','COZINHA','SKATE','BOLICHE',
       'ORTOPEDIA','BERIMBAL','VENEZUELA','ALFAIATE','NEVOEIRO','UNIVERSO','COMPRIMIDO','PERFORMANCE','ENGRAXATE',
       'DESODORANTE']
f=Forca()
f.titulo()
f.chute(lista)