import re
import json
import docx2txt

data = []
# regex untuk memisahkan pertanyaan, pilihan jawaban, dan jawaban yang benar
regex = r'(\d+)\.\s+(.*?)\s+(a)\.\s+(.*?)\s+(b)\.\s+(.*?)\s+(c)\.\s+(.*?)\s+(d)\.\s+(.*?)\s+(e)\.\s+(.*?)\s+Jawaban\s+:\s+(.*?)\s+'

# regex untuk mengambil nomor artikel
regex_artikel = r'Artikel\s+(.*?)\s+:\s+([\s\S]*?)\s?\n\d+\.'
# Artikel\s(\d+)\s:\n(?:[\w\s.,-]+?\n)+?(?:\d+|$)

# regex untuk mengambil nomor gambar
regex_gambar = r'Gambar\s+(.*?)\s+:\s+'

# membuka file yang berisi soal-soal
# text = docx2txt.process("Soal PPS Bagian 1.docx")

# extract text and write images in /tmp/img_dir
text = docx2txt.process("Soal PPS Bagian 1.docx",
                        "tmp/img_dir")


# mencari semua data soal menggunakan regex
matches = re.findall(regex, text, re.DOTALL)

# mengonversi data soal menjadi format json
for match in matches:
    number = match[0]
    question = match[1]
    options = {
        "a": match[3],
        "b": match[5],
        "c": match[7],
        "d": match[9],
        "e": match[11]
    }
    answer = match[12]

    # menambahkan data soal ke dalam variabel data
    data.append({
        "number": number,
        "question": question,
        "options": options,
        "answer": answer
    })

# menyimpan data soal dalam format json ke dalam file
with open("soal.json", "w") as f:
    json.dump(data, f)


# mencari semua data artikel menggunakan regex
matches = re.findall(regex_artikel, text, re.DOTALL)

# mengonversi data artikel menjadi format json
data = []
for match in matches:
    data.append({
        "number": match[0],
        "artikel": match[1]
    })

# menyimpan data artikel dalam format json ke dalam file
with open("artikel.json", "w") as f:
    json.dump(data, f)

# mencari semua data gambar menggunakan regex
matches = re.findall(regex_gambar, text, re.DOTALL)

# mengonversi data gambar menjadi format json
data = []
for index, match in enumerate(matches):
    data.append({
        "number": match,
        "image": f"image{index+1}.png"
    })

# menyimpan data gambar dalam format json ke dalam file
with open("gambar.json", "w") as f:
    json.dump(data, f)
