from yacs.config import CfgNode as CN


_C = CN()

_C.VERSION = 'v1.0'
_C.DESCRIPTION = "MonoCon Default Configuration"

_C.OUTPUT_DIR = "/home/user/Desktop/Geonsoo/monocon-pytorch/checkpoint/base-seed0"                      # Output Directory
_C.SEED = 0                             # -1: Random Seed Selection
_C.GPU_ID = 1                           # Index of GPU to use


# Data
_C.DATA = CN()
_C.DATA.ROOT = r'/home/user/SSD/KITTI'                  # KITTI Root
_C.DATA.BATCH_SIZE = 8
_C.DATA.NUM_WORKERS = 4
_C.DATA.TRAIN_SPLIT = 'train'
_C.DATA.TEST_SPLIT = 'val'

_C.DATA.STATS = CN()
_C.DATA.STATS.MEAN = [123.675, 116.28, 103.53]
_C.DATA.STATS.STD = [58.395, 57.12, 57.375]

_C.DATA.FILTER = CN()
_C.DATA.FILTER.MIN_HEIGHT = 25
_C.DATA.FILTER.MIN_DEPTH = 2
_C.DATA.FILTER.MAX_DEPTH = 65
_C.DATA.FILTER.MAX_TRUNCATION = 0.5
_C.DATA.FILTER.MAX_OCCLUSION = 2


# Model
_C.MODEL = CN()

_C.MODEL.BACKBONE = CN()
_C.MODEL.BACKBONE.NUM_LAYERS = 34
_C.MODEL.BACKBONE.IMAGENET_PRETRAINED = True

_C.MODEL.HEAD = CN()
_C.MODEL.HEAD.NUM_CLASSES = 3
_C.MODEL.HEAD.MAX_OBJS = 30


# Optimization
_C.SOLVER = CN()

_C.SOLVER.OPTIM = CN()
_C.SOLVER.OPTIM.LR = 2.25E-04
_C.SOLVER.OPTIM.WEIGHT_DECAY = 1E-05
_C.SOLVER.OPTIM.NUM_EPOCHS = 200        # Max Training Epochs

_C.SOLVER.SCHEDULER = CN()
_C.SOLVER.SCHEDULER.ENABLE = True

_C.SOLVER.CLIP_GRAD = CN()
_C.SOLVER.CLIP_GRAD.ENABLE = True
_C.SOLVER.CLIP_GRAD.NORM_TYPE = 2.0
_C.SOLVER.CLIP_GRAD.MAX_NORM = 35 


# Period
_C.PERIOD = CN()
_C.PERIOD.EVAL_PERIOD = 10               # In Epochs / Set -1 if you don't want validation
_C.PERIOD.LOG_PERIOD = 100               # In Steps

