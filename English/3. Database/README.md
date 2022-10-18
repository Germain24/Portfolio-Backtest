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

1. *https://financialmodelingprep.com/api/v3/profile/{ **Ticker** }?apikey=ce82b6a14287d6b24fdcaf5468401b12* for 
2. 
````python
````