from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class Nota(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        
        for index, row in data.iterrows():
            if(row['NOTA_EM'] > 10):
                data.loc[data.index == index, 'NOTA_EM'] = 10
            if(row['NOTA_DE'] > 10):
                data.loc[data.index == index, 'NOTA_DE'] = 10
            if(row['NOTA_MF'] > 10):
                data.loc[data.index == index, 'NOTA_MF'] = 10
            if(row['NOTA_GO'] > 10):
                data.loc[data.index == index, 'NOTA_GO'] = 10
                
        return data
