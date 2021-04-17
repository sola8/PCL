import gspread

def get_spreadsheet(): 
    # Have to set up gspread - change directory to 
    # wherever you save the service account file.
    file_location = input('Input the path location of the service account file: ')
    gc = gspread.service_account(filename=file_location)
    works = gc.open("PCL Master Resource").get_worksheet(4)
    wild_poke = works.batch_get(['A2:Y31'], major_dimension='ROWS')
    return wild_poke