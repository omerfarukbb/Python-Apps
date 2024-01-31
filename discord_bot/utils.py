import requests
from bs4 import BeautifulSoup

def get_ayat(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if ayat := soup.find(class_='verse-style__VerseTranslation-sc-abdc9719-1 itwMBU'):
            return ayat.text
        
    else:
        return '?'

def get_response(user_message: str, surahs) -> str:
    lowered = user_message.strip().lower()

    if lowered == 'help':
        return 'Usage: SurahName AyatNumber (Nahl 14)'

    words = lowered.split()

    if len(words) == 2:
        surah_name, ayat_number = words
        if surah_name.lower() not in surahs or not ayat_number.isnumeric():
            print(1, surah_name, ayat_number)
            print(surah_name.lower() in surahs.keys())
            print(ayat_number.isnumeric())
            return 'Wrong usage!'

        surah_number = surahs[surah_name.lower()]
        url = f'https://acikkuran.com/{surah_number}/{ayat_number}'
        ayat = get_ayat(url) + f' ({surah_name.capitalize()}/{ayat_number})'
        
        return ayat

    elif len(words) == 3:
        if words[0].lower() == 'ali' and words[1].lower() == 'imran' and words[2].isnumeric():
            surah_number, ayat_number = 3, words[2]
            url = f'https://acikkuran.com/{surah_number}/{ayat_number}'
            ayat = get_ayat(url) + f' (Ali İmran/{ayat_number})'
            
            return ayat
        else:
            return 'Wrong Usage!'

    else:
        return 'Wrong Usage!'
