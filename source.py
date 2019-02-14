import tensorflow as tf
import numpy as np
import pandas as pd
import os
#from sklearn import datasets, linear_model
def read_demand_dataframe():
  """Returns a dataframe with the results for demand updated csv features"""
  
  # Point to where you've stored the CSV file on your local machine
  "remember read demandv1.2 file attached as modified datset "
  "original demand file wil not work "
  desktop = os.path.join(os.path.expanduser('~'),"Desktop")
  filepath = os.path.join(desktop,"Demandv1.2.csv")
  
  

  dataframe = pd.read_csv(filepath, sep=",",names=['Month DD Raised','No. of FTE Request Raised','SkillList','Location'], header=1)

  


  return dataframe
def read_data():
  """Returns a tuple with 4 fields, the returns for Month DD Raised ,No of FTE Request Raised,Skillset,and Location.
  Each of the returns are in the form of a 1D array"""

  returns = read_demand_dataframe()

  # Filter out the data and convert into numpy array 
  x1Data = np.array(returns["Month DD Raised"])
  x2Data = np.array(returns["SkillList"])
  x3Data = np.array(returns["Location"])
  yData = np.array(returns["No. of FTE Request Raised"])

  return (x1Data,x2Data,x3Data,yData)

X1_DATA,X2_DATA,X3_DATA,Y_DATA = read_data()
"the commented lines is another way to fit linear model using sklearn"
"but our dataset dependcy on X is not linear"
"so ignore these lines and let them be cpommented"
#combined = np.vstack((X1_DATA , X2_DATA , X3_DATA)).T
#demandModel = linear_model.LinearRegression()
#demandModel.fit(combined, Y_DATA)
#print(demandModel.score(combined, Y_DATA))
#print (demandModel.coef_)
#print (demandModel.intercept_)
#print(5*0.00320073-0.00055801*1+0.00996026*1)


"Assigning variables for weights"
X1_W = tf.Variable(tf.zeros([1, 1]), name="X1_W")
X2_W = tf.Variable(tf.zeros([1, 1]), name="X2_W")
X3_W = tf.Variable(tf.zeros([1, 1]), name="X3_W")
b = tf.Variable(tf.zeros([1]),name="b")
"assigning placeholders for input features"
X1_X = tf.placeholder(tf.float32, [None, 1], name="X1_X")
X2_X = tf.placeholder(tf.float32, [None, 1], name="X2_X")
X3_X = tf.placeholder(tf.float32, [None, 1], name="X3_X")
"craeting the model y = A*(month)^(-5) + B(skilllist)^(-5) + C*(Location)^(-5)"
month_w_x = tf.matmul(tf.pow(X1_X,-5),X1_W)
skilllist_w_x = tf.matmul(tf.pow(X2_X,-5),X2_W)
location_w_x = tf.matmul(tf.pow(X3_X,-5),X3_W)

y = month_w_x + skilllist_w_x + location_w_x + b
" ground truth values"
y_ = tf.placeholder(tf.float32,[None,1])
"declaring cost function to evaluate model's performance"
cost  = tf.reduce_mean(tf.square(y_ - y))
" optimizing features"
train_step_ftrl = tf.train.FtrlOptimizer(1).minimize(cost)
"reshaping data values to be consistent with model"

all_x_month = X1_DATA.reshape(-1, 1)
all_x_skilllist = X2_DATA.reshape(-1, 1)
all_x_location = X3_DATA.reshape(-1, 1)
all_ys = Y_DATA.reshape(-1, 1)




dataset_size = len(X1_DATA)



"The evaluation takes place in this function"
"parameters  steps is tunable such as steps to include"
"and different values for steps can be used to see if cost further decreases"
"or global minimum can shift even down so that model converges better"
def trainWithMultiplePointsPerEpoch(steps, train_step, batch_size):
  " initialising all variables"
  init = tf.global_variables_initializer()
  "initiatig a session under which cost and optimizers will be calculated"
  with tf.Session() as sess:
    sess.run(init)

    for i in range(steps):

      if dataset_size == batch_size:
        batch_start_idx = 0
      elif dataset_size < batch_size:
        raise ValueError("dataset_size: %d, must be greater than batch_size: %d" % (dataset_size, batch_size))
      else:
        batch_start_idx = (i * batch_size) % dataset_size

      batch_end_idx = batch_start_idx + batch_size

      batch_x_month = all_x_month[batch_start_idx : batch_end_idx]
      batch_x_skilllist = all_x_skilllist[batch_start_idx : batch_end_idx]
      batch_x_location = all_x_location[batch_start_idx : batch_end_idx]
      batch_ys = all_ys[batch_start_idx : batch_end_idx]
      "passing features into dictionary so which is input to train_step_ftrl"
      feed = { X1_X: batch_x_month, X2_X: batch_x_skilllist,X3_X: batch_x_location, y_: batch_ys }

      sess.run(train_step_ftrl, feed_dict=feed)

      # Print result to screen for every 500 iterations
      if (i + 1) % 500 == 0:
        print("After %d iteration:" % i)
        print("W1: %s" % sess.run(X1_W))
        print("W2: %s" % sess.run(X2_W))
        print("W3: %s" % sess.run(X3_W))
        print("b: %f" % sess.run(b))

        print("cost: %f" % sess.run(cost, feed_dict=feed))




trainWithMultiplePointsPerEpoch(5000, train_step_ftrl, len(X1_DATA))

" The final weights calculated are "

" W1 = -0.09928789 "
" W2 = 1.4858187 "
" W3 = -0.33684832 "
" b = 2.511014 "

"These weights will be used to make predictions"


















