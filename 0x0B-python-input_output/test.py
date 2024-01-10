import os 

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("some random text\nmore text\nand more")

with open("mydata.txt", encoding="utf-8") as myFile:
	print(myFile.read())
 
os.rename("mydata.txt", "md.txt")
# os.mkdir("whew")
os.chdir("whew")
print("Current Dir is :", os.getcwd())
os.chdir("..")
os.r('whew')


