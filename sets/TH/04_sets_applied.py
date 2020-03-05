cs = {"Alice", "Bob", "Charlie", "Danielle"}
bio = {"Bob", "Ester", "Charlie", "Frank"}
math = {"Alice", "Charlie", "Gale", "Hank"}
french = {"Charlie", "Gale", "Isaac", "Jacob"}

cs_and_bio = cs & bio
print(cs_and_bio)

stem = cs | bio | math
print(stem)
