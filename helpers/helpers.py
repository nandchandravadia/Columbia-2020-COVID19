import pandas as pd


def extractPort_data(file):

    '''
    Purpose:
        -Extracts port data from Excel File and imports as Pandas DataFrame

    Inputs:
        -file: path to excel file

    Outputs:
        -port_traffic
    '''

    #Read CSV File
    port_traffic = pd.read_csv(file)
    #Resort By Date
    port_traffic_resorted = COVID19.sort_values(by=['Date'])

    return COVID19_resorted
