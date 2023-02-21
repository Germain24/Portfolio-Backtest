# Portoflio Backtest
Portoflio Backtest est un programme Python conçu pour calculer et visualiser la performance d'un portefeuille d'actions.

## Fonctionnalités
Le programme offre les fonctionnalités suivantes :

- Récupération des données historiques de plusieurs actions à partir de l'API de financialmodelingprep.com
- Calcul de la contribution de chaque action à la valeur du portefeuille en utilisant un ensemble de pondérations donné
- Agrégation des contributions pour obtenir la valeur totale du portefeuille sur une période de temps donnée
- Tracé de la performance du portefeuille sur la période de temps donnée
- Calcul de diverses statistiques de performance, telles que le rendement annuel, la volatilité annuelle, le ratio de Sharpe et le maximum drawdown

## Comment utiliser
Pour utiliser le programme, vous devez avoir Python 3.x installé sur votre système ainsi que les bibliothèques requests, pandas, numpy et matplotlib.pyplot. Vous pouvez installer ces bibliothèques en exécutant la commande suivante dans votre terminal :

```python
pip install requests pandas numpy matplotlib
```

Ensuite, vous pouvez exécuter le programme en exécutant le fichier nom-du-fichier.py dans votre terminal avec la commande suivante :

```python
python Portoflio_Backtest.py
```

Vous pouvez également personnaliser le programme en modifiant les symboles d'actions et les pondérations dans les listes tickers et weights, ainsi que les dates de début et de fin dans les variables start_date et end_date.

Auteur
Portoflio Backtest a été créé par [Germain De Sousa].
