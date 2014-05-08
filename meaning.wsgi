import sys
sys.path.insert(0, '/cust/docs/http-detroitnewspapers/meaning.detroitmedia.net/meaning')
activate_this = '/opt/.virtualenvs/meaning/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from meaning import app as application
