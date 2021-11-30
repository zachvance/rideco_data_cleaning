import pandas as pd

# File and cleaning of rides report.
file = r'C:\Users\ZVance\Documents\code\python\paratransit_report_downloader\ride.csv'
df = pd.read_csv(file)
df = df.filter(items=['Ride Date',
                      'Ride ID',
                      'Booking ID',
                      'Status',
                      'User Display Name',
                      'Driver Display Name',
                      'Provider',
                      'Fleet',
                      'Direct Duration (sec)',
                      'Distance in km',
                      'Payment Method',
                      'Origin Address',
                      'Origin Latitude',
                      'Origin Longitude',
                      'Destination Address',
                      'Destination Latitude',
                      'Destination Longitude',
                      'Program Name',
                      'Passenger Types',
                      ])
df['Payment Method'] = df['Payment Method'].str.replace('SCTC - ', '')
#df = df[df['Program Name'] == 'Thorold']

temp1 = df.groupby(['Fleet', 'Program Name'])['Payment Method'].value_counts()
temp2 = df.groupby(['Fleet', 'Program Name'])['Passenger Types'].value_counts()
temp3 = df['Fleet'].value_counts()
temp4 = df.groupby(['Fleet', 'Program Name'])['Status'].value_counts()
temp5 = df.filter(items=['Distance in km', 'Fleet']).groupby(['Fleet']).sum()

temp1.to_csv('payment_methods.csv')
temp2.to_csv('passenger_types.csv')
temp4.to_csv('statuses.csv')
temp5.to_csv('distance_in_km.csv')