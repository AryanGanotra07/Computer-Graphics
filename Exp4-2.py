import matplotlib.pyplot as plt  
  
   
# creating the dataset 
# data = {'Monday':20, 'Tuesday':15, 'Wednesday':30,  
#         'Thursday':35, 'Friday' : 0, 'Saturday' : 5, 'Sunday' : 20} 
keys = list(map(str, input("Enter keys: ").split()))
values = list(map(str, input("Enter values: ").split()))
courses = list(keys)
values = list(values) 
   
fig = plt.figure(figsize = (10, 5)) 
  
# creating the bar plot 
plt.bar(courses, values, color ='blue',  
        width = 0.4) 
  
# plt.xlabel("Weekdays") 
# plt.ylabel("No. of good produced") 
# plt.title("Goods produced on different weekdays") 
plt.show() 