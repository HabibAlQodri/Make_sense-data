# Insight otomatis

- Data: 178 sampel, 13 fitur, tanpa nilai kosong: True.
- 2 komponen PCA menjelaskan **55%** varians.
- Jumlah klaster terbaik (silhouette): **k=3** (skor 0.28); kecocokan dengan kelas asli ARI=0.90.
- Korelasi kuat: `total_phenols` ↔ `flavanoids` (r=+0.86).
- Korelasi kuat: `flavanoids` ↔ `od280/od315_of_diluted_wines` (r=+0.79).
- Korelasi kuat: `total_phenols` ↔ `od280/od315_of_diluted_wines` (r=+0.70).
- Klaster 0 (n=65): tinggi `hue` (+0.5σ), rendah `alcohol` (-0.9σ).
- Klaster 1 (n=51): tinggi `color_intensity` (+0.9σ), rendah `od280/od315_of_diluted_wines` (-1.3σ).
- Klaster 2 (n=62): tinggi `proline` (+1.1σ), rendah `alcalinity_of_ash` (-0.6σ).