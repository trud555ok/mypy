import os

# os.mkdir('dir_os')
os.makedirs('dz_os/papka1/papka2')
os.chdir('./dz_os')
fd = os.open("nant.py", os.O_CREAT)
os.close(fd)
os.chdir('./papka1')
fd = os.open("nant1111.py", os.O_CREAT)
os.close(fd)
fd = os.open("nant2222.py", os.O_CREAT)
os.close(fd)
os.chdir('./papka2')
fd = os.open("1111.py", os.O_CREAT)
os.close(fd)
fd = os.open("2222.py", os.O_CREAT)
os.close(fd)
os.chdir('./../../../')
print(os.getcwd())

for root, dirs, files in os.walk("dz_os"):
    # print(root, dirs, files)
    print(root)
    print('\t', dirs)
    print('\t', files)

