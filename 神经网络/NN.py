import tensorflow as tf
import numpy as np

BATCH_SIZE = 8 #每次喂给神经网络多少组数据

seed = 23455

#基于seed 产生随机数
rdm = np.random.mtrand.RandomState(seed)
#随机生成32行2列矩阵，表示32组特征集合(假设为体积和重量)作为输入数据集
X = rdm.rand(32, 2)
# print()

#遍历，x0 + x1 < 1 Y 赋值为1，否则 Y 赋值为0
Y = 0
for (x0,x1) in X:
    if x0 + x1 < 1:
        Y = 1
    else:
        Y = 0
# Y = [[int(x0 + x1 < 1)]]for(x0,x1) in X]

#定义神经网络输入、参数、输出。定义前向传播过程
x = tf.placeholder(tf.float32,shape=(None,2)) #只知道体积和体重，None 表示不知道可以拿到多少组特征
y_ = tf.placeholder(tf.float32,shape=(None,1)) #只知道特征是是否合格，不知道可以拿到多少组合格与否的特征(零件是否合格)
w1 = tf.Variable(tf.random_normal([2,3],stddev = 1, seed = 1))
w2 = tf.Variable(tf.random_normal([3,1],stddev = 1, seed = 1))

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
#选用均方误差定义损失函数
loss = tf.reduce_mean(tf.square(y-y_))
#选用梯度下降实现训练过程,学习率为0.0001（也可以选择Momentum和Adam）
train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(loss)
#生成会话
with tf.Session() as sess:
    init_op = tf.global_variables_initializer() #初始化数据
    sess.run(init_op)
    #输出未训练的参数
    print ("w1:\n",sess.run(w1))
        print ("w2:\n",sess.run(w2))
        
        #训练模型
        STEPS = 3000
            for i in range(STEPS):
                start = (i * BATCH_SIZE) % 32
                end = start + BATCH_SIZE
            sess.run(train_step,feed_dict={x:X[start,end],y_:Y[start,end]})
            # sess.run(train_step, feed_dict={x: X.index(X,beg=start,end=end), y_: Y.index(Y,beg=start,end=end)})
            total_loss = sess.run(loss,feed_dict={x:X,y_:Y})
            print("after %d training step(s),loss loss is %g" % (i,total_loss))
                #输出训练后的参数取值
                print ("\n")
                print ("w1:\n",sess.run(w1))
                print ("w1:\n",sess.run(w2))
