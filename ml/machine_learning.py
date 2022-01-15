
from sklearn import tree
from sklearn.metrics import accuracy_score
import psycopg2

def predict(x:list):
    # creating our tree instance 
    clf = tree.DecisionTreeClassifier() 
    # get the X,Y list that Y contains price also called labels. 
    X, Y = query_database() 
    predict_y = None
    if X and Y:
        clf.fit(X, Y)
        # predict our input base on how machine learned from our data.
        predict_y = clf.predict(x)
        """testing our prediction accuracy"""
        # predict_y = clf.predict(X)
        # print(accuracy_score(Y, predict_y,normalize=False)) # result in 100%
    return predict_y

def query_database():

    """connect to and query the database
     and split 'price'=Y with other column and return them."""
    try:
        cnn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='')
        cur = cnn.cursor()
        
        try:
            # X data are the rooms,space,year_of_constructions 
            # Y data is price of them.
            cur.execute('SELECT rooms, space, year_of_construction FROM houses')
            X =  cur.fetchall()
            cur.execute('SELECT price FROM houses')
            # prices column
            Y = cur.fetchall()
    
            cur.close()
            # print(X)
            # print(Y)
            X = [[*x] for x in X]
            Y = [[*y] for y in Y]
        except psycopg2.DatabaseError:
            X , Y = None, None
    except (Exception,psycopg2.DatabaseError) as err:
        return None

    finally:
        if cnn is not None:
            cnn.close()
            return X,Y


# print(predict([[2,35,1344]]))
