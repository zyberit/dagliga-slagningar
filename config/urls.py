"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin

from sortera.views import ladda_upp, ladda_ner_lista, ladda_ner_fil

urlpatterns = [
    url(r'^ladda-upp', ladda_upp, name="ladda-upp"),
    url(r'^ladda-ner-lista', ladda_ner_lista, name="ladda-ner-lista"),
    url(r'^ladda-ner-fil/(?P<filnamn>.*)/$', ladda_ner_fil, name="ladda-ner-fil"),
#     url(r'^admin/', admin.site.urls),
]
