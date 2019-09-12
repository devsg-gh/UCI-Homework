import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#open the csvfile at the path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # skip the header
    #create list to append data as per the requirement
    calc_val =[] 
    new_val =[]
    ind_val =[]
    total =0
    #SG -try to convert this in to single line of code

  #read the data in to list and calcuate the Len of the list, sum of profit/losses
    for row in csvreader:
      ind_val.append(row[0])
      calc_val.append(row [1])
      total += int(row[1])
      n= len(calc_val)
      i= 0
    while i < n-1: #using loop, push the difference from one list to another to further calculate avg, max and min
        new_val.append(int(calc_val[i +1]) -int(calc_val[i]))
        i+=1
    
    changeavg=round(sum(new_val) / float(len(new_val)),2)
    maxval = max(new_val)
    minval =min(new_val)
    max_int= new_val.index(maxval) + 1
    min_int =new_val.index(minval) + 1
    #format the info and print them
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {n}')
    print(f'Total: ${total}')
    print(f'Average  Change: ${changeavg}')
    print(f'Greatest Increase in Profits: {ind_val[max_int]} (${maxval})')
    print(f'Greatest Decrease in Profits: {ind_val[min_int]} (${minval})')
   


   


    
