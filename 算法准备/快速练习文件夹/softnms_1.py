# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: keras_soft_nms.py
@CreateTime: 2020/7/12 15:49
'''

import time
import numpy as np
import torch


def soft_nms_pytorch(dets, box_scores, sigma=0.5, thresh=0.001, cuda=0):
    """
    Build a pytorch implement of Soft NMS algorithm.
    # Augments
        dets:        boxes coordinate tensor (format:[y1, x1, y2, x2])
        box_scores:  box score tensors
        sigma:       variance of Gaussian function
        thresh:      score thresh
        cuda:        CUDA flag
    # Return
        the index of the selected boxes
    """

    # Indexes concatenate boxes with the last column
    N = dets.shape[0]
    if cuda:
        indexes = torch.arange(0, N, dtype=torch.float).cuda().view(N, 1)
    else:
        indexes = torch.arange(0, N, dtype=torch.float).view(N, 1)
    dets = torch.cat((dets, indexes), dim=1)

    # The order of boxes coordinate is [y1,x1,y2,x2]
    y1 = dets[:, 0]
    x1 = dets[:, 1]
    y2 = dets[:, 2]
    x2 = dets[:, 3]
    scores = box_scores
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    for i in range(N):
        # intermediate parameters for later parameters exchange
        tscore = scores[i].clone()
        pos = i + 1

        if i != N - 1:
            maxscore, maxpos = torch.max(scores[pos:], dim=0)
            if tscore < maxscore:
                dets[i], dets[maxpos.item() + i + 1] = dets[maxpos.item() + i + 1].clone(), dets[i].clone()
                scores[i], scores[maxpos.item() + i + 1] = scores[maxpos.item() + i + 1].clone(), scores[i].clone()
                areas[i], areas[maxpos + i + 1] = areas[maxpos + i + 1].clone(), areas[i].clone()

        # IoU calculate
        yy1 = np.maximum(dets[i, 0].to("cpu").numpy(), dets[pos:, 0].to("cpu").numpy())
        xx1 = np.maximum(dets[i, 1].to("cpu").numpy(), dets[pos:, 1].to("cpu").numpy())
        yy2 = np.minimum(dets[i, 2].to("cpu").numpy(), dets[pos:, 2].to("cpu").numpy())
        xx2 = np.minimum(dets[i, 3].to("cpu").numpy(), dets[pos:, 3].to("cpu").numpy())

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = torch.tensor(w * h).cuda() if cuda else torch.tensor(w * h)
        ovr = torch.div(inter, (areas[i] + areas[pos:] - inter))

        # Gaussian decay
        weight = torch.exp(-(ovr * ovr) / sigma)
        scores[pos:] = weight * scores[pos:]

    # select the boxes and keep the corresponding indexes
    keep = dets[:, 4][scores > thresh].int()
    return keep


def speed():
    boxes = 1000 * torch.rand((1000, 100, 4), dtype=torch.float)
    boxscores = torch.rand((1000, 100), dtype=torch.float)

    # cuda flag
    cuda = 1 if torch.cuda.is_available() else 0
    if cuda:
        boxes = boxes.cuda()
        boxscores = boxscores.cuda()

    start = time.time()
    for i in range(1000):
        soft_nms_pytorch(boxes[i], boxscores[i], cuda=cuda)
    end = time.time()
    print("Average run time: %f ms" % (end - start))


def test():
    # boxes and boxscores
    # boxes = torch.tensor([[200, 200, 400, 400],
    #                       [220, 220, 420, 420],
    #                       [200, 240, 400, 440],
    #                       [240, 200, 440, 400],
    #                       [1, 1, 2, 2]], dtype=torch.float)
    # boxscores = torch.tensor([0.8, 0.7, 0.6, 0.5, 0.9], dtype=torch.float)
    boxes = torch.tensor([[0.0,0.0,300.0,300.0],
                          [1.0,1.0,500.0,250.0],
                          [5.0,5.0,330.0,400.0],
                          [500.0,500.0,800.0,1000.0],
                          [450.0,600.0,900.0,900.0],
                          [470.0, 550.0, 990.0, 900.0]], dtype=torch.float)
    boxscores = torch.tensor([0.7, 0.6, 0.5, 0.8,0.7,0.65], dtype=torch.float)

# b = [[0.0,0.0,300.0,300.0,0.7],
#      [1.0,1.0,500.0,250.0,0.6],
#      [5.0,5.0,330.0,400.0,0.5],
# [500.0,500.0,800.0,1000.0,0.8],
# [450.0,600.0,900.0,900.0,0.7],
# [470.0,550.0,990.0,900.0,0.65]]


    # cuda flag
    cuda = 1 if torch.cuda.is_available() else 0
    if cuda:
        boxes = boxes.cuda()
        boxscores = boxscores.cuda()

    print(soft_nms_pytorch(boxes, boxscores, cuda=cuda))


if __name__ == '__main__':
    test()
    # speed()

