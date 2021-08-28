import random

GT_FILENAME = "Fictional_Ground_Truth.txt"
FS_FILENAME = "Fictional_System.txt"

def fictionalSystem():
    filename = "Fictional_System.txt"
    sorted_ratings = []
    for num in range(1, 1001):
        rating = round(random.uniform(0.67, 0.99), 2)
        sorted_ratings.append(rating)
    sorted_ratings.sort(reverse=True)

    f = open(filename, "w+")
    for idx, rating in enumerate(sorted_ratings):
        f.write("doc{} {}\n".format(idx+1,rating))
    f.close()

def groundTruthFile():
    f = open(GT_FILENAME, "w+")
    for num in range(1, 1001):
        rating = random.randint(0, 1)
        f.write("doc{} {}\n".format(num,rating))
    f.close()

def total_precision():
    filelines = open(GT_FILENAME, "r").readlines()
    num_rel = 0
    total_doc = 0
    for line in filelines:
        rating = line.split(" ")[1]
        if rating == "1\n":
            num_rel += 1
        total_doc += 1
    precision = round(num_rel / total_doc, 2)
    print("The total precision is: {}".format(precision))

def precision_at_k():
    filelines = open(GT_FILENAME, "r").readlines()
    try: 
        k = int(input("How many documents from 1-1000 to calculate precision@k: "))
    except:
        print("Did not write a proper answer. Try again.")

    num_rel = 0
    total_doc = 0
    for line in filelines[:k]:
        rating = line.split(" ")[1]
        if rating == "1\n":
            num_rel += 1
        total_doc += 1
    precision = round(num_rel / total_doc, 2)
    print("The precision is: {} from {} documents".format(precision, k))

def average_precision():
    filelines = open(FS_FILENAME, "r").readlines()
    total_doc = 0
    total_ratings = 0
    for line in filelines:
        rating = line.split(" ")[1]
        total_ratings += float(rating)
        total_doc += 1
    ans = round(total_ratings/total_doc, 2)
    print("The average precision is: {} from {} documents".format(ans, "1000"))

try: 
    choice = str(input("Type 1 for total precision, 2 for precision@k, and 3 for average precision: "))
except:
    print("You did something wrong, please try again.")

if choice == "1":
    total_precision()
elif choice == "2":
    precision_at_k()
else:
    average_precision()