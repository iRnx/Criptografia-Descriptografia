# CRIPTOGRAFIA #
def crypt(msg):
    s = ''
    chave = int(input('Digite a chave: '))
    for c in msg:
        s += chr(ord(c) + chave)
    return s


def decrypt(msg):
    chave = int(input('Qual a chave da descriptografia? '))
    s = ''
    for c in msg:
        s += chr(ord(c) - chave)
    return s


# Programa Principal #
print('''
[ 1 ] CRIPTOGRAFAR
[ 2 ] DESCRIPTOGRAFAR''')
escolha = int(input('1 OU 2 ?'))

if escolha == 1:
    frase1 = str(input('Frase para Criptografar: '))
    print(crypt(frase1))

elif escolha == 2:
    frase2 = str(input('Frase para Descriptografar: '))
    print(decrypt(frase2))
