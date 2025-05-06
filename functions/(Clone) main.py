%pip install pytest
import os
import sys
import pytest
#import tests.test_cleaning_utils
#import sum_func
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
repo_root = os.path.dirname(os.path.dirname(notebook_path))

print(repo_root)

dir=os.path.dirname(os.path.realpath('__file__'))
print(dir)
os.chdir(dir)
sys.dont_write_bytecode = True
print('---start---')
pytest.main([".", "-p", "no:cacheprovider"])
#pytest.main(["-v"])