near_driver = {
    'date': '2021-6-24',
    'driver': ['Mamat', 'Entong', 'Juki']
}

print(f'near driver {near_driver}')
print(f"First near driver is {near_driver['driver'][0]}")
print('-' * 22)

near_driver = {
    'date': '2021-6-24',
    'driver': [
        {'name': 'Mamat', 'distance': 100},
        {'name': 'Entong', 'distance': 300},
        {'name': 'Juki', 'distance': 250}
    ]
}

print(f'near driver {near_driver}')
print(f"First near driver is {near_driver['driver'][0]['name']} in {near_driver['driver'][0]['distance']} meters")
print('-' * 22)
