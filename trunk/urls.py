from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ecovolontaires.inscription.models import Fiche,FicheAdmin

admin.site.register(Fiche, FicheAdmin)

urlpatterns = patterns('',
    # Example:
    # (r'^ecovolontaires/', include('ecovolontaires.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'ecovolontaires.inscription.views.index'),
    (r'^inscription/', 'ecovolontaires.inscription.views.index'),
    (r'^fermer/', 'ecovolontaires.inscription.views.fermer'),
    (r'^documents/', 'ecovolontaires.inscription.views.documents')
)
