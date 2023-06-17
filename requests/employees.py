import pandas as Pandas

class Employees:
    def __init__(self):
        self.employeesDataFrame = Pandas.read_json('data/data_AppleEmployee.json')
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

    def Login(self, enterLogin, enterPassword):
        '''Parameters: (Login, Password)'''
        returnal = False
        for index, row in self.employeesDataFrame.iterrows():
            if (str(enterLogin) == str(row[0]['login']) and str(enterPassword) == str(row[0]['password'])):
                print("Login: " + row[0]['name'] + "  |  Password: " + row[0]['password'])
                returnal = True
                break
        return returnal