---
tags:
- bond-convexity
- convexity
- gaussian-hjm-model
- swaps
key_concepts:
- Convexity adjustments in fixed income
- Interest rate swaps and swap curve construction
- Practical examples and implementation
- Derivatives and structured financial instruments
last_enhanced: '2025-11-06 08:42:51'
---



# A Beginner's Guide to Linear Algebra for Machine Learning 
*(From Basics to Applications in ML)*  

---

## **1. Vectors and Vector Spaces**  
### **Intuitive Explanation**  
Vectors are mathematical objects that have **magnitude** and **direction** (geometric view) or represent **lists of numbers** (algebraic view). For example:  
- A 2D vector **v** = \[3, 4] can represent a point in 2D space or a force with magnitude √(3² + 4²) = 5.  
- In machine learning (ML), vectors often represent **data points** (e.g., features of a house: \[price, size, bedrooms]).  

### **Mathematical Definition**  
A vector **v** ∈ ℝⁿ is an ordered list of *n* real numbers:  
$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}
$$  
Operations:  
1. **Addition**: $\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}$  
2. **Scalar Multiplication**: $c\mathbf{v} = \begin{bmatrix} c v_1 \\ c v_2 \\ \vdots \\ c v_n \end{bmatrix}$  

### **Vector Spaces**  
A vector space (or linear space) is a set of vectors closed under addition and scalar multiplication.  
- **Example**: ℝ² (all 2D real vectors) is a vector space.  
- **Subspace**: A subset of a vector space that is itself a vector space.  
  - E.g., a line through the origin in ℝ² is a subspace.  

---

## **2. Matrices and Matrix Operations**  
### **Intuitive Explanation**  
Matrices are **rectangular arrays of numbers** that represent linear transformations (e.g., rotations, scalings) or data (e.g., a table of pixel values in an image).  

### **Mathematical Definition**  
A matrix $A \in \mathbb{R}^{m \times n}$ has *m* rows and *n* columns:  
$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$  

### **Key Operations**  
1. **Matrix Multiplication**:  
   $C = AB$, where $c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$.  
   - **Example**:  
     $$
     \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} 
     \begin{bmatrix} 5 \\ 6 \end{bmatrix} 
     = \begin{bmatrix} 1 \cdot 5 + 2 \cdot 6 \\ 3 \cdot 5 + 4 \cdot 6 \end{bmatrix} 
     = \begin{bmatrix} 17 \\ 39 \end{bmatrix}
     $$  
   - **Intuition**: Composition of linear transformations.  

2. **Transpose**: $A^\top$ swaps rows and columns.  
   $$
   A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad A^\top = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
   $$  

3. **Identity Matrix**: A square matrix $I$ where $I_{ij} = 1$ if $i=j$, else 0.  
   $$
   I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
   $$  

---

## **3. Determinants and Inverses**  
### **Determinants**  
- **Intuition**: The determinant of a square matrix measures how it scales areas/volumes under the linear transformation.  
- **Formula (2x2 matrix)**:  
  $$
  \det(A) = a_{11}a_{22} - a_{12}a_{21}
  $$  
- **Example**:  
  $$
  A = \begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix}, \quad \det(A) = 2 \cdot 4 - 1 \cdot 3 = 5
  $$  

### **Inverse of a Matrix**  
- **Definition**: A matrix $A^{-1}$ such that $AA^{-1} = I$.  
- **Existence**: Only for **non-singular** matrices ($\det(A) \neq 0$).  
- **Formula (2x2 matrix)**:  
  $$
  A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}
  $$  
- **Example**:  
  $$
  A = \begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix}, \quad A^{-1} = \frac{1}{5} \begin{bmatrix} 4 & -1 \\ -3 & 2 \end{bmatrix}
  $$  

---

## **4. Linear Systems and Solutions**  
### **Solving Linear Equations**  
A system of linear equations:  
$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
\end{cases}
$$  
Can be written as $A\mathbf{x} = \mathbf{b}$, where $A \in \mathbb{R}^{m \times n}$, $\mathbf{x} \in \mathbb{R}^n$, $\mathbf{b} \in \mathbb{R}^m$.  

### **Solution Methods**  
1. **Cramer's Rule** (for square invertible matrices):  
   $$
   x_i = \frac{\det(A_i)}{\det(A)}, \quad \text{where } A_i \text{ replaces column } i \text{ with } \mathbf{b}.
   $$  
2. **Gaussian Elimination**:  
   - Convert $A$ to row-echelon form using row operations.  
   - Back-substitute to find solutions.  

### **Homogeneous Systems**  
$A\mathbf{x} = \mathbf{0}$ always has the trivial solution $\mathbf{x} = \mathbf{0}$. Non-trivial solutions exist if $\det(A) = 0$.  

---

## **5. Vector Spaces and Bases**  
### **Linear Independence**  
A set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}$ is **linearly independent** if no vector can be written as a linear combination of the others.  
- **Mathematically**:  
  $$
  c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \Rightarrow c_1 = c_2 = \cdots = c_k = 0
  $$  

### **Basis and Dimension**  
- A **basis** is a linearly independent set that spans the vector space.  
- The **dimension** is the number of vectors in any basis.  
  - Example: Standard basis for ℝ³:  
    $$
    \mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{e}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    $$  

---

## **6. Eigenvalues and Eigenvectors**  
### **Intuition**  
Eigenvectors are vectors that remain in the same direction after a linear transformation (only scaled). The scaling factor is the eigenvalue.  

### **Mathematical Definition**  
For a square matrix $A$, eigenvalues $\lambda$ and eigenvectors $\mathbf{v}$ satisfy:  
$$
A\mathbf{v} = \lambda \mathbf{v}
$$  
- **Characteristic Equation**:  
  $$
  \det(A - \lambda I) = 0
  $$  
- **Example**:  
  $$
  A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}, \quad \det\left(\begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix}\right) = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0
  $$  
  Solving: $\lambda_1 = 3$, $\lambda_2 = 1$.  

---

## **7. Quadratic Forms and Positive Definiteness**  
### **Quadratic Form**  
A function $f(\mathbf{x}) = \mathbf{x}^\top A \mathbf{x}$, where $A$ is a symmetric matrix.  
- **Example**:  
  $$
  A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}, \quad f(x_1, x_2) = 2x_1^2 + 2x_1x_2 + 2x_2^2
  $$  

### **Positive Definite Matrices**  
A symmetric matrix $A$ is **positive definite** if $\mathbf{x}^\top A \mathbf{x} > 0$ for all $\mathbf{x} \neq \mathbf{0}$.  
- **Test**: All eigenvalues $\lambda_i > 0$.  
- **Application**: Hessian matrices in optimization (convexity).  

---

## **8. Singular Value Decomposition (SVD)**  
### **Intuition**  
SVD decomposes a matrix into three simpler matrices:  
$$
A = U \Sigma V^\top
$$  
- $U$ and $V$ are orthogonal matrices (rotations).  
- $\Sigma$ is a diagonal matrix of singular values (scaling factors).  

### **Mathematical Derivation**  
1. Compute $A^\top A$ and $AA^\top$.  
2. Find eigenvalues $\sigma_i^2$ and eigenvectors $\mathbf{v}_i$ of $A^\top A$.  
3. Define $\mathbf{u}_i = \frac{1}{\sigma_i} A\mathbf{v}_i$.  

**Example**:  
$$
A = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}, \quad U = V = I
$$
## **9. Applications in Machine Learning**  
### **1. Principal Component Analysis (PCA)**  
- **Goal**: Reduce dimensionality while preserving variance.  
- **Steps**:  
  1. Compute the covariance matrix $C = \frac{1}{n} X^\top X$.  
  2. Find eigenvectors $\mathbf{v}_i$ of $C$ (principal components).  
  3. Project data onto top-$k$ eigenvectors.  
### **2. Linear Regression**  
- **Model**: $\mathbf{y} = X\mathbf{\beta} + \mathbf{\epsilon}$.  
- **Solution**:  
  $$
  \hat{\beta} = (X^\top X)^{-1} X^\top \mathbf{y}
  $$
### **3. Neural Networks**  
- **Matrix Multiplication**: Weights and inputs are multiplied as matrices.  
- **Activation Functions**: Applied element-wise to vectors.  

---

## **Conclusion**  
Linear algebra provides the language for understanding and manipulating data in machine learning. From vectors and matrices to eigenvalues and SVD, these tools enable efficient computation and deep insights into complex systems.  

**Next Steps**:  
- Study **numerical linear algebra** for efficient algorithms.  
- Explore **optimization** techniques like gradient descent.  
- Learn about **kernel methods** and **deep learning** architectures.  

---

### **Jacobian Matrix**  
#### **Intuitive Explanation**  
The **Jacobian matrix** captures how a vector-valued function changes with respect to its inputs. It generalizes the concept of a derivative to functions that map between higher-dimensional spaces.  
- **Example**: If $ f: \mathbb{R}^n \to \mathbb{R}^m $, the Jacobian matrix $ J_f $ tells us how small changes in the input vector $ \mathbf{x} \in \mathbb{R}^n $ affect the output vector $ \mathbf{y} \in \mathbb{R}^m $.  
- **Geometric Interpretation**: The Jacobian matrix describes the **best linear approximation** of the function at a given point. For instance, in robotics, it maps joint velocities to end-effector velocities.  

#### **Mathematical Definition**  
Let $ f: \mathbb{R}^n \to \mathbb{R}^m $ be a function with components $ f_1, f_2, \dots, f_m $. The Jacobian matrix $ J_f $ is an $ m \times n $ matrix of partial derivatives:  
$$
J_f = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}
$$  
Each entry $ \frac{\partial f_i}{\partial x_j} $ represents how the $ i $-th output component changes with respect to the $ j $-th input variable.  

#### **Key Applications**  
1. **Probability Density Transformations**:  
   When transforming random variables (e.g., $ X \to Y = g(X) $), the **Jacobian determinant** adjusts the probability density to account for volume changes:  
   $$
   p_Y(y) = p_X(g^{-1}(y)) \cdot |\det(J_{g^{-1}}(y))|
   $$  
   Example: Converting from Cartesian to polar coordinates requires the Jacobian determinant to preserve probability mass.  

2. **Neural Networks**:  
   In backpropagation, the Jacobian matrix of the loss function with respect to the network parameters is used to update weights.  

3. **Robotics**:  
   The Jacobian matrix relates joint velocities to end-effector velocities in robotic arms.  

---

### **Hessian Matrix**  
#### **Intuitive Explanation**  
The **Hessian matrix** generalizes the second derivative to multivariable functions. It describes the **local curvature** of a function and is critical in optimization.  
- **Example**: For a function $ f(x, y) $, the Hessian tells you whether a critical point (where gradient is zero) is a minimum, maximum, or saddle point.  
- **Geometric Interpretation**: The Hessian encodes how the slope of the function changes in different directions, like how a valley curves upward or a hill curves downward.  

#### **Mathematical Definition**  
For a scalar-valued function $ f: \mathbb{R}^n \to \mathbb{R} $, the Hessian matrix $ H_f $ is an $ n \times n $ matrix of second-order partial derivatives:  
$$
H_f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
$$  
If $ f $ is twice continuously differentiable, the Hessian is symmetric (i.e., $ \frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i} $).  

#### **Key Applications**  
1. **Optimization**:  
   - **Newton’s Method**: Uses the Hessian to find minima/maxima by approximating the function as a quadratic:  
     $$
     \mathbf{x}_{k+1} = \mathbf{x}_k - H_f^{-1}(\mathbf{x}_k) \nabla f(\mathbf{x}_k)
     $$  
   - **Critical Point Classification**:  
     - **Positive Definite Hessian**: Local minimum.  
     - **Negative Definite Hessian**: Local maximum.  
     - **Indefinite Hessian**: Saddle point.  

2. **Machine Learning**:  
   - **Loss Function Analysis**: The Hessian’s eigenvalues indicate the curvature of the loss landscape. In deep learning, flat minima (small eigenvalues) are associated with better generalization.  
   - **Second-Order Optimization**: Algorithms like L-BFGS use Hessian approximations to accelerate convergence.  

3. **Physics and Economics**:  
   - Describes potential energy surfaces in molecular dynamics.  
   - Analyzes risk and volatility in financial models.  

---

### **Example: Quadratic Function**  
Let $ f(x, y) = x^2 + 2xy + 3y^2 $.  

#### **Jacobian Matrix**  
$$
J_f = \begin{bmatrix}
\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y}
\end{bmatrix}
= \begin{bmatrix}
2x + 2y & 2x + 6y
\end{bmatrix}
$$  

#### **Hessian Matrix**  
$$
H_f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2}
\end{bmatrix}
= \begin{bmatrix}
2 & 2 \\
2 & 6
\end{bmatrix}
$$  
The Hessian is constant (no $ x $ or $ y $ dependence), and its eigenvalues ($ \lambda_1 = 4 + \sqrt{8}, \lambda_2 = 4 - \sqrt{8} $) confirm it is positive definite (all eigenvalues > 0), so $ f(x, y) $ is convex.  

---

### **Key Differences**  
| **Aspect**          | **Jacobian Matrix**                | **Hessian Matrix**                |  
|----------------------|------------------------------------|-----------------------------------|  
| **Function Type**    | Vector-valued $ f: \mathbb{R}^n \to \mathbb{R}^m $ | Scalar-valued $ f: \mathbb{R}^n \to \mathbb{R} $ |  
| **Derivative Order** | First-order partial derivatives    | Second-order partial derivatives  |  
| **Symmetry**         | Not necessarily symmetric          | Symmetric (if $ f $ is smooth)  |  
| **Applications**     | Probability transformations, robotics | Optimization, curvature analysis |  

