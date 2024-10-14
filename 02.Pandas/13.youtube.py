import pandas as pd

df = pd.read_csv("youtube-ing.csv")


# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:10]

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result= df.columns.value_counts().reset_index()["index"]

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis=1, inplace=True)
result = df.columns.value_counts().reset_index()["index"]

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = df[["likes", "dislikes"]].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df.head(50)[["likes", "dislikes"]]

# 7- En çok görüntülenen video hangisidir ?
result = df[df.views == df.views.max()]["title"].values[0] #Nicky Jam x J. Balvin - X (EQUIS) | Video Oficial | Prod. Afro Bros & Jeon
result = df.sort_values(by= "views", ascending=False)["title"].values[0]

# 8- En düşük görüntülenen video hangisidir?
result = df[df.views == df.views.min()]["title"].values[0] # Mountain Bikers Worried About Military Land Being Fenced Off
result = df.sort_values(by="views")["title"].values[0]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values(by="views", ascending=False)["title"].head(10)

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id")[["likes"]].mean()

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id")[["comment_count"]].sum().sort_values(by="comment_count", ascending=False)

# 12- Her kategoride kaç video vardır ?
result = df.groupby("category_id")["title"].count()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] = df["title"].apply(len)
result = df.head()

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
df["tag_count"] = df["tags"].apply(lambda x:  len(x.split("|")))


# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

df["oran"] = df.apply(lambda x: x["likes"]/ (x["likes"] + x["dislikes"]) if x["likes"] + x["dislikes"] != 0 else 0 , axis=1)
result = df.sort_values(by="oran", ascending=False).head(10)

print(result) 
