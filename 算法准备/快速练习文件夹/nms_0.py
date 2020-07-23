# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: nms_0.py
@CreateTime: 2020/7/12 16:11
'''

import numpy as np
def nms(bboxes, confidence_score, threshold):
    """非极大抑制过程
    :param bboxes: 同类别候选框坐标
    :param confidence: 同类别候选框分数
    :param threshold: iou阈值
    :return:
    """
    # 1、传入无候选框返回空
    if len(bboxes) == 0:
        return [], []
    # 强转数组
    bboxes = np.array(bboxes)
    score = np.array(confidence_score)

    # 取出n个的极坐标点
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]

    # 2、对候选框进行NMS筛选
    # 返回的框坐标和分数
    picked_boxes = []
    picked_score = []
    # 对置信度进行排序, 获取排序后的下标序号, argsort默认从小到大排序
    order = np.argsort(score)
    areas = (x2 - x1) * (y2 - y1)
    while order.size > 0:
        # 将当前置信度最大的框加入返回值列表中
        index = order[-1]
        picked_boxes.append(bboxes[index])
        picked_score.append(confidence_score[index])

        # 获取当前置信度最大的候选框与其他任意候选框的相交面积
        x11 = np.maximum(x1[index], x1[order[:-1]])
        y11 = np.maximum(y1[index], y1[order[:-1]])
        x22 = np.minimum(x2[index], x2[order[:-1]])
        y22 = np.minimum(y2[index], y2[order[:-1]])
        w = np.maximum(0.0, x22 - x11)
        h = np.maximum(0.0, y22 - y11)
        intersection = w * h

        # 利用相交的面积和两个框自身的面积计算框的交并比, 将交并比大于阈值的框删除
        ratio = intersection / (areas[index] + areas[order[:-1]] - intersection)
        keep_boxes_indics = np.where(ratio < threshold)
        order = order[keep_boxes_indics]
    return picked_boxes, picked_score


if __name__ == '__main__':
    # bounding = [(187, 82, 337, 317), (150, 67, 305, 282), (246, 121, 368, 304)]
    # confidence_score = [0.9, 0.75, 0.8]
    bounding = [[0.0,0.0,300.0,300.0],
                          [1.0,1.0,500.0,250.0],
                          [5.0,5.0,330.0,400.0],
                          [500.0,500.0,800.0,1000.0],
                          [450.0,600.0,900.0,900.0],
                          [470.0, 550.0, 990.0, 900.0]]
    confidence_score = [0.7, 0.6, 0.5, 0.8,0.7,0.65]



    threshold = 0.4
    picked_boxes, picked_score = nms(bounding, confidence_score, threshold)
    print('阈值threshold为:', threshold)
    print('最终bbox列表：', picked_boxes)
    print('最终confidence分数列表：', picked_score)
