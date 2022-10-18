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