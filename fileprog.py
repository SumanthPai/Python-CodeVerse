def fun(name):
    numofword=0
    with open(name,"r") as file:
        for line in file:
            words=line.split("")
            numofwords=len(words)
            print("The number of words are =%d"%(numofword))
            print("The number of lines =%d"%(lines))

fun(input("Enter the file name : "))
