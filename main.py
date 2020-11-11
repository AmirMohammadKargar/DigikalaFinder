import requests
from bs4 import BeautifulSoup

url1 = 'https://www.digikala.com/search/category-notebook-netbook-ultrabook/?has_selling_stock=1&pageno={}&sortby=4'
url2 = 'https://www.digikala.com/search/category-mobile-phone/?has_selling_stock=1&pageno={}&sortby=4'
url3 = 'https://www.digikala.com/search/category-tablet/?has_selling_stock=1&pageno={}&sortby=4'

flag = True
page = 1
counter = 1

print('Choose category:')
print('1)LapTop\n2)Mobile\n3)Tablet')
c = int(input('Enter category number:'))

if c == 1:
    url = url1
elif c == 2:
    url = url2
elif c == 3:
    url = url3

minPrice = int(input('Enter minimun price(Toman):'))
maxPrice = int(input('Enter maximum price(Toman):'))

while flag:
    result =requests.get(url.format(str(page)))
    if result.status_code == 200:
        soup = BeautifulSoup(result.content)
        for div in soup.find_all('div', {"class":["c-product-box c-promotion-box js-product-box has-more is-plp", "c-product-box c-promotion-box js-product-box is-plp"]}):
            price=''
            for char in div.get('data-price'):
                if char == ',':
                    pass
                else:
                    price+=char
            if int(price) <= maxPrice and int(price) >=minPrice:
                print(str(counter)+') ',end='')
                print('Name:'+div.get('data-title-en'))
                print('Price:'+div.get('data-price')+' Toman')
                print('==================================')
                counter +=1
        page +=1
    else:
        exit()
