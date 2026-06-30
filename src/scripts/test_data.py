import numpy as np
import paths
import os
no_run_ci = os.getenv('CI', 'false') == 'true' and not snakemake.config['run_cache_rules_on_ci']
if no_run_ci or os.getenv('SYW_NO_RUN', 'false') == 'true':
    raise Exception('Output should have been downloaded from Zenodo.')
np.random.seed(0)
data = np.random.randn(100, 10)
np.savez(paths.data / 'test_data.npz', data=data)
