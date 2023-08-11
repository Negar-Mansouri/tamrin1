# Q1

num = int(input("adad ra vared konid: "))
prime = 0
for i in range (0,num):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
               break
        else:
            print(i)
            primee = i + primee
print(prime)



# Q2
araye = ["a","a","a",2,3,"a",2,3,9,3]

def tedad(araye):
    result = {}
    
    for i in araye:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
            
    max_count = max(result.values())
    most_common_element = [key for key, value in result.items() if value == max_count]
    
    return most_common_element, max_count

most_common_element, max_count = tedad(araye)
print(most_common_element , ":" ,max_count )

        
        
    

    
    
       
# Q3

araye = input("araye ra vared konid: ")

result = []
for eleman in araye:
    tekrar = araye.count(eleman)
    if tekrar == 2 :
        # print(eleman)    
        result.append(eleman)
result = set(result)
print(result)

            
    
    
    
    
    

#Q4         


arr1 = input("arr1 ra vared konid:")
arr2 = input("arr2 ra vared konid:")


def gheyre_tekrar(arr1,arr2):
    gheyre_list = []
    
    for eleman in arr1:
        if eleman not in arr2:
            gheyre_list.append(eleman)
            
    for eleman in arr2:
        if eleman not in arr1 and eleman not in gheyre_list:
            gheyre_list.append(eleman)
            
    return gheyre_tekrar 

javab = gheyre_tekrar(arr1,arr2)
print(javab)







#Q5

reshte = input("reshte ra vared konid: ")
print(reshte.swapcase())



