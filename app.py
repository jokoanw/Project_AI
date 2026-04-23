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
- Senin
- 07.00 - 08.45:Fisika Matematika (C3.05) 》 Mufli - Sugito
- 10.40 - 12.25:Bahasa Indonesia (A2.1) 》Bivit - Riyanto

Selasa
- 13.00 - 14.50:Algoritma dan Pemrograman (C2.04) 》 Wihan - Rizqi

Rabu 
- 07.00 - 08.45:Kewarganegaraan (B1.2) 》Kuni

Kamis
- 10.40 - 12.25:Mekanika 1 (C3.04) 》Kartika - Aris
- 13.00 - 15.40:Fisika Dasar 2 (C3.04) 》Mirda - Wihan

Jumat
- 08.50 - 10.35:Komunikasi Ilmiah (A2.2) 》Kartika - R Wahyu Wida
- 13.00 - 14.45:Termodinamika (C2.04) 》Ika - Efita

[JADWAL PRAKTIKUM]
- Kamis, 8.00 - 10.00: Praktikum Fisika Dasar 2

[TUGAS & DEADLINE]
- TUGAS TERSTRUKTUR - CBL - FISIKA MATEMATIKA - TUGAS KELOMPOK : deadline 25 April 2026 pukul 23:59 WIB

[INFO STRUKTURAL]
- Dekan FMIPA: Prof. Wahyu Tri Cahyanto, S.Si., M.Si., Ph.D.
- WakilKetua Kelas: Afdhi Abdilah
- Ketua Kelas : Reivan

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