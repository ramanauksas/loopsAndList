numbers = [1,5, 10]
print(numbers)

# 1 uzduotis
names = ["Audrius", "Giedre", "Aiste", "Agne"]
print(names[0], names[-1], len(names))

# 2 uzduotis
heights = [1.95, 1.80, 1.6, 1.45, 1.8, 2.0]
print(f"heights: {heights}; length: {len(heights)}")

# #  3 uzduotis
# attributes_str = input("Iveskite pozymiu sarasa, atskirdami tarpais:")
# attributes_list = attributes_str.split()
# print(f"Pozymiai: {attributes_list}; kiekis: {len(attributes_list)}")


# #  4 uzduotis
# town_list = ["Vilnius", "Kaunas", "Klaipeda"]
# initial_town_list = town_list[:]
# input_towns_str = input("Iveskite nauju miestu atskirdami kableliu: ")
# input_towns_list = input_towns_str.split(",")
# town_list.extend(input_towns_list)
# print(f"Pradinis miestu sarasas: {initial_town_list}\nPapildytas miestu sarasas: {town_list}")
# insert_town = input("Iterpkite nauja miesta: ")
# insert_position = int(input("Pasirinkite, kur iterpti: "))
# town_list.insert(insert_position, insert_town)
# print(f"Naujas miestu sarasas: {town_list}")


# # 5 uzduotis
# my_list = [1, 5, 10, 7, 8, 9, 12, 15]
# print(f"My initial list: {my_list}")
# my_list.pop(2)
# my_list.pop()
# print(f"My shortened list {my_list}")
# remove_num = int(input("Kiek irasu dar pasalinti? "))
# for i in range(0, remove_num):
#     my_list.pop()
# print(f"My final list: {my_list}")


# 6 uzduotis
my_list = [0, 1, 2, 3,]
if len(my_list)> 5:
    my_list.clear()
print(f"My list: {my_list}")


# # 7 uzduotis
# word_list = ["cia", "surasyti", "bet", "kokie", "zodziai"]
# word = input("Kokio zodzio ieskote: ")
# if word in word_list:
#     word_index = word_list.index(word)
#     print(f'Zodis "{word}" yra {word_index+1} vietoje sarase')
# else:
#     print(f'Zodzio "{word}" nera sarase')


# # 8 uzduotis
# grades = [10, 9, 8, 10, 9]
# print(f"Pazymiu sarasas: {grades}")
# new_grades_str=input("Iveskite dar du pazymius, atskirdami kableliu: ")
# new_grades_list=new_grades_str.split(",")
# new_grades_list = [int(grade) for grade in new_grades_list]
# grades.extend(new_grades_list)
# print(f"Studentas turi desimtuku: {grades.count(10)}")


# 9 uzduotis
car_brand_list = ["toyota", "honda", "hyundai", "mercedes"]
print(f"Automobiliu markes: {car_brand_list}")
car_brand_list.sort()
print(f"Automobiliu markes abeceline tvarka: {car_brand_list}")
car_brand_list.reverse()
print(f"Automobiliu markes mazejancia tvarka: {car_brand_list}")


# 10 uzduotis
grades = [6, 10, 9, 8, 9, 10, 8]
grades.sort()
print(f"Didziausi pazymiai: {grades[-3:]}")


#  11 uzduotis
grades = [6, 10, 9, 8, 9, 10, 3, 6, 2, 5, 4]
negative_grades_count = grades.count(1) + grades.count(2) + grades.count(3) + grades.count(4)
print(f"Neigiamu pazymiu skaicius: {negative_grades_count}")


#  12 uzduotis
my_list = [6, 10, 9, 8, 9, 10, 3, 6, 2, 5, 4]
print(f"masyvas: {my_list}")
print(f"Pirmi trys nariai: {my_list[:3]}")
print(f"Du nariai pradedant treciuoju: {my_list[3:3+2]}")
print(f"Paskutiniai keturi nariai: {my_list[-4:]}")
print(f"Kas antras narys pradedant treciuoju: {my_list[2::2]}")
my_list.reverse()
print(f"Atbuline tvarka: {my_list}")

# 13 uzduotis
grade_avgs = [2.5, 9, 8.5, 4.6, 7.8, 9.2, 8, 8.5]
grade_avgs.sort()
best_avgs = grade_avgs[-3:]
print(f"Studentu vidurkiai: {grade_avgs}")
print(f"Geriausi vidurkiai: {best_avgs}")

# # 14 uzduotis
# word_list = ["mano", "zodziu", "zodynas", "pradinis"]
# continue_loop = True
# while continue_loop:
#     new_word = input("Iveskite nauja zodi: ")
#     word_list.append(new_word)
#     word_list.sort()
#     print(f"Atnaujintas zodziu sarasas:{word_list}")
#     continue_loop = True if input("Ivesti nauja zodi (T/N)? ")=="T" else False

# 15 uzduotis
inventory = [("bulves", 10), ("duona", 15), ("miltai",9), ("sausainiai", 8), ("saldainiai", 4), ("gerimai",2), ("pienas",1)]
low_inventory_list = [item for item in inventory if item[1] < 5 ]
print(f"Prekes, kuriu likutis maziau nei penki: {low_inventory_list}")
inventory.sort(key=lambda x:x[1])
print(f"3 maziausi likuciai:{inventory[:3]}")

# Exercise 8





