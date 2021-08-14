 #for reading csv file
import csv
# for calculating time taken
import time
# for calculating memory
import os, psutil
process = psutil.Process(os.getpid())
start=time.time()
# file after translated from english words to french words
fout2 = open("D:\\word translation\\translated file.txt","w")
dic = {}
freq = {}
#input of dictionary files
with open("D:\\word translation\\french_dictionary.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dic[row[0]] = row[1]
#input file of paragragraph given
initialfile = open("D:\\word translation\\t8.shakespeare.txt")
for line in initialfile:
    final_line = ""
    temp = ""
    for char in line:
        if char.isalpha():
            temp = temp + char
        else:
            if temp != "":
                if temp.lower() in dic:
                    if temp.lower() in freq:
                        freq[temp.lower()] += 1
                    else:
                        freq[temp.lower()] = 1

                    if temp.islower():
                        final_line = final_line + dic[temp.lower()].lower()
                    else:
                        if temp[1].islower():
                           final_line = final_line + dic[temp.lower()].capitalize()
                        else:
                            final_line = final_line + dic[temp.lower()].upper()
                else:
                    final_line = final_line + temp
            final_line = final_line + char
            temp = ""
    fout2.write(final_line)

header = ['english word', 'french word', 'frequency']
with open('frequency.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    
    for word in sorted(freq.keys()):
        data = [word, dic[word], freq[word]]
        writer.writerow(data)
end=time.time()
print("Runtime is:",end-start)
#print("memory is:",sys.getsizeof(""))

print("memory is:",process.memory_info().rss) 
