import pandas as pd 

df = pd.read_csv('fp2.csv')

def clean_up(column): 
    
    new_df = df[column].values.reshape(-1,1)
    new_col = []
    
    for item in new_df:
        if type(item[0]) == str:
            
        
            col_data = item[0].split(',')
            column_lst = []
       
            for i in range(len(col_data)):
                col_data[i] = col_data[i].strip("'][ '")
                column_lst.append(col_data[i])
                
        
            new_col.append(column_lst)
    
        else: 
        
            new_col.append([])
        
        
    return new_col

cleanable_columns = ['Title:', 'Genre:', 'Developer:', 'Publisher:', 'Release Date:', 'Franchise:']

for item in cleanable_columns:
    clean_column = clean_up(item)
    
    df = df.drop(item, axis = 1)
    new_series = pd.Series(clean_column)
    df[item] = new_series

df = df.drop('Unnamed: 0', axis = 1)


def count_unique(column):
    
    unique_items = []
    
    for item in df[column]:
        for i in range(len(item)):
            
            if item[i] not in unique_items:
                
                unique_items.append(item[i])
    
    
    return unique_items


def one_hot(column, unique_lst):
    
    series = df[column]
    
    
    for genre in unique_lst:
        
        genre_check = []
        
        for i in range(len(series)):
            
            genre_value = 0
            
            for j in range(len(series[i])):
                
                if genre == series[i][j]:
                    genre_value += 1
                else:
                    genre_value += 0
                
               
            if genre_value >= 1:
                genre_check.append(1)
            else:
                genre_check.append(0)

          
        genre_series = pd.Series(genre_check)
        df[genre] = genre_series


unique = count_unique('Genre:')

one_hot('Genre:', unique)
df = df = df.drop('Genre:', axis = 1)


df.to_csv("new_data")
        
    





