from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("web.html") 

@app.route("/checkwall", methods=["POST", "GET"])
def checkwall():
  if request.method == "POST":
    user = request.form.get["user"]
    return redirect(url_for("user", usr=user))
  else:
    return render_template("login.html")  

@app.route("/<usr>", methods = ['POST'])
def user(usr):
  search_query = request.form.get("search_query")
  return f"<h1>{usr}</h1>" 

def check():
  bsc_url = 'https://bscscan.com/address/' + user
  bsc_result = (requests.get(bsc_url, headers=headers))
  bsc_doc = BeautifulSoup(bsc_result.text, "html.parser")
  bsc_bal = bsc_doc.find("div", {"class": "col-md-8"})
  bsc_bal_stripped = bsc_bal.text.strip()
  print(f"Balance from  BSC explorer: {bsc_bal_stripped}")  

if __name__ == "__main__":
  app.run(debug=True)