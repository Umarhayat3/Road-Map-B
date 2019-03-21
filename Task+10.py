import bs4
html = open('test.html').read()
bs = bs4.BeautifulSoup(html, 'html.parser')
special_list = bs.select(".special")
print(special_list)
special_item =special_list[0]
print(special_item.text)
print(special_item["class"])


