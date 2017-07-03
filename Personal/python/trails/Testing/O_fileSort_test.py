import os
from time import gmtime as gt
from time import strftime as t
tf = '%Y-%m-%d %H:%M:%S'
print t(tf,gt(os.path.getctime('.')))