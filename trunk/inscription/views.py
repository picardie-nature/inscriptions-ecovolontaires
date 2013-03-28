# coding=UTF-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ecovolontaires import inscription
from datetime import datetime,date
from os import listdir,mkdir,path,environ
import commands
from django.core.mail import send_mail

def fermer(request):
	logout(request)
	return render_to_response('fermer.html', {'login': None})

def confirmation(request):
	u = None
	if not request.user.is_authenticated():
		if request.method == 'POST':
			u = authenticate(username=request.POST['email'], password=request.POST['pwd'])
			if u:
				login(request, u)
	
	if not request.user.is_authenticated():
		return render_to_response('confirmation.html', {'login': None})
	
	# ici on est connecté
	fiche = inscription.models.Fiche.objects.get(user_id=request.user.id)
	candidat = inscription.models.CandidatRetenu.objects.get(fiche=fiche.id)
	return render_to_response('confirmation.html', {'login': True, 'fiche': fiche, 'candidat': candidat})
	
def mot_de_passe(request):
	msg = ""
	if request.method == "POST":
		u = User.objects.get(username=request.POST['email'])
		if u:
			mot_de_passe = commands.getoutput('pwgen -1')
			u.set_password(mot_de_passe)
			u.save()
			send_mail(u"Votre nouveau mot de passe","""Bonjour,

Votre nouveau mot de passe est : %s

""" % (mot_de_passe), 'support@picardie-nature.org', [u.email])
		msg = "Nouveau mot de passe envoyé"
	
	return render_to_response('mot_de_passe.html', {'msg': msg})

def documents(request):
	msg = ''
	form = None
	if not request.user.is_authenticated():
		if request.method == 'POST':
			u = authenticate(username=request.POST['email'], password=request.POST['pwd'])
			if u:
				login(request, u)

	if not request.user.is_authenticated():
		return render_to_response('login.html', {'login': None})
	else:
		if environ.has_key('DATA_PATH'):
			chemin = '%s/%s'%(environ['DATA_PATH'], request.user.id)
		else:
			chemin = 'data/%s'%(request.user.id)
		fiche = inscription.models.Fiche.objects.get(user_id=request.user.id)

		if request.method == 'POST':
			form = inscription.models.UploadForm(request.POST, request.FILES)
			if form.is_valid():
				msg = msg + 'FORM OK '
				fic = request.FILES['fic']
				if not path.exists(chemin):
					mkdir(chemin)
				f = open('%s/%s'%(chemin, fic.name), 'wb+')
				for part in fic.chunks():
					f.write(part)
				f.close()
				tmesg = "Fichier %s enregistré".decode('utf-8')
				msg = tmesg%(fic.name)
			else:
				msg = msg + 'PB FORMULAIRE '
		if form is None:
			form = inscription.models.UploadForm()
		u = request.user
		liste_fichiers = []
		
		if path.exists(chemin):
			liste_fichiers = listdir(chemin)
		else:
			msg = msg + ' (aucun fichier pour le moment)'
		return render_to_response('documents.html', 
			{'form': form, 'u': u, 'm': msg,
			 'liste_fichiers': liste_fichiers,
			 'fiche': fiche})


def index(request):
	if (date.today() < date(2014,3,11)):
		if request.method == 'POST':
			fiche = inscription.models.Fiche()
			f = inscription.models.FicheForm(request.POST, instance=fiche)
			if f.is_valid():
				fiche = f.save(commit=False)
				fiche.date_inscription = datetime.now()
				if fiche.dispo_soins_nb_semaine is None:
					fiche.dispo_soins_nb_semaine = 0;
				if fiche.duree_n_semaine is None:
					fiche.duree_n_semaine = 0

				login = fiche.email				
				mot_de_passe = commands.getoutput('pwgen -1')
				u = User.objects.create_user(login,login,mot_de_passe)
				u.email_user(u'Votre inscription comme écovolontaire',
						"""Votre inscription est enregistrée,

Pour la finaliser il vous reste a envoyer les documents administratifs.
Rendez-vous sur : http://ecovolontaires.picardie-nature.org/documents/
Votre mot de passe est : %s


""" % mot_de_passe)
				u.save()
				fiche.user_id = u.id;
				fiche.save()

				admins = User.objects.filter(username='admin')
				for admin in admins:
					sujet = u'Nouvel écovolontaire';
					msg = u"""Nouvel écovolontaire enregistré : %s %s

Adresse email : %s
Mot de passe : %s

Pour le suivi http://ecovolontaires.picardie-nature.org/admin

					""" % (fiche.nom, fiche.prenom, fiche.email, mot_de_passe)
					msg.encode('u8')
					admin.email_user(sujet, msg)
				
				return HttpResponseRedirect('/documents/')
			else:
				return render_to_response('formulaire.html', {'form': f})

		f = inscription.models.FicheForm()
		return render_to_response('formulaire.html', {'form': f})
	else:
		return render_to_response('inscription_fermee.tpl')
