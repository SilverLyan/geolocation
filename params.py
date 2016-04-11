'''
Created on 26 Feb 2016

@author: af
'''
from os import path
all_models = ['text_classification', 'network_lp_regression', 'network_lp_regression_collapsed', 'network_lp_classification', 'network_lp_classification_edgexplain']
models_to_run = ['text_classification']
prior = 'none'
if 'text_classification' not in models_to_run and 'network_lp_classification' not in models_to_run and 'network_lp_classification_edgexplain' not in models_to_run and prior=='none':
    do_not_discretize = True
else:
    do_not_discretize = False

DATASET_NUMBER = 3
TEXT_ONLY = False
DATA_HOME = '/home/arahimi/datasets'
DATASETS = ['cmu', 'na', 'world-original']
ENCODINGS = ['latin1', 'utf-8', 'utf-8']
buckets = [300 , 2400, 2400]
reguls = [5e-5, 1e-6, 2e-7]
celeb_thresholds = [5 , 15, 15]
BUCKET_SIZE = buckets[DATASET_NUMBER - 1]
celeb_threshold = celeb_thresholds[DATASET_NUMBER - 1]
GEOTEXT_HOME = path.join(DATA_HOME, DATASETS[DATASET_NUMBER - 1])
data_encoding = ENCODINGS[DATASET_NUMBER - 1]
users_home = path.join(GEOTEXT_HOME, 'processed_data')
testfile = path.join(users_home, 'user_info.test.gz')
devfile = path.join(users_home, 'user_info.dev.gz')
trainfile = path.join(users_home, 'user_info.train.gz')
priors = ['none', 'backoff', 'dongle']
print "dataset: " + DATASETS[DATASET_NUMBER - 1]
lngs = []
ltts = []
pointText = {}
keys = []
userFirstTime = {}
userLocation = {}
locationUser = {}
userlat = {}
userlon = {}
testUsers = {}
trainUsers = {}
devUsers = {}
classLatMedian = {}
classLonMedian = {}
classLatMean = {}
classLonMean = {}
trainClasses = {}
devClasses = {}
testClasses = {}
categories = []
mentions = []
testText = {}
devText = {}
trainText = {}



X_train = None
X_dev = None
X_test = None
Y_train = None
Y_dev = None
Y_test = None
U_train = None
U_dev = None
U_test = None


n_comp = 500
factorizers = []
results = {}
mention_graph = None
partitionMethod = 'median'
partitionMethods = ['kmeans', 'ward', 'average', 'complete', 'median','spectral', 'kmeans', 'meanShift', 'Birch']
binary = False
sublinear=False
penalty = 'elasticnet'
fit_intercept = True
norm = 'l2'
use_idf = True
node_orders = ['l2h', 'h2l', 'random']
feature_names = None