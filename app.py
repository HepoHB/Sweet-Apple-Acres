import pandas as pd

class JSonRequests:
    def __init__(self):
        self.employeesDataFrame = pd.read_json('data/data_AppleEmployee.json')
        pass
    
    def ListEmployees(self, status=None):
        '''Possible Parameters: None | Active | Vacation | Retired'''
        if status is not None:
            for index, row in self.employeesDataFrame.iterrows():
                if (row[0]['status'] == status):
                    print(row[0]['name'])
                elif (row[0]['status'] == status):
                    print(row[0]['name'])
                elif (row[0]['status'] == status):
                    print(row[0]['name'])
                else:
                    pass
        else:
            for index, row in self.employeesDataFrame.iterrows():
                print(row[0]['name'])
            

PDJson = JSonRequests()
PDJson.ListEmployees()