def NOT(p):
    return not p


def AND(p,q):
    return p and q


def OR(p,q):
    return p or q

def IFTHEN (p,q):
    if q == True: 
        return True
    if p == False and q == False: 
        return True
    else:
        return False


sentencas = []

tabela_verdade = [
    ['p','q'],
    ['V','V'],
    ['V','F'],
    ['F','V'],
    ['F','F'],
    
]

for i in range(1,4):

    sentenca = input(f"Insira a {i}ª sentença (ou digite '-' para sair)")
    
    if sentenca == '-':
        break

    sentencas.append(sentenca)

    if sentencas:
        abc = ['a','b','c']
        j = 0
        for s in sentencas:
            print(f"{abc[j]}: {s}")
            j+= 1


for sentenca in sentencas:
    sentenca_separada = sentenca.split(' ')
    print(sentenca_separada)