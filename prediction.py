import pickle

def detecting_fake_news(var):
    load_model = pickle.load(open('../../../PycharmProjects/flaskProject/final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])
    lst=[prediction[0],prob[0][1]]
    return lst
