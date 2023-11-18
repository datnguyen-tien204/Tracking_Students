# -*- coding: UTF-8 -*-
import cv2 as cv
import os
import sys
from pathlib import Path
from Pose.pose_visualizer import TfPoseVisualizer

file_path = Path.cwd()
cam_width, cam_height = 1280, 720
# input size to the model
# VGG trained in 656*368; mobilenet_thin trained in 432*368 (from tf-pose-estimation)
input_width, input_height = 656, 368


def choose_run_mode(camera):
    cap = cv.VideoCapture(camera)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cam_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cam_height)
    return cap


def load_pretrain_model(model):
    dyn_graph_path = {
        'VGG_origin': str(file_path / "Pose/graph_models/VGG_origin/graph_freeze.pb"),
        'mobilenet_thin': str(file_path / "Pose/graph_models/mobilenet_thin/graph_opt.pb")
    }
    graph_path = dyn_graph_path[model]
    if not os.path.isfile(graph_path):
        raise Exception('Graph file doesn\'t exist, path=%s' % graph_path)

    return TfPoseVisualizer(graph_path, target_size=(input_width, input_height))
