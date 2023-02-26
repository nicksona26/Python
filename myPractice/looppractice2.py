list = ["joe", "kyle", "gib", "frank", "amy", "", "yolanda", "greg"]
def name_adder(list):
    lst2 = []
    i = 0
    while i < len(list):
        if list[i] != "":
            lst2.append(list[i])
        i += 1
    return lst2  
print(name_adder(list))
