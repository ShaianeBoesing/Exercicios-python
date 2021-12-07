ano, mes, dia = input('Informe sua idade em anos, meses e dias: ').split()
idadeEmDias = int(ano)*365 + int(mes)*30 + int(dia)
print ('Você já viveu ', idadeEmDias, ' dias')
