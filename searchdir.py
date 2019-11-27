import os
import csv
import sys
import pandas as pd
import zipfile

def crawldir(rootdir):
    print('Searching...')
    data = []
    for r,d,f in os.walk(rootdir):
        for file in f:
            #informasi dasar file : path, file, size
            fullpath = os.path.join(r,file)
            content = []
            try:
                info = [r,file,str(os.path.getsize(fullpath))]
            except Exception :
                info = [r,file,'unk']
            if(zipfile.is_zipfile(fullpath)):
                info.append(True)
                a = zipfile.ZipFile(fullpath)
                for fz in a.namelist():
                    content.append([fullpath,a.getinfo(fz).filename,a.getinfo(fz).file_size,'isi'])
            else:
                info.append(False)
            data.append(info)
            data.extend(content)
    return data

def savefile(data):
    print('Saving to file...')
    name = 'index'
#    if sys.argv[2]:
#        name = 'index'+sys.argv[2]

    f = open(name+'.txt','w',encoding='utf-8')
    for i in data:
        f.write('\t'.join(i))
        f.write('\n')
    f.close()

#    #csv
#    with open(name+".csv","w",encoding="utf-8") as csvfile:
#        wr = csv.writer(csvfile)
#        wr.writerows(data)

if __name__ == "__main__":
    rootdir = os.getcwd()

#    if sys.argv[1]:
#        rootdir = sys.argv[1]

    data = crawldir(rootdir)

    df = pd.DataFrame(data)
    df.to_csv("index.csv")

#    savefile(data)
    print('Finished!')