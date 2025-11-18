from tensorflow.keras.preprocessing import sequence

cutlen = 10

def padding(x_train):
    return sequence.pad_sequences(x_train,cutlen)



if __name__ == "__main__":
    x_train = [[1,23,5,32,55,63,2,21,78,32,23.1],[2,32,1,23,1]]
    res = padding(x_train)
    print(res)
    