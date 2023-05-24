{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "028a9cb6-e855-4b01-811e-dfac882c90ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn import linear_model\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c36017db-639d-497c-a9b3-1d2b47da0455",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>per_capita_income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1970</td>\n",
       "      <td>3399.299037</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1971</td>\n",
       "      <td>3768.297935</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1972</td>\n",
       "      <td>4251.175484</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1973</td>\n",
       "      <td>4804.463248</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1974</td>\n",
       "      <td>5576.514583</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1975</td>\n",
       "      <td>5998.144346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1976</td>\n",
       "      <td>7062.131392</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1977</td>\n",
       "      <td>7100.126170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1978</td>\n",
       "      <td>7247.967035</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1979</td>\n",
       "      <td>7602.912681</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>1980</td>\n",
       "      <td>8355.968120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>1981</td>\n",
       "      <td>9434.390652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>1982</td>\n",
       "      <td>9619.438377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>1983</td>\n",
       "      <td>10416.536590</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>1984</td>\n",
       "      <td>10790.328720</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>1985</td>\n",
       "      <td>11018.955850</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>1986</td>\n",
       "      <td>11482.891530</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>1987</td>\n",
       "      <td>12974.806620</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>1988</td>\n",
       "      <td>15080.283450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>1989</td>\n",
       "      <td>16426.725480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>1990</td>\n",
       "      <td>16838.673200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>1991</td>\n",
       "      <td>17266.097690</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>1992</td>\n",
       "      <td>16412.083090</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>1993</td>\n",
       "      <td>15875.586730</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>1994</td>\n",
       "      <td>15755.820270</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>1995</td>\n",
       "      <td>16369.317250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>1996</td>\n",
       "      <td>16699.826680</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>1997</td>\n",
       "      <td>17310.757750</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>1998</td>\n",
       "      <td>16622.671870</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>1999</td>\n",
       "      <td>17581.024140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>2000</td>\n",
       "      <td>18987.382410</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>2001</td>\n",
       "      <td>18601.397240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>2002</td>\n",
       "      <td>19232.175560</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>2003</td>\n",
       "      <td>22739.426280</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>2004</td>\n",
       "      <td>25719.147150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>2005</td>\n",
       "      <td>29198.055690</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>2006</td>\n",
       "      <td>32738.262900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>2007</td>\n",
       "      <td>36144.481220</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>2008</td>\n",
       "      <td>37446.486090</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>2009</td>\n",
       "      <td>32755.176820</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>2010</td>\n",
       "      <td>38420.522890</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>2011</td>\n",
       "      <td>42334.711210</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>2012</td>\n",
       "      <td>42665.255970</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>2013</td>\n",
       "      <td>42676.468370</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>2014</td>\n",
       "      <td>41039.893600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>2015</td>\n",
       "      <td>35175.188980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>2016</td>\n",
       "      <td>34229.193630</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    year  per_capita_income\n",
       "0   1970        3399.299037\n",
       "1   1971        3768.297935\n",
       "2   1972        4251.175484\n",
       "3   1973        4804.463248\n",
       "4   1974        5576.514583\n",
       "5   1975        5998.144346\n",
       "6   1976        7062.131392\n",
       "7   1977        7100.126170\n",
       "8   1978        7247.967035\n",
       "9   1979        7602.912681\n",
       "10  1980        8355.968120\n",
       "11  1981        9434.390652\n",
       "12  1982        9619.438377\n",
       "13  1983       10416.536590\n",
       "14  1984       10790.328720\n",
       "15  1985       11018.955850\n",
       "16  1986       11482.891530\n",
       "17  1987       12974.806620\n",
       "18  1988       15080.283450\n",
       "19  1989       16426.725480\n",
       "20  1990       16838.673200\n",
       "21  1991       17266.097690\n",
       "22  1992       16412.083090\n",
       "23  1993       15875.586730\n",
       "24  1994       15755.820270\n",
       "25  1995       16369.317250\n",
       "26  1996       16699.826680\n",
       "27  1997       17310.757750\n",
       "28  1998       16622.671870\n",
       "29  1999       17581.024140\n",
       "30  2000       18987.382410\n",
       "31  2001       18601.397240\n",
       "32  2002       19232.175560\n",
       "33  2003       22739.426280\n",
       "34  2004       25719.147150\n",
       "35  2005       29198.055690\n",
       "36  2006       32738.262900\n",
       "37  2007       36144.481220\n",
       "38  2008       37446.486090\n",
       "39  2009       32755.176820\n",
       "40  2010       38420.522890\n",
       "41  2011       42334.711210\n",
       "42  2012       42665.255970\n",
       "43  2013       42676.468370\n",
       "44  2014       41039.893600\n",
       "45  2015       35175.188980\n",
       "46  2016       34229.193630"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(\"Canada_Per_Capita_Income.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5b94fc33-e9eb-4c71-8f00-7db79369929b",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.xlabel('year')\n",
    "plt.ylabel('per capita income (US$)')\n",
    "%matplotlib inline\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c6f6338d-6c53-4329-8a92-435fe0b43e72",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['year', 'per_capita_income '], dtype='object')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5a5f0a0d-cc19-4f1a-bf43-2cd2102288dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x7fa2bb844df0>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(df.year,df.per_capita_income )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "726fefae-9372-4602-8120-3bfa27e83e48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg=linear_model.LinearRegression()\n",
    "reg.fit(df[['year']],df.per_capita_income )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "50499c20-8dd4-450b-a2a9-0f1a008d5e91",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/envs/anaconda-2022.05-py39/lib/python3.9/site-packages/sklearn/base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([41288.69409442])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.predict([[2020]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "33de65cd-af50-4dc6-857b-36516ce1aa7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "d=pd.read_csv('year.csv')\n",
    "d.head(10)\n",
    "p=reg.predict(d)\n",
    "d['per_capita_income']=p\n",
    "d.to_csv(\"prediction.csv\",index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a0724516-6054-409e-8dc8-2a6cd0a03f26",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7fa2b784fee0>]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "plt.xlabel('year',fontsize=20)\n",
    "plt.ylabel('per_capita_income',fontsize=20)\n",
    "plt.scatter(df.year,df.per_capita_income, color=\"red\",marker='+')\n",
    "plt.plot(df.year,reg.predict(df[['year']]),color=\"blue\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2022.05-py39",
   "language": "python",
   "name": "conda-env-anaconda-2022.05-py39-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
