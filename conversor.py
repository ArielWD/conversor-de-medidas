import pandas as pd

def cm_a_inch(cm):
    return cm/2.54

df = pd.read_excel("muebles_medidas.xlsx")

df["Pulgadas"] = df["Centimetros"].apply(cm_a_inch)

df.to_excel("muebles_medidas_inch.xlsx", index=False)

print("Conversion Lista")
print("se ha creado el archivo muebles_medidas_inch.xlsx")