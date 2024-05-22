from newsapi import NewsApiClient
import requests
from win32com.client import Dispatch

# initialisation
newsapi = NewsApiClient(api_key='429f56c85dde485490e907c4b1b67557')

# a = newsapi.get_everything(q='sports')
#
# print(a)
query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "429f56c85dde485490e907c4b1b67557"
    }
main_url = 'https://newsapi.org/v1/articles'
res = requests.get(main_url, params=query_params)
open_bbc_page = res.json()

# getting all articles in a string article
article = open_bbc_page["articles"]

# empty list which will
# contain all trending news
results = []

for ar in article:
    results.append(ar["title"])

for i in range(len(results)):
    # printing all trending news
    print(i + 1, results[i])

# to read the news out loud for us
# from win32com.client import Dispatch

speak = Dispatch("SAPI.Spvoice")
speak.Speak(results)
