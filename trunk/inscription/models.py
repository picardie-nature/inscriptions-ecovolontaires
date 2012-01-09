# coding=UTF-8

from django.db import models
from django import forms
from datetime import datetime

from django.contrib import admin
class FicheAdmin(admin.ModelAdmin):
	list_display = ['nom', 'prenom','date_inscription']

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

	participation_csfs = models.BooleanField("Centre de sauvegarde")
	participation_protection = models.BooleanField("Protection des phoques")

	dispo_02_06_au_09_06 = models.BooleanField("Disponible du 02-06 au 09-06")
	dispo_09_06_au_16_06 = models.BooleanField("Disponible du 09-06 au 16-06")
	dispo_16_06_au_23_06 = models.BooleanField("Disponible du 16-06 au 23-06")
	dispo_23_06_au_30_06 = models.BooleanField("Disponible du 23-06 au 30-06")
	dispo_30_06_au_07_07 = models.BooleanField("Disponible du 30-06 au 07-07")
	dispo_07_07_au_14_07 = models.BooleanField("Disponible du 07-07 au 14-07")
	dispo_14_07_au_21_07 = models.BooleanField("Disponible du 14-07 au 21-07")
	dispo_21_07_au_28_07 = models.BooleanField("Disponible du 21-07 au 28-07")
	dispo_28_07_au_04_08 = models.BooleanField("Disponible du 28-07 au 04-08")
	dispo_04_08_au_11_08 = models.BooleanField("Disponible du 04-08 au 11-08")
	dispo_11_08_au_18_08 = models.BooleanField("Disponible du 11-08 au 18-08")
	dispo_18_08_au_25_08 = models.BooleanField("Disponible du 18-08 au 25-08")
	dispo_25_08_au_01_09 = models.BooleanField("Disponible du 25-08 au 01-09")
	dispo_01_09_au_08_09 = models.BooleanField("Disponible du 01-09 au 08-09")
	dispo_08_09_au_15_09 = models.BooleanField("Disponible du 08-09 au 15-09")
	dispo_15_09_au_22_09 = models.BooleanField("Disponible du 15-09 au 22-09")
	dispo_22_09_au_29_09 = models.BooleanField("Disponible du 22-09 au 29-09")
	dispo_29_09_au_06_10 = models.BooleanField("Disponible du 29-09 au 06-10")
	dispo_06_10_au_13_10 = models.BooleanField("Disponible du 06-10 au 13-10")
	dispo_13_10_au_20_10 = models.BooleanField("Disponible du 13-10 au 20-10")
	dispo_20_10_au_27_10 = models.BooleanField("Disponible du 20-10 au 27-10")
	dispo_27_10_au_03_11 = models.BooleanField("Disponible du 27-10 au 03-11")

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
	ancien_soigneur = models.BooleanField("Déjà été soigneur")
	dispo_soins_nb_semaine = models.IntegerField("Nombre de semaines", blank=True)
	veterinaire = models.BooleanField('Vétérinaire')
	auxiliaire_sante = models.BooleanField('Auxiliaire de santé animale')
	assistant_veterinaire = models.BooleanField('Assistant vétérinaire')
	soigneur_animalier = models.BooleanField('Soigneur animalier')
	autre_diplome_soins = models.CharField('Autre', max_length=200, blank=True)
	user_id = models.IntegerField("Id utilisateur", blank=True)

	class Meta:
		ordering = ['nom','prenom']

class FicheForm(forms.ModelForm):
	class Meta:
		model = Fiche

class UploadForm(forms.Form):
	fic = forms.FileField()

