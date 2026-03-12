print("----------Movie Ticket System----------")
original_price = 15.00
try:
  number = int(input("Enter the number of tickets you want to purchase : "))
  membership = int(input("ARE YOU A MEMBER? (1 = YES, 0 = NO):"))

  if membership == 1 :
    print("get 20% discount")
  elif membership == 0 :
    print("The price remains RM15.")
  else :
    print("INVALID CHOICE")

  if number >= 3 :
    original_price = original_price * number + 5
    print("GET BIG POPCORN")
except:
  print("please enter the number only")
print("\n" * 10)
print("=======================================")
print(f"PRICE : RM{original_price:.2f}")
print("see you again!")
print("=======================================")
