import  dirManager   as  helper
import connection as c
import  JsonParse as jmonday
import datetime
import log as l


pdInst = c.PandasDB()
inst = c.DB()

@l.logger
def upload_monday():
    f = helper.Files('Monday')
    for file in f.scanFiles:
        try:
            _mondayWrapper(f,file)
        except Exception as e:
            m = jmonday.ParseMonday(file['location'])
            info = ("error ---> ",file['location'], m.getTableName,str(e))

            f.Move(file['location'],file['fileName'],'error')
            err = l.Log("upload_monday",info,e)
            err.writeToLog()
            print (e)

    print ('done uploading Api ')

@l.logger
def _mondayWrapper(f,file):
    m = jmonday.ParseMonday(file['location'])
    dataFrame = pdInst.toDictDataFrame(m.getParsedData)
    if m.hasData:
        pdInst.replaceTable(m.getTableName, dataFrame)
        status = "Done --- > "
    else :
        status = "No Data on items ---> "

    f.Move(file['location'], file['fileName'], 'archive')
    return (status, str(file['fileName']) ,f' tbl {m.getTableName}',f" , rowCnt {len(dataFrame)}")



@l.logger
def upload_drugs():
    f_drugs = helper.Files('Drugs')
    for file in f_drugs.scanFiles:
        try:
            _drugsWarepper(file,f_drugs)

        except Exception as e:
            f_drugs.Move(file['location'],file['fileName'],'error')
            info = ("error ---> ", file['location'],str(e))

            err = l.Log("upload_drugs", info, e)
            err.writeToLog()
            print(e)


@l.logger
def _drugsWarepper(file,f_drugs):
    clean_nulls = """delete from [stg].[drugs_stock] where dr_objid is null or [מספר_תכשיר] is null  Or [שם_הקובץ] is null;"""
    seq = inst.getData("SELECT NEXT VALUE FOR stg.drugs_stocl_suq   AS seq_id;")
    dataFrame = pdInst.getExcelDataFrameDrugs(file['location'])
    dataFrame['createdDate'] = str(datetime.datetime.now())
    dataFrame['etl_id'] = seq[0][0]
    pdInst.appendTable('drugs_stock', dataFrame)

    f_drugs.Move(file['location'], file['fileName'], 'archive')
    inst.execQuery(clean_nulls)
    return (f"done uploading excels Drug : {file['fileName']} rowCnt {len(dataFrame)}")


def upload_to_tab():

    inst.execQuery("""exec  [stg].[sp_main];""")

