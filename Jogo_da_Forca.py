from random import choice

def cabeçalho(txt,tam=42):
    print('-'*tam)
    print(txt.center(42))
    print('-'*tam)

def palavraforca(lista):
    sorteada=choice(lista)
    sorteada_oculta=[]
    for c in sorteada:
        sorteada_oculta.append('_')
    erro = 0
    chutes=[]
    cabeçalho('Jogo da Forca')
    print(f'A palavra tem {len(sorteada)} letras')
    print('O jogo acaba com 7 erros')
    print('Digite as palavras sem acentuação')
    while True:
        for c in sorteada_oculta:
            print(c,end=' ')
        print()
        try:
            chute = input('Qual o seu chute:').upper().strip()[0]
            if chute.isalpha()==False:
                print(f'\n\033[31mDigite Apenas Letras\033[m')
                continue
            elif chute in chutes:
                print(f'\033[31mVocê já escolheu essa letra!\033[m')
                continue
        except:
            print(f'\033[31mOcorreu um erro! Digite Apenas Letras\033[m')
            continue
        chutes.append(chute)
        print(f'Seus chutes foram ',end='')
        for c in chutes:
            print(c,end=', ')
        print()
        if chute in sorteada:
            for c,v in enumerate(sorteada):
                if chute==v:
                    sorteada_oculta[c]=v
                    print(f'Você achou a letra {v} na {c+1}ª posição')
        else:
            erro+=1
            if erro<3:
                print(f'Você Errou {erro} vezes')
            elif erro<5:
                print(f'\033[33mVocê Errou {erro} vezes\033[m')
            else:
                print(f'\033[31mVocê Errou {erro} vezes\033[m')
        if '_' not in sorteada_oculta:
            cabeçalho(f'A palavra era {sorteada}')
            cabeçalho('Parábens! Você Ganhou!!!')
            break
        if erro==7:
            cabeçalho(f'A palavra era {sorteada}')
            cabeçalho('Você Perdeu!')
            break












lista=['NAVIO','BANANA','PERNAMBUCO','AZEITONA','TRATOR','BARRIGA','BISCOITO','COMPUTADOR','GARRAFA','MOCHILA'
       'LIVRARIA','TABUADA','CELULAR','CACHORRO','TRAVESSEIRO','PORTA','VESTIDO','PERFUME','PYTHON','FUTEBOL',
       'GAFANHOTO','COXINHA','PIZZARIA','UNIVERSIDADE','CASTELO','ELEFANTE','BASQUETE','COZINHA','SKATE']
palavraforca(lista)
