import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Les symboles des titres choisis pour le portefeuille
symboles = ['AAPL', 'MSFT']

# Les poids correspondants de chaque titre dans le portefeuille
poids = [0.25, 0.25]

# Définir la date de début et la date de fin pour l'analyse
date_debut = '2018-02-16'
date_fin = '2023-02-16'

# Normaliser les poids pour qu'ils se totalisent à 1
poids = [x / sum(poids) for x in poids]


# Fonction pour obtenir la valeur du portefeuille en fonction des dates
def get_portfolio_value(date_debut, date_fin):
    # Créer un DataFrame vide pour stocker les changements quotidiens de la valeur du portefeuille
    df0 = pd.DataFrame(index=pd.date_range(start=date_debut, end=date_fin, freq='D'), columns=['changement']).fillna(
        value=0)

    # Pour chaque titre, obtenir les données historiques des prix et ajouter les changements au DataFrame principal
    for i, symbole in enumerate(symboles):
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbole}?from={date_debut}&to={date_fin}&apikey=ce82b6a14287d6b24fdcaf5468401b12'
        data = requests.get(url).json()['historical']
        df = pd.DataFrame(data)
        df.set_index(pd.to_datetime(df['date'], format='%Y-%m-%d'), inplace=True)
        df["changement"] = poids[i] * (df['close'] / df['close'][-1])

        # Supprimer les colonnes inutiles et remplir les valeurs manquantes
        df.drop(['close', 'date', "open", "high", "low", "label", "changeOverTime", "adjClose", "volume", "vwap",
                 "unadjustedVolume", "change", "changePercent"], axis=1, inplace=True)
        df = df.reindex(pd.date_range(start=date_debut, end=date_fin), fill_value=np.nan)
        df.fillna(method='bfill', inplace=True)
        df.fillna(method='ffill', inplace=True)

        # Ajouter les changements de chaque titre au DataFrame principal
        df0['changement'] = df0['changement'] + df['changement']

    # Supprimer les jours où il n'y a pas de changement dans le portefeuille
    return df0.replace(0, np.nan).dropna()


# Fonction pour tracer le rendement du portefeuille au fil du temps
def plot_portfolio_value(portfolio_value):
    portfolio_value.plot(figsize=(10, 6))
    plt.title('Portfolio return evolution')
    plt.xlabel('Date')
    plt.ylabel('Portfolio value')
    plt.grid(True)
    plt.show()

# Obtenir la valeur du portefeuille et tracer le rendement

valeur_portefeuille = get_portfolio_value(date_debut, date_fin)
plot_portfolio_value(valeur_portefeuille)

# Afficher les performances du portefeuille

print('Performance du portefeuille :')
print(f"- Rendement annuel : {round(float(100 * valeur_portefeuille.pct_change().mean() * 365.25), 2)}%.")
print(f"- Volatilité annuelle : {round(float(100 * valeur_portefeuille.pct_change().std() * 365.25 ** 0.5), 2)}%.")
print(
    f"- Ratio de Sharpe : {round(float(valeur_portefeuille.pct_change().mean() / valeur_portefeuille.pct_change().std() * 365.25 ** 0.5), 2)}.")
print(
    f"- Maximum Drawdown : {round(float(((valeur_portefeuille / valeur_portefeuille.cummax()) - 1).min()) * 100, 2)}%.")