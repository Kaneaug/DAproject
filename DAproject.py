#Project will focus on indentifying the most profitable country for a globaliztion expansion effort

import numbpy as np
import pandas as pd


dataframe = pd.read_csv('WDIData.csv')
dataframe.head(100)
#dataframe.shape

class TARGET_COUNTRY:
	def __init__(self,country,gpd,debt)
		self.country = country
		self.gdp = gdp
		self.debt = debt