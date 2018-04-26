import tensorflow as tf


a = tf.constant(5)
b = tf.constant(4)
c = tf.multiply(a, b, name="nultiplier_c")
d = tf.add(a, b, name="adder_d")
e = tf.add(c, d, name="adder_e")


sess = tf.Session()
output = sess.run(e)


writer = tf.summary.FileWriter('./my_graph', sess.graph)
writer.close()
sess.close()
