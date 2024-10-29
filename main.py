# Liste örneği / List example
myList = [10, 20, "Python"]  # Farklı veri tiplerinden oluşan bir liste / A list with different data types
print("Başlangıçtaki liste: ", myList)  # Listeyi yazdırma / Print the initial list

# Değişken tanımlamaları / Variable definitions
x = 10
y = 20
z = "Python"
myList = [x, y, z]  # String ve değişkenleri içeren yeni bir liste / A new list containing variables and a string
print("Yeni liste: ", myList)  # Yeni listeyi yazdırma / Print the new list

# Liste ile ilgili temel işlemler / Basic list operations
print("Liste uzunluğu: ", len(myList))  # Liste uzunluğunu yazdırma / Print the length of the list
print("İlk eleman: ", myList[0])  # İlk elemanı yazdırma / Print the first element
print("Son eleman: ", myList[-1])  # Son elemanı yazdırma / Print the last element

# Listeye eleman ekleme / Adding an element to the list
myList.append("Javascript")  # Listenin sonuna "Javascript" ekleme / Add "Javascript" to the end of the list
print("Eleman eklendikten sonraki liste: ", myList)  # Eleman eklendikten sonraki listeyi yazdırma / Print the list after adding an element

# Liste elemanına erişim ve dilimleme / Accessing and slicing list elements
print("Dilim: ", myList[0:2])  # Liste dilimleme (ilk iki eleman) / List slicing (first two elements)

# Belirli bir değeri listeye ekleme / Inserting a specific value into the list
myList.insert(1, "Java")  # 1. indise "Java" ekleme / Insert "Java" at index 1
print("Java eklendikten sonraki liste: ", myList)  # Listeyi yazdırma / Print the list after inserting "Java"

# Liste elemanını silme / Removing an element from the list
myList.remove("Python")  # "Python" elemanını silme / Remove the element "Python"
print("Python silindikten sonraki liste: ", myList)  # Listeyi yazdırma / Print the list after removing "Python"

# Liste sonundaki elemanı çıkarma / Removing the last element
last_item = myList.pop()  # Son elemanı çıkarma ve saklama / Remove and store the last element
print("Son eleman çıkarıldı: ", last_item)  # Çıkarılan elemanı yazdırma / Print the removed element
print("Son eleman çıkarıldıktan sonraki liste: ", myList)  # Listeyi yazdırma / Print the list after removing the last element

# Listedeki belirli bir elemanın indeksi / Index of a specific element in the list
index_of_java = myList.index("Java")  # "Java"nın indeksini bulma / Find the index of "Java"
print("Java'nın indeksi: ", index_of_java)  # İndeksi yazdırma / Print the index

# Listedeki tüm elemanları temizleme / Clearing all elements in the list
myList.clear()  # Tüm listeyi temizleme / Clear all elements in the list
print("Liste temizlendikten sonraki hali: ", myList)  # Boş listeyi yazdırma / Print the cleared list
