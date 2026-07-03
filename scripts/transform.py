import pandas as pd
import os
import json

def limpar_dados_rnm(df):
    #get origin and location names from dict
    df["origin_name"] = df["origin"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)
    df["location_name"] = df["location"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)

    #get total episodes
    df["total_episodes"] = df["episode"].apply(len)
    
    #fill types with normal (there are empty strings and NA values)
    df["type"] = df["type"].replace("", "Normal").fillna("Normal")

    #transform created to datetime
    df["created"] = pd.to_datetime(df["created"])
    df["created"] = df["created"].dt.tz_localize(None)

    #transform status "unknown" into NA
    df["status"] = df["status"].replace("unknown", pd.NA)

    df.drop(columns=["origin", "location", "episode"], inplace=True)    

def transform_data(escolha):
    caminho_input = f"../data/raw/raw_{escolha}.json"
    caminho_output = f"../data/processed/processed_{escolha}.csv"

    with open(caminho_input, "r", encoding="utf-8") as f:
        dados_brutos = json.load(f)
    
    if escolha == "posts":
        df = pd.DataFrame(dados_brutos)
    elif escolha == "rnm":
        df = pd.DataFrame(dados_brutos["results"])
        limpar_dados_rnm(df)

    df.to_csv(caminho_output, index=False, encoding="utf-8")
    print(f"len(df): {len(df)}")


if __name__ == "__main__":
    select = int(input("Qual transformar?\n1-JSON\n2-RnM\n"))
    if select == 1:
        transform_data("posts")
    elif select == 2:
        transform_data("rnm")
    else:
        print("numero invalido")