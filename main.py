from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/input',methods=['POST'])
def pred():
    mba_p = request.form.get('mba_p')
    ssc_p = request.form.get('ssc_p')
    hsc_p = request.form.get('hsc_p')
    degree_p = request.form.get('degree_p')
    workex = request.form.get('workex')
    specialisation = request.form.get('specialisation')
    gender = request.form.get('gender')
    etest_p = request.form.get('etest')
    hsc_s = request.form.get('hsc_s')
    degree_t = request.form.get('degree_t')
    print('mba_p')
    #op = model.predict(mba_p,ssc_p,hsc_p,degree_p)
    return render_template('index.html',Output = 1)
    # ssc_b = request.form.get('ssc_b')

    # op = model.predict(mba_p,ssc_p,hsc_p,degree_p)
    # print(op)str(op = 1)




if __name__ == '__main__':
    app.run()
