# coding=UTF-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ecovolontaires import inscription
from datetime import datetime
from os import listdir,mkdir,path
import commands

def fermer(request):
	logout(request)
	return render_to_response('fermer.html', {'login': None})


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
			u.email_user('Inscription comme ecovolontaire',
					"""Votre inscription est enregistrée,

Pour la finaliser il vous reste a envoyer les documents administratifs.
Rendez-vous sur : http://ecovolontaires.picardie-nature.org/
Votre mot de passe est : %s


""" % mot_de_passe)
			u.save()
			fiche.user_id = u.id;
			fiche.save()
			
			return HttpResponseRedirect('/documents/')
		else:
			return render_to_response('formulaire.html', {'form': f})

	f = inscription.models.FicheForm()
	return render_to_response('formulaire.html', {'form': f})
