import numpy as np
import pandas as pd

import numpy as np
import pandas as pd

a = np.array([1, 2, 3])
b = pd.Series(a)

if (a == b).all():
    print(a)
else:
    print(b)