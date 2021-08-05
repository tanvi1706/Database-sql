from . import DataType
from . import OperatorType
class Condition:
    columnName = ''
    #operator
    comparisonValue = ''
    negation = False
    columnOrdinal = 0
    # DataType dataType 
    supportedOperators = ["<=", ">=", "<>", ">", "<", "="]
    def __init__(self, dataType: DataType):
        self.dataType = dataType
    def getOperatorType(strOperator: str)-> OperatorType:
        if strOperator == '>':
            return OperatorType.GREATERTHAN
        elif strOperator == '<':
            return OperatorType.LESSTHAN
        elif strOperator == '=':
            return OperatorType.EQUALTO
        elif strOperator == '>=':
            return OperatorType.GREATERTHANOREQUAL
        elif strOperator == '<=':
            return OperatorType.LESSTHANOREQUAL
        elif strOperator == '<>':
            return OperatorType.NOTEQUAL
        else:
            print('invalid operator')
            return OperatorType.INVALID
        

    # def compare(val1: str, val2: str, datatype: DataType)->int:
    #     if datatype == DataType.TEXT:
    #         if val1 == val2:
    #             return 0
    #         elif val1 < val2:
    #             return -1
    #         elif val1 > val2:
    #             return 1
    #     elif datatype == DataType.None:
            

    def doOperationOnDifference(operation: OperatorType, difference: int): #private
        pass

    def doStringCompare(currentValue: str, operation: OperatorType)->bool: #private
        pass
    def checkCondition(currentValue: str) -> bool:
        pass
    def setConditionValue(conditionValue: str):
        pass
    def setColumnName(self,columnName: str):
        self.columnName = columnName
    def setOperator(self,operator: str):
        self.operator = operator
    def setNegation(self, negate: bool):
        self.neagate = negate
    def negateOperator()->OperatorType:
        pass
    def getOperator(self)->OperatorType:
        if not self.negation:
            return self.operator
        else:
            return self.negateOperator()

   
