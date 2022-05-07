import time
import re

date_string = time.strftime("%Y-%m-%d")
print(date_string)

with open('README.md', 'r') as f:
    file_content = f.read()

updated_file_content = re.sub(r'Last updated: \d{4}-\d{2}-\d{2}',
                              f'Last updated: {date_string}',
                              file_content)

with open('README.md', 'w') as f:
    f.write(updated_file_content)
