# 读取doc_vectors/vector.npz得到所有候选文档的向量表示
# 对于测试集中的每个query，调用my_embedding_model.query_embedding()方法，得到query的向量表示
# 基于上述向量表示给出query查询到的前k个文档，输出为output/retrieved_doc.json

from .embedding_model import EmbeddingModel
my_embedding_model = EmbeddingModel()