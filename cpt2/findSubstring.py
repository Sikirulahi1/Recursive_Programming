def findSubstringIterative(Needle, Haystack):
    new = Haystack.split(" ")
    for i, n in enumerate(new):
        if n == Needle:
            return i
    
    return -1

