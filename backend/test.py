# -*-coding: utf-8 -*-
# @Author: 'walkerlee'


import re,os
module_names=[]
for file in os.listdir('api'):
    if file in ('__pycache__', 'base.py', '__init__.py','music163'):
        continue
    module_name_res = re.findall(r'(\w+)\.py', file)
    print(module_name_res)
    # module_names.append(module_name_res.group(1))
    module_names.append(module_name_res[0])

print(module_names)