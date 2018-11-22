import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA



def aufgabe14():

    #a)------------------------------------------------

    X, y = make_blobs(n_samples=1000, centers=2, n_features=4, random_state=0)

    print("Shape: ",X.shape)

    plt.scatter(X[:,0], X[:,1], c=y, s=50)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.savefig('a_scatter.pdf')
    plt.clf()

    #c)----------------------------------------------------

    pca = PCA()
    Xstrich = pca.fit_transform(X)

    print("Shape nach PCA: ", Xstrich.shape)


    covx = np.cov(Xstrich.T)
    eigenwerte, eigenvektor = np.linalg.eigh(covx)

    print("Eigenwerte: ", eigenwerte)

    #d)---------------------------------------------------

    x1strich = np.array(Xstrich[:,0])
    x2strich = np.array(Xstrich[:,1])
    x3strich = np.array(Xstrich[:,2])
    x4strich = np.array(Xstrich[:,3])
    print(x1strich.shape)

    plt.hist(x1strich, bins=50, histtype='step')
    plt.xlabel('$x_1\'$')
    plt.savefig('d_histx1.pdf')
    plt.clf()
    plt.hist(x2strich, bins=50, histtype='step')
    plt.xlabel('$x_2\'$')
    plt.savefig('d_histx2.pdf')
    plt.clf()
    plt.hist(x3strich, bins=50, histtype='step')
    plt.xlabel('$x_3\'$')
    plt.savefig('d_histx3.pdf')
    plt.clf()
    plt.hist(x4strich, bins=50, histtype='step')
    plt.xlabel('$x_4\'$')
    plt.savefig('d_histx4.pdf')
    plt.clf()

    plt.scatter(x1strich, x2strich, c=y, s=50)
    plt.xlabel('$x_1\'$')
    plt.ylabel('$x_2\'$')
    plt.savefig('d_scatterx1x4.pdf')
    
if __name__ == '__main__':
    aufgabe14()
