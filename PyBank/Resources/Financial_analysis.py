import os
import csv

fanancial_analysis = os.path.join("budget_data.csv")

with open(fanancial_analysis, 'r') as Finances:
    reader=csv.reader(Finances) #delimiter=",")
    Header = next(Finances)
    print(Header)
    
    Total = 1
    date_count = []
    counter = 0
    daily_change = []

    original_list = date_count  # Replace this with your list of numbers
    differences = []
    positive = []
    negative = []
    Dates = []
    
    for i in reader:
        number = int(i[1])
        date_count.append(int(i[1]))
        
        Dates.append(i[0])
        counter += 1
        
        
        if number < 0:
            negative.append(number)
        else:
            positive.append(number)

    for i in range(len(original_list) - 1):
        difference = original_list[i + 1] - original_list[i]
        differences.append(difference)

        
        
    print("Financial Analysis")
    print("---------------------")
    print("Total Months:", counter)
    print("Total:",sum(date_count))
    print("Average Change:",round(sum(differences)/len(differences),2))
    print("Greatest Increase in Profits:" + str(Dates[differences.index(max(differences))+1]) + " ($"+str(max(differences))+")")
    print("Greatest Decrease in Profits:" + str(Dates[differences.index(min(differences))+1]) + " ($"+str(min(differences))+")")




    
    
