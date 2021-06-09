
from flask import render_template, Flask, request,url_for
from keras.models import load_model
import pickle #
#import tensorflow as tf
#graph = tf.compat.v1.get_default_graph()
with open(r'count_vec.pkl','rb') as file:
    cv=pickle.load(file)
cla = load_model('phone.h5')
cla.compile(optimizer='adam',loss='binary_crossentropy')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/tpredict')
@app.route('/', methods = ['GET','POST'])
def page2():
    if request.method == 'GET':
        img_url = url_for('static',filename = 'style/3.jpg')
        return render_template('index.html',url=img_url)
    if request.method == 'POST':
        topic = request.form['tweet']
        print("Hey " +topic)
        topic=cv.transform([topic])
        print("\n"+str(topic.shape)+"\n")
        #with graph.as_default():
        y_pred = cla.predict(topic)
        print("pred is "+str(y_pred))
        if(y_pred > 0.5):
            img_url = url_for('static',filename = 'style/1.jpg')
            topic = "Positive Tweet"
        else:
            img_url = url_for('static',filename = 'style/2.jpg')
            topic = "Negative Tweet"

        return render_template('index.html',ypred = topic)
        



if __name__ == '__main__':
    app.run(host = 'localhost', debug = False , threaded = False)
    
