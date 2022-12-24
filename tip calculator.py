#program to find the tip
bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_p = tip / 100
total_tip = tip_p * bill
bill_t = bill + total_tip
split = bill_t / people #spliting bill between people
final_amt = round(split, 2)
final_amt=round(split,2)
print(f"each person should pay {final_amt}")
