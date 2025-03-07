from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love Animation</title>
    <style>
        body { text-align: center; font-family: Arial, sans-serif; }
        .heart { color: red; font-size: 50px; animation: heartbeat 1s infinite alternate; }
        @keyframes heartbeat {
            from { transform: scale(1); }
            to { transform: scale(1.5); }
        }
        .container { margin-top: 50px; font-size: 24px; }
    </style>
</head>
<body>
    <h2>Enter Names to See the Love Animation</h2>
    <form action="/" method="post">
        <input type="text" name="boy" placeholder="Boy's Name" required>
        <input type="text" name="girl" placeholder="Girl's Name" required>
        <button type="submit">Show Love</button>
    </form>
    {% if boy and girl %}
        <div class="container">
            {{ boy }} <span class="heart">❤️</span> {{ girl }}
        </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def love_page():
    if request.method == 'POST':
        boy = request.form.get('boy')
        girl = request.form.get('girl')
        return render_template_string(HTML_TEMPLATE, boy=boy, girl=girl)
    return render_template_string(HTML_TEMPLATE, boy=None, girl=None)

if __name__ == '__main__':
    app.run(debug=True)
