A, B, C = (input()).split()
A = float(A);
B = float(B);
C = float(C);

AREA_TRIANGULO = (A * C)/2
AREA_CIRCULO = pow(C,2) * 3.14159
AREA_TRAPEZIO = ((A+B)*C)/2
AREA_QUADRADO = pow(B,2)
AREA_RETANGULO = A * B

print(f'TRIANGULO: {AREA_TRIANGULO:.3f}')
print(f'CIRCULO: {AREA_CIRCULO:.3f}')
print(f'TRAPEZIO: {AREA_TRAPEZIO:.3f}')
print(f'QUADRADO: {AREA_QUADRADO:.3f}')
print(f'RETANGULO: {AREA_RETANGULO:.3f}')

