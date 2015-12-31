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

	dispo_14_05_au_21_05 = models.BooleanField("Disponible du 14-05 au 21-05 (surveillance estivale uniquement)")
	dispo_21_05_au_28_05 = models.BooleanField("Disponible du 21-05 au 28-05 (surveillance estivale uniquement)")
	dispo_28_05_au_04_06 = models.BooleanField("Disponible du 28-05 au 04-06 (surveillance estivale uniquement)")
	dispo_04_06_au_11_06 = models.BooleanField("Disponible du 04-06 au 11-06")
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
	dispo_27_08_au_03_09 = models.BooleanField("Disponible du 27_08 au 03-09 (centre de sauvegarde uniquement)")
	dispo_03_09_au_10_09 = models.BooleanField("Disponible du 03-09 au 10-09 (centre de sauvegarde uniquement)")
	dispo_10_09_au_17_09 = models.BooleanField("Disponible du 10-09 au 17-09 (centre de sauvegarde uniquement)")
	dispo_17_09_au_24_09 = models.BooleanField("Disponible du 17-09 au 24-09 (centre de sauvegarde uniquement)")
	dispo_24_09_au_01_10 = models.BooleanField("Disponible du 24-09 au 01-10 (centre de sauvegarde uniquement)")
	dispo_01_10_au_08_10 = models.BooleanField("Disponible du 01-10 au 08-10 (centre de sauvegarde uniquement)")
	dispo_08_10_au_15_10 = models.BooleanField("Disponible du 08-10 au 15-10 (centre de sauvegarde uniquement)")
	dispo_15_10_au_22_10 = models.BooleanField("Disponible du 15-10 au 22-10 (centre de sauvegarde uniquement)")
	dispo_22_10_au_29_10 = models.BooleanField("Disponible du 22-10 au 29-10 (centre de sauvegarde uniquement)")

	duree_n_semaine = models.IntegerField("Nombre de semaines de participation (à partir de 2 pour la surveillance estivale et maximum 2 pour le centre de sauvegarde)", max_length=2, blank=True)
	ancien_surveillant = models.BooleanField("J'ai déjà participé à ces actions")
	ancien_soigneur = models.BooleanField("Déjà été soigneur")
	adherent_autre_asso = models.CharField("Adhérent dans d'autres associations ?", max_length=200, blank=True)
	permis_b = models.BooleanField("Je suis titulaire du Permis B")
	vehicule = models.BooleanField("Je possède un véhicule que j'aurai à disposition pour la mission")
	permis_mer = models.BooleanField("Je possède un Permis Mer")
	navig_regulierement = models.BooleanField("Je navigue régulièrement")
	kayak_mer = models.BooleanField("Je pratique le Kayak en mer")
	kayak_niveau = models.CharField("Je suis titulaire d'une pagaie couleur justifiant mon niveau de kayak", choices=CHOIX_PRATIQUE_KAYAK, max_length=20, blank=True)
	afps = models.BooleanField("Je possède l'AFPS")
	psc1 = models.BooleanField("Je possède le PSC1")
	sauveteur_travail = models.BooleanField("Je suis Sauveteur secouriste du travail")
	autre = models.CharField("J'ai suivi une autre formation de secouriste", max_length=200, blank=True)
	bafa = models.BooleanField("Je possède le BAFA")
	bapaat = models.BooleanField("Je possède le BAPAAT")
	bpjeps = models.BooleanField("Je possède le BPJEPS")
	guide_nature = models.BooleanField("Je possède un diplôme de Guide nature")
	btps_gpn_opt_anim = models.BooleanField("Je possède le BTPS GPN")
	autre_anim = models.CharField("J'ai suivi une autre formation en animation", max_length=200, blank=True)
	mam_marins = models.BooleanField("J'ai des connaissances sur les Mammifères marins")
	oiseaux = models.BooleanField("J'ai des connaissances sur l'Avifaune")
	autre_competence_naturaliste = models.CharField("Mes autres compétences naturalistes", max_length=200, blank=True)
	veterinaire = models.BooleanField("Je possède une formation vétérinaire")
	auxiliaire_sante = models.BooleanField("Je possède une formation auxiliaire de santé animale")
	soigneur_animalier = models.BooleanField("Je possède une formation de soigneur animalier")
	autre_diplome_soins = models.CharField("J'ai suivi une autre formation en soins animaliers", max_length=200, blank=True)
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

Vous avez été sélectionné(e) pour participer aux missions de bénévolat pour les phoques de la baie de Somme qui se tiendront au cours des printemps et été 2016.

Merci de confirmer votre votre participation Pour cela, veuillez:
  - accepter le règlement intérieur (reçu par e-mail au format .pdf),
  - vous acquitter des frais de gestion de 50 € par personne,
  - vous acquitter des frais de participation à l'hébergement et à la nourriture de 20 € par semaine,
  - vérifier que vous êtes à jour de votre adhésion 2016, si ce n'est pas le cas: adhérez en ligne ! (http://dons.picardie-nature.org/)

Pour ce faire rendez-vous à cette adresse http://benevoles.bds.picardie-nature.org/confirmation, et identifiez-vous.

Rappels:
  - Les candidatures sont réceptionnées jusqu'au lundi 29 février 2016 dernier délai, 
  - Une première selection sera faites début mars, 
  - Une réponse sera envoyée par mail avant le 18 mars 2016, 
  - Tous les candidats ayant confirmé seront considérés comme participant bénévoles pour les phoques dès le 4 avril minuit. Dans le cas contraire, les places seront proposées à d'autres candidats.
  - Les candidats ayant confirmé leur participation seront considérés comme participant si leur dossier de candidature est complet au 4 avril minuit (attestation responsabilité civile, enveloppe timbrée libellée à vos nom et adresse, chèque de caution de 100 €, frais d'hébergement et de participation à la nourriture, adhésion). 
  - Les candidats sélectionnés qui ne souhaiteraient ou ne pourraient plus assurer leur période de bénévolat sont priés de prévenir de leur désistement au plus tôt.
    - En cas de désistement signalé avant le 1er mai, le chèque de caution vous sera retourné. 
    - En cas de désistement signalé après le 1er mai, le chèque de caution sera encaissé (ce cas comprend les désistements de dernière minute ainsi que les abandons au cours de la mission)
    - En cas de désistement signalé après le 1er mail, les frais de gestion ne seront pas remboursés,
    - En cas de désistement signalé après le 1er mai mais avan votre arrivée sur place, la participation aux frais d'hébergement et de nourriture de 20€ par semaine vous seront remboursés.
  - La participation à ces missions bénévoles ne donnent pas droit à signature d'une convention scolaire, cependant, tous les participants recevront une attestation de présence à l'automne 2016.
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
		('SOINS', 'Centre de sauvegarde de la faune sauvage'),
		('SURV', 'Surveillance des phoques')
	)

	fiche = models.ForeignKey(Fiche, unique=True)	
	retenu_14_05_au_21_05 = models.CharField("Présent du 14-05 au 21-05", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_21_05_au_28_05 = models.CharField("Présent du 21-05 au 28-05", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_28_05_au_04_06 = models.CharField("Présent du 28-05 au 04-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_04_06_au_11_06 = models.CharField("Présent du 04-06 au 11-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_11_06_au_18_06 = models.CharField("Présent du 11-06 au 18-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_18_06_au_25_06 = models.CharField("Présent du 18-06 au 25-06", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_25_06_au_02_07 = models.CharField("Présent du 25-06 au 02-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_02_07_au_09_07 = models.CharField("Présent du 02-07 au 09-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_09_07_au_16_07 = models.CharField("Présent du 09-07 au 16-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_16_07_au_23_07 = models.CharField("Présent du 16-07 au 23-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_23_07_au_30_07 = models.CharField("Présent du 23-07 au 30-07", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_30_07_au_06_08 = models.CharField("Présent du 30-07 au 06-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_06_08_au_13_08 = models.CharField("Présent du 06-08 au 13-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_13_08_au_20_08 = models.CharField("Présent du 13-08 au 20-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_20_08_au_27_08 = models.CharField("Présent du 20-08 au 27-08", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_27_08_au_03_09 = models.CharField("Présent du 27-08 au 03-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_03_09_au_10_09 = models.CharField("Présent du 03-09 au 10-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_10_09_au_17_09 = models.CharField("Présent du 10-09 au 17-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_17_09_au_24_09 = models.CharField("Présent du 17-09 au 24-09", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_24_09_au_01_10 = models.CharField("Présent du 24-09 au 01-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_01_10_au_08_10 = models.CharField("Présent du 01-10 au 08-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_08_10_au_15_10 = models.CharField("Présent du 08-10 au 15-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_15_10_au_22_10 = models.CharField("Présent du 15-10 au 22-10", max_length=5, choices=CHOIX_MISSION, blank=True)
	retenu_22_10_au_29_10 = models.CharField("Présent du 22-10 au 29-10", max_length=5, choices=CHOIX_MISSION, blank=True)

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
