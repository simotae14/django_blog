from django.shortcuts import render
from yandex_translate import YandexTranslate

from .forms import SearchForm

translate = YandexTranslate('trnsl.1.1.20160621T155434Z.69d8c9c1b6f3b2bc.a8526274aab360e721d467fe83fb9d880a2ab793')

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
            print(search_term)
            return render(request, 'traduzione/search.html', {'form': form})
    else:
        form = SearchForm()
    return render(request, 'traduzione/search.html', {'form': form})


def detectLang(search_term):
    print('Detect language:', translate.detect(search_term))

#print('Languages:', translate.langs)
#print('Translate directions:', translate.directions)

#print('Translate:', translate.translate('Привет, мир!', 'ru-en'))  # or just 'en'
#print('Translate:', translate.translate('Привет, мир!', 'ru-it'))  # or just 'en'
#print('Translate:', translate.translate('Привет, мир!', 'ru-es'))  # or just 'en'