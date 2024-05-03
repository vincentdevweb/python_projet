

from src.dao.utilisateur_dao import UtilisateurDao
from src.models.utilisateur import Utilisateur
from src.dao.compte_dao import CompteDao
from src.models.compte import Compte


# working!!!!---

# dao = UtilisateurDao()

# new_utilisateur = Utilisateur(0,"Doe","John","John@gmail.com","H","12345","1234")

# dao.start()
# dao.save(new_utilisateur)
# dao.commit()

# utilisateurs = dao.find_all()

# for utilisateur_tuple in utilisateurs:
#     utilisateur = Utilisateur(*utilisateur_tuple)
#     if utilisateur.prenom == "John":
#         utilisateur.prenom = "Johny"
#         dao.update(utilisateur)   
#         dao.commit()

# utilisateurs = dao.find_all()

# for utilisateur in utilisateurs:
#     print(utilisateur)

# dao.close()

# working!!!!---


# recherche dans utilisateurs les doublons et les supprimes avec la methode delete
# faire un dictionary key value unique

# utilisateurs_unique = {}

# for utilisateur in utilisateurs:
#     if utilisateur.nom not in utilisateurs_unique:
#         utilisateurs_unique[utilisateur.nom] = utilisateur
#     else:
#         dao.delete(utilisateur)

# working!!!!---
# p1 = Utilisateur(*dao.find_by_id(2))
# print(p1)
# dao.delete(p1)
# dao.commit()
# dao.close()
# working!!!!---

# working!!!!---
dao = CompteDao()
new_compte = Compte(3,"125568","54498849",2)
dao.start()
dao.save(new_compte)
dao.commit()

# for compte_tuples in dao.find_all():
#     compte = Compte(*compte_tuples)
#     print(compte)

# new_compte.sel = "voici du sel j'ai pas de poivre"
# dao.update(new_compte)
# dao.commit()

# print(*dao.find_by_id(3))

# dao.delete(Compte(*dao.find_by_id(2)))
# dao.commit()

dao.close()

