import shelve

shop = shelve.open("shop_dpts")

# shop["electronics"] = {
#     "smartphones": ["IPhone 14 Pro", "Samsung Galaxy Note N7", "Huawei P50 Pro"],
#     "laptops": ["Macbook Pro", "Lenovo Legion", "HP", "Dell"],
#     "headphones": ["Earbuds", "Air Pods", "Marshall 2"]
# }
# shop["stationery"] = {
#     "books for school": ["textbooks", "workbooks"],
#     "other": ["pens", "rulers", "pencils"]
# }

for smartphone in shop["electronics"]["smartphones"]:
    print(smartphone)

print(shop["electronics"]["laptops"])

shop.close()