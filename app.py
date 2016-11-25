from flask import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bio')
def render_Bio():
    return render_template('bio.html')

@app.route('/resume')
def render_resume():
    return render_template('resume.html')

@app.route('/art')
def render_Art():
    return render_template('art.html')

@app.route('/music')
def render_Music():
    return render_template('music.html')


@app.route('/test_route')
def test():
    return 'WE GOT ROUTES!'

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)