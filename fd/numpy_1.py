import numpy as np
'''
victor = numpy.array([
                    [1,2,3],
                    [2,3,4],
                    [2,4,5],
                    ])
print(victor)
print(victor.shape)
print(victor[1,1])
victor_column = (victor[:,1] == 3)
print(victor_column)
print(victor[victor_column,:])

vector = numpy.array([2,3,4])
vector_1 = (vector == 2)
print(vector_1)
print(vector[vector_1])

vector = numpy.array([10,15,20])
vector_r = (vector == 15)
print(vector_r)
print(vector[vector_r])

matrix = numpy.array([
                    [10,15,20],
                    [15,20,25],
                    [20,15,30],
                    ])
matrix_column = (matrix[:,1] == 20)
print(matrix_column)
print(matrix[matrix_column,:])

vector = numpy.array([10,20,30])
vector_r = (vector == 20)
print(vector[vector_r])
print(vector[1])

matrix = numpy.array([
                    [11,12,13],
                    [14,15,16],
                    [17,18,19]
                    ])
matrix_column = (matrix[:,1] == 15)
print(matrix[matrix_column,:])
print(matrix[1,1])


a = numpy.arange(1,31).reshape(2,3,5)
print(a)
b = numpy.random.random((3,5))
c = numpy.linspace(1,2,100)
d = numpy.zeros((3,5),dtype=int)
e = numpy.ones((3,5),dtype=int)
print(b)
print(c)
print(d)
print(e)


a = numpy.array([
                [1,2,3],
                [1,2,3],
                [1,2,3],
                ])
d = numpy.array([])
print(d)
for i in range(0,3):
    b = a[i,:]
    d = numpy.hstack((d,b))
print(d.astype(int))


data = numpy.sin(numpy.arange(0,15).reshape(3,5))
print(data)
print(data.shape[1])
print(data.shape[0])
print(range(data.shape[1]))
ind = data.argmax(axis=0)
print(ind)
data_max = data[ind,range(data.shape[1])]
print(data_max)


data = np.random.randint(1,5,15).reshape(3,5)
print(data)
a = np.random.random(5)
print(a)


print(np.array([[1,2,3],[4,5,6]]))
print(np.zeros((3,3),dtype=int))
print(np.ones((2,3,4),dtype=int ))
print(np.arange(5))
print(np.eye(3,3))
print(np.linspace(1,10,10))
print(np.random.rand(3,4))
print(np.random.randint(5, size=(2, 3)))
a = np.fromfunction(lambda x,y:x+y,(3, 3))
print(a)
print(a[2,2])
print(help(np.fromfunction))
b = lambda x,y:x+y


a = np.arange(4).reshape(2,2)
print(a)
b = np.array([[2,3],[4,5]])
print(np.dot(a,b))
print(a*b)
print(np.linalg.inv(b))


a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
b = np.arange(9).reshape(3,3)
print(a)
print(a[0])
print(a[-1])
print(a[:3])
print(np.dot(a,b))

a = np.arange(6).reshape(2,3)
b = a.reshape(3,2)
print(a)
print(b)
a.resize(3,2)
print(a)

z = np.ones((5,5),dtype=int)
z = np.pad(z, pad_width=1, mode='constant', constant_values=0)
print(z)

print(np.diag(np.arange(4)+1,k=-1))
Z = np.zeros((10,10),dtype=int)
Z[::2,::2] = 1
Z[1::2,1::2] = 1
print(Z)

Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print("Z1:", Z1)
print("Z2:", Z2)
print(np.intersect1d(Z1,Z2))

Z = np.random.uniform(0,10,10)
print("原始值: ", Z)

print ("方法 1: ", Z - Z%1)
print ("方法 2: ", np.floor(Z))
print ("方法 3: ", np.ceil(Z)-1)
print ("方法 4: ", Z.astype(int))
print ("方法 5: ", np.trunc(Z))

Z = np.linspace(0,1,6,endpoint=False)[1:]
print(Z)

Z = np.array([[7,4,3],[3,1,2],[4,2,6]])
print("原始数组: \n", Z)

Z.sort(axis=0)
print(Z)

Z = np.random.randint(0,10,(5,5))
print("排序前：\n",Z)

a = Z[:,2].argsort()
print(a)
print(Z[a])

Z = np.random.uniform(1,10,100)
print(Z)
z = 0.5
z = Z.flat[np.abs(Z-z).argmax()]
print(z)

Z = np.random.randint(0,10,50)
print("随机一维数组:", Z)
print(np.bincount(Z).argmax())

Z = np.random.randint(1,4,25).reshape(5,5)
print(Z)
Z[[0,1]] = Z[[1,0]]
print(Z)

Z=np.array([[0,1,2,3,0],[0,1,2,3,4]])
print(Z)

a = np.nonzero(Z)
print(a)

print(Z[a])

p = 5
Z = np.zeros((5,5))
np.put(Z,np.random.choice(range(5*5),p,replace=False ),1)
print(Z.astype(int))

Z = np.random.randint(1,100,100)
print(Z)

p = 5
print(np.argsort(Z))

print(np.argsort(Z)[-p:])

Z = np.random.random(5)
print(Z)
np.set_printoptions(precision=2)
print(Z)

Z = np.random.random([5,5])
print(Z)

Z = np.arange(15)
print(Z)
a = np.percentile(Z,q=[25,50,75])
print(a)

Z = np.random.random([10,10])
Z[np.random.randint(10,size=5),np.random.randint(10,size=5)] = np.nan
print(Z)
print("缺失个数：",np.isnan(Z).sum())
print("缺失值索引:",np.where(np.isnan(Z)))
print(Z[np.sum(np.isnan(Z), axis=1) == 0])

Z = np.random.randint(0,100,25).reshape(5,5)
print(Z)
print(np.unique(Z, return_counts=True)[1].sum())

Z = np.random.randint(1,4,10)
label_names = {1:"汽车", 2:"公交车", 3:"地铁"}
print(label_names)
a = [label_names[x] for x in Z]
print(a)

x =[1,2,3]
y =[1,2,3]
a = lambda x,y:x+y
print(a(x,y))

a = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (9, 9))
print(a)

'''
import operator
a = np.array([3,2,0,1])
b = a.argsort()
print(b)
labels = ['A','A','B','B']
classcount = {}
for i in range(3):
    d = labels[b[i]]
    print(d)
    classcount[d] = classcount.get(d,0) +1
    sortedclasscount = sorted(classcount.iteritems(),key=operator.itemgetter(1),reversw=True)
