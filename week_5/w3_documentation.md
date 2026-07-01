# Week 5 Tutorial 5 Activity

## 1. Problem Statement
Write a Python program that helps calculate the customer's bill for a simple cafe menu. The program should allow the user to choose drinks, enter quantities, calculate the subtotal for each item, calculate the total amount, and print a receipt.

## 1.1 Define the problem
The program must solve the problem of producing a bill for a customer based on the selected drinks and quantities. It should be simple, interactive, and easy to understand.

## 1.2 What are the inputs?
The program takes the following inputs:
- Item name: Coffee or Tea
- Quantity of each drink
- Menu prices:
  - Coffee = RM 6.00
  - Tea = RM 12.00

## 1.3 What are the outputs?
The program produces the following outputs:
- A receipt that shows each selected item
- The quantity entered for each item
- The subtotal for each item
- The final total bill

## 1.4 What would be the typical process flow?
1. Display the menu with prices.
2. Ask the user to enter an item name.
3. Ask the user to enter the quantity.
4. Repeat until the user finishes adding items.
5. Calculate the total cost.
6. Print the receipt.

## 1.5 How do you decompose the problem into smaller tasks?
The problem can be divided into smaller tasks as follows:
- Display the menu.
- Collect the user order.
- Validate the item and quantity.
- Calculate the subtotal for each item.
- Calculate the final total.
- Print a receipt.

## 1.6 What are the constraints?
- Only two drink types are supported: Coffee and Tea.
- Quantity must be a positive whole number.
- The program should stop when the user enters "done".

## 2. Pseudocode
```text
DISPLAY the menu with item prices
INITIALIZE an empty order list
WHILE user has more items
    ASK for an item name
    IF item is not valid
        DISPLAY an error message
    ELSE
        ASK for quantity
        ADD item and quantity to the order
STOP when the user enters done
CALCULATE the total cost
PRINT the receipt
```

## 3. Code Implementation
The program has been implemented in the following files:
- main.py: contains the main program flow
- utils.py: contains helper functions for calculation and receipt printing

## 4. Challenge Summary
The challenge was to separate the logic into functions so that the main program stays simple. The helper functions are responsible for:
- calculating a subtotal
- calculating the final total
- printing the receipt
