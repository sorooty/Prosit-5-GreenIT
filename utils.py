# Fonctions utiles (chargement Excel, génération,..)
import os
import pandas as pd

def load_datasets(folder_path):
    datasets = {}
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(folder_path, file))
            datasets[file] = df
        elif file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder_path, file))
            datasets[file] = df
            print(df.head(10))
            print("\n" + "-"*50 + "\n")

    return datasets

