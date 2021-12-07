import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config import FLEET_GROUPS, PASSENGER_GROUPS

# File and cleaning of rides report.
rides = r'C:\Users\ZVance\Documents\code\python\paratransit_report_downloader\ride.csv'
hours = r'C:\Users\ZVance\Documents\code\python\paratransit_report_downloader\vehicle_hours.csv'
df = pd.read_csv(rides)
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
                      'Actual/Estimated Pickup Time',
                      ])
df['Payment Method'] = df['Payment Method'].str.replace('SCTC - ', '')
df['Payment Method'] = df['Payment Method'].str.replace('/Commission Member', '')

df['Group'] = df['Fleet'].map(FLEET_GROUPS)
df['Passenger Groups'] = df['Passenger Types'].map(PASSENGER_GROUPS)

#temp1 = df.groupby(['Group', 'Fleet', 'Program Name'])['Payment Method'].value_counts()
temp1 = df.filter(['Group', 'Fleet', 'Program Name', 'Payment Method'])

#temp2 = df.groupby(['Group', 'Fleet', 'Program Name'])['Passenger Groups'].value_counts()
temp2 = df.filter(['Group', 'Fleet', 'Program Name', 'Passenger Groups'])
temp3 = df['Group'].value_counts()
#temp4 = df.groupby(['Group', 'Fleet', 'Program Name'])['Status'].value_counts()
temp4 = df.filter(items=['Group', 'Fleet', 'Program Name', 'Status'])
temp5 = df.filter(items=['Distance in km', 'Group', 'Fleet', 'Program Name'])
#[~df['Status'].isin(['Abandoned'])]


temp1.to_csv('payment_methods.csv')
temp2.to_csv('passenger_types.csv')
temp4.to_csv('statuses.csv')
temp5.to_csv('distance_in_km.csv')

hours = pd.read_csv(hours)
hours = hours.filter(items=['Program Name',
                            'Agenda Day',
                            'Booking ID',
                            'Driver Email',
                            'Online Time (minutes)',
                            'Offline Time (minutes)',
                            'Working Time (minutes)',
                            'Trips Offered',
                            'Trips Accepted',
                            'Trips Ignored',
                            'Trips Rejected',
                            ])


temp = df.filter(['Booking ID', 'Fleet'])
#hours = hours.merge(temp, on='Booking ID', how='right')


#hours['Group'] = hours['Fleet'].map(FLEET_GROUPS)

temp1 = hours.filter(items=['Online Time (minutes)',
                            'Offline Time (minutes)',
                            'Working Time (minutes)',
                            'Program Name',
                            ])
temp1['Online Hours'] = temp1['Online Time (minutes)'] / 60
temp1['Offline Hours'] = temp1['Offline Time (minutes)'] / 60
temp1['Working Hours'] = temp1['Working Time (minutes)'] / 60

temp1 = temp1.filter(items=['Online Hours',
                            'Offline Hours',
                            'Working Hours',
                            'Program Name',
                            ])
#temp1 = temp1.groupby(['Fleet', 'Group', 'Program Name']).sum()

temp2 = hours.filter(items=['Trips Offered',
                            'Trips Accepted',
                            'Trips Ignored',
                            'Trips Rejected',
                            'Fleet',
                            'Group',
                            'Program Name',
                            ])

temp1.to_csv('hours.csv')
temp2.to_csv('accepted_ignored.csv')

data = df.filter(items=['Actual/Estimated Pickup Time', 'Direct Duration (sec)'])
data = data.dropna()
data['Hour of Day'] = pd.to_datetime(data['Actual/Estimated Pickup Time'])
data['Hour of Day'] = data['Hour of Day'].dt.strftime('%H')
data['Hour of Day'] = data['Hour of Day'].astype(int)

sns.lineplot(x='Hour of Day', y='Direct Duration (sec)', data=data)
plt.show()