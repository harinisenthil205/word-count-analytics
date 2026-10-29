from flask import Flask, render_template, request, Response
from collections import Counter
import re
import csv
import io

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB upload limit


def analyze_text(text):
    """Count words after converting to lowercase and extracting word tokens."""
    words = re.findall(r"\b[\w']+\b", text.lower(), flags=re.UNICODE)
    counts = Counter(words)
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "total_characters": len(text),
        "word_counts": sorted_counts,
        "top_words": sorted_counts[:10],
    }


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        text = request.form.get("text_data", "").strip()
        uploaded_file = request.files.get("dataset")

        if uploaded_file and uploaded_file.filename:
            if not uploaded_file.filename.lower().endswith(".txt"):
                error = "Please upload a .txt file."
            else:
                try:
                    text = uploaded_file.read().decode("utf-8-sig")
                except UnicodeDecodeError:
                    error = "The file must be saved as UTF-8 text."
        elif not text:
            error = "Enter some text or upload a .txt dataset."

        if not error:
            text = text.strip()
            if not text:
                error = "The dataset is empty. Please enter text or upload another file."
            else:
                results = analyze_text(text)
                return render_template("results.html", results=results)

    return render_template("index.html", error=error)


@app.route("/download")
def download():
    text = request.args.get("text", "")
    if not text.strip():
        return "No text was provided for download.", 400

    results = analyze_text(text)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Word", "Frequency"])
    writer.writerows(results["word_counts"])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=word_frequency.csv"},
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
