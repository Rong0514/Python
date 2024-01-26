import jieba        
import webbrowser   
import pandas as pd  
from flask import Flask , render_template , request
from sklearn.metrics.pairwise import linear_kernel  
from sklearn.feature_extraction.text import TfidfVectorizer 

app = Flask(__name__) 

'''__________________________________________________________________首頁連結'''
@app.route('/home')
def home():
    return render_template('home.html') 

'''______________________________________________________________展示所有資訊'''
@app.route('/show')
def show():
    datas = pd.read_csv('output.csv')   
    datas.dropna(inplace = True)       
    data_list = []                     

    for data in datas.itertuples(index = False): 
        title   = data.title
        link    = data.link_url
        photo   = data.photo_url
        address = data.address
        price   = data.price
        star    = data.star
        feature = data.feature
        
        data_list.append({'title'  : title, 
                          'link'   : link,
                          'photo'  : photo,
                          'address': address,
                          'price'  : price,
                          'star'   : star,
                          'feature': feature})

    return render_template('show.html', datas=data_list) 

'''___________________________________________________________2. 展示搜尋結果'''
@app.route('/search', methods=['GET', 'POST'])
def search():
    user_input = request.args.get('query', '') 
    df = pd.read_csv('output.csv')             
    df.dropna(inplace = True)                 
    df1 = df['feature']                        
    tokenized_corpus = [list(jieba.cut(sentence)) for sentence in df1] # 使用jieba進行分詞
    vectorizer = TfidfVectorizer()             # 初始化TfidfVectorizer
    
    '''_________________使用TfidfVectorizer將tokenized_corpus轉換成TF-IDF矩陣'''
    tfidf_matrix = vectorizer.fit_transform([' '.join(tokens) for tokens in tokenized_corpus])
    
    '''_______________________________________________將用戶輸入的文字進行分詞'''
    user_tokens = list(jieba.cut(user_input))
    
    '''_______________________________________將用戶輸入的文字轉換成TF-IDF向量'''
    user_tfidf_vector = vectorizer.transform([' '.join(user_tokens)])
    
    '''________________________________計算用戶輸入的文字與所有文本的餘弦相似度'''
    user_cosine_similarities = linear_kernel(user_tfidf_vector, tfidf_matrix).flatten()
    
    '''____________根據餘弦相似度對所有文本進行排序，並取出相似度最高的前10個文本'''
    similarity_ranking = sorted(enumerate(user_cosine_similarities),
                                key=lambda x: x[1],
                                reverse=True)[:10]
    
    data_list = []                           
    for i, similarity in similarity_ranking:
        data = df.iloc[i]                   
        title   = data['title']
        link    = data['link_url']
        photo   = data['photo_url']
        address = data['address']
        price   = data['price']
        star    = data['star']
        feature = data['feature']
        
        data_list.append({'title'     : title,
                          'link'      : link,
                          'photo'     : photo,
                          'address'   : address,
                          'price'     : price,
                          'star'      : star,
                          'feature'   : feature,
                          'similarity': str(round(100 * similarity, 2))})
        
    return render_template('show.html', datas = data_list, user_input = user_input)

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/home")
    app.run(debug = True, use_reloader = False) 
