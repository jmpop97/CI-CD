import pickle
import time
import sys
N=10**5
n=10**3

test=sys.argv[1:];

# record.append(time.time()-start)
with open("list_5.pkl","wb") as f:
    pickle.dump(test,f)

print("fail000",test)
