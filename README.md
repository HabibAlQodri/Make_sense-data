# Make Sense of Data with Analysis and AI

Alur analisis data lengkap dalam satu file: **EDA → standardisasi → PCA → KMeans (pilih k via silhouette) → insight teks otomatis**.
Dataset: *wine* (bawaan scikit-learn).

```bash
pip install numpy pandas scikit-learn matplotlib
python analisis_data.py
```
Keluaran: `insight.md` (ringkasan temuan dalam kalimat), `analisis_hasil.png`.

**Lanjutan:** ganti dengan CSV Anda, kirim `insight.md` ke LLM untuk narasi laporan, tambah deteksi outlier.
