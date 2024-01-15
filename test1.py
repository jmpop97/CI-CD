import pickle

with open("list_5.pkl","rb") as f:
    list1 = pickle.load(f)
print("test1",list1)