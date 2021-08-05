import ColumnInfo
# from BPlusOneTree import BPlusOneTree
# from Attribute import Attribute
from DataType import DataType
# from TableMetaData import TableMetaData
# from DavisBaseBinaryFile import DavisBaseBinaryFile
from pathlib import Path
from os import listdir
from os.path import isfile, join
import os
import Table

class DavisBasePrompt:
    prompt = 'davisql> '
    version = 'v1.0'
    copyright = 'Team Green'
    isExit = False
    pageSize = 512
    lstcolumnInformation = {}

    def getTBLFilePath(tableName:str)->str:
        return 'data/' + tableName + '.tbl'

    def getNDXFilePath(tableName: str, columnName: str)->str:
        return 'data/' + tableName + '_' + columnName + '.ndx'

    def line(s: str, num: int) -> str:
        a = ""
        for i in range(num):
            a += s
        return a

    def printCmd(s: str):
        print("\n\t" + s + "\n")

    def printDef(s: str):
        print("\t\t" + s)

    def help(self):
        pass

    def getVersion(self) -> str:
        return self.version

    def getCopyright(self) -> str:
        return self.copyright

    def displayVersion(self):
        print("Davisbase version" + self.getVersion())
        print(self.getCopyright())

    def test(self):
        pass
    def displayScreen(self):
        print("-"*80)
        print("Welcome to DavisBase, team green")
        print("version: ", self.version)
        print(self.getCopyright())
        print("Type 'help;' to display supported commands.")
        print("-"*80)

    # def parseQuery(self, queryString):
    #     table_name = ""
    #     column_names = []
    #     queryTableTokens = queryString.split(" ")
    #     i = 0
    #     while i < len(queryTableTokens):
    #         if queryTableTokens[i] == 'from':
    #             i += 1
    #             table_name = queryTableTokens[i]
    #             break
    #         elif not queryTableTokens[i] == '*' and not queryString[i] == ',':
    #             if ',' in queryTableTokens[i]:
    #                 colList = list(queryTableTokens[i].split(','))
    #                 for col in colList:
    #                     column_names.append(col)
    #             else:
    #                 column_names.append(queryTableTokens[i])
    #     tableMetaData = TableMetaData(table_name)
    #     if not tableMetaData.tableExists:
    #         print("The table does not exists!")
    #         return

    #     condition = None
    #     try:
    #         pass
    #         #condition = extractConditionFromQuery(tableMetaData, queryString)
    #     except:
    #         print("error")
    #         return
    #     if column_names.size() == 0:
    #         column_names = tableMetaData.columnNames
    #     try:
    #         pass
    #     except:
    #         pass 





    # def dropTable(self, dropTableString: str):
    #     tokens = dropTableString.split(" ")
    #     if not(tokens[0].lower() == 'drop' and tokens[1].lower() == 'table'):
    #         print("Error")
    #         return
    #     dropTableTokens = dropTableString.split(" ")
    #     tableName = dropTableTokens[2]
    #     self.parseDelete("delete from table " + DavisBaseBinaryFile.tablesTable + " where table_name = '" + tableName + "' ")
    #     self.parseDelete("delete from table " + DavisBaseBinaryFile.columnsTable + " where table_name = '" + tableName + "' " )
    #     tableFile = "data/" + tableName + ".tbl"
    #     if tableFile.delete():
    #         print("table deleted")
    #     else:
    #         print("table doesn't exist")

    #     onlyfiles = [f for f in listdir('data') if isfile(join('data/', f))]
    #     iFlag = False
    #     for f in onlyfiles:
    #         if f.startswith(tableName) and f.endswith("ndx"):
    #             iFlag = True
    #             os.remove("data/" + f)
    #             print("index file deleted")
    #     if iFlag:
    #         print("drop "+tableName)
    #     else:
    #         print("index doesn't exist")
        

    def parseCreateTable(self, createTableString):
        createTableTokens = createTableString.split('(')
        #print(createTableTokens)
        if createTableTokens[0].split(' ')[1] != 'table':
            print('syntax error')
            return
        tablename = createTableTokens[0].split(' ')[2]
        if len(tablename.strip()) == 0:
            print('tablename can not be empty')
            return 
        if tablename in self.lstcolumnInformation:
            print('table name already exists')
        try:
            columnTokens = createTableTokens[1][:len(createTableTokens[1])-2].split(',')
            for i in range(len(columnTokens)):
                 columnTokens[i] = columnTokens[i].strip()
            self.lstcolumnInformation[tablename] = {"columnTokens": columnTokens}
            #print(self.lstcolumnInformation)
            print('Table created !')
            # Table.storeMetaData(self.lstcolumnInformation, tablename)
            # if not os.path.isdir('data'):
            #     d = os.mkdir("data")
            # with open('data/table.txt', 'w') as f:
            #     f.write('13')
            #     # f.write(len(lstDict[tablename]['records']))
            #     f.write('15')
            #     f.write('15')
            #     f.write('15')
            #     f.write('15')
        except:
            print('exception occured')          


    def parseInsert(self,userCommand):
        insertTokens = userCommand.lower().strip().split('table')
        inserts = insertTokens[1].strip().split('values')
        tablename = inserts[0].strip().split(' ')[-1]
        #print(tablename)
        colval = inserts[1].strip()[1:len(inserts[1]) - 3]
        d = {}
        if not self.lstcolumnInformation[tablename].get('records', 0):
            self.lstcolumnInformation[tablename]['records'] = []
        self.lstcolumnInformation[tablename]['records'].append(colval)
        #print(self.lstcolumnInformation)
        print('Record Inserted!')
        return 

    def parseDelete(self, userCommand):
        deleteToken = userCommand.lower().strip().split(' ')
        tablename = deleteToken[3]
        if tablename not in self.lstcolumnInformation:
            print('Table does not exist')
        else:
            col = deleteToken[5]
            val = deleteToken[7][:len(deleteToken[7])-1]
            # print(col)
            # print(val)
            for i, elem in enumerate(self.lstcolumnInformation[tablename]['columnTokens']):
                v = elem.strip().split(' ')
                if v[0] == col:
                    index = i
            # print(index)
            for i, elem in enumerate(self.lstcolumnInformation[tablename]['records']):
                j = elem.strip().split(', ')
                # print(j[index])
                if j[index] == val:
                    self.lstcolumnInformation[tablename]['records'].pop(i)
                    print('Record deleted')
                    return
            print('Record not found')
        return




    def parseUpdate(self,userCommand):
        updateTokens = userCommand.lower().strip().split('set')
        tablename = updateTokens[0].strip().split(' ')[1]
        columnname = updateTokens[1].strip().split(' ')[0]
        newValue = updateTokens[1].strip().split(' ')[2]
        cond = userCommand.lower().strip().split('where')[1]
        cond = cond[: len(cond) - 1].strip()
        # print(cond)
        condsplit = cond.split(' ')
        findindexcol = condsplit[0]
        # print(findindexcol)
        val = condsplit[2]
        # print('val', val)
        if tablename not in self.lstcolumnInformation:
            print('Table does not exist')
        else:
            ele = self.lstcolumnInformation[tablename]['columnTokens']
            for i,e in enumerate(ele):
                v = e.strip().split(' ')
                if v[0] == findindexcol:
                    index = i
                    # print('index ',index)
                if v[0] == columnname:
                    toset = i
                    # s

            ele = self.lstcolumnInformation[tablename]['records']
            #self.lstcolumnInformation[tablename]['records'] = []
            print(ele)
            m = ""
            for i,e in enumerate(ele):
                j = e.strip().split(', ')
                for x in j:
                    # print(x)
                    if x == val:
                        index = i
                        j[toset] = newValue
                        m = j
                        break
                
            self.lstcolumnInformation[tablename]['records'][index] = ', '.join(m)  
        # print(self.lstcolumnInformation)
        print('Record updated!')
        return

    def showTables(self):
        for item in self.lstcolumnInformation.keys():
            print(item)
        return

    def parseQuery(self, unserselect):
        parsetokens = unserselect.strip().split(' ')
        tablename = parsetokens[3][: len(parsetokens[3]) - 1]
        print(tablename)
        if tablename not in self.lstcolumnInformation:
            print('Table does not exists')
            return
        if parsetokens[1].strip() == '*':
            for elem in self.lstcolumnInformation[tablename]['columnTokens']:
                j = elem.split(' ')
                print('{:<10}'.format(j[0]), end = '')
            print()
            for elem in self.lstcolumnInformation[tablename]['records']:
                j = elem.split(', ')
                for e in j:
                    print('{:<10}'.format(e), end = '')
                print()
        return



    def dropTable(self, deletecommand):
        tablename = deletecommand.strip().split(' ')[2]
        tablename = tablename[:len(tablename)-1]
        if tablename in self.lstcolumnInformation:
            del self.lstcolumnInformation[tablename]
            print('Table dropped!')
        else:
            print('The table you want to delete does not exists.')
        return
        

    # def parseInsert(self, queryString: str):
    #     insertTokens = queryString.split(" ")

    #     if not (insertTokens[1] == 'into') or not (") values" in queryString):
    #         print("Syntax error")
    #         print("Expected syntax : INSERT INTO TABLE (column_list) table_name VALUES (value1, value2....);")
    #         return
    #     try:
    #         tableName = insertTokens[4]
    #         if not len(tableName) == 0:
    #             print("Table name can not be empty!")
    #             return
    #         dsMetaData = TableMetaData(tableName)
    #         if not dsMetaData.tableExists:
    #             print('The table does not exists!')
    #             return
    #         columnlist = insertTokens[3][1:len(insertTokens[3])].split(',')
    #         for colToken in columnlist:
    #             if not colToken in dsMetaData.columnNames:
    #                 print("Invalid column "+ colToken)
    #                 return
    #         valueTokens = insertTokens[6][1:len(insertTokens)].split(',')
    #         attributeToInsert = []

    #         for colInfo in dsMetaData.columnNameAttrs:
    #             i = 0
    #             columnProvided = False
    #             for i in range(len(columnlist)):
    #                 if columnlist[i] == colInfo.columnName:
    #                     columnProvided = True
    #                     try:
    #                         value = valueTokens[i].replace("'", "").replace("\"","")
    #                         if valueTokens[i] == None:
    #                             if not colInfo.isNullable:
    #                                 print("cannot insert null values!")
    #                                 return
    #                         colInfo.dataType = DataType.NONE
    #                         value = value.upper()

    #                         attr = Attribute(colInfo.dataType, value)
    #                         attributeToInsert.add(attr)
    #                         break
    #                     except:
    #                         print('Invalid data for' + columnlist[i] + ' values: ' + valueTokens[i])

    #             if len(columnlist) > i:
    #                 columnlist.remove(i)
    #                 valueTokens.remove(i)
                
    #             if not columnProvided:
    #                 if colInfo.isNullable:
    #                     attributeToInsert.add(Attribute(DataType.NONE, "None"))
    #                 else:
    #                     print("can not insert NONE into "+ colInfo.columnName)
    #                     return
    #     except:
    #         pass
            
            # pathh = self.getTBLFilePath(tableName)
            # with open(pathh, 'rw') as dstTable:
            #     dstPageNo = BPlusOneTree.getPageNoForInsert(dstTable, dsMetaData.rootPageNo)
            #     dstPage = page(dstTable, dstPageNo)
            #     rowNo = dstPage.addTableRow(tableName, attributeToInsert)
            #     if rowNo != -1:
            #         for i in range(len(dsMetaData.columnNameAttrs)):
            #             col = dsMetaData.columnNameAttrs[i]
            #             if col.hasIndex:
            #                 pass
            #               #  indexFile = 
            #             pass
            #         pass

        
    

    def parseUserCommand(self, userCommand: str):
        commandTokens = list(userCommand.split(" "))
        firstcommand = commandTokens[0]
        if firstcommand == "show":
            if commandTokens[1] == 'tables;':
                self.showTables()
            # elif commandTokens[1] == 'rowid':
            #     # DavisBaseBinaryFile.showRowId = True
            #     print("* Table select will show RowId as well")
            else:
                print("I could not understand the command: '"+userCommand+"'")
        elif firstcommand == "select":
            self.parseQuery(userCommand)
        elif firstcommand == "drop":
            self.dropTable(userCommand)
        elif firstcommand == "create":
            self.parseCreateTable(userCommand)
            # if commandTokens[1] == 'table':
            #     self.parseCreateTable(userCommand)
            # elif commandTokens[1] == 'index':
            #     self.parseCreateIndex(userCommand)
        elif firstcommand == 'update':
            self.parseUpdate(userCommand)
        elif firstcommand == 'insert':
            self.parseInsert(userCommand)
        elif firstcommand == 'delete':
            self.parseDelete(userCommand)
        elif firstcommand == 'help':
            self.help()
        elif firstcommand == 'version':
            self.getVersion()
        elif firstcommand == 'exit' or firstcommand == 'quit':
            self.isExit = True
        elif firstcommand == 'test':
            self.test()
        else:
            print("I could not understand the command '"+ userCommand + "'")




pd = DavisBasePrompt()      


pd.displayScreen()
dataDir = 'data'
    # tablesTablepath = Path(dataDir + '/' + DavisBaseBinaryFile.tablesTable + '.tbl')
    # columnsTablepath = Path(dataDir + '/' + DavisBaseBinaryFile.columnsTable + '.tbl')
    # if (not tablesTablepath.is_file()) or (not columnsTablepath.is_file()):
    #     DavisBaseBinaryFile.initializeDataStore()
    # else:
    #     DavisBaseBinaryFile.dataStoreInitialized = True

userCommand = ""

while (not pd.isExit):
    print(pd.prompt, end='')
    userCommand = input().lower()
    pd.parseUserCommand(userCommand)

print("Exiting....")


    