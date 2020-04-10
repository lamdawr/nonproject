"""

Give me six hours to chop down a tree and I will spend the first four sharpening the axe. - Abraham Lincoln

"""
import numpy as np
import pandas as pd
import pandas_profiling
from sklearn.datasets import fetch_openml


# open data sets : https://www.openml.org/search?type=data 

cardiotocography = fetch_openml(name='diabetes', version=1)

cardio_df = pd.DataFrame(data= np.c_[cardiotocography['data'], cardiotocography['target']], columns= cardiotocography['feature_names'] + ['target'])

print(cardio_df.head())

######## Pandas profiling for easy EDA and pair plotting

profile = pandas_profiling.ProfileReport(cardio_df, title='Pandas Profiling Report', html={'style':{'full_width':True}})

profile.to_file(output_file="cardio_report.html")


