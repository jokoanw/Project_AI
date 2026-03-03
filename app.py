import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# API Key kamu
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route('/')
def home():
    # Ini akan memanggil file HTML kita nanti
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Ini instruksi khusus buat AI-nya biar bertingkah layaknya asisten ketua kelas!
    prompt = f"Kamu adalah Asisten Kelas yang pintar dan ramah untuk mahasiswa Fisika. Tugasmu membantu mengingatkan jadwal, tugas, dan materi kuliah. Jawablah pertanyaan berikut dengan bahasa yang asik. Pertanyaan: {user_message}"
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Waduh, ada error sistem: {str(e)}"}), 500

if __name__ == '__main__':
    # Menjalankan server web di laptopmu
    app.run(debug=True)