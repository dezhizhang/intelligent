import torch
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.python.ops.gen_summary_ops import summary_writer
from torch.utils.tensorboard import SummaryWriter
import jieba
import torch.nn as nn

def dm02_embedding_show():
    sentence1 = '传智教育是一家上市公司, 旗下有黑马程序员品牌。我是在黑马这里学习人工智能'
    sentence2 = '我爱自然语言处理'
    sentences = [sentence1, sentence2]

    world_list = []
    for s in sentences:
        world_list.append(jieba.lcut(s))

    print(f"list-->{world_list}")
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(world_list)

    # print(f"tokenizer:{tokenizer.word_index}")

    seq_ids = tokenizer.texts_to_sequences(world_list)

    # 获取样本中的所有单词
    words = tokenizer.word_index.keys()

    # 实例化embedding对像
    embed = nn.Embedding(num_embeddings=len(words),embedding_dim=8)


    summarywriter = SummaryWriter()
    summarywriter.add_embedding(embed.weight,words)
    summarywriter.close()

    print(f"embed->{embed.weight}")



if __name__ == "__main__":
    dm02_embedding_show()

