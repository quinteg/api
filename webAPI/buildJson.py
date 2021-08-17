# -*- coding: utf-8 -*-
import pandas as pd
import hJson as hj

dir = "data/"

def getdict(rows, c, listCols, s):
    pfad = {}
    data = {}
    row = {}
    j = 0
    for r in rows:
        col = listCols[j]
        if j < c:
            if pd.isna(r):
                pass
            else:
                if col == 'Pfad 1':
                    pass
                else:
                    pfad[col] = r
        else:
            if pd.isna(r):
                pass
            else:
                data[col] = r
        j = j + 1

    datafv = data['Key']
    data = hj.dataDict(data)

    if bool(pfad):
        for p in pfad:
            lenPfad= len(pfad) + 1
            if lenPfad == 2:
                row = {pfad['Pfad 2']: {datafv: {'DATA': data[datafv]}}}
            elif lenPfad == 3:
                row = {pfad['Pfad 2']: {pfad['Pfad 3']: {datafv: {'DATA': data[datafv]}}}}
            elif lenPfad == 4:
                row = {pfad['Pfad 2']: {pfad['Pfad 3']: {pfad['Pfad 4']: {datafv: {'DATA': data[datafv]}}}}}
            elif lenPfad == 5:
                row = {pfad['Pfad 2']: {pfad['Pfad 3']: { pfad['Pfad 4']: {pfad['Pfad 5']: {datafv: {'DATA': data[datafv]}}}}}}
            elif lenPfad == 6:
                row = {pfad['Pfad 2']: {pfad['Pfad 3']: {pfad['Pfad 4']: {pfad['Pfad 5']: {pfad['Pfad 6']: {datafv: {'DATA': data[datafv]}}}}}}}
            elif lenPfad == 7:
                row = {pfad['Pfad 2']: {pfad['Pfad 3']: {pfad['Pfad 4']: {pfad['Pfad 5']: {pfad['Pfad 6']: {pfad['Pfad 7']:{datafv: {'DATA': data[datafv]}}}}}}}}
            elif lenPfad == 8:
                row = {pfad['Pfad 2']: {pfad['Pfad 3']: {pfad['Pfad 4']: {pfad['Pfad 5']: {pfad['Pfad 6']: {pfad['Pfad 7']: {pfad['Pfad 8']: {datafv: {'DATA': data[datafv]}}}}}}}}}
    else:
        row = {datafv: {'DATA': data[datafv]}}
    return row


class Excelfile():
    def __init__(self, filename):
        self.filename = dir + filename
        self.dfSheets = pd.read_excel(self.filename, None);
        self.include = {}
        print("filename: ", self.filename)

    def read_excelsheet(self, sheet):
        self.pdsheet = pd.read_excel(self.filename, sheet_name=sheet, engine='openpyxl')
        return self.pdsheet

    def getIncludes(self, str):
        imatrix = []
        irow = {}

        if str[0] == '/':
            str = str[1:]
        lpath = str.split('/')
        l = len(lpath)

        includeSheet_df = self.read_excelsheet(lpath[0])
        list_of_cols = includeSheet_df.columns.values.tolist()
        col = list_of_cols[len(lpath)-1]

        # Key index ermitteln
        ikey = hj.indexKey(list_of_cols)
        number_of_rows = len(includeSheet_df.index)
        for r in range(number_of_rows):
            if lpath[l-1] == includeSheet_df[col][r]:
                row = includeSheet_df.loc[r]
                dict_data = getdict(row, ikey, list_of_cols, lpath[0])
                irow[lpath[0]] = dict_data
                imatrix.append(dict_data)

        self.include[lpath[0]] = hj.getResult(imatrix)


def readsheet(filename, arbeitsblatt):
        matrix = []
        file = Excelfile(filename)
        excel_data_df = file.read_excelsheet(arbeitsblatt)
        number_of_rows = len(excel_data_df.index)
        list_of_cols = excel_data_df.columns.values.tolist()

        #Key index ermitteln
        ikey = hj.indexKey(list_of_cols)

        for i in range(number_of_rows):
            row = excel_data_df.loc[i]
            if row['Type'] == "include":
                file.getIncludes(row['Enum Values'])
            else:
                dict_data = getdict(row, ikey, list_of_cols, arbeitsblatt)
                matrix.append(dict_data)

        #for i in range(len(matrix)):
        #    print("i:", i, matrix[i])
        resultDict = {}
        res = hj.getResult(matrix)
        if len(file.include) > 0:
                for i in file.include:
                    res[i].update(file.include[i])

        resultDict['root'] = {arbeitsblatt: res}

        return resultDict


if __name__ == '__main__':
    readsheet("Strukturtabelle_InKalkTierchenhaltung.xlsx", 'Vorgarten')