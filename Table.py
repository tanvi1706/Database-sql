class Table:
    datatypes = {
        'NULL': [0, hex(0)], 
        'TINYINT': [1, hex(1)],
        'SMALLINT': [2, hex(2)],
        'INT': [4, hex(3)],
        'BIGINT': [8, hex(4)],
        'LONG': [8, hex(4)],
        'FLOAT': [4, hex(5)],
        'DOUBLE': [8, hex(6)],
        'YEAR': [1, hex(8)],
        'TIME': [4, hex(9)],
        'DATETIME': [8, hex(10)],
        'DATE': [8, hex(11)],
        'TEXT': [hex(12)]

    }
    def storeMetaData(lstDict,tablename):
        with open('data/table.txt', 'rw') as f:
            f.write(13)
            # f.write(len(lstDict[tablename]['records']))
            f.write(15)
            f.write(15)
            f.write(15)
            f.write(15)
