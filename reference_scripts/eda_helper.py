"""

Give me six hours to chop down a tree and I will spend the first four sharpening the axe. - Abraham Lincoln

"""
import pandas as pd
import pandas_profiling

data = pd.read_csv('/Users/lakshmi/projects/nasa_engine_degradation/CMAPSSData/train_FD001.txt')
profile = pandas_profiling.ProfileReport(data, title='Pandas Profiling Report', html={'style':{'full_width':True}})
profile.to_file(output_file="your_report.html")


