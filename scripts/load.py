import pandas as pd
from sqlalchemy import create_engine

def load_data():
    database_url = "postgresql://gbrl014:gbrl014@localhost:5432/rnm_dw"

    try:
        df = pd.read_csv("../data/processed/processed_rnm.csv")
        
        engine = create_engine(database_url)
        df.to_sql(name="rnm", con=engine, if_exists="replace", index=False)
        print("dados carregados na tabela rnm")

    except Exception as e:
        print(f"erro ao carregar dados: {e}")

if __name__ == "__main__":
    load_data()