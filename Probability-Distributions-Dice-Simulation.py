# Gerekli kütüphaneleri içe aktaralım
import numpy as np
import matplotlib.pyplot as plt

# Tekrar üretilebilirlik için rastgele tohum belirleyelim
np.random.seed(42)

# ------------------------------ Bölüm 1: Olasılık Dağılımlarının Uygulanması ------------------------------

# Normal Dağılımdan rastgele veri üretme
data_normal = np.random.normal(loc=0, scale=1, size=1000)

# Poisson Dağılımından rastgele veri üretme
data_poisson = np.random.poisson(lam=3, size=1000)

# Üstel Dağılımdan rastgele veri üretme
data_exponential = np.random.exponential(scale=1, size=1000)

# Binom Dağılımdan rastgele veri üretme
data_binomial = np.random.binomial(n=10, p=0.5, size=1000)

# Pareto Dağılımdan rastgele veri üretme
data_pareto = np.random.pareto(a=2, size=1000)

# Üretilen dağılımları bir sözlükte saklayalım
distributions = {
    "Normal Dağılım": data_normal,
    "Poisson Dağılımı": data_poisson,
    "Üstel Dağılım": data_exponential,
    "Binom Dağılımı": data_binomial,
    "Pareto Dağılımı": data_pareto
}

# Her dağılımın histogramını çizelim ve ortalama ile varyansı hesaplayalım
for name, data in distributions.items():
    plt.figure(figsize=(6,4))
    plt.hist(data, bins=30, alpha=0.7, color='b', edgecolor='black', density=True)
    plt.title(f"{name} Histogramı")
    plt.xlabel("Değerler")
    plt.ylabel("Frekans")
    plt.grid(True)
    plt.show()
    
    print(f"{name} Ortalaması: {np.mean(data):.2f}, Varyansı: {np.var(data):.2f}")

# ------------------------------ Bölüm 2: 1000 Kez Zar Atımı ve Farklı Dağılımlar ile Simülasyon ------------------------------

# Klasik zar atımı (Eşit olasılıklı zar atımı)
zar_atimlari = np.random.randint(1, 7, 1000)

# Frekansları hesaplayalım
unique, counts = np.unique(zar_atimlari, return_counts=True)

# Klasik zar atımı sonucu çubuk grafiği
plt.figure(figsize=(6,4))
plt.bar(unique, counts, color='c', edgecolor='black')
plt.xlabel("Zar Yüzü")
plt.ylabel("Frekans")
plt.title("Klasik Zar Atımının Sonuçları")
plt.xticks(range(1, 7))
plt.grid(True)
plt.show()

# Normal Dağılım ile Zar Atımı
zar_normal = np.round(np.random.normal(3.5, 1, 1000)).astype(int)
zar_normal = np.clip(zar_normal, 1, 6)  # 1 ile 6 arasında sınırlandıralım

# Poisson Dağılımı ile Zar Atımı
zar_poisson = np.random.poisson(3, 1000)
zar_poisson = np.clip(zar_poisson, 1, 6)  # 1 ile 6 arasında sınırlandıralım

# Farklı dağılımların sonuçlarını karşılaştırmak için grafik çizelim
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Normal Dağılım Zar Atımı Grafiği
unique, counts = np.unique(zar_normal, return_counts=True)
axs[0].bar(unique, counts, color='m', edgecolor='black')
axs[0].set_title("Normal Dağılım ile Zar Atımı")
axs[0].set_xlabel("Zar Yüzü")
axs[0].set_ylabel("Frekans")

# Poisson Dağılımı Zar Atımı Grafiği
unique, counts = np.unique(zar_poisson, return_counts=True)
axs[1].bar(unique, counts, color='g', edgecolor='black')
axs[1].set_title("Poisson Dağılımı ile Zar Atımı")
axs[1].set_xlabel("Zar Yüzü")

plt.tight_layout()
plt.show()

# ------------------------------ Bölüm 3: 6'nın Gelme Olasılığını Artırma ------------------------------

# Ağırlıklı Zar Atımı ile 6'nın Gelme Olasılığını Artıralım
weights = [0.1, 0.1, 0.15, 0.15, 0.2, 0.3]  # 6 daha sık gelecek şekilde ayarladık
zar_hileli = np.random.choice([1, 2, 3, 4, 5, 6], p=weights, size=1000)

# Frekans analizini yapalım
unique, counts = np.unique(zar_hileli, return_counts=True)

# Hileli zar sonuçlarını çubuk grafiği ile gösterelim
plt.figure(figsize=(6,4))
plt.bar(unique, counts, color='r', edgecolor='black')
plt.xlabel("Zarın Yüzü")
plt.ylabel("Frekans")
plt.title("Hileli Zar Atımının Sonuçları (6'nın Olasılığı Artırıldı)")
plt.xticks(range(1, 7))
plt.grid(True)
plt.show()

# Hileli zarın yüzdelerini hesaplayalım
probabilities = counts / 1000
for num, prob in zip(unique, probabilities):
    print(f"{num}: %{prob * 100:.2f}")
