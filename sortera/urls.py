"""config URL Configuration
"""

from django.conf.urls import url
from .views import ladda_upp, ladda_ner_lista, ladda_ner_fil

urlpatterns = [
    url(r'^ladda-upp', ladda_upp, name="ladda-upp"),
    url(r'^ladda-ner-lista', ladda_ner_lista, name="ladda-ner-lista"),
    url(r'^ladda-ner-fil/(?P<filnamn>.*)/$', ladda_ner_fil, name="ladda-ner-fil"),
]
