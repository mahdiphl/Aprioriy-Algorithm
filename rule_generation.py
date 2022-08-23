import itertools
import numpy as np



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


support = 20
L1 = []
for key in di:
    if (100 * di[key] / transactions) >= support:
        list = []
        list.append(key)
        L1.append(list)        



## support in percent %
support = 80
L1 = []
for key in di:
    if (100 * di[key] / transactions) >= support :
        list = []
        list.append(key)
        L1.append(list)        


print(L1)

confidence = 70

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
my_lst = []


def frequent_itemsets():
    k = 2
    Lk_1 = []
    Lk = []
    L = []
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
            if (100 * count / transactions) >= support:
                c.sort()
                Lk.append(c)
        Lk_1 = []
        print("FREQUENT %d-ITEMSET:" % k)
        print(Lk)
        print("------------------------------------------------------------------")
        for l in Lk:
            Lk_1.append(l)
        k += 1
        if Lk != []:
            L.append(Lk)
        
    return L
# generate_association_rules function to mine and print all the association rules with
# given support and confidence value



def generate_association_rules():
    s = []
    r = []
    length = 0
    count = 1
    inc1 = 0
    inc2 = 0
    num = 1
    m = []
    L = frequent_itemsets()
    print("ASSOCIATION RULES:")
    print("RULES \t\t\t\t    SUPPORT   CONFIDENCE")
    for list in L:
        for l in list:
            length = len(l)
            count = 1
            while count < length:
                s = []
                r =  findsubsets(l, count)
                count += 1
                for item in r:
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []
                    for i in item:
                        s.append(i)
                    for T in arr:
                        if set(s).issubset(set(T)) == True:
                            inc1 += 1
                        if set(l).issubset(set(T)) == True:
                            inc2 += 1
                    if 100 * inc2 / inc1 >= confidence:
                        for index in l:
                            if index not in s:
                                m.append(index)
                        print("Rule#  %d : %s ==> %s %d %d" % (num, s, m, 100 * inc2 / len(arr), 100 * inc2 / inc1))
                        num += 1


generate_association_rules()


print('________________________________________')

print(my_lst)