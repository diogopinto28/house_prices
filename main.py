import requests
from bs4 import BeautifulSoup
import smtplib

budget = 550

URL = ['https://www.imovirtual.com/pt/anuncio/t1-kitchnette-com-terraco-em-matosinhos-sul-ID11uqi.html#f523fbcd8f', 'https://www.imovirtual.com/pt/anuncio/t1-ao-hosp-s-joao-arroteia-com-lg-de-garagem-ID14tnw.html#f523fbcd8f']

headers = {'UserAgent': '##insert your user Agent - check readme to know how'}

for i in URL:
    page = requests.get(i, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find("h1", {"class": "css-11t1qm5"}).get_text()
    price = soup.find('strong', {'class': 'css-1mojccp'}).get_text()
    new_price = int(price[0:4])

    print('O apartamento', title, 'tem um custo de', new_price)


    def send_drop_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('dsomethingmail.com', 'Your password')

        subject = 'Price DROP!'
        body = 'Ve o link da casa que desceu o preco:'


        server.sendmail(
            'something@gmail.com',
            'something@gmail.com',
            msg=f'Subject: {subject}\n\n{body}'
            )

        print('Email foi enviado!')

        server.quit()

    def send_same_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('something@gmail.com', 'Your password')

        subject = 'Price EQUAL!'
        body = 'Ve o link da casa que nao alterou o preco:'


        server.sendmail(
            'something@gmail.com',
            'something@gmail.com',
            msg=f'Subject: {subject}\n\n{body}'
            )

        print('Email foi enviado!')

        server.quit()


    if(new_price < budget):
        send_drop_mail()

    if(new_price > budget):
        print('preço não dentro do objetivo!')
        send_same_mail()


