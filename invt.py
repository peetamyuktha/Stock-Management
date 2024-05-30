import mysql.connector as sql

mycon = sql.connect(host="localhost", user="root", passwd="1234567", database="inventory")
cursor = mycon.cursor()

from prettytable import PrettyTable
from datetime import date

today = date.today()

while True:
    is_break = False
    login_option = int(input("Login:\n1.Admin\n2.Customer\n3.Supplier "))
    add_table_head = 1
    
    while True:
        if login_option == 1:
            admin_username = input("Enter Admin Username: ")
            admin_password = input("Enter Password: ")
            query = "SELECT COUNT(*) FROM admin WHERE id=%s AND pswd=%s"
            params = (admin_username, admin_password)
            cursor.execute(query, params)
            is_valid = cursor.fetchone()[0]
            while is_valid:
                action = int(input("What do you want to do:\n1.Check Stock\n2.Order Stock\n3.Exit "))
                if action == 1:
                    print("Existing stock")
                    cursor.execute("SELECT * FROM stock")
                    data = cursor.fetchall()
                    table = PrettyTable(['Sno', 'PID', 'PName', 'Price', 'Quantity'])
                    sno = 1
                    for row in data:
                        a, b, c, d = row
                        l = [sno, a, b, c, d]
                        table.add_row(l)
                        sno += 1
                    print(table)

                elif action == 2:
                    pid = int(input("Enter PID to Order: "))
                    quantity = int(input("Enter Quantity: "))
                    cursor.execute("INSERT INTO orders VALUES({}, {})".format(pid, quantity))
                    mycon.commit()
                    print("Order Placed Successfully")

                elif action == 3:
                    is_break = True
                    break
                else:
                    print("Wrong choice")
                    is_break = True
                    break
            if is_break:
                break
            else:
                print("Invalid User\n")
        
        elif login_option == 2:
            customer_username = input("Enter Customer Username: ")
            customer_password = input("Enter Password: ")
            query = "SELECT COUNT(*) FROM customer WHERE id=%s AND pswd=%s"
            params = (customer_username, customer_password)
            cursor.execute(query, params)
            is_valid = cursor.fetchone()[0]
            if is_valid == True:
                total_amount = 0
                print("Existing stock")
                cursor.execute("SELECT * FROM stock")
                data = cursor.fetchall()
                table = PrettyTable(['Sno', 'PID', 'PName', 'Price', 'Quantity'])
                sno = 1
                for row in data:
                    a, b, c, d = row
                    l = [sno, a, b, c, d]
                    table.add_row(l)
                    sno += 1;
                print(table)
                while True:
                    table = PrettyTable(['Sno', 'PID', 'PName', 'Price', 'Quantity'])
                    order_placed = False
                    enter_item_code = input("Enter PID to Add Cart || Enter F to Finish: ")
                    if enter_item_code != 'F':
                        order_placed = True
                        cursor.execute("SELECT * FROM stock WHERE pid=%s", (int(enter_item_code),))
                        data = cursor.fetchall()
                        for row in data:
                            sno = 1
                            a, b, c, d = row
                            l = [sno, a, b, c, d]
                            table.add_row(l)

                        print(table)
                        quantity = int(input("Enter Quantity: "))
                        remaining_in_stock = d - quantity
                        cursor.execute("UPDATE Stock SET Quantity={} WHERE pid={}".format(remaining_in_stock, int(enter_item_code)))
                        mycon.commit()
                        if add_table_head == 1:
                            checkout_table = PrettyTable(['Sno', 'PID', 'PName', 'Price', 'Quantity'])
                        add_table_head += 1
                        tablerow = [add_table_head - 1, a, b, c * quantity, quantity]
                        total_amount += c * quantity
                        checkout_table.add_row(tablerow)
                    else:
                        breakout = True
                        if order_placed == True:
                            print(checkout_table)
                            print("Total Amount to be Paid:", total_amount)
                            total_amount = 0
                        break
                if breakout == True:
                    break

            else:
                print("Invalid User\n")
        
        else:
            supplier_username = input("Enter Supplier Username: ")
            supplier_password = input("Enter Password: ")
            query = "SELECT COUNT(*) FROM supplier WHERE id=%s AND pswd=%s"
            params = (supplier_username, supplier_password)
            cursor.execute(query, params)
            is_valid = cursor.fetchone()[0]
            if is_valid == True:
                print("Remaining Orders")
                cursor.execute("SELECT * FROM orders")
                data = cursor.fetchall()
                table = PrettyTable(['Sno', 'PID', 'Quantity'])
                sno = 1
                for row in data:
                    a, b = row
                    l = [sno, a, b]
                    table.add_row(l)
                    sno += 1;
                print(table)

                supply = input("Supply y or no n: ")
                if supply == 'n':
                    break
                else:
                    enter_item_code = int(input("Enter PID to Supply: "))
                    cursor.execute("SELECT * FROM stock WHERE pid=%s", (int(enter_item_code),))
                    old_data = cursor.fetchone()
                    old_a, old_b, old_c, old_d = old_data
                    cursor.execute("SELECT * FROM orders WHERE pid=%s", (int(enter_item_code),))
                    data = cursor.fetchone()
                    a, b = data
                    cursor.execute("UPDATE Stock SET Quantity={} WHERE pid={}".format(b + old_d, enter_item_code))
                    mycon.commit()
                    cursor.execute("DELETE FROM orders WHERE pid={}".format(enter_item_code,))
                    mycon.commit()
            else:
                print("Invalid User\n")
                break
