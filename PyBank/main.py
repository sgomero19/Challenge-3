import os
import csv
budget_path=r"C:\Users\balth\OneDrive\Desktop\Phyton\Challenge-3\PyBank\Resources\budget_data.csv"

#budget_path= os.path.join("..","Resources","budget_data.csv")
with open (budget_path) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    csv_header=next(csv_reader)
    firstrow=next(csv_reader)
    Previous_net= int(firstrow[1])

    Date=[]
    Profit_losses=[]
    Changes=[]
    Months_count=1
    for row in csv_reader:
     row_1=int(row[1])
     Date.append(row[0])  
     Profit_losses.append(row_1)
     Changes.append(int(row_1)-Previous_net)
     Previous_net=row_1

     Months_count+=1 
    Profit_losses_sum= sum(Profit_losses)
    Average_change= sum(Changes)/len(Changes)
    Greatest_increase_profit=max(Changes)
    Greatest_decrease_profit=min(Changes)
    Greatest_increase_date=Date[Changes.index(Greatest_increase_profit)]
    Greatest_decrease_date=Date[Changes.index(Greatest_decrease_profit)]
    

    print("Financial Analysis")
    print("------------------------------------------------")
    print(f"Total Months: {Months_count}\n")
    print(f"Total: ${Profit_losses_sum}\n")
    print(f"Average Change: ${round(Average_change,2)}\n")
    print(f"Greatest Increase in Profit: "+str(Greatest_increase_date)+"($"+str(Greatest_increase_profit)+")")
    print(f"Greatest Decrease in Profit: "+str(Greatest_decrease_date)+"($"+str(Greatest_decrease_profit)+")")

output_file = os.path.join("Analysis","budget_analysis.txt")
with open(output_file,'w') as text:
   f=open(output_file,"w+")
   f.write("-----------------------------------------\n")
   f.write("Financial Analysis\n")
   f.write(f"Total Months: {Months_count}\n")
   f.write(f"Total ${Profit_losses_sum}\n")
   f.write(f"Average change: ${Average_change}\n")
   f.write(f"Greatest Increase in Profit: {Greatest_increase_date} (${Greatest_increase_profit})\n")
   f.write(f"Greatest Decrease in Profit: {Greatest_decrease_date} (${Greatest_decrease_profit})\n")
   f.close()

           
    





   
           








    

     
