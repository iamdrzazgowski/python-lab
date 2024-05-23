from requests import get
import re


def stolica(nazwa):
    response = get("https://pl.wikipedia.org/wiki/" + nazwa, stream=True)

    html_content = response.text
    pattern = r'<tr>(?:(?!<\/?tr>).)*Stolica(?:(?!<\/?tr>).)*<\/tr>'

    match = re.search(pattern, html_content, re.DOTALL)

    if match:
        match_fragment = match.group(0)
        # print(match_fragment)
        match = re.findall(r'(?<=title=")(.*?)(?=">)', match_fragment, re.DOTALL)
        # print(match)
        return match[1]

    else:
        print("Nie znaleziono dopasowania.")

    response.close()


# def stolica2(s):
#     f = get("https://pl.wikipedia.org/wiki/" + s, stream=True)
#     b, c, d = '', '', ''
#
#     for l in f.iter_lines():
#         a, b, c, d = (b, c, d, l.decode('utf-8'))
#         if "Stolica</a>" in a:
#             f.close()
#             return d.split('">')[1].split('<')[0]

countries = ['Polska', 'Niemcy', 'Szwecja', 'Islandia', 'Japonia', 'Tanzania', 'Kanada', 'Australia', 'Słowacja',
             'Rumunia']

print(list(map(stolica, countries)))
