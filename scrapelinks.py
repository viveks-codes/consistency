# https://bootcamp.prod.machinehack.com/practices/getAllPracticeQuestionsUser?limit=5000&current_page=1&tags=630ca05637ffb072c933e527,6336741320ebf05c5b2faf48,63425ac40587b2b15540fb92,6307069ffc5ad19ffb3d2521,63045d8efc5ad17dde3d2463,62ed0e268a26274cbc5ad699,62ecbbb4901e7ebb02e18fc0,62ecb08d8a2627084a5ad60d,62ecb0764f08065cbdb49248,62ecb04b0aeb057e013be0fb,62da435e465856c044cef06d,62d901ac1de0c02d13df060e,62ce647e77eae5e26b56423b,62cd6a285b321a42b7702cab,62c676ae6748a823c6e1691e,62c6766a77213a77d5fa9f5b,635a04e72e718c39b1c0e5e2

# read above link and get all the links from the page and store it in a list

import requests
from json import loads
import pandas as pd
import pprint
url = 'https://bootcamp.prod.machinehack.com/practices/getAllPracticeQuestionsUser?limit=5000&current_page=1&tags=630ca05637ffb072c933e527,6336741320ebf05c5b2faf48,63425ac40587b2b15540fb92,6307069ffc5ad19ffb3d2521,63045d8efc5ad17dde3d2463,62ed0e268a26274cbc5ad699,62ecbbb4901e7ebb02e18fc0,62ecb08d8a2627084a5ad60d,62ecb0764f08065cbdb49248,62ecb04b0aeb057e013be0fb,62da435e465856c044cef06d,62d901ac1de0c02d13df060e,62ce647e77eae5e26b56423b,62cd6a285b321a42b7702cab,62c676ae6748a823c6e1691e,62c6766a77213a77d5fa9f5b,635a04e72e718c39b1c0e5e2'
r = requests.get(url)
data = loads(r.text)

# url has following json
"""{"status":{"code":200,"message":"Success"},"result":{"message":"Success","data":[{"_id":"6388278c08e99472efaa9e68","tags":[{"_id":"638825f59ff1ec0f201a0198","title":"Union"},{"_id":"6388264308e9949cefaa9ad9","title":"Breadth First Search"},{"_id":"6388262e3b5a5d1b31259c37","title":"Depth First Search"}],"acceptanceRate":50,"premium":true,"featured":false,"createdAt":"2022-12-01T04:03:24.211Z","categoryId":{"_id":"638825eb3b5a5dffdd259c2c","title":"Union"},"questionTitle":"Replace the beans","slug":"replace-the-beans-dbe1a","difficulty":"Intermediate","difficultyCode":2,"priority":939,"likes":0,"disLikes":0},{"_id":"63882bef4f44fe93bd87218e","tags":[{"_id":"638825f59ff1ec0f201a0198","title":"Union"},{"_id":"6388264308e9949cefaa9ad9","title":"Breadth First Search"},{"_id":"6388262e3b5a5d1b31259c37","title":"Depth First Search"}],"acceptanceRate":25,"premium":true,"featured":false,"createdAt":"2022-12-01T04:22:07.588Z","categoryId":{"_id":"638825eb3b5a5dffdd259c2c","title":"Union"},"questionTitle":"Prevent people from landmines","slug":"prevent-people-from-landmines-33522","difficulty":"Intermediate","difficultyCode":2,"priority":942,"likes":0,"disLikes":0}],"totalCount":2}}"""

# make excel file with following columns
# questionTitle, slug, difficulty, tags
df = pd.DataFrame(columns=['questionTitle', 'slug', 'difficulty', 'tags'])
# also add https://machinehack.com/practices/ to the slug column in start and .html in the end
# also fix the difficulty column to be easy, medium, hard instead of 1, 2, 3
# also fix the tags column to be comma separated instead of list of dictionaries
# also fix the questionTitle column to be without any special characters

for i in range(len(data['result']['data'])):
    df.loc[i] = [data['result']['data'][i]['questionTitle'], 'https://machinehack.com/practices/' + data['result']['data'][i]['slug'] + '.html', data['result']['data'][i]['difficulty'], ','.join([data['result']['data'][i]['tags'][j]['title'] for j in range(len(data['result']['data'][i]['tags']))])]
    if df.loc[i]['difficulty'] == 1:
        df.loc[i]['difficulty'] = 'Easy'
    elif df.loc[i]['difficulty'] == 2:
        df.loc[i]['difficulty'] = 'Medium'
    else:
        df.loc[i]['difficulty'] = 'Hard'
    
    # df[tag] :- [{'_id': '62c6766a77213a77d5fa9f5b', 'title': 'SciPy'}, {'_id': '62c676ae6748a823c6e1691e', 'title': 'NumPy'}, {'_id': '62c5376ab2eafa9078842a0c', 'title': 'Matrix'}, {'_id': '62bd7e44ba9acc065345c413', 'title': 'Array'}]
    # newdf[tag] :- SciPy,NumPy,Matrix,Array
    # import ast
    for j in range(len(data['result']['data'][i]['tags'])):
        # df.loc[i]['tags'] = ast.literal_eval(df.loc[i]['tags'])[j]['title']
        df.loc[i]['tags'] = ','.join([data['result']['data'][i]['tags'][j]['title'] for j in range(len(data['result']['data'][i]['tags']))])
                                                                                                                                                                                                                                                                                                          
df.to_csv('machinehack.csv', index=False)
