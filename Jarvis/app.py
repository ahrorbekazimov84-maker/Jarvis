from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get("message").lower()
    
    # Jarvisning javob mantiqi
    if "salom" in user_message:
        response = "Salom! Men Jarvisman. Sizga qanday yordam bera olaman?"
    elif "vaqt" in user_message:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"Hozir soat {now}"
    elif "eslatma" in user_message:
        response = "Eslatmani saqlab qo'ydim (Hozircha test rejimida)."
    else:
        response = "Kechirasiz, buni hali o'rganmadim. Lekin rivojlanyapman!"
        
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)