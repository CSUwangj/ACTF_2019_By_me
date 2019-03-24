import os

for i in os.scandir("."):
    if not i.is_dir():
        continue
    open(i.path + "/README.md", "w").close()
    open(i.path + "/PROBLEM.md", "w").close()
    open(i.path + "/HINTS.md", "w").close()
    os.mkdir(i.path + "/src")
    os.mkdir(i.path + "/rel")
    os.mkdir(i.path + "/sol")
    open(i.path + "/sol/README.md", "w").close()
    
