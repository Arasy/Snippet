import os
import csv
import sys

def crawldir(rootdir):
    print('Searching...')
    data = []
    for r,d,f in os.walk(rootdir):
        for file in f:
            try:
                data.append([r,file,str(os.path.getsize(os.path.join(r,file)))])
            except FileNotFoundError:
                data.append((r,file,'unk'))
    return data

def savefile(data):
    print('Saving to file...')
    name = 'index'
    if sys.argv[2]:
        name = 'index'+sys.argv[2]

    f = open(name+'.txt','w',encoding='utf-8')
    for i in data:
        f.write('\t'.join(i))
        f.write('\n')
    f.close()

    #csv
    with open(name+".csv","w",encoding="utf-8") as csvfile:
        wr = csv.writer(csvfile)
        wr.writerows(data)


if __name__ == "__main__":
    rootdir = os.getcwd()

    if sys.argv[1]:
        rootdir = sys.argv[1]

    data = crawldir(rootdir)
    savefile(data)
    print('Finished!')