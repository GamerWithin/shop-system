from time import sleep

p = print
purchased = ...
itemcounter = 1
item1unitssold = 0
item2unitssold = 0
item3unitssold = 0
item4unitssold = 0
item5unitssold = 0


def checkaction():
    if action == "help":
        helpprint()
    if action == "stats":
        status()
    if action == "check":
        checkitem(input("NAME:"))
    if action == "add":
        add()


def checkitem(selectitem):
    if selectitem == item1name:
        p("____________________________________________________")
        p("name")
        p(item1name)
        p("price")
        p(item1price)
        p("units")
        p(item1units)
        p("units sold")
        p(item1unitssold)
        p("how much it cost to make")
        p(item1mfprice)
        p("____________________________________________________")
    if itemamount >= 2 and selectitem == item2name:
        p("____________________________________________________")
        p("name")
        p(item2name)
        p("price")
        p(item2price)
        p("units")
        p(item2units)
        p("units sold")
        p(item2unitssold)
        p("how much it cost to make")
        p(item2mfprice)
    if itemamount >= 3 and selectitem == item3name:
        p("name")
        p(item3name)
        p("price")
        p(item3price)
        p("units")
        p(item3units)
        p("units sold")
        p(item3unitssold)
        p("how much it cost to make")
        p(item3mfprice)
        p("____________________________________________________")
    if itemamount >= 4 and selectitem == item4name:
        p("____________________________________________________")
        p("name")
        p(item4name)
        p("price")
        p(item4price)
        p("units")
        p(item4units)
        p("units sold")
        p(item4unitssold)
        p("how much it cost to make")
        p(item4mfprice)
        p("____________________________________________________")
    if itemamount >= 5 and selectitem == item5name:
        p("____________________________________________________")
        p("name")
        p(item5name)
        p("price")
        p(item5price)
        p("units")
        p(item5units)
        p("units sold")
        p(item5unitssold)
        p("how much it cost to make")
        p(item5mfprice)
        p("____________________________________________________")


def helpprint():
    p("____________________________________________________")
    p("|ok                                                |")
    p("|                                                  |")
    p("|these are the commands                            |")
    p("|                                                  |")
    p("|for help type help                                |")
    p("|                                                  |")
    p("|to add purchase type add                          |")
    p("|                                                  |")
    p("|to see status type stats                          |")
    p("|                                                  |")
    p("|to check something about item type check          |")
    p("|                                                  |")
    p("|and if done using this just close the app         |")
    p("|                                                  |")
    p("____________________________________________________")


def add():
    p("which item was purchased, name first")
    purchase = input()
    p("how many")
    amount = int(input())
    if itemamount >= 1 and purchase == item1name:
        global item1units
        item1units -= amount
        global item1unitssold
        item1unitssold += amount
    if itemamount >= 2 and purchase == item2name:
        global item2units
        item2units -= amount
        global item2unitssold
        item2unitssold += amount
    if itemamount >= 3 and purchase == item3name:
        global item3units
        item3units -= amount
        global item3unitssold
        item3unitssold += amount
    if itemamount >= 4 and purchase == item4name:
        global item4units
        item4units -= amount
        global item4unitssold
        item4unitssold += amount
    if itemamount >= 5 and purchase == item5name:
        global item5units
        item5units -= amount
        global item5unitssold
        item5unitssold += amount
    p("added")


def status():
    if itemamount == 1:
        profit = 0
        earnings = 0
        units = item1units
        moneyworthstuff = item1price * item1units
        moneytooktomfg = item1mfprice * item1units
        profit -= moneytooktomfg + rent
        p("____________________________________________________")
        p(f"\nprofit  {profit}                                 ")
        p(f"\nearned  {earnings}                                ")
        p(f"\n{moneyworthstuff}  bucks worth stuff              ")
        p(f"\nunits in stock {units}                            ")
        p(f"\n{item1name} sold {item1unitssold}                 ")
        p("____________________________________________________")
    if itemamount == 2:
        profit = 0
        earnings = 0
        units = item1units + item2units
        moneyworthstuff = item1price * item1units + item2price * item2units
        moneytooktomfg = item1mfprice * item1units + item2mfprice * item2units
        totalunitssold = item2unitssold + item1unitssold
        profit -= moneytooktomfg and rent
        p("____________________________________________________")
        p(f"profit  {profit}")
        p(f"\nearned   {earnings}")
        p(f"\n{moneyworthstuff}  bucks worth stuff")
        p(f"\nunits in stock {units}")
        p(f"\n{item1name} sold {item1unitssold}")
        p(f"\n{item2name} sold {item2unitssold}")
        p(f"\n{item3name} sold {item3unitssold}")
        p(f"\n{item4name} sold {item4unitssold}")
        p(f"\n{item5name} sold {item5unitssold}")
        p(f"\ntotal units sold {totalunitssold}")
        p("____________________________________________________")
    if itemamount == 3:
        profit = 0
        earnings = 0
        units = item5units + item2units + item3units + item2units + item1units
        moneyworthstuff = item1price * item1units + item2price * item2units + item3price * item3units
        moneytooktomfg = item1mfprice * item1units + item2mfprice * item2units + item3mfprice * item3units
        totalunitssold = item3unitssold + item2unitssold + item1unitssold
        profit -= moneytooktomfg + rent
        p("____________________________________________________")
        p(f"profit  {profit}")
        p(f"\nearned  {earnings}")
        p(f"\n{moneyworthstuff} bucks worth stuff")
        p(f"\nunits in stock {units}")
        p(f"\n{item1name} sold {item1unitssold}")
        p(f"\n{item2name} sold {item2unitssold}")
        p(f"\n{item3name} sold {item3unitssold}")
        p(f"\ntotal units sold {totalunitssold}")
        p("____________________________________________________")
    if itemamount == 4:
        profit = 0
        earnings = 0
        units = item4units + item3units + item2units + item1units
        moneyworthstuff = item1price * item1units + item2price * item2units + item3price * item3units + \
                          item4price * item4units
        moneytooktomfg = item1mfprice * item1units + item2mfprice * item2units + item3mfprice * item3units + \
                         item4mfprice * item4units
        totalunitssold = item4unitssold + item3unitssold + item2unitssold + item1unitssold
        profit -= moneytooktomfg + rent
        p("____________________________________________________")
        p(f"profit  {profit}")
        p(f"\nearned  {earnings}")
        p(f"\n{moneyworthstuff}  bucks worth stuff")
        p(f"\nunits in stock {units}")
        p(f"\n{item1name} sold {item1unitssold}")
        p(f"\n{item2name} sold {item2unitssold}")
        p(f"\n{item3name} sold {item3unitssold}")
        p(f"\n{item4name} sold {item4unitssold}")
        p(f"\ntotal units sold {totalunitssold}")
        p("____________________________________________________")
    if itemamount >= 5:
        profit = 0
        earnings = 0
        units = item5units + item4units + item3units + item2units + item1units
        moneyworthstuff = item1price * item1units + item2price * item2units + item3price * item3units + \
                          item4price * item4units + item5price * item5units
        moneytooktomfg = item1mfprice * item1units + item2mfprice * item2units + item3mfprice * item3units + \
                         item4mfprice * item4units + item5mfprice * item5units
        totalunitssold = item5unitssold + item4unitssold + item3unitssold + item2unitssold + item1unitssold
        profit -= moneytooktomfg + rent
        p("____________________________________________________")
        p(f"profit  {profit}")
        p(f"\nearned  {earnings}")
        p(f"\n{moneyworthstuff}  bucks worth stuff")
        p(f"\nunits in stock {units}")
        p(f"\n{item1name} sold {item1unitssold}")
        p(f"\n{item2name} sold {item2unitssold}")
        p(f"\n{item3name} sold {item3unitssold}")
        p(f"\n{item4name} sold {item4unitssold}")
        p(f"\n{item5name} sold {item5unitssold}")
        p(f"\ntotal units sold {totalunitssold}")
        p("____________________________________________________")


# start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
p("hi welcome to shop management app, created by Shujat A")
sleep(2)
p("before you start using it i need some info")
sleep(1.5)
p("ok lets start")
sleep(0.7)
p("whats your shop name")
shopName = input("ShopName:")
sleep(2)
p("do you pay rent for your shop")
p("if no type 0")
rent = int(input("Rent:"))
p("how many items do you sell,  max 5 if you want more than 5 ask shujat")
itemamount = int(input())
p(" almost there")
p("whats your item1 name")
item1name = input()
p(f"price of {item1name}")
item1price = int(input())
p(f"how much did it cost to manufacture {item1name}")
item1mfprice = int(input())
p(f"how many units of {item1name} do you have")
item1units = int(input())
if itemamount >= 2:
    itemcounter2 = 0
    p("whats your item2 name")
    item2name = input()
    p(f"price of {item2name}")
    item2price = int(input())
    p(f"how much did it cost to manufacture {item2name}")
    item2mfprice = int(input())
    p(f"how many units of {item2name} do you have")
    item2units = int(input())
    if itemamount >= 3:
        itemcounter3 = 0
        p("whats your item3 name")
        item3name = input()
        p(f"price of {item3name}")
        item3price = int(input())
        p(f"how much did it cost to manufacture {item3name}")
        item3mfprice = int(input())
        p(f"how many units of {item3name} do you have")
        item3units = int(input())

        if itemamount >= 4:
            itemcounter4 = 0
            p("whats your item4 name")
            item4name = input()
            p(f"price of {item4name}")
            item4price = int(input())
            p(f"how much did it cost to manufacture {item4name}")
            item4mfprice = int(input())
            p(f"how many units of {item4name} do you have")
            item4units = int(input())

            if itemamount >= 5:
                itemcounter5 = 0
                p("whats your item5 name")
                item5name = input()
                p(f"price of {item5name}")
                item5price = int(input())
                p(f"how much did it cost to manufacture {item5name}")
                item5mfprice = int(input())
                p(f"how many units of {item5name} do you have")
                item5units = int(input())



itemcounter = 1

sleep(1)
helpprint()
sleep(5)
# loop starts !DONT GO! ITS A MAZE
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
action = input()
checkaction()
