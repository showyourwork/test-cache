import numpy as np
import paths
import os
if os.getenv('CI', 'false') == 'true' or os.getenv('SYW_NO_RUN', 'false') == 'true':
    raise Exception('Output should have been downloaded from Zenodo.')
np.random.seed(0)
data = np.random.randn(100, 10)
np.savez(paths.data / 'test_data.npz', data=data)
