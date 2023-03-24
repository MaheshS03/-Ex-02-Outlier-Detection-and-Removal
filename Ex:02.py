#READ DATA FROM BHP.CSV FILE:
import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df=pd.read_csv("bhp.csv")
df
#REMOVE OUTLIERS USING IQR AND ZSCORE:
import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df=pd.read_csv("bhp.csv")
q1=df['price_per_sqft'].quantile(0.25)
q3=df['price_per_sqft'].quantile(0.75)
IQR=q3-q1
print("First quantile:",q1," Third quantile:",q3," IQR: ",IQR,"\n")
lower=q1-1.5*IQR
upper=q3+1.5*IQR
outliers=df[(df['price_per_sqft']>=lower)&(df['price_per_sqft']<=upper)]
print("Outliers: \n")
print(outliers)
from scipy.stats import zscore
z=outliers[(zscore(outliers['price_per_sqft'])<3)]
print("Cleaned Data: \n")
print(z)
#READ DATA FROM HEIGHT_WEIGHT.CSV FILE:
import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df=pd.read_csv("height_weight.csv")
df
# USING IQR DETECT WEIGHT OUTLIERS:
import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df=pd.read_csv("height_weight.csv")
q1=df['weight'].quantile(0.25)
q3=df['weight'].quantile(0.75)
IQR=q3-q1
print("First quantile:",q1," Third quantile:",q3," IQR: ",IQR,"\n")
lower=q1-1.5*IQR
upper=q3+1.5*IQR
outliers=df[(df['weight']>=lower)&(df['weight']<=upper)]
print("Outliers: \n")
print(outliers)
# USING IQR DETECT HEIGHT OUTLIERS:
import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df=pd.read_csv("height_weight.csv")
q1=df['height'].quantile(0.25)
q3=df['height'].quantile(0.75)
IQR=q3-q1
print("First quantile:",q1," Third quantile:",q3," IQR: ",IQR,"\n")
lower=q1-1.5*IQR
upper=q3+1.5*IQR
outliers=df[(df['height']>=lower)&(df['height']<=upper)]
print("Outliers: \n")
print(outliers)
