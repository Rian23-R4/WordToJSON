import re
import json
import docx2txt

data = []
# regex untuk memisahkan pertanyaan, pilihan jawaban, dan jawaban yang benar
# regex = r'(\d+)\.\s+(.*?)\s+\n(a)\.\s(.*?)\s+\n(b)\.\s(.*?)\s+\n(c)\.\s(.*?)\s+\n(d)\.\s(.*?)\s+\n(e)\.\s(.*?)\s+\nJawaban\s:\s(\w)'
# regex = r'(\d+)\.\s(.*?)\s+(a)\.\s(.*?)\s+(b)\.\s(.*?)\s+(c)\.\s(.*?)\s+(d)\.\s(.*?)\s+(e)\.\s(.*?)\s+Jawaban\s:\s(\w)'
regex = r'(\d+)\.\s+(.*?)\s+(a)\.\s+(.*?)\s+(b)\.\s+(.*?)\s+(c)\.\s+(.*?)\s+(d)\.\s+(.*?)\s+(e)\.\s+(.*?)\s+Jawaban\s:\s+(.*?)\s+'
# (\d+)\.\s+(.*?)\s+(a)\.\s+(.*?)\s+(b)\.\s+(.*?)\s+(c)\.\s+(.*?)\s+(d)\.\s+(.*?)\s+(e)\.\s+(.*?)\s+Jawaban\s+?:\s+(.*?)\s+
# (\d+)\.?\s+(.*?)\s+(a)\.?\s+(.*?)\s+(b)\.?\s+(.*?)\s+(c)\.?\s+(.*?)\s+(d)\.?\s+(.*?)\s+(e)\.?\s+(.*?)\s+Jawaban\s+?:\s+(.*?)\s+

# membuka file yang berisi soal-soal
# text = docx2txt.process("Soal PPS Bagian 1.docx")

# extract text and write images in /tmp/img_dir
text = docx2txt.process("Soal PPS Bagian 1.docx",
                        "tmp\img_dir")


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
