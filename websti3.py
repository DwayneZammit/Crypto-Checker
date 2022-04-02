from flask import Flask, redirect, url_for, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


@app.route("/")
def home():
  return render_template("web.html") 

@app.route("/checkwall", methods=["POST", "GET"])
def checkwall():
  if request.method == "POST":
    user = request.form["nm"]
    return redirect(url_for("user", usr=user))
  else:
    return render_template("login.html")  

@app.route("/<usr>")
def user(usr):

  bsc_url = 'https://bscscan.com/address/' + usr
  bsc_result = (requests.get(bsc_url, headers=headers))
  bsc_doc = BeautifulSoup(bsc_result.text, "html.parser")
  bsc_bal = bsc_doc.find("div", {"class": "col-md-8"})
  bsc_bal_stripped = bsc_bal.text.strip()
  print(f"Balance from  BSC explorer: {bsc_bal_stripped}")
  
  eth_url = 'https://etherscan.io/address/' + usr
  eth_result = (requests.get(eth_url, headers=headers))
  eth_doc = BeautifulSoup(eth_result.text, "html.parser")
  eth_bal = eth_doc.find("div", {"class": "col-md-8"})
  eth_bal_stripped = eth_bal.text.strip()
  print(f"Balance from Ether scan: {eth_bal_stripped}")

  polygon_url = 'https://polygonscan.com/address/' + usr
  polygon_result = (requests.get(polygon_url, headers=headers))
  polygon_doc = BeautifulSoup(polygon_result.text, "html.parser")
  polygon_bal = polygon_doc.find("div", {"class": "col-md-8"})
  polygon_bal_stripped = polygon_bal.text.strip()
  print(f"Balance from Polygon: {polygon_bal_stripped}")

  snowtrace_url = 'https://snowtrace.io/address/' + usr
  snowtrace_result = (requests.get(snowtrace_url, headers=headers))
  snowtrace_doc = BeautifulSoup(snowtrace_result.text, "html.parser")
  snowtrace_bal = snowtrace_doc.find("div", {"class": "col-md-8"})
  snowtrace_bal_stripped = snowtrace_bal.text.strip()
  results = (f"BSC Balance is {bsc_bal_stripped}        ")
  results += (f"ETH Balance is {eth_bal_stripped}       ")
  results += (f"Polygon Balance is {polygon_bal_stripped}         ")
  results += (f"Polygon Balance is {snowtrace_bal_stripped}         ")
  return(results)


if __name__ == "__main__":
  app.run(debug=True)