from flask import Flask, render_template
import random

app = Flask(__name__)

# Some popular status codes with cats
STATUS_CODES = [200, 201, 204, 400, 401, 403, 404, 500, 502, 503]

@app.route('/')
def random_cat():
    code = random.choice(STATUS_CODES)
    cat_url = f"https://http.cat/{code}"
    return render_template('index.html', cat_url=cat_url, code=code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
