from sqlalchemy import create_engine
import pymysql
import pandas as pd

class DatabaseConnection:
    def __init__(self):
        self.pwd = 'pwd'
        self.url = f"mysql+pymysql://student1:{self.pwd}@159.203.63.26/sofvie_test"
        self.con = None

    def initialize(self):
        if self.con is None:
            engine = create_engine(self.url)
            self.con = engine.connect()

    def run_sql(self, sql):
        self.initialize()
        data = pd.read_sql(sql, con=self.con)
        return data

if __name__ == '__main__':
    database = DatabaseConnection()
    data = database.run_sql("""select * from employee_training""")
    print(data.head(5))
