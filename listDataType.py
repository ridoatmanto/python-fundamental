# children = ['Davin', 'Kiran', 'Kafka', 'Ainun', 'Danis', 'Alvin']
children = []
children.append('Davin')
children.append('Kiran')
children.append('Kafka')
children.append('Ainun')
children.append('Danis')
children.append('Alvin')
print('\nAll children')
for item in children:
    print(f'Child name is {item}')

print('\nAnother style for showing List')
for a in range(0, len(children)):
    print(f'{a+1}. Child name is {children[a]}')
