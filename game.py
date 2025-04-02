import msvcrt
import time
import threading


# Variable
compteur = 0
touche = ""
amélio = 1
achat_ajoute1 = 0
achat_ajoute2 = 0
gain_par_seconde = 0

# Dictionnaire des améliorations
ameliorations = {
    "Ajoute 1 a tes clicks" : 1,
}


#Boutique d'amélioration

def boutique(compteur, amélio, achat_ajoute1, achat_ajoute2, gain_par_seconde):
    print("\nBienvenue à la boutique !")
    print(f"Tu as {compteur} cookies.")    
    print(f"1. Amélioration de vitesse (+1) : {(achat_ajoute1 +1) *50} cookies (Acheté {achat_ajoute1} fois)")
    print(f"2. Amélioration de gain automatique : {(achat_ajoute2 + 1) * 200} cookies (Acheté {achat_ajoute2} fois)")
    print("Appuie sur 'q' pour quitter la boutique.")

    while True:
        choix = msvcrt.getch().decode("utf-8")
        if choix == "1" and compteur >= 50:
            amélio += 1
            compteur -= 50
            achat_ajoute1 += 1
            print("Amélioration de vitesse achetée ! 🚀")
        elif choix == "2" and compteur >= 200:
            gain_par_seconde += 0.5
            def auto_gain():
                global compteur
                while True:
                    compteur += gain_par_seconde
                    time.sleep(1)

                    if not hasattr(boutique, "thread_started"):
                        thread = threading.Thread(target=auto_gain, daemon=True)
                        thread.start()
                        boutique.thread_started = True
                        
            thread = threading.Thread(target=auto_gain, daemon=True)
            thread.start()
            compteur -= 200
            achat_ajoute2 += 1

            
            print(f"Bravo ! Tu es a {gain_par_seconde} cookies/secondes ✨")
        elif choix == "q":
            print("Merci pour ta visite !")
            break
        else:
            print("Option invalide ou pas assez de cookies.")
    return compteur, amélio, achat_ajoute1, achat_ajoute2, gain_par_seconde


print("Appuie sur 'Espace' pour miner des cookies. \nAppuie sur 'b' pour accéder à la boutique.\nAppuie sur 'q' pour quitter.")

while touche != "q":
    touche = msvcrt.getch().decode("utf-8")

    if touche == " ":
        compteur += amélio
        print(f"Cookies : {compteur}")

    if touche == "b":
        compteur, amélio, achat_ajoute1, achat_ajoute2, gain_par_seconde  = boutique(compteur,amélio,achat_ajoute1,achat_ajoute2,gain_par_seconde)
print("Fin du programme.")