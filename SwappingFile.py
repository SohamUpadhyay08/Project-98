def SwapFileData():
    file1 = input("please select file : ")
    file2 = input("please select file2 : ")
    f1 = open(file1,"r")
    data_a = f1.read()
    f2 = open(file2,"r")
    data_b = f2.read()
    f1 = open(file1,"w")
    f1.write(data_b)
    f2 = open(file2,"w")
    f2.write(data_a)

SwapFileData()
    