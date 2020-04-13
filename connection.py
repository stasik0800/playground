import pyodbc
import pandas as pd
import sqlalchemy
from fast_to_SQL import fast_to_SQL as f
import urllib


class auth:
    host = "host"
    user = "user"
    pw = "pw"
    db = "CoronaFighters"
    driver = "{ODBC Driver 17 for SQL Server}"
    params = urllib.parse.quote_plus(f"DRIVER={driver};"
                                     f"SERVER={host};"
                                     f"DATABASE={db};"
                                     f"UID={user};"
                                     f"PWD={pw}")

    dns = "mssql+pyodbc:///?odbc_connect={}?charset=utf8'".format(params)


class DB:
    def __init__(self):
        self._set_connetion()

    def _set_connetion(self):
        self.conn = pyodbc.connect(
            f'DRIVER={auth.driver};SERVER={auth.host};DATABASE={auth.db};UID={auth.user};PWD={auth.pw}',
            autocommit=True)
        self.cur = self.conn.cursor()

    def getData(self, query):
        x = self.cur.execute(query)
        return x.fetchall()

    def execQuery(self, query):
        # """EXEC [stg].[uploader];"""
        self.cur.execute(query)



    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def execQueryParams(self, query, data=None):
        self.cur.execute(query, data)

class PandasDB(DB):
    def __init__(self):
        super(PandasDB, self).__init__()
        self.engine = sqlalchemy.create_engine(auth.dns,encoding="UTF-8")

    def getExcelDataFrameDrugs(self,file):
        return pd.read_excel(file, usecols='A:AE', na_values=['nan'], skip_blank_lines=True)

    # @logger
    def replaceTable(self, tblName, dataFrame):
        f.to_sql_fast(dataFrame, tblName, self.engine, if_exists='replace' )

    def appendTable(self, tblName, dataFrame):
        f.to_sql_fast(dataFrame, tblName, self.engine, if_exists='append')

    def toDictDataFrame(self,data):
        return pd.DataFrame.from_dict(data)

    def parseCsv(self, file):
        df = pd.read_csv(file, sep=',', encoding="UTF-8")
        return df

    def getExcelDataFrame(self, file, sheet):
        x = pd.ExcelFile(file)
        return x.parse(sheet)

    def ViewData(self, query, records=5):
        df = pd.read_sql(query, self.conn)
        print(df.head(records))



