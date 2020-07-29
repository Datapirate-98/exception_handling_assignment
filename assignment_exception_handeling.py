
1.
def excep():
    try:
        print(5/0)
    except Exception as e:
        print(f"{e} is not-defined")

excep()

2.
def gen(sub,verbs,objects):
        for i in sub:
            for j in verbs:
                for k in objects:
                    print(f"{i} {j} {k}")
                    

gen(["Americans","Indians"], ["play","watch"], ["Baseball","Cricket"])
