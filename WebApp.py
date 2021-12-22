from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
  return "Hello 2"

def run():
  app.run('0.0.0.0', '5902')

def keep_Alive():
  server = Thread(target=run)
  server.start()