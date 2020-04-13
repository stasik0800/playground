import json


class ParseMonday:

    def __init__(self, path):
        self.path = path
        self.jsonData =self._initilized(path)
        self.hasData = True if self.jsonData["items"] else False
        self.subItem = True if 'subitems' in str(self.jsonData['name']).lower() else False


    def _initilized(self,path):
        _x = open(path,encoding="UTF-8")
        _jsonData = json.load(_x)
        return _jsonData

    @property
    def getTableName(self):
        return self.jsonData["name"] + "_tbl"

    @staticmethod
    def _reverseColumn(dicts):
        _dd = {}
        for inx, val in enumerate(dicts):
            column = val['title']
            value = val['text']
            # _keys.append(column)
            _dd[column] = value
        return _dd

    @property
    def getParsedData(self):
        data = []

        for inx, row in enumerate(self.jsonData['items']):
            # #ToDo : subItems is a use case when i need to emplement deeper logic on data objects parser
            # #Need to create Mapper Class

            row['id'] = self._subItemExtractIds(row)
            row['group'] = row['group']['title']
            row.update(ParseMonday._reverseColumn(row['column_values']))
            del row['column_values']


            if row["creator"]:
                row["creator"] = row["creator"]["name"]
            else :
                row["creator"]= ''

            if self.subItem:
                row = {k.lower() +"_subitem":v  for k,v in row.items()}

            data.append(row)

        return data

    def _subItemExtractIds(self,row):
        rowid = row['id']
        if self.subItem:
             rowid = str(row['group']['id']).replace('subitems_of_', '')
             if not rowid.isdigit():
                 return row['id']
        return rowid