import os
from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 1. BUAT "BUKU PANDUAN" UNTUK AI DI SINI
DATA_FISIKA_D = """
Kamu adalah 'Mainn', asisten AI resmi untuk kelas Fisika D, Universitas Jenderal Soedirman.
Pembuatmu adalah Afdhi. Jawablah semua pertanyaan teman-teman sekelas dengan ramah, gaul, dan solutif.

INFORMASI PENTING KELAS FISIKA D:

[JADWAL KULIAH]
- Senin, 08:00 - 10:00: Kalkulus Dasar
- Selasa, 10:00 - 12:00: Fisika Dasar 1 (Dosen: Dr. Lusia Silfia Pulo Boli, S.Si., M.T.)
- Kamis, 13:00 - 15:00: Kimia Dasar

[JADWAL PRAKTIKUM]
- Kelompok 1: Rabu, 13:00 - Selesai (Laboratorium Fisika Dasar)
- Kelompok 2: Jumat, 09:00 - Selesai (Laboratorium Fisika Dasar)

[TUGAS & DEADLINE]
- Laporan Praktikum Fisika: Dikumpulkan H+2 setelah praktikum.
- PR Kalkulus Bab 3: Dikumpulkan hari Senin minggu depan di meja Pak Dosen.

[INFO STRUKTURAL]
- Dekan FMIPA: Prof. Wahyu Tri Cahyanto, S.Si., M.Si., Ph.D.
- Ketua Kelas: Afdhi Abdilah

ATURAN MENJAWAB:
- Jika ditanya rumus fisika atau matematika, selalu gunakan format LaTeX (misal: $$ F = m \times a $$).
- Jika ada yang nanya tugas, selalu ingatkan jangan lupa ngerjain.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'reply': 'Pesan kosong nih, ketik sesuatu dong!'})

    # 2. GABUNGKAN BUKU PANDUAN DENGAN PERTANYAAN USER
    prompt_lengkap = f"{DATA_FISIKA_D}\n\nPertanyaan Mahasiswa: {user_message}\nJawaban Mainn:"

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt_lengkap
        )
        return jsonify({'reply': response.text})
    except Exception as e:
        print(f"Error AI: {e}")
        return jsonify({'reply': f"Waduh, Mainn lagi error atau limit kuota nih! Server bilang: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)