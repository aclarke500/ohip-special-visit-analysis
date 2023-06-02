import matplotlib.pyplot as plt

file_path = 'data.txt'
data = []
# Step 1: Open the file
with open(file_path, 'r') as file:
    # Step 2: Read all the lines
    lines = file.readlines()

    # Step 3: Iterate over the lines or perform desired operations
    for line in lines:
       data.append(line.strip())
results = {
    "nights":0,
    "weekdaysDaytime":0,
    "weekdaysEvening":0,
    "weekendOrHoliday":0
}
for d in data:
    for key in results:
        if d == key:
            results[key]+=1
            
plt.xlabel("Categories")
plt.ylabel("Occurences")
plt.title("Frequency of validity for column in OHIP special visit tables")
plt.bar(["nights", "weekdaytime", "weekevening", "weekends/holiday"], [results["nights"], results["weekdaysDaytime"], results["weekdaysEvening"], results["weekendOrHoliday"]])
plt.show()