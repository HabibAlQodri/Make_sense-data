"""Make Sense of Data: EDA -> PCA -> KMeans -> insight otomatis (dataset wine bawaan sklearn)."""
import numpy as np, pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

d = load_wine(as_frame=True); df, y = d.data, d.target
Z = StandardScaler().fit_transform(df)
pca = PCA(2).fit(Z); P = pca.transform(Z)
sil = {k: silhouette_score(Z, KMeans(k, n_init=10, random_state=0).fit_predict(Z)) for k in range(2, 7)}
k = max(sil, key=sil.get); lab = KMeans(k, n_init=10, random_state=0).fit_predict(Z)
corr = df.corr().where(np.triu(np.ones((13, 13), bool), 1)).stack()
top = corr.abs().sort_values(ascending=False).head(3).index
dev = (df.groupby(lab).mean() - df.mean()) / df.std()          # ciri khas tiap klaster
ins = ["# Insight otomatis\n", f"- Data: {df.shape[0]} sampel, {df.shape[1]} fitur, tanpa nilai kosong: {df.isna().sum().sum() == 0}.",
       f"- 2 komponen PCA menjelaskan **{pca.explained_variance_ratio_.sum():.0%}** varians.",
       f"- Jumlah klaster terbaik (silhouette): **k={k}** (skor {sil[k]:.2f}); kecocokan dengan kelas asli ARI={adjusted_rand_score(y, lab):.2f}."]
for a, b in top: ins.append(f"- Korelasi kuat: `{a}` ↔ `{b}` (r={corr[(a, b)]:+.2f}).")
for c in range(k):
    hi, lo = dev.loc[c].idxmax(), dev.loc[c].idxmin()
    ins.append(f"- Klaster {c} (n={np.sum(lab == c)}): tinggi `{hi}` ({dev.loc[c, hi]:+.1f}σ), rendah `{lo}` ({dev.loc[c, lo]:+.1f}σ).")
open("insight.md", "w").write("\n".join(ins)); print("\n".join(ins))
fig, ax = plt.subplots(1, 3, figsize=(16, 4.5))
ax[0].scatter(*P.T, c=lab, cmap="Set2", edgecolor="k", s=35); ax[0].set(title="PCA + klaster", xlabel="PC1", ylabel="PC2")
ax[1].plot(list(sil), list(sil.values()), "o-", color="#0072B2"); ax[1].set(title="Silhouette vs k", xlabel="k")
im = ax[2].imshow(df.corr(), cmap="RdBu_r", vmin=-1, vmax=1); ax[2].set(title="Korelasi fitur"); plt.colorbar(im, ax=ax[2])
plt.tight_layout(); plt.savefig("analisis_hasil.png", dpi=120)
