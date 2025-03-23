from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        with open("user_data.txt", "a") as file:
            file.write(f"Name: {name}, Email: {email}, Message: {message}\n")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
