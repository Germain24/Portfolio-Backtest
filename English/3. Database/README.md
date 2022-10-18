# La stratégie de Warren Buffett
## Database

Now that we know how Warren Buffet chooses his stocks, we are going to create a program that takes financial elements from all stock from an API.
For the database, we are going to take care of the data of the last 10 years of each stock.

We need 3 types of elements :
1. Constant elements :
   1. Name of company
   2. Ticker
   3. Sector
   4. Country

2. Financial element from the last 20 years :
   1. Revenue
   2. Cost of revenue
   3. Net income
   4. Total liabilities
   5. Total assets
   6. Cash and cash equivalents
   7. Research and development expenses
   8. Retained earnings
   9. Operating expenses
   10. Total stockholders equity
   11. Common stock number

For this we are going to take financialmodelingprep.com API.
We need 5 links :

| Link                                                                                                                            | Utility                                                                                                                     | Give us                 |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------|
| https://<i></i>financialmodelingprep.com/api/v3/profile/{**Ticker**}?apikey=ce82b6a14287d6b24fdcaf5468401b12                    | Country - Sector - Name                                                                                                     | Global data information |
| https://<i></i>financialmodelingprep.com/api/v3/income-statement/{**Ticker**}?apikey=ce82b6a14287d6b24fdcaf5468401b12           | Revenue - Cost of revenue - Net income                                                                                      | Income Statement        |
| https://<i></i>financialmodelingprep.com/api/v3/balance-sheet-statement/{**Ticker**}?apikey=ce82b6a14287d6b24fdcaf5468401b12&limit=120 | Total liabilities - Total assets - Cash and cash equivalents - Retained earnings - Total stockholders equity - Common stock | Balance Sheet Statement |
| https://<i></i>financialmodelingprep.com/api/v3/income-statement/{**Ticker**}?limit=120&apikey=ce82b6a14287d6b24fdcaf5468401b12 | Research and development expenses - Operating expenses                                                                      | Income statement        |

We need this function to extract data from the API :

````python
from urllib.request import urlopen
import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)
````

I'm going to give you somme exemple :

get_jsonparsed_data function give us a list, each element give us data from most recent one to oldest ones ( [0] for the last and [-1] for the oldest )

### Exemple 1 Apple global information

Code :

````python

print(get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=ce82b6a14287d6b24fdcaf5468401b12")[0])

````

Output :

````python

{'symbol': 'AAPL', 'price': 142.41, 'beta': 1.249815, 'volAvg': 81088200, 'mktCap': 2288642686976
   , 'lastDiv': 0.9, 'range': '129.04-182.94', 'changes': 4.029999, 'companyName': 'Apple Inc.', 'currency': 'USD'
   , 'cik': '0000320193', 'isin': 'US0378331005', 'cusip': '037833100', 'exchange': 'NASDAQ Global Select', 'exchangeShortName': 'NASDAQ'
   , 'industry': 'Consumer Electronics', 'website': 'https://www.apple.com'
   , 'description': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. In addition, the company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; AirPods Max, an over-ear wireless headphone; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, and iPod touch. Further, it provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. Additionally, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.'
   , 'ceo': 'Mr. Timothy Cook', 'sector': 'Technology', 'country': 'US', 'fullTimeEmployees': '154000', 'phone': '14089961010'
   , 'address': '1 Apple Park Way', 'city': 'Cupertino', 'state': 'CALIFORNIA', 'zip': '95014', 'dcfDiff': 2.07175, 'dcf': 144.482
   , 'image': 'https://financialmodelingprep.com/image-stock/AAPL.png', 'ipoDate': '1980-12-12', 'defaultImage': False, 'isEtf': False
   , 'isActivelyTrading': True, 'isAdr': False, 'isFund': False}

````
