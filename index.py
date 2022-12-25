with open("sql.txt") as f:
    lib = f.read().split(',')
print("----------------------图书管理系统----------------------")
while True:
    s = 0
    for i in range(len(lib)):
        if "@" in lib[i] or "" == lib[i]:
            s += 1
            continue
        print(f'''
书籍展示：第{i+1}项：
    {lib[i]}              
                ''')
    if s == len(lib):
        print("\n没有书了哦")
    cmd = input('''
请输入命令
1:借书
2:还书
3:增加书籍
4:查询需还书籍
5:退出                
                ''')
    if cmd == "5":
        break
    elif cmd == "1":
        func = input("请问您是要通过名字还是通过项数获取书名(name/index)：")
        if func == "name":
            book = input("请输入书名：")
        elif func == "index":
            book = lib[int(input("请输入项数："))-1]
        else:
            cmd1 = input("没有这个命令，您是想退出吗（Y/N）")
            if cmd1 == 'Y':
                break
        username = input("请输入您的名字：")
        try:
            index = lib.index(book)
        except ValueError as e:
            print("这本书被人借走了哦", repr(e))
            continue
        lib.remove(lib[index])
        lib.append(book+"@"+username)
    elif cmd == "2":
        username = input("请输入您的名字：")
        book = input("请输入您要还的书籍名称：")
        s = 0
        for i in range(len(lib)):
            if book+"@"+username == lib[i]:
                s += 1
                lib[i] = lib[i].split("@")[0]
        if s == 0:
            print("用户名或书籍名有误！")
    elif cmd == "3":
        book = input("添加的书籍名字：")
        lib.append(book)
    elif cmd == "4":
        username = input("请输入您的名字：")
        print("您要还：")
        s = 0
        for i in lib:
            if "@"+username in i:
                s += 1
                print(i.split("@")[0])
        if s == 0:
            print("没有书可以还了")
    else:
        cmd1 = input("没有此命令，您是要退出吗？(Y/N)")
        if cmd1 == 'Y':
            break
    with open("sql.txt", 'w') as f:
        f.write(",".join(lib))
