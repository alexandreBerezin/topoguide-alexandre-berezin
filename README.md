# topoguide-alexandre-berezin

# Description

Nous allons réaliser une application Topoguide dont le but est de gérer un journal public de randonnées. Les utilisateurs peuvent consulter des itinéraires de randonnée et partager avec les autres utilisateurs l'expérience vécue lors d'une sortie correspondant à l'un de ces itinéraires : conditions météo, durée réelle, etc. À un itinéraire donné correspondent donc 0, 1 ou plusieurs sorties, chaque sortie étant enregistrée par un utilisateur authentifié.

# Objectif : 
1. Une page d'authentification
    basique //OK 


2. Une page de liste des itinéraires
    basique // OK 
    compléter le modèles de itinéraires
    afficher la page sous forme de tableau 


3. Une page de liste des sorties partagées pour un itinéraire particulier
    modèle d'une sortie //OK
    basique //OK

4. Visualisation d'une sortie
    basique //OK

5. Saisie d'une sortie
    basique // OK

6. Modification d'une sortie (uniquement par l'utilisateur qui a saisi la sortie)
    basique //OK 


# modèle itinéaraire  
- le titre
- le point de départ
- la description
- l'altitude de départ
- l'altitude min
- l'altitude max
- le dénivelé positif cumulé
- le dénivelé négatif cumulé
- la durée estimée (en heures)
- la difficulté estimée (de 1 à 5)

# modèle sortie 
- l'utilisateur qui a enregistré la sortie
- l'itinéraire correspondant dans le topoguide
- la date de la sortie
- la durée réelle (en heures)
- le nombre de personnes ayant participé à la sortie
- l'expérience du groupe (à choisir dans une liste tous débutants, tous expérimentés, mixte)
- la météo (à choisir dans une liste bonne, moyenne, mauvaise)
- la difficulté ressentie (de 1 à 5)


# Navigation 
- boutons de navigation 
    se connecter /deconnecter // OK
- boutons de connection