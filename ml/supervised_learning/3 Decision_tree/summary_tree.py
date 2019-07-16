import treePlotter as tP
import trees
mydata,labels = trees.createdataset()
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','teartate']
lensestree = trees.createTree(lenses,lensesLabels)
tP.createplot(lensestree)