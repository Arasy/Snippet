# -*- coding: utf-8 -*-

import os
import csv
import sys
import pandas as pd
import zipfile
from datetime import datetime

def crawldir(rootdir):
    global log
    print('Building folder list...')
    log.append([datetime.now(),'Building folder list'])
    data = []
    oswalk = os.walk(rootdir)
    lenwalk = len(list(oswalk))
    print('Info : %d folder' % lenwalk)
    log.append([datetime.now(),'Info : '+str(lenwalk)+' folder'])
    c = 1
    for r,d,f in os.walk(rootdir):
        print('    %d/%d : %s \t %d dir,\t %d file'% (c,lenwalk,r,len(d),len(f)))
        log.append([datetime.now(),'{}/{} : {} \t {} dir,\t {} file'.format(c,lenwalk,r,len(d),len(f))])
        c=c+1
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
                #coba buka file zipnya
                try:
                    a = zipfile.ZipFile(fullpath)
                    for fz in a.namelist():
                        content.append([fullpath,a.getinfo(fz).filename,a.getinfo(fz).file_size,'isi'])
                except Exception:
                    print('        %s failed' % fullpath)
                    log.append([datetime.now(), fullpath+' failed'])
            else:
                info.append(False)
            data.append(info)
            data.extend(content)
    return data

if __name__ == "__main__":
    sall = datetime.now()
    rootdir = os.getcwd()
    directory = os.listdir(rootdir)

    global log
    log = []

    count=1
    for i in directory:
        try:
            if os.path.isdir(rootdir+'\\'+i):
                s = datetime.now()
                data = crawldir(rootdir+'\\'+i)
                m = 'Saving content of folder '+i+' to file index'+str(count)+'.csv'
                print(m)
                log.append([datetime.now(),m])
                df = pd.DataFrame(data)
                df.to_csv("index"+str(count)+".csv")
                f = datetime.now()
                print('    finished in '+str((f-s).seconds)+','+str((f-s).microseconds)+' seconds\n')
                log.append([datetime.now(),'Part '+str(count)+' finished in '+str((f-s).seconds)+','+str((f-s).microseconds)+' seconds'])
                count+=1
        except Exception:
            print('folder '+i+' gagal, reason : '+str(Exception))
            log.append([datetime.now(),'folder '+i+' gagal'])
    fall = datetime.now()
    print('Finished!')
    print('Total time '+str((fall-sall).seconds)+','+str((fall-sall).microseconds)+' seconds')
    log.append([datetime.now(),'Finished! Total time '+str((fall-sall).seconds)+','+str((fall-sall).microseconds)+' seconds'])
    pd.DataFrame(log).to_csv('log.csv')