from test import showErrors
nom=""
prenom=""
age=0

while True:
	#Variable choix
	a = "1.Tapez votre nom\n"
	b = "2.Tapez votre prenom\n"
	c = "3.Tapez votre âge\n"
	d = "4.Afficher vos données\n"
	e = "5.Quitter\n"

	print(a, b, c, d)
	"\n"

	#Entrez choix
	choix = int(input("Tapez votre choix :"))
	if(choix==5):
		print("QUITTER")
		break

	else:
		if(choix==1):
			nom=input("Entrez votre nom :")

		elif(choix==2):
			prenom=input("Entrez votre prenom :")

		elif(choix==3):
			age=int(input("Entrez votre âge :"))

		elif(choix==4):
			erreurs=[]

			if(nom==""):
				erreurs.append("nom")

			if(prenom==""):
				erreurs.append("prenom")

			if(age==0):
				erreurs.append("age")

			if(erreurs):
				print("Les champs vides sont :")
				showErrors(erreurs)
				

			else:
				infos = {"nom": nom, "prenom" : prenom, "age" : age}
				print("Voici vos données :", infos)
