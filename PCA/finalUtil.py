from sklearn.decomposition import PCA

def MyPCA(n,img,show=False):
    mPCA= PCA(n)
    img=mPCA.fit_transform(img)
    return mPCA.inverse_transform(img)

