
def lam (fun , list):
    newlist =[]

    for i in list:
        newitem=fun(i)
        newlist.append(newitem)
    return newlist





mylist=[200,70,60,401,5033]

Result = lam(lambda x:x+x, mylist)

print(Result)