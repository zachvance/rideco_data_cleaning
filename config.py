
# File paths
RIDES = 'path\\to\\rides.csv'
HOURS = 'path\\to\\hours.csv'

# Groupings
FLEET_GROUPS = {'Coventry Taxi Minivan': 'Contracted',
                'SCTC 2008/11 Paratransit Bus': 'Paratransit',
                'SCTC 2014/16 Low Floor Paratransit Bus': 'Paratransit',
                'SCTC 2018-2019 Paratransit Bus': 'Paratransit',
                'SCTC Caravan': 'Paravan',
                'SCTC Paravan Bus': 'Paravan',
                'SCTC Paravan Bus (WC Accessible)': 'Paravan',
                '': 'Cancelled',
                }

PAYMENT_GROUPS = {}

PASSENGER_GROUPS = {'Companion;Scooter': 'Wheelchair',
                    'Companion;Walker': 'Walker',
                    'Companion;Wheelchair': 'Wheelchair',
                    'Oversized wheelchair': 'Wheelchair',
                    'Oversized wheelchair;Child': 'Wheelchair',
                    'Oversized wheelchair;Companion': 'Wheelchair',
                    'Oversized wheelchair;Walker': 'Wheelchair',
                    'Scooter': 'Wheelchair',
                    'Scooter;Wheelchair': 'Wheelchair',
                    'Support Person;Companion;Wheelchair': 'Support Person',
                    'Support Person;Walker': 'Support Person',
                    'Support Person;Walk-On': 'Support Person',
                    'Support Person;Wheelchair': 'Support Person',
                    'Walker': 'Walker',
                    'Walker;Child': 'Walker',
                    'Walk-On': 'Walk-On',
                    'Walk-On;Child': 'Walk-On',
                    'Walk-On;Companion': 'Walk-On',
                    'Walk-On;Walker': 'Walker',
                    'Walk-On;Wheelchair': 'Wheelchair',
                    'Wheelchair': 'Wheelchair',
                    }

PROGRAM_NAMES = ['St. Catharines Paratransit', 'Thorold']

AMBULATORY_STATUS = {'Support Person': 'Ambulatory',
                     'Walker': 'Ambulatory',
                     'Walk-On': 'Ambulatory',
                     'Wheelchair': 'Non-Ambulatory',
                     }