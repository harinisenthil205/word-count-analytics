WORDWISE ANALYTICS - WORD COUNT MINI PROJECT

REQUIREMENTS
- Python 3.10 or later recommended
- Internet connection for Google Fonts and Chart.js CDN (the word count backend works without the chart CDN)

PROJECT STRUCTURE
word_count_website/
  app.py
  requirements.txt
  sample_dataset.txt
  templates/
    base.html
    index.html
    results.html
    about.html
  static/
    css/
      style.css

RUN ON WINDOWS (VS CODE TERMINAL / POWERSHELL)
1. Extract the ZIP file.
2. Open the extracted word_count_website folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:
      py -m venv venv
5. Activate it in PowerShell:
      .\venv\Scripts\Activate.ps1
   If activation is blocked, run this command for the current terminal only:
      Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   Then activate again.
6. Install Flask:
      python -m pip install -r requirements.txt
7. Start the website:
      python app.py
8. Open this address in your browser:
      http://127.0.0.1:5000
9. Paste text or upload sample_dataset.txt and click Analyze text.

IMPORTANT
- Keep app.py, templates, and static in the same project structure.
- Stop the local server with Ctrl+C in the terminal.
- This version runs on one computer. It demonstrates the Word Count algorithm but is not itself a distributed Hadoop/Spark cluster.
- For a classroom demonstration, explain Map -> Shuffle/Sort -> Reduce and then discuss how Hadoop/Spark can distribute these steps across machines.
