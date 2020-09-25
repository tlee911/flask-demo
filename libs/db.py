import MySQLdb
import getpass

class DB():
  def __init__(self, host, port, database, username, password=None):
    self.db = database
    if password is None:
      password = getpass.getpass('PB password for {user}:'.format(user=username))
    self.connection = MySQLdb.connect(
      host=host,
      port=port,
      user=username,
      passwd=password,
    )

  def query(self, sql):
    cursor = self.connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return (tuple(columns), results)

  def insert(self, sql):
    cursor = self.connection.cursor()
    cursor.execute(sql)
    self.connection.commit()
    return 

  def format_dict(self, results):
    keys = results[0]
    rows = [list(row) for row in list(results[1])]
    results = []
    for row in rows:
      results.append(dict(zip(keys, rows)))
    return results

  def get_result(self, key):
    sql = """
    select
        result
    from {db}.results
    where input = '{key}'
    """.format(db=self.db, key=key)
    rows = self.query(sql)
    return self.format_dict(rows)

  def save_result(self, key, result):
    sql = """
    insert into {db}.results
    (input, result) values ({key}, {result})
    """.format(db=self.db, key=key, result=int(result))
    return self.insert(sql)
    