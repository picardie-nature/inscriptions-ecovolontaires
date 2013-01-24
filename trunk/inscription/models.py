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
	CHOIX_TSHIRT = (
		('S','Taille S'),
		('M','Taille M'),
		('L','Taille L'),
		('XL','Taille XL'),
		('XXL', 'Taille XXL')
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

	dispo_08_06_au_15_06 = models.BooleanField("Disponible du 08-06 au 15-06")
	dispo_15_06_au_22_06 = models.BooleanField("Disponible du 15-06 au 22-06")
	dispo_22_06_au_29_06 = models.BooleanField("Disponible du 22-06 au 29-06")
	dispo_29_06_au_06_07 = models.BooleanField("Disponible du 29-06 au 06-06")
	dispo_06_07_au_13_07 = models.BooleanField("Disponible du 06-07 au 13-07")
	dispo_13_07_au_20_07 = models.BooleanField("Disponible du 13-07 au 20-07")
	dispo_20_07_au_27_07 = models.BooleanField("Disponible du 20-07 au 27-07")
	dispo_27_07_au_03_08 = models.BooleanField("Disponible du 27-07 au 03-07")
	dispo_03_08_au_10_08 = models.BooleanField("Disponible du 03-08 au 10-08")
	dispo_10_08_au_17_08 = models.BooleanField("Disponible du 10-08 au 17-08")
	dispo_17_08_au_24_08 = models.BooleanField("Disponible du 17-08 au 24-08")
	dispo_24_08_au_31_08 = models.BooleanField("Disponible du 24-08 au 31-08")
	dispo_31_08_au_07_09 = models.BooleanField("Disponible du 31-08 au 07-09")
	dispo_07_09_au_14_09 = models.BooleanField("Disponible du 07-09 au 14-09")
	dispo_14_09_au_21_09 = models.BooleanField("Disponible du 14-09 au 21-09")
	dispo_21_09_au_28_09 = models.BooleanField("Disponible du 21-09 au 28-09")
	dispo_28_09_au_05_10 = models.BooleanField("Disponible du 28-09 au 05-10 (centre de sauvegarde uniquement)")
	dispo_05_10_au_12_10 = models.BooleanField("Disponible du 05-10 au 12-10 (centre de sauvegarde uniquement)")
	dispo_12_10_au_19_10 = models.BooleanField("Disponible du 12-10 au 19-10 (centre de sauvegarde uniquement)")
	dispo_19_10_au_26_10 = models.BooleanField("Disponible du 19-10 au 26-10 (centre de sauvegarde uniquement)")
	dispo_26_10_au_02_11 = models.BooleanField("Disponible du 26-10 au 02-11 (centre de sauvegarde uniquement)")

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
	tshirt = models.CharField("T-Shirt", max_length=3, choices=CHOIX_TSHIRT, blank=True)

	class Meta:
		ordering = ['nom','prenom']

class FicheForm(forms.ModelForm):
	class Meta:
		model = Fiche

class UploadForm(forms.Form):
	fic = forms.FileField()

