"""f=open('sets.py','a')
f.write("hello world ")
f.close()"""

f=open("exp.py","r")
print(f.read())
f.close()

f=open("exp.py","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()

f=open("exp.py","w")
lines=["line1\n","line2\n","line3"]
f.writelines(lines)
f.close()