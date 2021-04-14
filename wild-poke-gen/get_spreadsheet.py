import gspread
def get_spreadsheet(): 
    # Have to set up gspread - change directory to 
    # wherever you save the service account file.
    gc = gspread.service_account(filename='/Users/sola/dev/keys/pokejson-generator-b11e8367ae62.json')
    works = gc.open("PCL Master Resource").get_worksheet(4)
    wild_poke = works.batch_get(['A2:Y31'], major_dimension='ROWS')
    return wild_poke