import time
import json
from datetime import datetime

data = {'datetime': datetime.now().isoformat(), 'ts': int(time.time())}
print(json.dumps(data))
