def strcmp(a, b):
    i = 0
    j = 0
    while i != len(b) and j != len(a):
        if (b[i] == a[j]):
            i += 1
            j += 1
        elif (b[i] == '*'):
            if (b[i] == '*' and i < len(b)):
                i += 1
            if (b[i] != a[j] and j < len(a)):
                j += 1
        else:
            return "KO"
    return "OK"
      
print(strcmp("1234567890", "1*8*"))       
print(strcmp("1234567890", "1****5*"))       
print(strcmp("1234567890", "1**5*"))       
print(strcmp("1234567890", "1*"))       