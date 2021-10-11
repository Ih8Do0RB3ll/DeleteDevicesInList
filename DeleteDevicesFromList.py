import os

file_path = input('Enter file path: ')

with open(file_path.replace('"','')) as f:
    for line in f:
        os.system(f'cmd /c "pnputil /remove-device "{line}""')

