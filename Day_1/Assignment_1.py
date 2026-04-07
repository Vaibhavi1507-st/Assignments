expenses=[200, 150, 300, 400, 100, 250, 350]
total =sum(expenses)
print("Total:",total)
avg=total/len(expenses)
print("Average:",avg)
highest=max(expenses)
lowest=min(expenses)
print("Highest and Lowest:",highest,lowest)
count=0
for exp in expenses:
  if exp > avg:
     count+=1
print("Expenses above average:",count)
if total>1500:
  print("Savings Needed")
else:
  print("Within Budget")
