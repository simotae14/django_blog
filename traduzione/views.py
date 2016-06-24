from django.shortcuts import render
from django.conf import settings

import requests
import json

from .forms import SearchForm


mappingLingue = { 'en' : "Inglese", 'es' : "Spagnolo", 'de' : "Tedesco", 'fr' : "Francese", 'ru' : "Russo" }

# Create your views here.
def search(request):
    form = SearchForm()
    return render(request, 'traduzione/search.html', {'form': form})

# traduco
def translate(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            resultMap = {}
            for key, value in mappingLingue.items():
                r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + settings.YANDEX_KEY + '&text=' + search_term + '&lang=' + key)
                jsonRes = r.json()
                if (jsonRes['code'] == 200):
                    testo = jsonRes['text']
                    testo = testo[0]
                    resultMap[value] = testo
            return render(request, 'traduzione/translate.html', {'result': resultMap})
    else:
        form = SearchForm()
    return render(request, 'traduzione/search.html', {'form': form})



#print('Languages:', translate.langs)
#print('Translate directions:', translate.directions)

#print('Translate:', translate.translate('Привет, мир!', 'ru-en'))  # or just 'en'
#print('Translate:', translate.translate('Привет, мир!', 'ru-it'))  # or just 'en'
#print('Translate:', translate.translate('Привет, мир!', 'ru-es'))  # or just 'en'