# dopo aver aperto gli strumenti per sviluppatori nella playlist di youtube che si vuole scaricare,  si apre l'intero
# blocco che contiene tutti i video e si espandono tutti i campi del contenitore, dopo si copia con seleziona tutto
# dopo aver selezionato modifica come html e si incolla in un file .txt e si seleziona la codifica utf-8,  poi si entra
# in questo modulo del programma e si apre il file e si otterrano tutti i link di youtube dei video  della playlist
# (da 0 a n - 1 ), e non resta che passarli al modulo main per scaricarli autoomaticamente.

from bs4 import BeautifulSoup

parse_text = BeautifulSoup(open('youtube_link_into_tag.txt'), 'html.parser')

url_playlist = []

for link in parse_text.find_all('a', class_='yt-simple-endpoint inline-block style-scope ytd-thumbnail'):
    get_href = link.get('href')
    divide_href_in_elem_by_equal = get_href.split('=')
    get_the_main_link = divide_href_in_elem_by_equal[1]
    url_playlist.append("https://www.youtu.be/" + get_the_main_link[:-5])

print(url_playlist)
print(len(url_playlist))
