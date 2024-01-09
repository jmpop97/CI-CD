import pickle

with open("list_3.pkl","rb") as f:
    list1 = pickle.load(f)
print(list1)