from numpy import *
def autoNorm(dataset):
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals-minVals
    Normmatrix = zeros(shape(dataset))
    m = dataset.shape[0]
    normdataset = dataset-tile(minVals,(m,1))
    normdataset = normdataset/tile(ranges,(m,1))
    return normdataset

