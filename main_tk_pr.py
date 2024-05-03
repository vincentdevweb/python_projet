from tkinter import Button, Entry, Label, Tk, messagebox, ttk
from src.dao.utilisateur_dao import UtilisateurDao
from src.models.utilisateur import Utilisateur
from src.dao.compte_dao import CompteDao
from src.models.compte import Compte
from utils.custom_crypt import CustomCrypt
from src.mail.mail_inscript import mail_inscription

def update_utilisateur():
    pass

def delete_utilisateur(id_utilisateur:int ) -> None:
    dao_utilisateur = UtilisateurDao()
    dao_utilisateur.delete(id_utilisateur)
    dao_utilisateur.commit()
    dao_utilisateur.close()
    messagebox.showinfo("Suppression", "Utilisateur supprimé vous pouvez quitter la fenetre courante")

def new_frame():
    new_window = Tk()
    new_window.title("Lecture Utilisateur")
    new_window.geometry("400x400")
    new_window.config(bg="#000000")
    return new_window

def inscription_bdd_compte(mdp: str, new_utilisateur:Utilisateur) -> str:
    
    dao_compte = CompteDao()
    crypt = CustomCrypt(mdp)
    
    print(new_utilisateur.id)
    new_compte = Compte(0,'|'.join(str(element) for element in crypt.cle),crypt.sel,new_utilisateur.id)
    dao_compte.start()
    dao_compte.save(new_compte)
    dao_compte.commit()
    dao_compte.close()
    return crypt.mdp_chiffrer

def inscription_bdd_utilisateur(nom:str, email:str, mdp:str) -> None:
    dao_utilisateur = UtilisateurDao()
    
    # cree l'utilisateur avec mdp temporaire(On cherche a avoir l'id_u pour le mettre dans compte)
    new_utilisateur = Utilisateur(0,nom,"John",email,"H",mdp,"12457")
    dao_utilisateur.start()
    dao_utilisateur.save(new_utilisateur)
    dao_utilisateur.commit()
    recup_utilisateur = Utilisateur(*dao_utilisateur.find_by_email(email))
    print(recup_utilisateur)
    
    # ajoute les differentes cle de l'utilisateur a compte puis recupere le mdp chiffre
    mdp_encrypt = inscription_bdd_compte(mdp, recup_utilisateur)
    
    # met a jour l'utilisateur avec son mdp chiffer , on recuperer l'ancien mdp chiffrer
    recup_utilisateur.old_password = recup_utilisateur.password
    recup_utilisateur.password = mdp_encrypt
    dao_utilisateur.update(recup_utilisateur)
    dao_utilisateur.commit()
    
    # On ferme toutes les connexions l'inscription est terminer 
    dao_utilisateur.close()

def inscription_bdd(nom:str, email:str, mdp:str) -> None:
    try:
        inscription_bdd_utilisateur(nom,email,mdp)
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'inscription dans notre system : {e}")
        
def inscription():
    try:        
        nom = str(entry1.get())
        email = str(entry2.get())
        mdp = str(entry3.get())
        
        inscription_bdd(nom, email, mdp)
        
        messagebox.showinfo("Résultat", f"inscription reussi vous allez recevoir un mail d'incription")
        # clear entry
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'inscription : {e}")
        
def connexion():
    try:
        dao_utilisateur = UtilisateurDao()
        dao_compte = CompteDao()
        
        email = str(entry2.get())
        mdp = str(entry3.get())
        
        # encrypt le mot de passe recupere 
        crypt = CustomCrypt(mdp)
        
        # recupere les compte Utilisateur et Compte associated
        recup_utilisateur = Utilisateur(*dao_utilisateur.find_by_email(email))
        recup_compte = Compte(*dao_compte.find_by_utilisateur_id(recup_utilisateur.id))
        
        # On cherche a determiner si la clé crypter de l'utilisateur est equale a celle entrer par l'utilisateur
        cle = tuple(int(element) for element in recup_compte.cle.split('|'))
        mdp_sel = mdp + recup_compte.sel
        mdp_crypter = crypt.crypt(cle,mdp_sel)
        
        if(mdp_crypter == recup_utilisateur.password):
            messagebox.showinfo("Résultat", f"Connexion reussi vous allez recevoir un mail de connexion")
            frame2 = new_frame()
            labelf2_1 = Label(frame2, text="Nom")
            labelf2_2 = Label(frame2, text="E-Mail")
            labelf2_3 = Label(frame2, text="Change Mdp")
            labelf2_1.grid(row = 0 , column = 0)
            labelf2_2.grid(row = 1 , column = 0)
            labelf2_3.grid(row = 2 , column = 0)

            entryf2_1 = Entry(frame2)
            entryf2_1.insert(0,str(recup_utilisateur.name))
            
            entryf2_2 = Entry(frame2)
            entryf2_2.insert(0,str(recup_utilisateur.email))
            
            entryf2_3 = Entry(frame2)
            
            entryf2_1.grid(row = 0 , column =1)
            entryf2_2.grid(row = 1 , column =1)
            entryf2_3.grid(row = 2 , column =1)

            buttonf2_1 = Button(frame2, text="Update",command=update_utilisateur)
            buttonf2_1.grid(row = 4 , column = 1)
            buttonf2_2 = Button(frame2, text="Delete",command=lambda: delete_utilisateur(recup_utilisateur))
            buttonf2_2.grid(row = 5 , column = 1)
            buttonf2_3 = Button(frame2, text="Exit",command=frame2.destroy)
            buttonf2_3.grid(row = 6 , column = 1)
            
            frame2.mainloop()
        else:
            messagebox.showinfo("Résultat", f"Connexion échoué")

        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')

    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur pb serveur {e}")

frame = Tk()

width = 400
height = 400
frame.title('Programme inscriptions/connexion en faveur des chats de pallas')
frame.geometry(f"{width}x{height}")

label1 = Label(frame, text="Nom")
label2 = Label(frame, text="E-Mail")
label3 = Label(frame, text="Mdp")
label1.grid(row = 0 , column = 0)
label2.grid(row = 1 , column = 0)
label3.grid(row = 2 , column = 0)

entry1 = Entry(frame)
entry2 = Entry(frame)
entry3 = Entry(frame)
entry1.grid(row = 0 , column =1)
entry2.grid(row = 1 , column =1)
entry3.grid(row = 2 , column =1)

button1 = Button(frame, text="Inscription",command=inscription)
button1.grid(row = 4 , column = 1)
button2 = Button(frame, text="Connexion",command=connexion)
button2.grid(row = 5 , column = 1)

frame.mainloop()