from random import choice, randint


class CustomCrypte:
    
    def __init__(self, mdp: str):
        self.__mdp = mdp
        self.__sel = self.sel_generator(self.__mdp)
        self.__cle = self.generate_tuples(len(self.__sel))
        self.__mdp_chiffrer = self.crypt(self.__cle, str(self.__mdp+self.__cle))
        
    def crypt(cle: tuple , mdp_sel: str) -> str:
        res_str = ""
        for i,v in enumerate(cle):
            res = int((v + ord(mdp_sel[i])) % 128)
            res_str += chr(res)
        return res_str

    def generate_tuples(len_mdp_sel: int) -> tuple:
        return tuple(randint(0,55) for _ in range(len(len_mdp_sel)))
    
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
    

    @property
    def mdp(self):
        return self.__mdp

    @mdp.setter
    def mdp(self, value):
        self.__mdp = value
        
    property
    def sel(self):
        return self.__sel

    @sel.setter
    def sel(self, value):
        self.__sel = value

    @property
    def cle(self):
        return self.__cle

    @cle.setter
    def cle(self, value):
        self.__cle = value

    @property
    def mdp_chiffrer(self):
        return self.__mdp_chiffrer

    @mdp_chiffrer.setter
    def mdp_chiffrer(self, value):
        self.__mdp_chiffrer = value

    def __str__(self) -> str:
        return f"mdp: {self.__mdp}\nsel: {self.__sel}\ncle: {self.__cle}\nmdp_chiffrer: {self.__mdp_chiffrer}"