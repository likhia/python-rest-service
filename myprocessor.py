class MyProcessor:     
    def run(self, df):        
        return df.agg(['min', 'max'])