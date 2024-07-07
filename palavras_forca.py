import pandas as pd
import random

def palavras_excel(caminho):
    df = pd.read_excel(caminho)
    return df

def escolher_palavra_aleatoria(df):
    palavras = df['Palavras'].tolist() #tolist converte a coluna Palavras em uma lista
    palavra_escolhida = random.choice(palavras)
    return palavra_escolhida

caminho = r"Palavras para forca.xlsx"
palavras_df = palavras_excel(caminho)
palavra_escolhida = escolher_palavra_aleatoria(palavras_df)
