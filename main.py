import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config import FLEET_GROUPS, PASSENGER_GROUPS, AMBULATORY_STATUS, RIDES, HOURS
import numpy as np


def clean_rides() -> None:
    # Rides summary
    df = pd.read_csv(RIDES)
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
    df['Group'] = df['Group'].fillna(0)
    df['Group'] = np.where(df['Group'] == 0, 'Cancelled', df['Group'])
    df['Passenger Groups'] = df['Passenger Types'].map(PASSENGER_GROUPS)
    df['Ambulatory Status'] = df['Passenger Groups'].map(AMBULATORY_STATUS)

    #temp = df.groupby(['Group', 'Fleet', 'Program Name'])['Payment Method'].value_counts()
    temp = df.filter(['Group', 'Fleet', 'Program Name', 'Payment Method'])
    temp.to_csv('payment_methods.csv')

    #temp = df.groupby(['Group', 'Fleet', 'Program Name'])['Passenger Groups'].value_counts()
    temp = df.filter(['Group', 'Fleet', 'Program Name', 'Passenger Groups'])
    temp.to_csv('passenger_types.csv')

    #temp = df.groupby(['Group', 'Fleet', 'Program Name'])['Status'].value_counts()
    temp = df.filter(items=['Group', 'Fleet', 'Program Name', 'Status'])
    temp.to_csv('statuses.csv')

    temp = df.filter(items=['Distance in km', 'Group', 'Fleet', 'Program Name'])
    temp.to_csv('distance_in_km.csv')

    temp = df.filter(['Group', 'Fleet', 'Program Name', 'Ambulatory Status'])
    temp.to_csv('ambulatory_statuses.csv')


def clean_hours() -> None:
    # Hours summary
    df = pd.read_csv(HOURS)
    df = df.filter(items=['Program Name',
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

    temp = df.filter(items=['Online Time (minutes)',
                            'Offline Time (minutes)',
                            'Working Time (minutes)',
                            'Program Name',
                            ])

    temp['Online Hours'] = temp['Online Time (minutes)'] / 60
    temp['Offline Hours'] = temp['Offline Time (minutes)'] / 60
    temp['Working Hours'] = temp['Working Time (minutes)'] / 60

    temp = temp.filter(items=['Online Hours',
                              'Offline Hours',
                              'Working Hours',
                              'Program Name',
                              ])

    #temp = temp.groupby(['Fleet', 'Group', 'Program Name']).sum()
    temp.to_csv('hours.csv')

    temp = df.filter(items=['Trips Offered',
                             'Trips Accepted',
                             'Trips Ignored',
                             'Trips Rejected',
                             'Fleet',
                             'Group',
                             'Program Name',
                             ])

    temp.to_csv('accepted_ignored.csv')

    # Below is code for a Seaborn/Matplotlib plot of trip time over time of day
    '''data = df.filter(items=['Actual/Estimated Pickup Time', 'Direct Duration (sec)'])
    data = data.dropna()
    data['Hour of Day'] = pd.to_datetime(data['Actual/Estimated Pickup Time'])
    data['Hour of Day'] = data['Hour of Day'].dt.strftime('%H')
    data['Hour of Day'] = data['Hour of Day'].astype(int)
    
    sns.lineplot(x='Hour of Day', y='Direct Duration (sec)', data=data)
    plt.show()'''


if __name__ == '__main__':
    clean_rides()
    clean_hours()
