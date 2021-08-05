from typing import List
# from TableMetaData import TableMetaData
import math

class DavisBaseBinaryFile:
    columnsTable = 'davisbase_colums'
    tablesTable = 'davisbase_tables'
    showRowId = False
    dataStoreInitialized = False
    pageSizePower = 9
    pageSize = int(math.pow(2, pageSizePower))
    file = ''
    
    def __init__(self, file):
        self.file = file
    
    # def recordExists(tablemetaData: TableMetaData, columnNames: List[int], ):
    #     pass

    def updateRecords():
        pass

    def selectRecords():
        pass

    def getRootPageNo() -> int:
        pass

    def initializeDataStore():
        pass