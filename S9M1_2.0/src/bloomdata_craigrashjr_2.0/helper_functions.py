import pandas as pd
import numpy as np

df=pd.DataFrame({'a':[1,np.nan,3,5,"string","stringa","stringa","string","stringa","string","stringa"],
                "b":[1,np.nan,3,5,"stringb","stringb","stringb","stringb","stringb","stringb","stringb"],
                "c":[1,np.nan,3,5,"stringc","stringc","stringc","stringc","stringc","stringc","stringc"],
                "d":[1,np.nan,3,5,"stringd","stringd","stringd","stringd","stringd","stringd","stringd"],
                "e":[1,np.nan,3,5,"stringe","stringe","stringe","stringe","stringe","stringe","stringe"],
                "f":[1,np.nan,3,5,"stringf","stringf","stringf","stringf","stringf","stringf","stringf"],
                "g":[1,np.nan,3,5,"stringg","stringg","stringg","stringg","stringg","string","stringg"]})

def null_count(df):
    nan_count=0
    num_rows=df.shape[0]
    num_columns=df.shape[1]
    for i in range(num_columns):
        print(i)
        for k in range(len(df.iloc[i])):
            print(i,k)
            if pd.isna(df.iloc[i,k]):
                nan_count=nan_count+1
    return nan_count

def train_test_split(df, frac):
    df_length=len(df)
    if frac >100:
        return "Error:","fraction must be a number equal or less than 100",
    if frac > 1:
        frac= frac/100
    cuttoff=df_length*frac
    train=df[:round(cuttoff)]
    test=df[round(cuttoff):]
    return train,test
a,b=train_test_split(df,350)
print(a,b)