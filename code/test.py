# import tensorflow as tf
import tensorflow.compat.v1 as tf
h = tf.constant("hello")
w = tf.constant(" world!")
z = tf.add(h, w)
hw = h + w

with tf.Session() as sess:
    ans = sess.run(hw)
    
print(ans)