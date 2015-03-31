# coding=UTF-8
from django.db import models
from django import forms
from datetime import datetime
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.contrib import admin
from datetime import datetime

from django.contrib.auth.models import User

class FicheAdmin(admin.ModelAdmin):
	list_display = ['nom', 'prenom','date_inscription','mobile']
		
class Fiche(models.Model):
	def __unicode__(self):
		return self.nom+' '+self.prenom

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

	dispo_06_06_au_13_06 = models.BooleanField("Disponible du 06-06 au 13-06")
	dispo_13_06_au_20_06 = models.BooleanField("Disponible du 13-06 au 20-06")
	dispo_20_06_au_27_06 = models.BooleanField("Disponible du 20-06 au 27-06")
	dispo_27_06_au_04_07 = models.BooleanField("Disponible du 27-06 au 04-07")
	dispo_04_07_au_11_07 = models.BooleanField("Disponible du 04-07 au 11-07")
	dispo_11_07_au_18_07 = models.BooleanField("Disponible du 11-07 au 18-07")
	dispo_18_07_au_25_07 = models.BooleanField("Disponible du 18-07 au 25-07")
	dispo_25_07_au_01_08 = models.BooleanField("Disponible du 25-07 au 01-08")
	dispo_01_08_au_08_08 = models.BooleanField("Disponible du 01-08 au 08-08")
	dispo_08_08_au_15_08 = models.BooleanField("Disponible du 08-08 au 15-08")
	dispo_15_08_au_22_08 = models.BooleanField("Disponible du 15-08 au 22-08")
	dispo_22_08_au_29_08 = models.BooleanField("Disponible du 22-08 au 29-08")
	dispo_29_08_au_05_09 = models.BooleanField("Disponible du 29_08 au 05-09 (centre de sauvegarde uniquement)")
	dispo_05_09_au_12_09 = models.BooleanField("Disponible du 05-09 au 12-09 (centre de sauvegarde uniquement)")
	dispo_12_09_au_19_09 = models.BooleanField("Disponible du 12-09 au 19-09 (centre de sauvegarde uniquement)")
	dispo_19_09_au_26_09 = models.BooleanField("Disponible du 19-09 au 26-09 (centre de sauvegarde uniquement)")
	dispo_26_09_au_03_10 = models.BooleanField("Disponible du 26-09 au 03-10 (centre de sauvegarde uniquement)")
	dispo_03_10_au_10_10 = models.BooleanField("Disponible du 03-10 au 10-10 (centre de sauvegarde uniquement)")
	dispo_10_10_au_17_10 = models.BooleanField("Disponible du 10-10 au 17-10 (centre de sauvegarde uniquement)")
	dispo_17_10_au_24_10 = models.BooleanField("Disponible du 17-10 au 24-10 (centre de sauvegarde uniquement)")
	dispo_24_10_au_31_10 = models.BooleanField("Disponible du 24-10 au 31-10 (centre de sauvegarde uniquement)")

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

def envoyer_mail_confirmation(modeladmin, request, queryset):
	for candidat in queryset:
		u = User(candidat.fiche.user_id)
		candidat.date_dernier_envoi_mail = datetime.now()
		candidat.save()
		send_mail(u"Confirmation de participation au bénévolat phoques",u"""Confirmation de participation au bénévolat pour les phoques

Vous avez été sélectionné(e) pour participer aux cessions de bénévolat pour les phoques qui se tiendront au cours de l'été 2015.

Merci de confirmer votre votre participation Pour cela, veuillez:
  - accepter le règlement intérieur,
  - vous acquitter des frais de gestion de 50€ par personne,
  - vous acquitter des frais de participation à l'hébergement et à la nourriture de 20€ par semaine,
  - vérifier que vous êtes à jour de votre adhésion 2015, si ce n'est pas le cas: adhérez en ligne ! (http://dons.picardie-nature.org/)

Pour ce faire rendez-vous à cette adresse http://benevoles.bds.picardie-nature.org/confirmation, et identifiez-vous.

Rappels:
  - Tous les candidats ayant confirmé seront considérés comme bénévoles pour les phoques dès le 8 avril minuit. Dans le cas contraire, les places seront proposées à d'autres candidats.
  - Les candidats sélectionnés qui ne souhaiteraient ou ne pourraient plus assurer leur période de bénévolat sont priés de prévenir de leur désistement au plus tôt.
    - En cas de désistement signalé avant le 1er mai, le chèque de caution vous sera retourné. Passé cette date, ce dernier sera encaissé,
    - En cas de désistement les frais de gestion ne seront pas remboursés,
    - En cas de désistement, la participation aux frais d'hébergement et de nourriture de 20€ par semaine vous seront remboursés.
""", 'support-vbds@picardie-nature.org', [candidat.fiche.email])


envoyer_mail_confirmation.short_description = "Envoyer mails confirmation inscription"


class CandidatRetenuAdmin(admin.ModelAdmin):
	list_display = ['fiche','frais_hebergement','frais_inscription','date_validation','date_dernier_envoi_mail','date_confirmation','date_reception_paiement']
	list_filter = ['annulation','adhesion']
	readonly_fields = ('date_validation','date_dernier_envoi_mail','date_confirmation')
	actions = [envoyer_mail_confirmation]
	pass

class CandidatRetenu(models.Model):
	CHOIX_MISSION = (
		('SOINS', 'Centre de soins'),
		('SURV', 'Surveillance des phoques')
	)

	fiche = models.ForeignKey(Fiche, unique=True)	
	retenu_06_06_au_13_06 = models.CharField("Présent du 06-06 au 13-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_13_06_au_20_06 = models.CharField("Présent du 13-06 au 20-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_20_06_au_27_06 = models.CharField("Présent du 20-06 au 27-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_27_06_au_04_07 = models.CharField("Présent du 27-06 au 04-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_04_07_au_11_07 = models.CharField("Présent du 04-07 au 11-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_11_07_au_18_07 = models.CharField("Présent du 11-07 au 18-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_18_07_au_25_07 = models.CharField("Présent du 18-07 au 25-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_25_07_au_01_08 = models.CharField("Présent du 25-07 au 01-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_01_08_au_08_08 = models.CharField("Présent du 01-08 au 08-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_08_08_au_15_08 = models.CharField("Présent du 08-08 au 15-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_15_08_au_22_08 = models.CharField("Présent du 15-08 au 22-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_22_08_au_29_08 = models.CharField("Présent du 22-08 au 29-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_29_08_au_05_09 = models.CharField("Présent du 29-08 au 05-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_05_09_au_12_09 = models.CharField("Présent du 05-09 au 12-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_12_09_au_19_09 = models.CharField("Présent du 12-09 au 19-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_19_09_au_26_09 = models.CharField("Présent du 19-09 au 26-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	
	retenu_26_09_au_03_10 = models.CharField("Présent du 26-10 au 03-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_03_10_au_10_10 = models.CharField("Présent du 03-10 au 10-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_10_10_au_17_10 = models.CharField("Présent du 10-10 au 17-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_17_10_au_24_10 = models.CharField("Présent du 17-10 au 24-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_24_10_au_31_10 = models.CharField("Présent du 24-10 au 31-10", max_length=5, choices=CHOIX_MISSION, blank=True)

	date_validation = models.DateTimeField("Date validation", blank=True,null=True)
	date_confirmation = models.DateTimeField("Date confirmation", blank=True,null=True)
	frais_inscription = models.IntegerField('Frais inscription', default=50) # 50 €
	frais_hebergement = models.IntegerField('Frais hébergement, nourriture') # n_semaine * 20€
	date_dernier_envoi_mail = models.DateTimeField("Date envoi demande paiement", blank=True,null=True)
	date_reception_paiement = models.DateTimeField("Date réception paiement", blank=True,null=True)
	annulation = models.BooleanField("Inscription annulée")
	adhesion = models.BooleanField("Adhésion confirmée")

def calcul_frais(sender, instance, **kwargs):
	semaines = ['retenu_06_06_au_13_06', 'retenu_13_06_au_20_06', 'retenu_20_06_au_27_06', 'retenu_27_06_au_04_07', 'retenu_04_07_au_11_07', 'retenu_11_07_au_18_07', 'retenu_18_07_au_25_07', 'retenu_25_07_au_01_08', 'retenu_01_08_au_08_08', 'retenu_08_08_au_15_08', 'retenu_15_08_au_22_08', 'retenu_22_08_au_29_08', 'retenu_29_08_au_05_09', 'retenu_05_09_au_12_09', 'retenu_12_09_au_19_09', 'retenu_19_09_au_26_09','retenu_26_09_au_03_10','retenu_03_10_au_10_10','retenu_10_10_au_17_10','retenu_17_10_au_24_10','retenu_24_10_au_31_10']
	instance.frais_inscription = 50
	instance.frais_hebergement = 0
	cout_semaine = 20

	for semaine in semaines:
		if getattr(instance, semaine):
			instance.frais_hebergement += cout_semaine
	
	if not instance.date_validation:
		instance.date_validation = datetime.now()
		

pre_save.connect(calcul_frais, sender=CandidatRetenu)

class FicheForm(forms.ModelForm):
	class Meta:
		model = Fiche

class UploadForm(forms.Form):
	fic = forms.FileField()
