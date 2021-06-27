import visualkeras
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from keras.utils.vis_utils import plot_model

classs = 7

model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape = (256,256,3), activation='relu', padding='same', name='block1_conv1'))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv2'))
model.add(MaxPooling2D((2, 2), name='block1_pool'))
model.add(Dropout(0.25))

# Block 2
model.add(Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv1'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv2'))
model.add(MaxPooling2D((2, 2), name='block2_pool'))
model.add(Dropout(0.25))

# Block 3
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv1'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv2'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv3'))
model.add(MaxPooling2D((2, 2), name='block3_pool'))
model.add(Dropout(0.25))

# Block 4
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', name='block4_conv1'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', name='block4_conv2'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', name='block4_conv3'))
model.add(MaxPooling2D((2, 2), name='block4_pool'))
model.add(Dropout(0.25))

# Block 5
model.add(Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv1'))
model.add(Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv2'))
model.add(Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv3'))
model.add(MaxPooling2D((2, 2), name='block5_pool'))
model.add(Dropout(0.25))

#strides=(2, 2),

model.add(Flatten())
model.add(Dense(units = 128, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(units = 64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(units = 32, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(units = classs, activation = 'softmax'))

# visualkeras.layered_view(model).show() # display using your system viewer
# visualkeras.layered_view(model, to_file='output.png') # write to disk
# visualkeras.layered_view(model, to_file='output.png').show() # write and show

# visualkeras.layered_view(model)
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)