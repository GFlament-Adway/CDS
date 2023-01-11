import cdsapi

#Downloading the data
c = cdsapi.Client()

c.retrieve(
    'sis-tourism-fire-danger-indicators',
    {
        'format': 'zip',
        'time_aggregation': 'daily_indicators',
        'product_type': 'single_model',
        'variable': 'daily_fire_weather_index',
        'gcm_model': 'cnrm_cm5',
        'experiment': 'rcp4_5',
        'version': 'v2_0',
        'period': [
            '2006'
        ],
    },
    'download.zip')
