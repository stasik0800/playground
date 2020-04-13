import monday



def main():
    monday.upload_monday()

    monday.upload_drugs()

    monday.upload_to_tab()

main()


# import pandas as pd
# import connection as c
#
# pdInst = c.PandasDB()
# d = pd.read_excel("""M:\\scanOnce\\תרופות - שדות לתחקור.xlsx""",usecols='A:I',encoding="UTF-8")
# pdInst.appendTable("drugs_codes",d)
#


# pm2 start C:\Users\corona\PycharmProjects\integration\main.py --interpreter=C:\Users\corona\AppData\Local\Programs\Python\Python38-32\python.exe