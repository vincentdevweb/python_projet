# generer un sel aleatoire

# retoune le code ASCII d'un caractere passe en parametre
print(ord('z'))
number_ascii = ord('z')
char_ascii = chr(number_ascii)
print(char_ascii)

def cle(t: tuple) -> str:
    res = ''
    for i in range(len(t)):
        res += chr(t[i])
    return res