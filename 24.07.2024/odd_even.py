#Given an integer, , perform the following conditional actions:
#•	If  is odd, print Weird
#•	If  is even and in the inclusive range of  to , print Not Weird
#•	If  is even and in the inclusive range of  to , print Weird
#•	If  is even and greater than , print Not Weird

  n = int(input().strip())
  if n% 2!=0 or (n>=6 and n <= 20) and n% 2==0:
       print("Weird")
  elif n>=2 and n<=5 and n % 2==0 or n>20 and n% 2==0:
       print("Not Weird")
