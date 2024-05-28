import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model
from tensorflow.python.framework import graph_io
from tensorflow.python.framework import graph_util


def create_model(input_length, output_length, vocab_size):
    encoder_inputs = Input(shape=(input_length,))
    encoder = LSTM(256, return_state=True)
    encoder_outputs, state_h, state_c = encoder(encoder_inputs)
    encoder_states = [state_h, state_c]

    decoder_inputs = Input(shape=(output_length,))
    decoder_lstm = LSTM(256, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
    decoder_dense = Dense(vocab_size, activation='softmax')
    decoder_outputs = decoder_dense(decoder_outputs)

    model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    return model

# Define the model
input_length = 100  # example length of input sequence
output_length = 100  # example length of output sequence
vocab_size = 10000  # example vocabulary size

model = create_model(input_length, output_length, vocab_size)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# Assuming X_train and y_train are your input and output training data
model.fit([X_train, y_train], y_train, batch_size=64, epochs=10, validation_split=0.2)

def freeze_model(session, model, output_node_names):
    graph = session.graph
    input_graph_def = graph.as_graph_def()
    output_graph_def = graph_util.convert_variables_to_constants(
        session,
        input_graph_def,
        output_node_names.split(",")
    )
    return output_graph_def

sess = tf.keras.backend.get_session()
output_graph_def = freeze_model(sess, model, output_node_names="dense/Softmax")
graph_io.write_graph(output_graph_def, ".", "frozen_inference_graph_816.pb", as_text=False)