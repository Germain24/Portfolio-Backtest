# Analyse de portefeuille avec Python
Ce programme permet d'analyser l'évolution d'un portefeuille d'actions en utilisant l'API de financialmodelingprep.com. Le programme prend en entrée une liste de tickers d'actions et une liste de pourcentages correspondants, et génère un graphique de l'évolution de la valeur du portefeuille sur une période donnée.

## Prérequis
Python 3.x
Bibliothèques Python : requests, pandas, matplotlib

## Utilisation
Cloner le dépôt sur votre ordinateur.

Ouvrir un terminal et naviguer vers le dossier du projet.

Installer les bibliothèques Python nécessaires en exécutant la commande suivante :

pip install -r requirements.txt

Renommer le fichier .env.example en .env, puis ajouter votre clé d'API financialmodelingprep.com.

Ouvrir le fichier portfolio_analysis.py dans votre éditeur de code et modifier les listes tickers et weights selon vos besoins.

Exécuter le programme en utilisant la commande suivante :


python portfolio_analysis.py

Le programme affichera un graphique de l'évolution du portefeuille sur une période donnée, ainsi que des statistiques sur la performance du portefeuille.

## Auteur

Ce projet a été créé par De Sousa Germain.

## Code

``` python
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = os.getenv('API_KEY')
tickers = ['AAPL', 'AMZN', 'GOOGL', 'MSFT']
weights = [0.25, 0.25, 0.25, 0.25]

def get_portfolio_value(start_date, end_date):
    prices = []
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start_date}&to={end_date}&apikey={API_KEY}'
        data = requests.get(url).json()['historical']
        df = pd.DataFrame(data)
        df.set_index('date', inplace=True)
        prices.append(df['close'])
    portfolio_value = pd.concat(prices, axis=1).dot(weights)
    return portfolio_value

def plot_portfolio_value(portfolio_value):
    portfolio_value.plot(figsize=(10, 6))
    plt.title('Évolution de la valeur du portefeuille')
    plt.xlabel('Date')
    plt.ylabel('Valeur du portefeuille')
    plt.show()

start_date = '2020-01-01'
end_date = '2020-12-31'

portfolio_value = get_portfolio_value(start_date, end_date)
plot_portfolio_value(portfolio_value)

print('Performance du portefeuille :')
print(f'- Rendement annuel : {portfolio_value.pct_change().mean() * 252:.2%}')
print(f'- Volatilité annuelle : {portfolio_value.pct_change().std() * 252 ** 0.5:.2%}')
print(f'- Ratio de Sharpe : {portfolio_value.pct_change().mean() / portfolio_value.pct_change().std() * 252 ** 0.5:.2f}')
print(f'- Maximum Drawdown : {((portfolio_value / portfolio_value.cummax()) - 1).min():.2%}')

```

Cela calcule les statistiques de performance suivantes :

Rendement annuel : le rendement moyen du portefeuille par an.
Volatilité annuelle : l'écart-type du rendement annuel du portefeuille.
Ratio de Sharpe : le rendement moyen du portefeuille ajusté au risque (mesuré par la volatilité) par unité de temps (généralement annuel).
Maximum Drawdown : la plus grande perte subie par le portefeuille depuis son plus haut historique.