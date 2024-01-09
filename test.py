import pickle
import time
N=10**5
n=10**3

test=[i for i in range(N)]

# record.append(time.time()-start)
with open("list_3.pkl","wb") as f:
    pickle.dump(test,f)
print("hello world")