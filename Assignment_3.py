attendance=[1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
total=len(attendance)
count=0
for at in attendance:
  if at==0:
    count+=1
print("No.of Absent days:",count)
  
count1=0
for at in attendance:
 if at==1:
  count1+=1
print("No.of Present days",count1)
 # Attendance Percentage
percentage=count1/total*100
print("Attendance Percentage is:",percentage)
#Eligibility
if percentage>=75:
  print("Eligible")
else:
  print("Not Eligible")
