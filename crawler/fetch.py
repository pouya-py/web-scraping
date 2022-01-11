import psycopg2
import requests
from bs4 import BeautifulSoup
import re


class InsertIntoDb:
    """class to connect to our database and then put all data fetched from the request
    into the db table."""
    
    def __init__(self,
        request_url = 'https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%DA%A9%D8%B1%D9%85%D8%A7%D9%86%D8%B4%D8%A7%D9%87'):
        self.request_url = request_url

    def connect_to_db(self):
        """connect to database and insert into a table data that is fetch from 'fetch_data' function. """
        try:
            cnn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='')
            # builfing a cursor
            cur = cnn.cursor()
            data = self.fetch_data()
            keys_list = list(data.keys())
            # for every elements get price and detail values in order to insert them into  database.
            for n,d in enumerate(data.values()):
                
                rooms = d['detail_list'][1] 
                space = d['detail_list'][0]
                year_of_construction = d['detail_list'][-1]
                price = d['price']
                id = int(keys_list[n])
                cur.execute('INSERT INTO houses(id, rooms, space, year_of_construction, price)\
                VALUES (%s ,%s, %s, %s, %s)',(id, rooms, space, year_of_construction, price))
                    
            cnn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as err:
            print('Database error: '+str(err))
        finally:
            if cnn is not None:
                cnn.close()
    def fetch_data(self):
        """fetches data using request's get method and pass all the page source  in the Beautiful soup module,
        to get elements with specfic class."""
        data = {}
        # using for loop to request data from two pages
        for i in range(1,3):
            r = requests.get(f'{self.request_url}?page={i}')
            # if request was successfull continue
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                # get the element that contains all information.
                elements = soup.find_all('div', class_='list_infoBox__iv8WI')
                
                for txt in elements:
                    # Search for element contain price and the one with having more info
                    price = txt.find('span',class_ = 'list_infoPrice___aJXK')
                    specs = txt.find('div',class_='list_infoSpecs__EACNx')
                    specs_text = re.findall(r'(\d+)',specs.text)
                    # Add price and detail of a house to dictionary if it doesn't already exist.
                    if ''.join(specs_text) not in data:
                        # dictionary key based on specs number to be as unique as possible
                        data[''.join(specs_text)] = {

                            'price': int(price.text.split(' ')[0].replace(',','')),
                            'detail_list': [int(i) for i in specs_text],
                        }     
            else:
                print('There is a problem with the url.')
                return None
        return data
    

insert_into_db = InsertIntoDb()
insert_into_db.connect_to_db()