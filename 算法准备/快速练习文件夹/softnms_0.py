# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: nms.py
@CreateTime: 2020/6/16 23:02
'''
import copy
import cv2
import numpy as np
def soft_nms(dets, iou_thresh=0.3, sigma=0.5, thresh=0.001, method=1):
    '''
    https://github.com/DocF/Soft-NMS/blob/master/soft_nms.py
    :param dets: [[x1, y1, x2, y2, score]，[x1, y1, x2, y2, score]，[x1, y1, x2, y2, score]]
    :param iou_thresh: iou thresh
    :param sigma: std of gaussian
    :param thresh: the last score thresh
    :param method: 1、linear 2、gaussian 3、originl nms
    :return: keep bboxes
    '''
    N = dets.shape[0]  # the size of bboxes
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    for i in range(N):
        temp_box = copy.deepcopy(dets[i, :4])
        temp_score = dets[i, 4]
        temp_area = areas[i]
        pos = i + 1

        if i != N - 1:
            maxscore = np.max(dets[:, 4][pos:]) # 最大分数是多少
            maxpos = np.argmax(dets[:, 4][pos:]) # 最大分数在数组中的位置，pos初始值为1得到的位置+1就是
        else:
            maxscore = dets[:, 4][-1]
            maxpos = -1

        if temp_score < maxscore:
            dets[i, :4] = dets[maxpos + i + 1, :4]
            dets[maxpos + i + 1, :4] = temp_box

            dets[i, 4] = dets[maxpos + i + 1, 4]
            dets[maxpos + i + 1, 4] = temp_score

            areas[i] = areas[maxpos + i + 1]
            areas[maxpos + i + 1] = temp_area

        xx1 = np.maximum(x1[i], x1[pos:])
        xx2 = np.maximum(x2[i], x2[pos:])
        yy1 = np.maximum(y1[i], y1[pos:])
        yy2 = np.maximum(y2[i], y2[pos:])

        w = np.maximum(xx2 - xx1 + 1.0, 0.)
        h = np.maximum(yy2 - yy1 + 1.0, 0.)

        inters = w * h
        ious = inters / (areas[i] + areas[pos:] - inters)

        if method == 1:
            weight = np.ones(ious.shape)
            weight[ious > iou_thresh] = weight[ious > iou_thresh] - ious[ious > iou_thresh]
        elif method == 2:
            weight = np.exp(-ious * ious / sigma)
        else:
            weight = np.ones(ious.shape)
            weight[ious > iou_thresh] = 0

        dets[pos:, 4] = dets[pos:, 4] * weight

    print('dets:',dets[:, 4])
    inds = np.argwhere(dets[:, 4] > thresh)
    print('inds:',inds)
    keep = inds.astype(int)
    return keep

if __name__ == '__main__':
    bboxs = [[0.0,0.0,300.0,300.0,0.7],[1.0,1.0,500.0,250.0,0.6],[5.0,5.0,330.0,400.0,0.5],[500.0,500.0,800.0,1000.0,0.8],[450.0,600.0,900.0,900.0,0.7],[470.0,550.0,990.0,900.0,0.65]]
    img = np.ones((1000,1000,3))*255
    # for box in bboxs:
    #     cv2.rectangle(img,(int(box[0]),int(box[1])),(int(box[2]),int(box[3])),(0,0,255),2)
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    b = np.array(bboxs)
    print(soft_nms(b))