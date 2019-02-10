import os
import csv

budget_data_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Resources', 'Bank_Output.txt')
output = open(output_path, 'w')

#output_path = os.path.join('OutPut', 'Bank_Output.txt')
Profit = [] #holds profit and losses
Difference = [] #finds change (profit/loss) btwn months ex. month2 - month1
Change = [] #used to find greatest increase/decrease
Month = [] #stores months so they can be matched up with greatest increase/decrease
header = """Financial Analysis
----------------------------"""
print(header)
print(header, file = output)

with open(budget_data_path, newline = '') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_reader)

    #print(f"CSV Header {csv_header}")

    count = 0 # for getting number of months
    total_profit = 0
    
    #Populate Profit and Month list
    for row in csv_reader:
        count += 1
        total_profit += int(row[1])
        Profit.append(row[1])
        Month.append(row[0])
       
    print(f"Total Months: {count}")
    print(f"Total: ${total_profit}")
    print(f"Total Months: {count}", file = output)
    print(f"Total: ${total_profit}", file = output)

    # store all values in profit into difference starting at index 1
    for i in range(1,len(Profit)): 
        diff = Profit[i]
        Difference.append(diff)
        

    # Find difference list
    change = 0 # for average change
    change2 = 0 #for greatest increase/decrease
    i = 0 #To iterate through profit list
    countList = 0 #to calculate average
    for diff in Difference:
        change += int(diff) - int(Profit[i]) #find a better way than i
        change2 = int(diff) - int(Profit[i])
        Change.append(change2)
        countList += 1
        i += 1
    
    #print average change after previous for loop calculated it   
    print(f"Average Change: ${round(change/countList,2)}")
    print(f"Average Change: ${round(change/countList,2)}", file = output) 
   
    #Find greatest increase and corresponding month
    max_value = 0
    i = 0
    for large in Change:
        if max_value < large:
            max_value = large
            month = Month[i + 1]
        i += 1
            
    print(f"Greatest Increase in Profits: {month} (${max_value}) ")
    print(f"Greatest Increase in Profits: {month} (${max_value}) ", file = output)

    #Find greatest decrease and corresponding month
    min_value = 0
    j = 0
    for small in Change:
        if min_value > small: 
            min_value = small
            month = Month[j + 1]
        j += 1
   
    print(f"Greatest Decrease in Profits: {month} (${min_value}) ")
    print(f"Greatest Decrease in Profits: {month} (${min_value}) ", file = output)
    output.close()


  
