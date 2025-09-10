from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, letters, numbers, symbols):
    characters = ""
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        return "❌ Select at least one option!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length"))
        letters = request.form.get("letters") == "on"
        numbers = request.form.get("numbers") == "on"
        symbols = request.form.get("symbols") == "on"

        password = generate_password(length, letters, numbers, symbols)
    
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
