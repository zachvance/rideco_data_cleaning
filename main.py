import glob
import pandas as pd
import pathlib as pth

print(pth.Path().absolute())
mainpath = pth.Path().absolute()
#mainpath = input(r'Enter the filepath that contains all of the data folders: ')
hours = r'%s/hours/' % mainpath
rides = r'%s/ride/' % mainpath
fares = r'%s/fare/' % mainpath


def consolidatefiles(path, file):
    all_files = glob.glob(path + "/*.csv")
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    frame.replace('SCTC - ', '', regex=True, inplace=True)
    frame.to_csv('%s.csv' % file)


ptfile = 'pthours'
consolidatefiles(hours, ptfile)
consolidatefiles(rides, 'ptrides')
consolidatefiles(fares, 'ptfares')

def loopthrough():
    lspaths = [hours, rides, fares]
    lsfiles = ['pthours', 'ptrides', 'ptfares']
    for f, p in zip(lspaths, lsfiles):
        consolidatefiles(f, p)

#loopthrough()