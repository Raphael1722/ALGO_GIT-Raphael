def bubblesort(zahlen):
    i = len(zahlen)
    while i >=1 :
        for j in range(len(zahlen)-1):
            if zahlen[j] > zahlen[j+1]:
                einfachSo = zahlen[j]
                zahlen[j] = zahlen[j+1]
                zahlen[j+1] = einfachSo
        i = i - 1
    return zahlen

meineUnordnung = [2,99,45,14,8,5,23,1,25,9,4,6,345,54,69,]
ich_YB_Ordnung = bubblesort(meineUnordnung)

print (ich_YB_Ordnung)
#Es probierte die 15  zehnte stelle auszulesen welche es nicht gibt
#einfachso ist ein zwischen speicher
#man kann einfach das > zu < machen