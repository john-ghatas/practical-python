#!/bin/python
text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'

import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
