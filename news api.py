from newsapi import NewsApiClient
import requests
from win32com.client import Dispatch

# initialisation very imp***
newsapi = NewsApiClient(api_key='YOUR_API_KEY')

# a = newsapi.get_everything(q='sports')
#
# print(a)
# now for the parameters whihch needs to be passed on
query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "429f56c85dde485490e907c4b1b67557"
    }
main_url = 'https://newsapi.org/v1/articles'
res = requests.get(main_url, params=query_params)
open_bbc_page = res.json()

# getting the required articles
article = open_bbc_page["articles"]

# some logic
results = []

for ar in article:
    results.append(ar["title"])

for i in range(len(results)):
    # printing all trending news
    print(i + 1, results[i])

# to make the text talk
speak = Dispatch("SAPI.Spvoice")
speak.Speak(results)
