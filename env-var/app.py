import requests
import os

def verifier_disponibilite_chapitre(url_site_web, chapitre):
    try:
        response = requests.get(url_site_web)
        response.raise_for_status()  
        if f"chapitre {chapitre}" in response.text.lower():
            print(f"Le chapitre {chapitre} est disponible sur le site {url_site_web}.")
        else:
            print(f"Le chapitre {chapitre} n'est pas disponible sur le site {url_site_web}.")
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requete :", e)

# Utilisation du script
if __name__ == "__main__":
    url_site_web = "http://www.volonte-d.com/"
    chapitre_recherche = os.environ.get('env_var', 'Valeur par default')

    verifier_disponibilite_chapitre(url_site_web, chapitre_recherche)
