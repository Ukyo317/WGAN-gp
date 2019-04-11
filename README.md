## Introduction

  Generative adversarial network(GAN) has shown great results in many generative tasks, which try to replicate rich contents in the real world, such as images, human language, and music.

  The nerwork was based on game theory: two models, which are named as generator and discriminator, compete with each other in order to enable both to become stronger at the same time. However, it is real a challenge that train a perfect GAN model. And people have met many issues like training instability and failing to achieve convergence in the training process.

  In order to solve these problems, some new methods were proposed, one of them was called WGAN, which has proved its great performance in experiments. Compared to the classical GAN, the WGAN uses Wasserstein distance as cost function instead of JS or KL divergence, which efficiently solve the “gradient disappear” and “mode collapse” problems of original model. In detail, the Wasserstein distance is the minimum cost of transporting mass in converting the data distribution q to the data distribution p, and that is a kind of meaningful and smooth representation of distance in special cases.

  Although the WGAN has made improvement, in real experiments there still exists problems like hard to train and slow to converge. Aimed to solve these deficiencies, researchers put up with an advanced version of WGAN: WGAN-gp(Wasserstein GAN with gradient penalt. The WGAN-gp inherits advantages of stable training precess and avoiding mode collapse problem in WGAN by adding a gradient penalty term as a part of cost.

  In conclusion, WGAN-gp is a fancy and stable machine learning model on which we want to implement experiments and compare several different optimization strategies learned from classes in this term.

## Our Work

  In this project, We complete two tasks mainly: Verifying the great performance of the WGAN-gp model, and comparing the effects of different optimization methods.

  We use Tensorflow 1.4 and Pytorch 0.4 to train WGAN-gp model under python 3.6 environment. As GAN has two parts: generator and discriminator, we use simple three layers CNN and similarly three layers DCNN to build these two parts.

  Then based on two different image datasets, MNIST and Cifar10 Datasets, we try to train WGAN-gp model to generate data which has the similar distribution with MNIST and Cifar10, as well as attempt to generate “fake” images. In each task, we separately try three different kinds of optimization methods, which are SGD, Adam, RMSprop respectively. Furthermore, we plot the cost history of the generator and discriminator to monitor the whole process of training. And we also plot the Wasserstein distance to identify performance of the final model, since the WGAN uses Wasserstein distance to measure distance between generated data and true data. Most importantly, we utilize a special measure method inception score to reflect the quality of the generated data based on the Cifar10 dataset. We hope to make sure whether we could use Adam to optimize WGAN-gp.

## Experiments

### MNIST Dataset

  First of all, we try different optimizers on MNIST dataset to train WGAN-gp model. In this part, we have used SGD, Adam with β=(0.9,0.99)β=(0.9,0.99), RMSprop with α=0.9α=0.9 with the same learning 10−410−4.

#### Cost History

![](C:\Users\cheny\OneDrive\Desktop\backup\NU Courses\18Fall\395\Images\mnist_cost.png)



Wasserstein Distance

![](C:\Users\cheny\OneDrive\Desktop\backup\NU Courses\18Fall\395\Images\mnist_distance.png)

### Cifar10 Dataset

Then we try different optimizers on Cifar10 dataset to train WGAN-gp model. In this part we also use SGD, Adam with β=(0.9,0.99)β=(0.9,0.99), RMSprop with α=0.9α=0.9with the same learning 10−410−4 to compare their performance.

#### Cost History

![](C:\Users\cheny\OneDrive\Desktop\backup\NU Courses\18Fall\395\Images\cifar_cost.png)

Wasserstein Distance

![](C:\Users\cheny\OneDrive\Desktop\backup\NU Courses\18Fall\395\Images\cifar_distance.png)

Generated Images

![](C:\Users\cheny\OneDrive\Desktop\backup\NU Courses\18Fall\395\Images\cifar_image.png)

Inception Score

![](C:\Users\cheny\OneDrive\Desktop\backup\NU Courses\18Fall\395\Images\cifar_inception.png)

Analysis

  In the process of training, we found that the GAN would cost much time to train both networks. Therefore, after repeated attempts, we choose to train 80000 epochs of each optimization strategies to compare their performance eventually.

  According to the cost history, we can find that Adam and RMSprop algorithms converge well, but SGD algorithm does not converge to zero. Besides, the Adam and RMSprop converge faster than SGD method. What’s more, the plots shows that the training process is stable and able to generate figures that are similar to the true images. That means no mode collapse existed for each optimizers. As a result, the training process of WGAN-gp is stable without being concerned about mode collapse and convergence hardness. Furthermore, it is claimed that RMSprop and SGD work well for training WGAN but Adam does not work. However, our results shows that Adam method converges well in WGAN-gp case, which solves the problem of choosing proper optimizers.

  After the analysis of the cost history, we pay attention to Wasserstein Distance. As can be seen in these plots, Adam and RMSprop algorithms converge to zero very fast, but SGD is slow, which also implies that Adam and RMSprop have good converging performance and all these optimizers can be used to train WGAN-gp model.

  Inception score is a measurement of generated image’s quality for Cifar10 dataset. From the plots, we can summarized that both Adam and RMSprop algorithms converge to high inception score and RMSprop is slightly faster than Adam. SGD fails to get a high inception score due to insufficient convergence. From the results, we make the conclusion that Adam and RMSprop can train good generator and RMSprop is slightly faster than Adam.

## Conclusion

  In this project, we compare three different optimizers’ performance on traing WGAN-gp case. According to the results, we are able to make the conclusion that the whole traing process is stable with all optimizers and could generate images that is similar to the real pictures with no mode collapse problem. What’s more, all of the optimizers work, which enable us to eliminate the so-called problem that Adam algorithms does not work in WGAN case. Moreover, RMSprop and Adam outperform SGD, and RMSprop converges slightly faster than Adam. As a result, we can conclude that RMSprop is the best optimizer for training WGAN-gp model.

  All in all, we have achieved all of our objectives in this project. We gain experience using deep learning packages like Tensorflow and Pytorch to write code, as well as use GPU of our laptop to train deep neural networks. Furthermore, we compare the performance of different optimizers on a specific task training WGAN-gp model and get the conclusion that RMSprop is the best choice of the three. Optimization is the one of the best components for deep neural network and we gain a lot of experience in this project.

  Our presentation is shown in this Youtube link.

<https://www.youtube.com/watch?v=Nhl0n87kxhY&feature=youtu.be>