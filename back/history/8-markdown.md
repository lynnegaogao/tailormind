## Deep Learning and AI Knowledge Points

### Deep Learning Architectures
- **Convolutional Neural Networks (CNNs):** Includes discussions on the architecture, data augmentation techniques, dropout method, and performance results.
- **Deep Belief Networks (DBNs):** Examines issues with backpropagation and presents the structure and training, including Boltzmann machines, restricted Boltzmann machines (RBMs), and deep Boltzmann machines (DBMs). Highlights the benefits of pre-training with experiments on digit image recognition.

### Gradient-Based Learning
- **Advantages:**
  1. Easy to implement with reduced computational complexity.
  2. Capable of achieving high accuracy by minimizing the loss function.
  3. Robustness to various types of data.
  4. Scalability with large datasets or complex models.

- **Disadvantages:**
  1. Slow convergence due to multiple iterations needed for parameter updates.
  2. Possibility of falling into local minima, leading to suboptimal performance.
  3. Sensitivity to noise in the input data.
  4. Lack of interpretability of the model's decisions.

### Backpropagation in Machine Learning
- A method used to train neural networks, allowing the network to learn patterns and make accurate predictions. Essential for training deep neural networks with multiple layers by adjusting weights and biases to minimize error.

### Batch Normalization
- A technique to improve training speed and stability of neural networks by normalizing the input data distribution within each batch. This addresses issues of gradient vanishing or exploding and contributes to faster training and better feature learning.