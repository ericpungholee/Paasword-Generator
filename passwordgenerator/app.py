from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key = ""

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST", "GET"])
def password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"
    special = ["@", "#", "$", "%", "&", "*", "."]
    numerics = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        length = request.values.get("Length")
        if length.isnumeric():
            length = int(length)
            if length > 0:
                break
            else:
                flash("Too short")
                return render_template("index.html")
        else:
            flash("Wrong Input")
            return render_template("index.html")


    while True:
        specialLen = request.values.get("Special Charchter")
        if specialLen.isnumeric():
            specialLen = int(specialLen)
            if specialLen < 0 or specialLen > length:
                flash(f"Wrong Input")
                return render_template("index.html")
            else:
                break
    while True:
        numofnum = request.values.get("Numeric")
        if numofnum.isnumeric():
            numofnum = int(numofnum)
            if numofnum < 0 or numofnum > length or  numofnum > (length - specialLen): 
                flash(f"Wrong Input")
                return render_template("index.html")
            elif length - specialLen == 0: 
                break
            else:
                break

    password = []
    if length == 1:
        lst = [chars, special, numerics]
        password.append(random.choice(random.choice(lst)))
        password = ''.join(str(e) for e in password)
        flash(f"Password: {password}")
        return render_template("index.html")
    else:
        noc = length - specialLen - numofnum
        password = []
        password += random.choices(chars, k=noc)
        password += random.choices(special, k=specialLen)
        password += random.choices(numerics, k=numofnum)
        random.shuffle(password)
        password = ''.join(random.sample(password, k=length))
        flash(f"Password: {password}")
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
