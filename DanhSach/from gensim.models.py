from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

# Chuẩn bị dữ liệu
data = ["I love machine learning", "I love natural language processing", "I love coding"]

tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]

# Train mô hình Doc2Vec
model = Doc2Vec(vector_size=20, min_count=2, epochs=10)
model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

# Sử dụng mô hình để nhúng đoạn văn bản
vector = model.infer_vector(word_tokenize("I love coding"))
print(vector)
