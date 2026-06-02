"""
DIMENSIONALITY REDUCTION MASTERCLASS
===================================

Algorithms Covered
------------------
1. PCA
2. SVD
3. LDA
4. Kernel PCA
5. t-SNE
6. UMAP
7. ICA
8. Factor Analysis
9. NMF
10. Autoencoder

This file is designed as a learning resource. Read the comments,
run individual functions, and inspect the plots and outputs.

Install:
pip install numpy pandas matplotlib scikit-learn umap-learn tensorflow
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine, load_iris, load_digits, make_moons
from sklearn.decomposition import PCA, KernelPCA, FastICA, FactorAnalysis, NMF
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# ============================================================
# PCA
# ============================================================

def pca_demo():
    """
    PCA finds directions that preserve maximum variance.

    Real World:
    Customer data may contain 100 columns.
    PCA can reduce them to 10-20 dimensions while
    preserving most information.
    """
    data = load_wine()
    X = StandardScaler().fit_transform(data.data)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    print("\n=== PCA ===")
    print("Explained Variance Ratio:", pca.explained_variance_ratio_)
    print("Total Variance Preserved:", pca.explained_variance_ratio_.sum())

    plt.figure(figsize=(6,4))
    plt.scatter(X_pca[:,0], X_pca[:,1], c=data.target)
    plt.title("PCA Projection")
    plt.show()


# ============================================================
# SVD
# ============================================================

def svd_demo():
    """
    SVD decomposes matrix:

    A = U * S * V^T

    PCA is internally based on SVD in many implementations.

    Used in:
    - Recommendation Systems
    - NLP
    - Image Compression
    """
    A = np.array([[1,2],[3,4],[5,6]])

    U,S,VT = np.linalg.svd(A)

    print("\n=== SVD ===")
    print("U:\n", U)
    print("Singular Values:\n", S)
    print("VT:\n", VT)


# ============================================================
# LDA
# ============================================================

def lda_demo():
    """
    PCA preserves variance.

    LDA preserves class separation.

    Use LDA mainly for classification tasks.
    """
    iris = load_iris()

    lda = LinearDiscriminantAnalysis(n_components=2)
    X_lda = lda.fit_transform(iris.data, iris.target)

    print("\n=== LDA ===")
    print("Shape:", X_lda.shape)

    plt.figure(figsize=(6,4))
    plt.scatter(X_lda[:,0], X_lda[:,1], c=iris.target)
    plt.title("LDA Projection")
    plt.show()


# ============================================================
# Kernel PCA
# ============================================================

def kernel_pca_demo():
    """
    PCA works on linear relationships.

    Kernel PCA handles nonlinear relationships
    using the kernel trick.
    """
    X,y = make_moons(n_samples=500, noise=0.1)

    kpca = KernelPCA(n_components=2, kernel="rbf")
    X_new = kpca.fit_transform(X)

    print("\n=== Kernel PCA ===")
    print("Output Shape:", X_new.shape)

    plt.figure(figsize=(6,4))
    plt.scatter(X_new[:,0], X_new[:,1], c=y)
    plt.title("Kernel PCA")
    plt.show()


# ============================================================
# t-SNE
# ============================================================

def tsne_demo():
    """
    Best for visualization.

    Preserves local neighborhood structure.
    Often used for embeddings and clustering analysis.
    """
    digits = load_digits()

    tsne = TSNE(n_components=2, random_state=42)
    X_tsne = tsne.fit_transform(digits.data)

    print("\n=== t-SNE ===")
    print("Output Shape:", X_tsne.shape)

    plt.figure(figsize=(6,4))
    plt.scatter(X_tsne[:,0], X_tsne[:,1], c=digits.target)
    plt.title("t-SNE")
    plt.show()


# ============================================================
# UMAP
# ============================================================

def umap_demo():
    """
    UMAP is often faster than t-SNE
    and preserves both local and global structure.
    """
    import umap

    digits = load_digits()

    reducer = umap.UMAP(random_state=42)
    X_umap = reducer.fit_transform(digits.data)

    print("\n=== UMAP ===")
    print("Output Shape:", X_umap.shape)

    plt.figure(figsize=(6,4))
    plt.scatter(X_umap[:,0], X_umap[:,1], c=digits.target)
    plt.title("UMAP")
    plt.show()


# ============================================================
# ICA
# ============================================================

def ica_demo():
    """
    ICA finds statistically independent components.

    Famous Example:
    Cocktail Party Problem
    """
    data = load_wine()
    X = StandardScaler().fit_transform(data.data)

    ica = FastICA(n_components=2, random_state=42)
    X_ica = ica.fit_transform(X)

    print("\n=== ICA ===")
    print("Output Shape:", X_ica.shape)


# ============================================================
# Factor Analysis
# ============================================================

def factor_analysis_demo():
    """
    Assumes hidden factors generate observed variables.

    Example:
    Student marks may be generated by hidden
    intelligence or aptitude factors.
    """
    data = load_wine()
    X = StandardScaler().fit_transform(data.data)

    fa = FactorAnalysis(n_components=2)
    X_fa = fa.fit_transform(X)

    print("\n=== Factor Analysis ===")
    print("Output Shape:", X_fa.shape)


# ============================================================
# NMF
# ============================================================

def nmf_demo():
    """
    Non-Negative Matrix Factorization

    Produces interpretable components.

    Used in:
    - Topic Modeling
    - Recommendation Systems
    """
    digits = load_digits()

    X = digits.data

    nmf = NMF(n_components=10, max_iter=500)
    X_nmf = nmf.fit_transform(X)

    print("\n=== NMF ===")
    print("Output Shape:", X_nmf.shape)


# ============================================================
# AUTOENCODER
# ============================================================

def autoencoder_demo():
    """
    Deep Learning version of dimensionality reduction.

    Encoder compresses information.
    Decoder reconstructs information.
    """
    from tensorflow.keras.layers import Dense, Input
    from tensorflow.keras.models import Model

    input_layer = Input(shape=(784,))

    encoded = Dense(64, activation="relu")(input_layer)
    encoded = Dense(32, activation="relu")(encoded)

    decoded = Dense(64, activation="relu")(encoded)
    decoded = Dense(784, activation="sigmoid")(decoded)

    autoencoder = Model(input_layer, decoded)

    print("\n=== AUTOENCODER ===")
    autoencoder.summary()


# ============================================================
# COMPARISON
# ============================================================

def comparison_notes():
    print("""

================ COMPARISON =================

PCA
- Linear
- Variance preservation

SVD
- Matrix decomposition
- Foundation of PCA

LDA
- Supervised
- Class separation

Kernel PCA
- Nonlinear PCA

t-SNE
- Visualization only
- Slow

UMAP
- Faster visualization
- Preserves more structure

ICA
- Independent signals

Factor Analysis
- Hidden latent factors

NMF
- Non-negative interpretable factors

Autoencoder
- Deep learning
- Complex nonlinear patterns

================================================
""")


if __name__ == "__main__":
    comparison_notes()

    # Uncomment one by one while learning.

    # pca_demo()
    # svd_demo()
    # lda_demo()
    # kernel_pca_demo()
    # tsne_demo()
    # umap_demo()
    # ica_demo()
    # factor_analysis_demo()
    # nmf_demo()
    # autoencoder_demo()
