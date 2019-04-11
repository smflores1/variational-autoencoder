import os

# File names:
MODEL_DETAILS = 'model_details.json'

# Directories
DIR_MODELS = 'models'
DIR_SAVED_MODEL = 'saved_model'

# File paths:
PATH_ROOT = os.getcwd()

# Lists:
LIST_TRAIN_TESTA_TESTB_KEYS = ['train', 'testa', 'testb']
LIST_ATTRIBUTES = ['graph',
                   'encoder_list',
                   'decoder_list',
                   'learning_rate',
                   'model_name',
                   'project_name',
                   'inputs_shape_list',
                   'inputs',
                   'inputs_shape',
                   '_inputs_shape',
                   'layer_shape_list',
                   '_layer_shape_list',
                   'optimizer',
                   'init',
                   'saver',
                   'sess',
                   'latent_means',
                   'latent_lstd2',
                   'latent_stdvs',
                   'encoder_shape_list',
                   '_encoder_shape_list',
                   'latent_shape',
                   '_latent_shape',
                   'latent_sample',
                   'output_means',
                   'output_lstd2',
                   'output_stdvs',
                   'decoder_shape_list',
                   '_decoder_shape_list',
                   'output_shape',
                   '_output_shape',
                   'output_sample',
                   'loss',
                   'project_path',
                   'models_path',
                   'model_path',
                   'num_trained_epochs',
                   'model_details_path',
                   'timestamp',
                   'avg_loss',
                   'saved_model_path',
                   'builder',
                   'is_training',
                   'use_batch_normalization',
                   'averaging_axes_length',
                   'loss_type',
                   'loss_inputs_shape_list',
                   'percept_list',
                   '_percept_shape_list',
                   'percept_shape_list',
                   'loss_type',
                   'encoder_loss_weight',
                   'decoder_loss_weight',
                   'is_variational',
                   'encoder_loss',
                   'decoder_loss']
LIST_MODEL_DETAIL_KEYS = ['encoder_list',
                          'decoder_list',
                          'inputs_shape_list',
                          'learning_rate',
                          'project_name',
                          'model_name',
                          'num_trained_epochs',
                          'use_batch_normalization',
                          'loss_type',
                          'encoder_loss_weight',
                          'decoder_loss_weight',
                          'is_variational']

PERCEPT_LIST = [{'layer_type': 're-size', 'output_shape': [224, 224], 'loss_weight': 0},
                {'layer_type': 'convolu', 'kernel_shape': [3, 3], 'output_chann': [64],  'pool_shape': [1, 1], 'activation': 'relu', 'loss_weight': 0.333},
                {'layer_type': 'convolu', 'kernel_shape': [3, 3], 'output_chann': [64],  'pool_shape': [2, 2], 'activation': 'relu', 'loss_weight': 0},
                {'layer_type': 'convolu', 'kernel_shape': [3, 3], 'output_chann': [128], 'pool_shape': [1, 1], 'activation': 'relu', 'loss_weight': 0.333},
                {'layer_type': 'convolu', 'kernel_shape': [3, 3], 'output_chann': [128], 'pool_shape': [2, 2], 'activation': 'relu', 'loss_weight': 0},
                {'layer_type': 'convolu', 'kernel_shape': [3, 3], 'output_chann': [256], 'pool_shape': [1, 1], 'activation': 'relu', 'loss_weight': 0.333}]
