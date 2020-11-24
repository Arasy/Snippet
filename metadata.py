#bikin file csv isi data training
import os
import csv
import scipy.io.wavfile as wav

lokasi = os.getcwd()
namafile = "audio.csv"

listfile = os.listdir(lokasi)
data = [['file','length','id','framerate','speaker'],]
error = []
for i in listfile:
    try :
        #load file
        fs, y = wav.read(lokasi+'/'+i)
        #hitung length
        l = len(y)
        #parsing id dari nama file
        hid = i[0]
        #parsing speaker dari nama file
        s = i[2:6]
        #simpan ke list data
        data.append([i,l,hid,fs,s])
        print("add %s" % str(i))
    except Exception as e:
        #print exception, list file
        print("file %s error %s" % (i,e))
        error.append([i,e])
#masukkan ke file csv
with open(namafile,'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print("saved as %s" % namafile)
if error:
    with open("error.csv","w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(error)
    print("error saved as error.csv")