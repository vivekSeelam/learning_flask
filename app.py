from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':"Data analyst",
        'location': "bangalore",
        'salary': '100,000'
    },
    {
        'id':2,
        'title':"Data analyst",
        'location': "bangalore",
        'salary': '100,000'
    },
    {
        'id':3,
        'title':"Data analyst",
        'location': "bangalore",
    },
    {
        'id':4,
        'title':"Data analyst",
        'location': "bangalore",
        'salary': '100,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name = "Vivek Inc")

@app.route('/jobs')
def return_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

