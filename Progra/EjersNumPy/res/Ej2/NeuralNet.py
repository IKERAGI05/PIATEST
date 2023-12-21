import tensorflow._api.v2.compat.v1 as tf
class NeuralNet:
# INSERTAR CÓDIGO AQUÍ SEGUNDA TAREA#######################
    def __init__(self):
        self.iX=0
        self.iY=0
        self.py=0
        self.loss=0
        self.optimizer=0

    def create_nn(self, topology_v, lr):
        self.iX=tf.placeholder('float', shape=[None, 2])
        self.iY=tf.placeholder('float', shape=[None])

        W1 = tf.Variable(tf.random_normal([topology_v[0], topology_v[1]]), name='Weights_1')
        b1 = tf.Variable(tf.random_normal([topology_v[1]]), name='bias_1')

        l1 = tf.nn.relu(tf.add(tf.matmul(self.iX, W1), b1))

        # Capa 2
        W2 = tf.Variable(tf.random_normal([topology_v[1], topology_v[2]]), name='Weights_2')
        b2 = tf.Variable(tf.random_normal([topology_v[2]]), name='bias_2')

        l2 = tf.nn.relu(tf.add(tf.matmul(l1, W2), b2))

        # Capa 3
        W3 = tf.Variable(tf.random_normal([topology_v[2], topology_v[3]]), name='Weights_3')
        b3 = tf.Variable(tf.random_normal([topology_v[3]]), name='bias_3')

        # Vector de predicciones de Y.
        self.py = tf.nn.sigmoid(tf.add(tf.matmul(l2, W3), b3))[:, 0]

        # Evaluación de las predicciones.
        self.loss = tf.losses.mean_squared_error(self.py, self.iY)


        self.optimizer = tf.train.GradientDescentOptimizer(lr).minimize(self.loss)




###########################################################
