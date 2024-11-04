

#using split function to split user input according to space
#using map to convert each string to integer after splitting
nums = list(map(int, input("Enter  list of integers : ").split()))

#generate 2 lists
even=[]
odd=[]

#this function list user input and specify integers in 2 list even or odd
def special_rearrangement(nums):
   #this for loop to path all integers to if
   for num in nums:
      if num % 2 == 0:
         even.append(num)
      else:
       odd.append(num)

   return special_rearrangement(nums)
#print lists after function 
print(even)
print(odd)


   
   


    

   
    

