from scrapping_IDX import scrape_companyprofile_idx
import time
start_time = time.time()

# ======== START ==========
# scrapping from IDX
# input name of emiten
emiten = ["AALI", "ABBA"]
data = scrape_companyprofile_idx(emiten)

# ======== FINISH ==========
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.2f} detik")
