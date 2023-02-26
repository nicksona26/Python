def dupKey(adict):
    vals = adict.values()
    prevElements = []
    count = 0
    for element in vals:
        prevElements.append(element)
    set1 = set(prevElements)
    len1 = len(prevElements)
    len2 = len(set1)
    if len1 != len2:
        return False
    else:
        return True
    
def main():
    adict = {'Joe':'Smith','Kait':'Brown','Ashley':'Brown'}
    print(adict)
    print(dupKey(adict))


main()
