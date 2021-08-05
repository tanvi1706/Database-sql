
from DataType import DataType


class ColumnInfo:
    dataType = []
    columnName = ''
    isUnique = False
    isNullable = True
    ordinalPosition = 0
    hasIndex = False
    tableName = ''
    isPrimaryKey = False
    
    def __init__(self):
        pass

    # def __init__(self, tableName = ' ', dataType, columnName: str, isUnique: bool, isNullable: bool, ordinalPosition: int):
    #     self.dataType = dataType
    #     self.columnName = columnName
    #     self.isUnique = isUnique
    #     self.isNullable = isNullable
    #     self.ordinalPosition = ordinalPosition
    #     self.tableName = tableName
    #     self.hasIndex = DavisBasePrompt.getNDXFilePath(tableName, columnName).exists()



    # def setAsPrimaryKey():
    #     isPrimaryKey = True