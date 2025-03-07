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
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: white;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .heart {
            color: red;
            font-size: 50px;
            animation: heartbeat 1s infinite alternate;
        }
        @keyframes heartbeat {
            from { transform: scale(1); }
            to { transform: scale(1.5); }
        }
        .container {
            margin-top: 50px;
            font-size: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        .heart-animated {
            width: 50px;
            height: 50px;
            background-color: red;
            clip-path: polygon(50% 15%, 100% 40%, 80% 90%, 50% 100%, 20% 90%, 0% 40%);
            animation: pulse 1s infinite alternate;
        }
        @keyframes pulse {
            from { transform: scale(1); opacity: 0.8; }
            to { transform: scale(1.3); opacity: 1; }
        }
        .form-container {
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
        input, button {
            padding: 10px;
            margin: 10px;
            border: none;
            border-radius: 5px;
        }
        button {
            background: red;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h2>Enter Names to See the Love Animation</h2>
    <div class="form-container">
        <form action="/" method="post">
            <input type="text" name="boy" placeholder="Boy's Name" required>
            <input type="text" name="girl" placeholder="Girl's Name" required>
            <button type="submit">Show Love</button>
        </form>
    </div>
    {% if boy and girl %}
        <div class="container">
            <span>{{ boy }}</span>
            <div class="heart-animated"></div>
            <span>{{ girl }}</span>
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
