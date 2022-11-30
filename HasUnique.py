# Testing Sets and Lists

def isUnique(arr):
    # Use dict to keep track of repeats on @arr

    l = {}
    for a in arr:
        if a in l.keys():
            l[a] = l[a] + 1
        else:
            l[a] = 1
    
    # Check built Dict Counter
    print(str(l))
    
    # Check Values by Key to find repeats, if found return False, append to list 
    o = []
    for k in l:
        if l[k] in o:
            return False
        o.append(l[k])
    
    # No repeats found, return True
    return True

def main():
    arr = [1,2,2,1,1,3]
    print(isUnique(arr))


if __name__ == "__main__":
    main()