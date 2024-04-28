import os
from typing import Dict

import numpy as np
import pandas as pd

from constants import CONFIG_FILE
from helpers import get_toml_data


def get_config() -> Dict:
    # Obtenir le répertoire du module actuel
    current_dir = os.path.dirname(__file__)

    # Construire le chemin complet vers le fichier de configuration
    path = os.path.join(current_dir, CONFIG_FILE)

    # Charger et retourner les données du fichier de configuration
    return get_toml_data(path)


def get_data():
    # Obtenir la configuration du fichier
    config = get_config()

    # Extraire les dates de début et de fin de la configuration
    begin_date = config["initialisation"]["begin_date"]
    end_date = config["initialisation"]["end_date"]

    # Obtenir le répertoire du module actuel
    current_dir = os.path.dirname(__file__)

    # Construire le chemin complet vers le fichier CSV du portefeuille
    csv_path = os.path.join(current_dir, "input", "crisis_portfolio.csv")

    # Lire les données du portefeuille à partir du fichier CSV
    data = pd.read_csv(
        csv_path,
        delimiter=",",
        index_col="Date",
        parse_dates=["Date"],
    )

    # Sélectionner les données dans la plage de dates spécifiée
    data = data.loc[begin_date:end_date]

    return data


def get_weights(config: Dict) -> np.array:
    return np.array(list(config["portfolio"].values()))


if __name__ == "__main__":
    conf = get_config()
    print(get_weights(conf))
    print("*" * 20)
    results = get_data()
    print(results.columns)
    print(results.columns.nlevels)
    print(results)
    print("toml", "-" * 20)
    print(get_config())
