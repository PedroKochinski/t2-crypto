import sys
from math import sqrt
# n = p*q
# d eh a chave privada

# sabemos: p,q primos menores que 1024 e {e,n} é conhecida

# f(n) = (p-1)(q-1) euler totient

# (e * d) % f(n) = 1
# e * d  = 1 % (f(n))
# d = 1 % ((p-1)(q-1))/e

#encontra o proximo numero primo
def next_prime(prime):
        next = prime + 1
        while (True):
                isprime = True
                #procura divisor
                for i in range (2, (next//2 + 1)):
                        if (next % i == 0):
                                isprime = False
                                break
                if(not isprime):
                        next+=1
                else:
                        break
                
        return next

#forca bruta ate achar n tal que p e q sao menores que 1024 (especificacao do trabalho) e n eh p*q garantidamente (especificacao do rsa)
def prime_factorization(n):
        i = 1
        j = 1
        while(i < 1024):
               i = next_prime(i)
               while(j < 1024):
                      j = next_prime(j)
                      if(i*j == n):
                             return i,j
               j = 1
        return -1,-1


def euler_totient(p,q):
        return ((p-1)*(q-1))

def extended_gcd(a, b):
    if b == 0:  # Caso base: quando o divisor é 0
        return a, 1, 0  # Retorna o MDC e os coeficientes de Bézout
    gcd, x1, y1 = extended_gcd(b, a % b)  # Chamada recursiva com o divisor e o resto
    x = y1  # Atualiza o coeficiente x
    y = x1 - (a // b) * y1  # Atualiza o coeficiente y
    return gcd, x, y  # Retorna o MDC e os coeficientes atualizados

# encontra chave privada. e*d é congruente a 1 % euler_totient
def find_private_key(euler, e):
        gcd, d, _ = extended_gcd(e, euler)  # Calcula o MDC e os coeficientes
        if gcd == 1:  # Verifica se o inverso modular existe
                d = d % euler  # Ajusta d para o intervalo positivo
                # Ajustar para garantir d > e
                while d <= e:  # Adiciona múltiplos do cociente de euler até que d > e
                        d += euler
                return d
        else:
                return -1

def main():
        """
        Le a chave publica e o numero N {e,n}        
        """
        if(len(sys.argv) < 2):
               print('Argumento Inválido: utilize python3 quebra.py e n')
               exit(1)
        e = int(sys.argv[1])
        n = int(sys.argv[2])
        p,q = prime_factorization(n)
        euler = euler_totient(p,q)
        d = find_private_key(euler, e)
        print(f'Chave publica e: ({e}, {n})')
        print(f'fatores primos de {n}: {p, q}')
        print(f'Euler Totient = {euler}')
        print(f'Chave privada d: ({d}, {n})')

if __name__ == '__main__':
    main()