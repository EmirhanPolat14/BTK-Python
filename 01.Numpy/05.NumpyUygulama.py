import numpy as np
# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
result = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
result = np.arange(5,15)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
result = np.arange(50,100,5)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
result = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
result = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
result = np.linspace(0,100,5)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
result = np.random.randint(10,30,5)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
result = np.random.randn(10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
result = np.random.randint(10,50,size=(3,5))

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?
satir,sütun = result.sum(axis=0), result.sum(axis=1) 
# print(result, satir, sütun)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
max, min, avg = result.max(), result.min(), result.mean()
# print(result)
# print(max, min, avg)

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?
# print(result.argmax())

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
arr = np.arange(10,20)
result = arr[:3]

# 14- Üretilen dizinin elemanlarını tersten yazdırın.
result = arr[::-1]

# 15- Üretilen matrisin ilk satırını seçiniz.
matris = np.random.randint(10,50,size=(3,5))
print(matris)
result = matris[0,:]

# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?
result = matris[2,3]

# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.
result = matris[:,0]

# 18- Üretilen matrisin her bir elemanının karesini alınız.
result = np.square(matris)

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? 
result = matris[(matris % 2 == 0) & (matris > 0)]

print(result)

