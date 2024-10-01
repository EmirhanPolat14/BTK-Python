import pandas as pd

df = pd.read_csv("nba.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- Toplam kaç kayıt vardır ?
result = len(df.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
result = df["Salary"].sum() / (  len(df.index) - df["Salary"].isnull().sum() )

# 4- En yüksek maaşı ne kadardır ?
result = df["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?
result = df[df["Salary"] == df.Salary.max()]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["Age"] >= 20) & (df.Age <= 25)][["Name", "Team", "Age"]].sort_values(by="Age", ascending=False)

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = df[df["Name"]=="John Holland"]["Team"].values[0] # .iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = df.groupby("Team")[["Salary"]].mean().sort_values(by="Salary", ascending=False)

# 9- Kaç farklı takım mevcut ?
result = df["Team"].nunique()
# result = len(df.groupby("Team"))

# 10- Her takımda kaç oyuncu oynamaktadır ?
result = df.groupby("Team")["Name"].count()
# result = df["Team"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
result = df[(df["Name"].isnull()== False) & (df["Name"].str.contains("and"))] 

print(result)