import sys


class Book:
    def __init__(self):
        self.books = []
        with open("sql.txt")as f:
            s = f.read().split(',')
            for i in s:
                if "@" in i:
                    continue
                self.books.append(i)

    def getBooks(self):
        return self.books

    def borrowBooks(self, name, book):
        try:
            self.books.remove(book)
            self.books.append(book+"@"+name)
        except Exception as e:
            print("用户名或书名有误！", repr(e))

    def bookReturn(self, name, book):
        if book+"@"+name in self.books:
            for i in self.books:
                if book+"@"+name == i:
                    self.books.remove(book+"@"+name)
                    self.books.append(book)
                    return True
        else:
            return False

    def addBook(self, book):
        self.books.append(book)

    def searchBook(self, name):
        s = 0
        ret = []
        for i in self.books:
            if name in i:
                s += 1
                ret.append(i.split("@")[0])
        if s == 0:
            return "没有书可以还了"
        return ret


class System:
    def __init__(self, book: Book):
        self.book = book
        self.books = self.book.getBooks()
        print("-------------------------------图书管理系统-------------------------------")

    def printBooks(self):
        s = 0
        for i in range(len(self.books)):
            if "@" in self.books[i] or '' == self.books[i]:
                continue
            s += 1
            print(f'''
书籍展示：第{i+1}项：
{self.books[i]}                  
                  ''')
        if s == 0:
            print("\n没有书了哦")


if __name__ == '__main__':
    book = Book()
    system = System(book)
    while True:
        system.printBooks()
        cmd = input('''
请输入指令:
1:借书
2:还书
3:添加书籍
4:查询需还书籍
5:退出
              ''')
        if cmd == "1":
            name = input("请输入您的名字")
            bookName = input("请输入书的名字")
            book.borrowBooks(name, bookName)
        elif cmd == "2":
            name = input("请输入您的名字")
            bookName = input("请输入书的名字")
            s = book.bookReturn(name, bookName)
            if s != True:
                print("用户名或书名有误")
        elif cmd == "3":
            bookName = input("请输入书的名字")
            book.addBook(bookName)
        elif cmd == "4":
            name = input("请输入您的名字")
            for i in book.searchBook(name):
                print(i)
        elif cmd == "5":
            sys.exit()
        else:
            continue
        with open("sql.txt", 'w')as f:
            f.write(",".join(book.getBooks()))
