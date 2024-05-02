# # generer un sel aleatoire

# # retoune le code ASCII d'un caractere passe en parametre
# print(ord('z'))
# number_ascii = ord('z')
# char_ascii = chr(number_ascii)
# print(char_ascii)

# def cle(t: tuple) -> str:
#     res = ''
#     for i in range(len(t)):
#         res += chr(t[i])
#     return res


from random import choice, randint


def sel_generator(n: int , min: bool = True, maj: bool = True, chif: bool = True, cs: bool = True):
    alphabet_min = [ chr(i) for i in range(97,123) ]
    alphabet_maj = [ chr(i) for i in range(65,91) ]
    chiffres = [ str(i) for i in range(0,10) ]
    caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

    alphabets = {}
    key = 0
    if min:
        alphabets[key] = alphabet_min
        key += 1
    if maj:
        alphabets[key] = alphabet_maj
        key += 1
    if chif:
        alphabets[key] = chiffres
        key += 1
    if cs:
        alphabets[key] = caracteres_speciaux
        key += 1
    
    mdp = ''
    for _ in range(n):
            s = randint(0,key-1)
            mdp += choice( alphabets[s] )
            
    return mdp

mot_de_passe = "miaou"

sel = sel_generator(len(mot_de_passe))
print(sel)

mdp_sel = mot_de_passe+sel
print(mdp_sel)

# retourne un tuple aleatoire de 0 a 10 de la longueur de mdp_sel
def generate_tuples(len_mdp_sel: int) -> tuple:
    return tuple(randint(0,55) for _ in range(len(len_mdp_sel)))

cle = generate_tuples(mdp_sel)
print(cle)

def crypt(cle: tuple , mdp_sel: str) -> str:
    res_str = ""
    for i,v in enumerate(cle):
        res = int((v + ord(mdp_sel[i])) % 128)
        res_str += chr(res)
    return res_str

print(crypt(cle,mdp_sel))