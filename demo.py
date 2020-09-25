import json
from flask import Flask
from lib.groups import Grid
from lib.db import DB

DATA = (
  [1,1,0,1,0,0],
  [1,1,0,1,0,0],
  [0,1,0,0,0,0],
  [1,1,0,0,0,1],
)

db = DB('192.168.50.178', 3306, 'demo', 'root', 'change_me')

app = Flask(__name__)

@app.route('/')
def root():
  return 'Hi!'

@app.route('/count', methods=['GET'])
def count_groups():
  grid = Grid(())
  return str(grid.count_groups())

@app.route('/count/<key>', methods=['GET'])
def lookup(key):
  result = db.get_result(key)
  if not result:
    grid = Grid(())
    result = grid.count_groups()
    db.save_result(key, result)
  return str(result)