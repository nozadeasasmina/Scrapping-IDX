# Scrapping-IDX

Scrapping-IDX adalah proyek Python untuk melakukan scraping data dari situs resmi Indonesia Stock Exchange (IDX). 
Proyek ini bertujuan untuk mengumpulkan data company profile dari emiten secara otomatis, yang dapat digunakan untuk analisis data atau keperluan riset lainnya.
File scrapping akan disimpan dalam format JSON.

### 1. Clone repository

```bash
git clone https://github.com/nozadeasasmina/Scrapping-IDX.git
cd Scrapping-IDX
```

### 2. Install dependency

```bash
pip install -r requirements.txt
```

### 3. Add emiten name in main.py script
```bash
# if only one emiten
emiten = ["AALI"] 

# if having more than one emiten
emiten = ["AALI", "ABBA"]  
```

### 4. Run main script
```bash
python main.py
```