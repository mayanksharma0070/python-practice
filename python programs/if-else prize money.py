# a program to find the prize money awarded on basis of marks obtained
mark_sci=int(input("enter the marks of science: "))
mark_mat=int(input("enter the marks of math: "))
if(mark_sci>=80 and mark_mat>=80):
    print("congratulations.! you have won 10k")
elif(mark_sci>=80 and mark_mat<80):
    print("congratulations.! you have won 5k")
elif(mark_sci<80 and mark_mat>=80):
    print("congratulations.! you have won 5k")
else:
    print("try harder again.! ")