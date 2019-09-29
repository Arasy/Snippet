import os

path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
dirpath = 'C:\\Windows\\System32\\drivers\\etc\\'
line = '127.0.0.1\t www.youtube.com'
lineoff = '# 127.0.0.1\t www.youtube.com'
f = open(path,'r').readlines()

def yton():
    #hapus baris terakhir
    with open(path,'r+') as file:
        file.seek(0, os.SEEK_END)
        pos = file.tell()-1
        while pos > 0 and file.read(1) != "\n":
            pos -= 1
            file.seek(pos, os.SEEK_SET)
        if pos > 0:
            file.seek(pos, os.SEEK_SET)
            file.truncate()
    
def ytoff():
    #ganti baris terakhir ke line
    with open(path,'a') as file:
        file.input(line)

if(f[-1]==lineoff):
    #kalau youtubenya sudah pernah diblok tapi lagi dikasih akses, tutup aksesnya
    #buka file dengan mode write, ganti baris terakhir ke line
    #repot ah, ganti baris terakhir ke line aja
    ytoff()
elif(f[-1]==line):
    #kalau youtubenya sedang diblok, buka aksesnya
    #buka file dengan mode write, hapus baris terakhir
    yton()
else:
    #kalo gak dua duanya berarti belum pernah diblok, blok aksesnya
    #buka file dengan mode write, tambahkan line ke baris terakhir
    ytoff()
    