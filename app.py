from flask import Flask, render_template ,jsonify

app = Flask(__name__)

JOBS = [
  {
    'Id' : 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'

  },
  {
    'Id' : 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'Id' : 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'Id' : 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html" ,jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)






