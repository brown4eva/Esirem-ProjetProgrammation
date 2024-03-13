# Define the Joueur class
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.nombre_de_victoires = 0

    def enregistrer_victoire(self):
        self.nombre_de_victoires += 1

    def __str__(self):
        return f"{self.nom} a {self.nombre_de_victoires} victoire(s)."

# Create a Joueur instance
joueur = Joueur("Team IE")

# Print initial status (should show 0 victories)
print(joueur)

# Simulate a victory and print the updated status
joueur.enregistrer_victoire()
print(joueur)

# Simulate another victory and print the updated status again
joueur.enregistrer_victoire()
print(joueur)
