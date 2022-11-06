def sort(str):
    lst=[str[i] for i in range(0,len(str))]
    lst.sort()
    return lst
def anagram(str1,str2):
    temp1=sort(str1)
    temp2=sort(str2)
    if temp1==temp2:
        print("Anagram")
    else:
        print("Not Anagram")
str1=input()
str2=input()
anagram(str1,str2)

#sample ip: Astronomer = moonstarer
#op:Anagram