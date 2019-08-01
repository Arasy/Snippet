# Snippet
small piece of code

Ini beberapa kode python kecil yang saya buat yang bukan bagian dari project. Masing masing punya task spesifik yang bisa dimanfaatkan. Kayaknya sih ada yang lebih optimal, tapi nulis kode seperti ini juga jadi bagian dari latihan saya menuangkan ide ke kode.

### Metadata
file untuk menggenerate metadata file training dalam praktikum audio processing NLP. Data audio disimpan dalam folder tertentu, file akan memeriksa seluruh isi folder tersebut dan menggenerate informasi dari wavfilenya.

### Scrapvid
memanfaatkan urllib2, pytube, dan beautifulsoup untuk mendownload video berdasarkan playlistnya.

### Searchdir
menggunakan os.walk untuk mengambil index dari folder tree. yang dicatat adalah folder, nama file, dan ukurannya.
```bash
python searchdir.py C:\ Master
```
maka python akan mengambil seluruh file di bawah C:\ dan menuliskannya ke file IndexMaster.txt dan IndexMaster.csv

### SudokuQUBO
sudoku solver, menggunakan simulated annealing (memanfaatkan api digital annealernya Fujitsu). Hasil dari tantangan Quantum Computing https://www.topcoder.com/challenges/30081256
