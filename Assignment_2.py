sales=[1200, 1500, 1100, 1800, 2000, 1700, 1600]
total=sum(sales)
print("Total:",total)
avg=total/len(sales)
print("Average:",avg)
highest=max(sales)
lowest=min(sales)
print("Highest and Lowest:",highest,lowest)
count=0
for sal in sales:
  if sal > avg:
    count+=1
print("Expenses above average:",count)
if avg>1700:
 print("Excellent Performance")
elif 1400<avg<1700:
   print("Good Performance") 
else:
   print("Average Performance")