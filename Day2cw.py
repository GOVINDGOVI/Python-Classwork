head = """| BOOK STORE
RECIEPT |"""
print(head)

book1_name = "Python Basics"
book2_name = "Data Science intro"
book1_price = 450
book2_price = 600

book1_str = "The book Title is '{}' and the price is '{}'"
book2_str = "The book Title is '{}' and the price is '{}'"
book1_fr = book1_str.format(book1_name, book1_price)
book2_fr = book2_str.format(book2_name, book2_price)
print(book1_fr)
print(book2_fr) 

total_price = book1_price + book2_price
total_str = "The total price of the books = '{}'"
total_str_fr = total_str.format(total_price)
print(total_str_fr)

tq_msg = "Thank you for shopping with us!"
print(tq_msg)

full_reciept = "\t" + head + "\n" + book1_fr + "\n" + book2_fr + "\n" + total_str_fr + "\n" + "\t" + tq_msg
print(full_reciept)

print(full_reciept.upper())