
# Deep Learning and AI Knowledge Points

## Self-Attention Mechanisms and Transformers
- **Overview**: Focus on the fundamental concepts of self-attention, advantages over traditional RNN and CNN models, architecture of transformers, and their applications in NLP tasks.
- **Key Components**: Includes mathematical formulations, algorithmic descriptions, illustrations of the transformer model, and significant research references.

## Difference Between Self-Attention and Traditional Attention Mechanisms
- **Focus of Attention**: Self-attention explores the relationship among various positions within the data, unlike traditional mechanisms that relate input to output.
- **Computational Complexity**: Self-attention has a higher computational cost due to attention weight calculations for each position.
- **Memory Usage**: Requires more memory to store attention weights for all positions, compared to traditional methods.
- **Applications**: More suitable for sequences with long lengths or complex structures, e.g., machine translation and natural language generation.

## Limitations of RNNs and CNNs in NLP
- **RNNs**: Struggle to capture long-range dependencies between texts due to sequential processing.
- **CNNs**: Efficient in capturing local patterns but falter with long-range dependencies.
- _Key Point_: The advent of the Transformer model addresses these limitations by leveraging self-attention mechanisms for better processing speed and handling long-distance relationships in text data.

## Query Vectors Construction
- Methods for constructing query vectors depend on specific applications and include word embeddings, TF-IDF, N-grams, sentiment analysis, and text clustering techniques.

## Masked Self-Attention
- **Purpose**: Implemented to prevent the model from learning irrelevant information by masking certain parts of the input during training, enhancing the model's generalization capabilities.

## Encoder-Decoder Attention vs. Transformer Attention
- **Encoder-Decoder Attention**: Utilized to focus the decoder on specific parts of the input for tasks like machine translation and text summarization.
- **Transformer Attention**: Essential in the Transformer model for capturing relationships within the input sequence and between input and output tokens, facilitating accurate outputs in various NLP tasks.
