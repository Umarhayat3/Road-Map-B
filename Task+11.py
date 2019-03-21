import bs4

html = open("forecast.html").read()
bs = bs4.BeautifulSoup(html, "html.parser")
days_list = bs("b")
details_list = bs.find_all('div', class_="grid col-75 forecast-text")
item = details_list[0]

print(item)

