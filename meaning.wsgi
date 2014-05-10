# virtualenv
activate_this = '/opt/.virtualenvs/meaning/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# get meaning application and add it to system paths
import sys  
sys.path.insert(0, '/cust/docs/http-detroitnewspapers/meaning.detroitmedia.net/meaning')
# import the app
from meaning import app as application  
