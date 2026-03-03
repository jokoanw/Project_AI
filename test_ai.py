from google import genai
# Ini API Key kamu
client = genai.Client(api_key="AIzaSyCc4n8BxlABh6F4N9dYYWZ4uGsE76Jrn4E")

print("AI sedang berpikir...")

# Kita panggil model AI terbaru menggunakan format client yang baru
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="Halo! Tolong beri satu kalimat semangat untuk mahasiswa cowok jurusan Fisika yang lagi asyik belajar coding Python."
)

print("Jawaban AI:")
print(response.text)
