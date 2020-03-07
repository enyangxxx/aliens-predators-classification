import glob

def loadDataFromOneSet(directory='validation', targetSize=(64,64)):
    '''
    Loading images including resizing, without the option of data augmentation
    '''
    aliens_file_list = sorted(glob.glob('dataset/' + directory + '/alien/*.jpg'))
    aliens_x = np.asarray([cv2.cvtColor(cv2.resize(cv2.imread(fname), targetSize), cv2.COLOR_BGR2RGB) for fname in aliens_file_list])
    
    predators_file_list = glob.glob('dataset/' + directory + '/predator/*.jpg')
    predators_x = np.asarray([cv2.cvtColor(cv2.resize(cv2.imread(fname), targetSize), cv2.COLOR_BGR2RGB) for fname in predators_file_list])
    
    aliens_y = np.ones((aliens_x.shape[0], 1), dtype=np.int8)
    predators_y = np.zeros((predators_x.shape[0], 1), dtype=np.int8)
    
    data_X = np.vstack((aliens_x, predators_x))
    print("Shape of data_X: " + str(data_X.shape))

    data_y = np.vstack((aliens_y, predators_y))
    data_y = np.ravel(data_y)
    
    return data_X, data_y


def loadDataFromOneSetWithFlip(directory='train', addFlip=False, targetSize=(100,100)):
    '''
    Loading images including resizing and the option of data augmentation
    '''
    aliens_file_list = sorted(glob.glob('dataset/' + directory + '/alien/*.jpg'))
    aliens_x = np.asarray([cv2.cvtColor(cv2.resize(cv2.imread(fname), targetSize), cv2.COLOR_BGR2RGB) for fname in aliens_file_list])
    if addFlip==True:
        aliens_flipped = np.flip(aliens_x, axis=2)
        aliens_x = np.vstack((aliens_x, aliens_flipped))
    
    predators_file_list = glob.glob('dataset/' + directory + '/predator/*.jpg')
    predators_x = np.asarray([cv2.cvtColor(cv2.resize(cv2.imread(fname), targetSize), cv2.COLOR_BGR2RGB) for fname in predators_file_list])
    if addFlip==True:
        predators_flipped = np.flip(predators_x, axis=2)
        predators_x = np.vstack((predators_x, predators_flipped))
    
    aliens_y = np.ones((aliens_x.shape[0], 1), dtype=np.int8)
    predators_y = np.zeros((predators_x.shape[0], 1), dtype=np.int8)
    
    data_X = np.vstack((aliens_x, predators_x))
    print("Shape of data_X: " + str(data_X.shape))

    data_y = np.vstack((aliens_y, predators_y))
    data_y = np.ravel(data_y)
    
    return data_X, data_y