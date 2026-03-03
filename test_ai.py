import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Ambil kunci dari file .env yang aman
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("AI sedang berpikir...")
try:
    # KITA BALIK KE 2.5 FLASH! (Model terbaru yang pasti ada)
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents="Halo! Tolong beri satu kalimat semangat untuk mahasiswa cowok jurusan Fisika yang lagi asyik belajar coding Python."
    )
    print("JAWABAN AI:\n", response.text)
except Exception as e:
    print(f"Waduh, masih error nih: {e}")