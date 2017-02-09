import pandas as pd 
import numpy as np 
import scipy.stats as st 
import xlsxwriter 

file_location = "C:/Anaconda3/dataset_Facebook.csv" 
out = pd.read_csv(file_location, sep=';', header=0) 
db=out.drop("Type",axis=1) 
def params(x): 
    _x = np.array(x, dtype=np.float) 
    _x = _x[~np.isnan(_x)*~np.isinf(_x)] 
    result = [] 
    result.append(np.mean(_x)) 
    result.append(np.min(_x)) 
    result.append(np.max(_x)) 
    result.append(np.percentile(_x,50)) 
    result.append(st.mode(_x)) 
    return tuple(result) 
print('ALL:')
for i in {'Page total likes', 'Post Month', 'Post Weekday', 
          'Post Hour', 'Paid', 'Lifetime Post Total Reach', 
          'Lifetime Post Total Impressions', 'Lifetime Engaged Users', 
          'Lifetime Post Consumers', 'Lifetime Post Consumptions', 
          'Lifetime Post Impressions by people who have liked your Page', 
          'Lifetime Post reach by people who like your Page', 
          'Lifetime People who have liked your Page and engaged with your post', 
          'comment', 'like', 'share', 'Total Interactions'}: 
    print(i) 
    sample=db[i] 
    m,mini,maxi,medi,mode=params(sample) 
    print('Среднее значение: {0:.4f}'.format(m)) 
    print('Минимальное значение: {0:.4f}'.format(mini)) 
    print('Максимальное значение: {0:.4f}'.format(maxi)) 
    print('Медиана: {0:.4f}'.format(medi)) 
    print('Мода:{}'.format(mode[0])) 
photo=out[out.Type == 'Photo'] 
photo=photo.drop("Type",axis=1) 
print() 
print('Photo:') 
for i in {'Page total likes', 'Post Month', 'Post Weekday', 
          'Post Hour', 'Paid', 'Lifetime Post Total Reach', 
          'Lifetime Post Total Impressions', 'Lifetime Engaged Users', 
          'Lifetime Post Consumers', 'Lifetime Post Consumptions', 
          'Lifetime Post Impressions by people who have liked your Page', 
          'Lifetime Post reach by people who like your Page', 
          'Lifetime People who have liked your Page and engaged with your post', 
          'comment', 'like', 'share', 'Total Interactions'}: 
    print(i) 
    sample=photo[i] 
    m,mini,maxi,medi,mode=params(sample) 
    print('Среднее значение: {0:.4f}'.format(m)) 
    print('Минимальное значение: {0:.4f}'.format(mini)) 
    print('Максимальное значение: {0:.4f}'.format(maxi)) 
    print('Медиана: {0:.4f}'.format(medi)) 
    print('Мода:{}'.format(mode[0])) 
status=out[out.Type == 'Status'] 
status=status.drop("Type",axis=1) 
print() 
print('Status:') 
for i in {'Page total likes', 'Post Month', 'Post Weekday', 
          'Post Hour', 'Paid', 'Lifetime Post Total Reach', 
          'Lifetime Post Total Impressions', 'Lifetime Engaged Users', 
          'Lifetime Post Consumers', 'Lifetime Post Consumptions', 
          'Lifetime Post Impressions by people who have liked your Page', 
          'Lifetime Post reach by people who like your Page', 
          'Lifetime People who have liked your Page and engaged with your post', 
          'comment', 'like', 'share', 'Total Interactions'}: 
    print(i) 
    sample=status[i] 
    m,mini,maxi,medi,mode=params(sample) 
    print('Среднее значение: {0:.4f}'.format(m)) 
    print('Минимальное значение: {0:.4f}'.format(mini)) 
    print('Максимальное значение: {0:.4f}'.format(maxi)) 
    print('Медиана: {0:.4f}'.format(medi)) 
    print('Мода:{}'.format(mode[0])) 
video=out[out.Type == 'Video'] 
video=video.drop("Type",axis=1) 
print() 
print('Video:') 
for i in {'Page total likes', 'Post Month', 'Post Weekday', 
          'Post Hour', 'Paid', 'Lifetime Post Total Reach', 
          'Lifetime Post Total Impressions', 'Lifetime Engaged Users', 
          'Lifetime Post Consumers', 'Lifetime Post Consumptions', 
          'Lifetime Post Impressions by people who have liked your Page', 
          'Lifetime Post reach by people who like your Page', 
          'Lifetime People who have liked your Page and engaged with your post', 
          'comment', 'like', 'share', 'Total Interactions'}: 
    print(i) 
    sample=video[i] 
    m,mini,maxi,medi,mode=params(sample) 
    print('Среднее значение: {0:.4f}'.format(m)) 
    print('Минимальное значение: {0:.4f}'.format(mini)) 
    print('Максимальное значение: {0:.4f}'.format(maxi)) 
    print('Медиана: {0:.4f}'.format(medi)) 
    print('Мода:{}'.format(mode[0])) 
link=out[out.Type == 'Link'] 
link=link.drop("Type",axis=1) 
print()
print('Link:') 
for i in {'Page total likes', 'Post Month', 'Post Weekday', 
          'Post Hour', 'Paid', 'Lifetime Post Total Reach', 
          'Lifetime Post Total Impressions', 'Lifetime Engaged Users', 
          'Lifetime Post Consumers', 'Lifetime Post Consumptions', 
          'Lifetime Post Impressions by people who have liked your Page', 
          'Lifetime Post reach by people who like your Page', 
          'Lifetime People who have liked your Page and engaged with your post', 
          'comment', 'like', 'share', 'Total Interactions'}: 
    print(i) 
    sample=link[i] 
    m,mini,maxi,medi,mode=params(sample) 
    print('Среднее значение: {0:.4f}'.format(m)) 
    print('Минимальное значение: {0:.4f}'.format(mini)) 
    print('Максимальное значение: {0:.4f}'.format(maxi)) 
    print('Медиана: {0:.4f}'.format(medi)) 
    print('Мода:{}'.format(mode[0]))
