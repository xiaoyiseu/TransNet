from Transformer.transformer import *
from tensorflow.keras.layers import MaxPooling1D,Conv1D,LSTM
from tensorflow.keras.models import Model
from att import Attention

def TransNet():  # 稍作改动，以便维度对齐
    inputs1 = layers.Input(shape=(1, 30,), name="input1")
    inputs2 = layers.Input(shape=(43,), name="input2")

    def Text(inputs1):
        cnn1 = LSTM(32, dropout=0.2, return_sequences=True)(inputs1)
        cnn1 = MaxPooling1D(pool_size=2, padding='same')(cnn1)
        cnn2 = Conv1D(32, 4, padding='same', strides=1, activation='relu')(inputs1)
        cnn2 = MaxPooling1D(pool_size=2, padding='same')(cnn2)
        cnn3 = Conv1D(32, 5, padding='same', strides=1, activation='relu')(inputs1)
        cnn3 = MaxPooling1D(pool_size=2, padding='same')(cnn3)
        cnn4 = layers.concatenate([cnn1, cnn2, cnn3], axis=-1)
        cnn5 = LSTM(32, dropout=0.2, return_sequences=True)(cnn4)
        cnn6 = MaxPooling1D(pool_size=2, padding='same')(cnn5)
        return cnn6

    def Text2(inputs1):
        cnn1 = LSTM(32, dropout=0.2, return_sequences=True)(inputs1)
        cnn2 = Conv1D(32, 4, padding='same', strides=1, activation='relu')(inputs1)
        cnn2 = MaxPooling1D(pool_size=2, padding='same')(cnn2)
        cnn3 = Conv1D(32, 5, padding='same', strides=1, activation='relu')(inputs1)
        cnn3 = MaxPooling1D(pool_size=2, padding='same')(cnn3)
        cnn4 = layers.concatenate([cnn1, cnn2, cnn3], axis=1)
        cnn5 = LSTM(36, dropout=0.2, return_sequences=True)(cnn4)
        return cnn5

    def Trans(inputs2):
        embedding_layer = TokenAndPositionEmbedding(43, 6000, 36)
        x = embedding_layer(inputs2)
        transformer_block = TransformerBlock(36, 6, 32)
        x = transformer_block(x)
        return x

    F = layers.concatenate([Text2(inputs1), Trans(inputs2)], axis=1)
    ConcatFeature = Attention(16, name="attention1")(F)

    output1 = layers.Dense(4, activation='softmax', name="dense1")(ConcatFeature)
    output2 = layers.Dense(10, activation='softmax', name="dense2")(ConcatFeature)
    model = Model(inputs=[inputs1, inputs2], outputs=[output1, output2])
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

