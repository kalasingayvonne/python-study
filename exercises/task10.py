#TASK 10: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

#prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

def total_stock(products):
    total = 0
    for product in products:
        total += int(product[-1])
    return total

prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]

print(total_stock(prods))
