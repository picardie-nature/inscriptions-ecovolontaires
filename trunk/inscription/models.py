# coding=UTF-8

from django.db import models
from django import forms
from datetime import datetime

class Fiche(models.Model):
	CHOIX_SEXE = (
		('H', 'Homme'),
		('F', 'Femme')
	)
	CHOIX_POSTE = (
		('ANI', 'Animateur'),
		('SUR', 'Surveillant'),
		('SAN', 'Surveillant et animateur')
	)
	CHOIX_LOC = (
		('B_A', 'Baie d\'Authie'),
		('B_S', 'Baie de Somme'),
		('BSA', 'Baie de Somme et d\'Authie')
	)
	CHOIX_PRATIQUE_KAYAK = (
		('J', 'Jaune'),
		('V', 'Vert'),
		('B', 'Bleu'),
		('R', 'Rouge'),
		('N', 'Noir')
	)
	date_inscription = models.DateTimeField("Date d'inscription", default=datetime.now, blank=True)
	nom = models.CharField("Nom", max_length=200)
	prenom = models.CharField("Prénom", max_length=200)
	sexe = models.CharField("Sexe", max_length=1, choices=CHOIX_SEXE)
	age = models.IntegerField("Age", max_length=2)
	email = models.EmailField("Adresse électronique")
	mobile = models.CharField("Numéro de mobile", max_length=10)
	dispo_11_06_au_18_06 = models.BooleanField("Disponible du 11-06 au 18-06")
	dispo_18_06_au_25_06 = models.BooleanField("Disponible du 18-06 au 25-06")
	dispo_25_06_au_02_07 = models.BooleanField("Disponible du 25-06 au 02-07")
	dispo_02_07_au_09_07 = models.BooleanField("Disponible du 02-07 au 09-07")
	dispo_09_07_au_16_07 = models.BooleanField("Disponible du 09-07 au 16-07")
	dispo_16_07_au_23_07 = models.BooleanField("Disponible du 16-07 au 23-07")
	dispo_23_07_au_30_07 = models.BooleanField("Disponible du 23-07 au 30-07")
	dispo_30_07_au_06_08 = models.BooleanField("Disponible du 30-07 au 06-08")
	dispo_06_08_au_13_08 = models.BooleanField("Disponible du 06-08 au 13-08")
	dispo_13_08_au_20_08 = models.BooleanField("Disponible du 13-08 au 20-08")
	dispo_20_08_au_27_08 = models.BooleanField("Disponible du 20-08 au 27-08")
	dispo_27_08_au_03_09 = models.BooleanField("Disponible du 27-08 au 03-09")
	duree_n_semaine = models.IntegerField("Nombre de semaines (à partir de 2)", max_length=2, blank=True)
	ancien_surveillant = models.BooleanField("Déjà été surveillant")
	poste = models.CharField("Poste souhaité", max_length=3, choices=CHOIX_POSTE, blank=True)
	loc_baie = models.CharField("Localisation des missions", max_length=3, choices=CHOIX_LOC, blank=True)
	adherent_autre_asso = models.CharField("Adhérent dans d'autres associations ?", max_length=200, blank=True)
	permis_b = models.BooleanField("Permis B")
	vehicule = models.BooleanField("Véhicule")
	permis_mer = models.BooleanField("Permis Mer")
	navig_regulierement = models.BooleanField("Navigue régulièrement")
	kayak_mer = models.BooleanField("Pratique du Kayak en mer")
	kayak_niveau = models.CharField("Niveau de pratique kayak", choices=CHOIX_PRATIQUE_KAYAK, max_length=20, blank=True)
	afps = models.BooleanField("AFPS")
	psc1 = models.BooleanField("PSC1")
	sauveteur_travail = models.BooleanField("Sauveteur secouriste du travail")
	autre = models.CharField("Autre formation secouriste", max_length=200, blank=True)
	bafa = models.BooleanField("BAFA")
	bapaat = models.BooleanField("BAPAAT")
	bpjeps = models.BooleanField("BPJEPS")
	guide_nature = models.BooleanField("Guide nature")
	btps_gpn_opt_anim = models.BooleanField("BTPS GPN option Animation")
	autre_anim = models.CharField("Autre formation animation", max_length=200, blank=True)
	mam_marins = models.BooleanField("Mammifères marins")
	oiseaux = models.BooleanField("Avifaune")
	autre_competence_naturaliste = models.CharField("Autres compétences naturalistes", max_length=200, blank=True)
	dispo_soins_28_05_au_04_06 = models.BooleanField('Disponible soins 28-05 au 04-06')
	dispo_soins_04_06_au_11_06 = models.BooleanField('Disponible soins 04-06 au 11-06')
	dispo_soins_11_06_au_18_06 = models.BooleanField('Disponible soins 11-06 au 18-06')
	dispo_soins_18_06_au_25_06 = models.BooleanField('Disponible soins 18-06 au 25-06')
	dispo_soins_25_06_au_02_07 = models.BooleanField('Disponible soins 25-06 au 02-07')
	dispo_soins_02_07_au_09_07 = models.BooleanField('Disponible soins 02-07 au 09-07')
	dispo_soins_09_07_au_16_07 = models.BooleanField('Disponible soins 09-07 au 16-07')
	dispo_soins_16_07_au_23_07 = models.BooleanField('Disponible soins 16-07 au 23-07')
	dispo_soins_23_07_au_30_07 = models.BooleanField('Disponible soins 23-07 au 30-07')
	dispo_soins_30_07_au_06_08 = models.BooleanField('Disponible soins 30-07 au 06-08')
	dispo_soins_06_08_au_13_08 = models.BooleanField('Disponible soins 06-08 au 13-08')
	dispo_soins_13_08_au_20_08 = models.BooleanField('Disponible soins 13-08 au 20-08')
	dispo_soins_20_08_au_27_08 = models.BooleanField('Disponible soins 20-08 au 27-08')
	dispo_soins_27_08_au_03_09 = models.BooleanField('Disponible soins 27-08 au 03-09')
	dispo_soins_03_09_au_10_09 = models.BooleanField('Disponible soins 03-09 au 10-09')
	dispo_soins_10_09_au_17_09 = models.BooleanField('Disponible soins 10-09 au 17-09')
	dispo_soins_17_09_au_24_09 = models.BooleanField('Disponible soins 17-09 au 24-09')
	dispo_soins_24_09_au_01_10 = models.BooleanField('Disponible soins 24-09 au 01-10')
	dispo_soins_01_10_au_08_10 = models.BooleanField('Disponible soins 01-10 au 08-10')
	dispo_soins_08_10_au_15_10 = models.BooleanField('Disponible soins 08-10 au 15-10')
	dispo_soins_15_10_au_22_10 = models.BooleanField('Disponible soins 15-10 au 22-10')
	dispo_soins_22_10_au_29_10 = models.BooleanField('Disponible soins 22-10 au 29-10')
	dispo_soins_29_10_au_05_11 = models.BooleanField('Disponible soins 29-10 au 05-11')
	dispo_soins_05_11_au_12_11 = models.BooleanField('Disponible soins 05-11 au 12-11')
	dispo_soins_12_11_au_19_11 = models.BooleanField('Disponible soins 12-11 au 19-11')
	ancien_soigneur = models.BooleanField("Déjà été soigneur")
	dispo_soins_nb_semaine = models.IntegerField("Nombre de semaines", blank=True)
	veterinaire = models.BooleanField('Vétérinaire')
	auxiliaire_sante = models.BooleanField('Auxiliaire de santé animale')
	assistant_veterinaire = models.BooleanField('Assistant vétérinaire')
	soigneur_animalier = models.BooleanField('Soigneur animalier')
	autre_diplome_soins = models.CharField('Autre', max_length=200, blank=True)
	user_id = models.IntegerField("Id utilisateur", blank=True)

class FicheForm(forms.ModelForm):
	class Meta:
		model = Fiche

class UploadForm(forms.Form):
	fic = forms.FileField()



