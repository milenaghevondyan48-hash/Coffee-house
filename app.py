from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {"name": "Cappuccino", "price": "1200 ֏", "description": "Սուրճ, կաթ և նուրբ փրփուր"},
    {"name": "Latte", "price": "1300 ֏", "description": "Նուրբ և կաթնային սուրճ"},
    {"name": "Americano", "price": "900 ֏", "description": "Դասական սև սուրճ"},
    {"name": "Cheesecake", "price": "1800 ֏", "description": "Թարմ և նուրբ չիզքեյք"},
    {"name": "Croissant", "price": "1000 ֏", "description": "Թարմ թխված կրուասան"},
    {"name": "Iced Coffee", "price": "1500 ֏", "description": "Սառը սուրճ՝ ամառային տրամադրությամբ"},
]

@app.route("/")
def home():
    return render_template("index.html", menu=menu)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Շնորհակալություն, {name}! Ձեր հաղորդագրությունը ստացվեց։"
    return render_template("contact.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)


