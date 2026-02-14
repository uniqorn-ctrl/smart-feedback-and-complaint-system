from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (for hackathon demo)
complaints = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        issue = request.form["issue"]

        complaint = {
            "id": len(complaints) + 1,
            "name": name,
            "issue": issue,
            "status": "Pending"
        }

        complaints.append(complaint)
        return redirect(url_for("home"))

    return render_template("index.html", complaints=complaints)


@app.route("/resolve/<int:complaint_id>")
def resolve(complaint_id):
    for complaint in complaints:
        if complaint["id"] == complaint_id:
            complaint["status"] = "Resolved"
            break
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
