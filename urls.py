from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from inscription.models import Fiche,FicheAdmin,CandidatRetenu,CandidatRetenuAdmin

admin.site.register(Fiche, FicheAdmin)
admin.site.register(CandidatRetenu, CandidatRetenuAdmin)

urlpatterns = patterns('',
    # Example:
    # (r'^', include('foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'inscription.views.fermer'),
    (r'^test/', 'inscription.views.index'),
    (r'^inscription/', 'inscription.views.index'),
    (r'^fermer/', 'inscription.views.fermer'),
    (r'^documents/', 'inscription.views.documents'),
    (r'^confirmation/', 'inscription.views.confirmation'),
    (r'^confirmation_fin', 'inscription.views.confirmation_fin'),
    (r'^mot_de_passe/', 'inscription.views.mot_de_passe'),
)
