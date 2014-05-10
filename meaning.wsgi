activate_this = '/opt/.virtualenvs/meaning/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys  
sys.path.insert(0, '/cust/docs/http-detroitnewspapers/meaning.detroitmedia.net/meaning')
from meaning import app as application  
