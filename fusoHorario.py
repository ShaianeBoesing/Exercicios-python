S, T, F =  input().split()
S = int(S)
T = int(T)
F = int(F)

def calculaHoraLocalDestino(S, T, F):
    horaLocalDestino = S + T + F
    if 0 <= horaLocalDestino < 24:
        print(horaLocalDestino)
    elif horaLocalDestino >= 24:
        print(horaLocalDestino - 24)
    elif horaLocalDestino < 0:
        print(24 + horaLocalDestino)


calculaHoraLocalDestino(S, T, F)