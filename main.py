import re
import json
import docx2txt
import os

# clear console
os.system('cls' if os.name == 'nt' else 'clear')

# regex untuk memisahkan pertanyaan, pilihan jawaban, dan jawaban yang benar
regex = r'(\d+)\.\s+([\s\S]*?)\s+(a)\.\s+(.*?)\s+(b)\.\s+(.*?)\s+(c)\.\s+(.*?)\s+(d)\.\s+(.*?)\s+(e)\.\s+(.*?)\s+Jawaban\s+:\s+(.*?)\s+'

# regex untuk mengambil nomor artikel
regex_artikel = r'Artikel\s+(.*?)\s+:\s+([\s\S]*?)\s?\n\d+\.'
# Artikel\s(\d+)\s:\n(?:[\w\s.,-]+?\n)+?(?:\d+|$)

# regex untuk mengambil nomor gambar
regex_gambar = r'Gambar\s+(.*?)\s+:\s+'

# regex untuk mengambil nomor group soal
regex_group = r'Group soal\s+(.*?)\s+:\s+'

# membuka file yang berisi soal-soal
# text = docx2txt.process("Soal PPS Bagian 1.docx")

# extract text and write images in /tmp/img_dir
text = docx2txt.process("Soal PPS Bagian 1.docx",
                        "tmp/img_dir")


data_soal = []
data_artikel = []
data_gambar = []
data_group = []

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
    data_soal.append({
        "number": number,
        "question": question,
        "options": options,
        "answer": answer
    })

# menyimpan data_soal soal dalam format json ke dalam file
with open("soal.json", "w") as f:
    json.dump(data_soal, f)


# mencari semua data artikel menggunakan regex
matches = re.findall(regex_artikel, text, re.DOTALL)

# mengonversi data artikel menjadi format json
for match in matches:
    data_artikel.append({
        "number": match[0],
        "artikel": match[1]
    })

# menyimpan data_artikel artikel dalam format json ke dalam file
with open("artikel.json", "w") as f:
    json.dump(data_artikel, f)

# mencari semua data gambar menggunakan regex
matches = re.findall(regex_gambar, text, re.DOTALL)

# mengonversi data gambar menjadi format json
for index, match in enumerate(matches):
    data_gambar.append({
        "number": match,
        "image": f"image{index+1}.png"
    })

# menyimpan data_gambar gambar dalam format json ke dalam file
with open("gambar.json", "w") as f:
    json.dump(data_gambar, f)

# mencari semua data group soal menggunakan regex
matches = re.findall(regex_group, text, re.DOTALL)
list_data_group = []

# mengonversi data group soal menjadi format json
for match in matches:
    listGroup = []
    start = int(match.split("-")[0])
    end = int(match.split("-")[1])
    for group in range(start, end+1):
        list_data_group.append(group)
        listGroup.append(group)
    data_group.append(listGroup)

# menyimpan data_group group soal dalam format json ke dalam file
with open("group.json", "w") as f:
    json.dump(data_group, f)


for index, soal in enumerate(data_soal):
    check_in_group = False
    if int(soal["number"]) in list_data_group:
        check_in_group = True
    else:
        check_in_group = False
    if check_in_group == False:
        data_group.append([int(soal["number"])])
data_test = []

print(data_group)
print(data_artikel)
print(data_gambar)

format_group_soal = [{
    "group": {
        "artikel": "",
        "gambar": "",
        "soal": []
    },
}]
panjang_group = len(data_soal) - len(data_group)
for i in range(panjang_group):
    data_test.append(format_group_soal)


# print(json.dumps(data_test, indent=4))
