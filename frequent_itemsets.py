import itertools
import numpy as np
from matplotlib import pyplot as plt



transactions = 0
for line in open('mushroom.dat').readlines(  ): transactions += 1

lst = []
with open('mushroom.dat') as f:
    for i in range(8124):
        x = f.readline()
        temp = x.split(' ')
        temp.pop(-1)
        lst.append(temp)
              
f.close()

arr = np.array(lst)

di = {}

for i in arr:
    for j in i:
        if j in di:
            di[j] += 1
        else:
            di[j] = 1



def get_itemsets(s):
    support = s
    L1 = []
    for key in di:
        if di[key] >= support:
            list = []
            list.append(key)
            L1.append(list)        
    
    #print(L1)
    #confidence = 70
    
    def apriori_gen(Lk_1, k):
        length = k
        Ck = []
        for list1 in Lk_1:
            for list2 in Lk_1:
                count = 0
                c = []
                if list1 != list2:
                    while count < length - 1:
                        if list1[count] != list2[count]:
                            break
                        else:
                            count += 1
                    else:
                        if list1[length - 1] < list2[length - 1]:
                            for item in list1:
                                c.append(item)
                            c.append(list2[length - 1])
                            if not has_infrequent_subset(c, Lk_1, k):
                                Ck.append(c)
                                c = []
        return Ck
    
    # function to compute 'm' element subsets of a set S 
    def findsubsets(S, m):
        return set(itertools.combinations(S, m))
    
    
    # has_infrequent_subsets function to determine if pruning is required to remove unfruitful candidates (c)
    # using the Apriori property, with prior knowledge of frequent (k-1)-itemset (Lk_1)
    
    def has_infrequent_subset(c, Lk_1, k):
        list = []
        list = findsubsets(c, k)
        for item in list:
            s = []
            for l in item:
                s.append(l)
            s.sort()
            if s not in Lk_1:
                return True
        return False
    
    # frequent_itemsets function to compute all frequent itemsets
    
    
    
    def frequent_itemsets():
        k = 2
        Lk_1 = []
        Lk = []
        L = []
        my_lst = []
        count = 0
        transactions = 0
        for item in L1:
            Lk_1.append(item)
        while Lk_1 != []:
            Ck = []
            Lk = []
            Ck = apriori_gen(Lk_1, k - 1)
            #print( "CANDIDATE %d-ITEMSET:" % k)
            #print( "Ck: %s" % Ck)
            #print ("------------------------------------------------------------------")
            for c in Ck:
                count = 0
                transactions = 0
                s = set(c)
                for T in arr:
                    transactions += 1
                    t = set(T)
                    if s.issubset(t) == True:
                        count += 1
                if count >= support:
                    c.sort()
                    Lk.append(c) 
            Lk_1 = []
            my_lst.append(len(Lk))
            print("FREQUENT %d-ITEMSET:" % k)
            print(Lk)
            print("------------------------------------------------------------------")
            for l in Lk:
                Lk_1.append(l)
            k += 1
            if Lk != []:
                L.append(Lk)
            
        return my_lst
    
    return frequent_itemsets()




lst_plot = []


for i in range(3000, 5001, 500):
    a = get_itemsets(i)
    lst_plot.append(a)
    
#print(lst_plot)

def get_arr(x):
    m = 0
    for i in x:
       if len(i) > m :
           m = len(i)
    #print(m)
    it = 0
    for i in x:
        if len(i)<m:
            for j in range(0, m-len(i)):
                #print(x[it])
                x[it].append(0)
        it += 1
    
    arr = np.asarray(x)
    arr1 = np.transpose(arr)
    return arr1

q = get_arr(lst_plot)


print(q, '\n')
for i in q:
    plt.plot(i)