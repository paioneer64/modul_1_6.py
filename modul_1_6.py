my_book = {"Катерина": "November 28", "Александр": "Februare 24", "Константин": "December 10", "Лев": "August 26",}
print(my_book)
print(my_book["Катерина"])
my_book ["Елена"] = "September 01"
print(my_book)
my_book.update({"Ксения": "November 08","Людмила": "April 19"})
print(my_book)
del my_book["Людмила"]
print(my_book.get("Людмила"))
print(my_book)

my_set_ = {2,2,2,1,1,5,"book", True, (4,6,7)}
print(my_set_)
list_ = (1,2,4,8,9)
list_ = set(list_)
print(list_)
print(list_.remove(8))
print(list_)
