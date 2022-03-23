#On crée la class utilisateurs dans laquelle l'IMC du client sera calculer et ses données seront stocker dans un fichier texte.
class Utilisateur:

    def __init__(self,age,prenom,nom,poids,taille):
        self.age = str(age)
        self.prenom = str(prenom)
        self.nom = str(nom)
        self.poids = str(poids)
        self.taille = str(taille)

#On crée la fonction "IMC" qui calculera IMC en fonction des paramètres définit auparavant.
    def IMC(self):
        IMC = int(self.poids)//(float(self.taille)**2)
        stat = 0
        if IMC > 40:
            stat = 0
            print("\t","Votre IMC :",IMC,"\n","\t","Vous êtes en état d'obésité morbide")
        if IMC > 35 and IMC <= 40:
            stat = 1
            print ("\t","Votre IMC :",IMC,"\n","\t","Vous êtes en état d'obésité sévere")
        if IMC > 30 and IMC <= 35:
            stat = 2
            print ("\t","Votre IMC :",IMC,"\n","\t","Vous êtes en état d'obésité modérée")
        if IMC > 25 and IMC <= 30:
            stat = 3
            print ("\t","Votre IMC :",IMC,"\n","\t","Vous êtes en état de surpoids")
        if IMC > 18.5 and IMC <= 25:
            stat = 4
            print ("\t","Votre IMC :",IMC,"\n","\t","Vous êtes en état de corpulence normale")
        if IMC > 16.5 and IMC <= 18.5:
            stat = 5
            print ("\t","Votre IMC :",IMC,"\n","\t","Vous êtes en état de maigreur")
        if IMC < 16.5:
            stat = 6
            print ("\t","Votre IMC :",IMC,"\n","\t","Vous êtes en état de famine")
        return [IMC, stat]

#La fonction "txt" va ici nous servir a créer un ficher texte dans lequel sera afficher l'IMC et l'état du client.

    def txt(self):
        stat0 = "Obésité morbide"
        stat1 = "Obésité sévere"
        stat2 = "Obésité modérée"
        stat3 = "Surpoids"
        stat4 = "Corpulence normale"
        stat5 = "Maigreur"
        stat6 = "Famine"
        Stat = (stat0,stat1,stat2,stat3,stat4,stat5,stat6)
        lines = ["IMC de l'utilisateur : "+str(self.IMC()[0]),"Etat de l'utilisateur : "+Stat[self.IMC()[1]]]
        with open(r'D:\Projet\Données Utilisateur.txt', 'w+') as f:
            for line in lines:
                f.write(line)
                f.write('\n')

#On définit les états des clients qui seront renvoyés dans le fichier texte
stat0 = ["Obésité morbide"]
stat1 = ["Obésité sévere"]
stat2 = ["Obésité modérée"]
stat3 = ["Surpoids"]
stat4 = ["Corpulence normale"]
stat5 = ["Maigreur"]
stat6 = ["Famine"]
Stat = ([stat0],[stat1],[stat2],[stat3],[stat4],[stat5],[stat6])

#Exemple d'utilisateurs
U1 = Utilisateur(17,"Wilem","Akli",93,1.82)
U2 = Utilisateur(17,"Ali","Hussain",70,1.75)
U3 = Utilisateur(18,"Kyz","Barbar",54,1.70)
U4 = Utilisateur(17,"Soulé","Koudil",84,1.80)
U5 = Utilisateur(17,"Alexandre","Mestre",63,1.80)
U6 = Utilisateur(17,"Mamadou","Grs",70,1.86)
U7 = Utilisateur(17,"Badrou","Moussa",59,1.80)

class Programme Sportif:
    def __init__(self,IMC,)

