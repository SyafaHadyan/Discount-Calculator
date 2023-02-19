User_Input = float(input("Price:"))

Price = User_Input
Discount = 0


if Price <= 10:
    Discount = 0.10
  
elif Price <= 20:
    Discount = 0.15
  
elif Price <= 40:
    Discount = 0.20
  
elif Price <= 70:
    Discount = 0.25
  
elif Price >= 100:
    Discount = 0.30
  
Discount_Percentage = Discount * 100
Discount_Percentage = f"{Discount_Percentage}%"
Discounted_Price = Price * Discount
Discounted_Price = Price - Discounted_Price

print(f"Price: {Price}")
print(f"Discount: {Discount_Percentage}")
print(f"Discounted Price: {Discounted_Price}")
