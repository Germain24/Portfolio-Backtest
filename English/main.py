def main():
    while True:
        # Partie 1 : récupération des données
        data = get_data()

        # Partie 2 : traitement des données
        processed_data = process_data(data)

        # Partie 3 : analyse des données
        results = analyze_data(processed_data)

        # Partie 4 : affichage des résultats
        display_results(results)

        # Demander à l'utilisateur s'il souhaite continuer ou quitter
        user_input = input("Voulez-vous continuer ? (o/n)")
        if user_input.lower() == "n":
            break


if __name__ == "__main__":
    main()