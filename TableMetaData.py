


from DavisBasePrompt import DavisBasePrompt


class TableMetaData:
    recordCount = 0
    columnData = [] #list[TableRecord]
    columnNameAttrs = [] #list[ColumnInfo]
    columnNames = [] #list[String]
    tableName = ''
    tableExists = False
    rootPageNo = 0
    lastRowId = 0
    # def TableMetaData(self, tableName:str):
    #     self.tableName = tableName
    #     tableExists = True
    #     try:
    #         with open(DavisBasePrompt.getTBLFilePath())
