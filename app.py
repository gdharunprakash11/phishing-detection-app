from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            url = request.form.get("feature1")

            if url is None or url.strip() == "":
                result = "Enter URL ❗"
            else:
                url = url.strip().lower()

                # 🔥 RULE BASED DETECTION
                if "@" in url or "login" in url or "bank" in url or "verify" in url:
                    result = "Phishing ⚠️"
                else:
                    result = "Safe ✅"

        except Exception as e:
            print("ERROR:", e)
            result = "Invalid Input ❌"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)