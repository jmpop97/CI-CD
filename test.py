import pickle
import time
N=10**5
n=10**3

test=[i for i in range(N)]
record=[None for _ in range(N)]
while test:
    start= time.time()
    i=test[0]
    record[i]=time.time()-start
    test.pop()
record=record[::n]
record=record[::-1]

# record.append(time.time()-start)
with open("list_2.pkl","wb") as f:
    pickle.dump(record,f)
print("end")