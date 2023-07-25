from datetime import datetime
from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/check-chapter")
def check_chapter():
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
    url_site_web = "http://www.volonte-d.com/"
    chapitre_recherche = os.environ.get('env_var', 'Valeur par default')

    verifier_disponibilite_chapitre(url_site_web, chapitre_recherche)

@app.route("/volume")
def volume():
    # Current datetime
    now = datetime.datetime.now()

    # Écriture dans un fichier en mode append =('a')
    # si le fichier n'existe pas il est créé
    with open('file.txt', 'a') as f: 
        f.write('Thank you.\n')

if __name__ == "__main__":
    app.run(host="192.168.11.10", port=8000)