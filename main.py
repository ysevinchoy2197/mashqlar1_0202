#1-misol
values = [12, 5, 8, 19, 3, 15]

eng_katta = max(values)
eng_kichik = min(values)

farqi = eng_katta - eng_kichik
index_eng_katta = values.index(eng_katta)

values.remove(eng_kichik)

print("Eng katta element:", eng_katta)

print("Eng kichik element:", eng_kichik)

print("Ularning farqi:", farqi)

print("Eng katta element indeksi:", index_eng_katta)

print("Yakuniy ro'yxat:", values)

#2-misol
words = ['apple', 'banana', 'cherry', 'date']

teskari = words[::-1]
print(words)
