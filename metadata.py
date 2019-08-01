#bikin file csv isi data training
import os
import csv
import scipy.io.wavfile as wav

lokasi = 'Clean'
listfile = os.listdir(lokasi)
data = [['file','length','id','framerate','speaker'],]
for i in listfile:
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
#masukkan ke file csv
with open('audio.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)


