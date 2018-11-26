import tensorflow as tf

class TFLogger():
    def __init__(selg, log_dir):
        self.writer = tf.FileWriter(log_dir) 
    def scalar_summary(self, tag, value, step):
        summary = tf.Summary(value=[tf.Summary.Value(tag=tag, sample_value=value)])
        self.writer.add_summary(summary, step)