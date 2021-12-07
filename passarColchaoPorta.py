A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

H,L = input().split()
H = int(H)
L= int(L)

def passarColchaoPorta(A,B,C,H,L):
    if (B < H and A < L):
        return 'S'
    else:
        return 'N'

colchao = passarColchaoPorta(A,B,C,H,L)

if (colchao == 'S'):
    print ('Parabéns pela compra!')
else:
    print ('Você deve escolher outro colchão!')
