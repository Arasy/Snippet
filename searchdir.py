import os
import csv

rootdir = os.getcwd()

print('Searching...')
data = []
for r,d,f in os.walk(rootdir):
    for file in f:
        try:
            data.append([r,file,str(os.path.getsize(os.path.join(r,file)))])
        except FileNotFoundError:
            data.append((r,file,'unk'))

print('Saving to file...')
f = open('index.txt','w')
for i in data:
    f.write('\t'.join(i))
    f.write('\n')
f.close()

#csv
with open("index.csv","w") as csvfile:
    wr = csv.writer(csvfile)
    wr.writerows(data)

print('Finished!')
