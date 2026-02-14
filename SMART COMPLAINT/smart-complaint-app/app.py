from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

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


# Serve all other HTML pages from templates
@app.route("/<path:filename>")
def serve_page(filename):
    if os.path.exists(os.path.join("templates", filename)):
        return render_template(filename)
    return "404 Not Found", 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
