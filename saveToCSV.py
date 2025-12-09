import pandas as pd
import os

def save_to_csv(data, filename):
    df = pd.DataFrame(data)

    if os.path.isfile(filename):
        df.to_csv(filename, mode="a", header=False, index=False)
        print(f"Dodano novih redaka u {filename}")
    else:
        df.to_csv(filename, index=False)
        print(f"Dataset spremljen u {filename} duljine {len(df)}")
