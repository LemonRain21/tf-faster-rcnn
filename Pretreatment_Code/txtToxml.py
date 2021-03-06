# -*- coding: utf-8 -*-
"""
Created on Tue Apr  11 09:23:44 2018

@author: QinLong


"""
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import glob #返回所有匹配的文件路径列表
import os
from PIL import Image
from tqdm import tqdm #Tqdm 是一个快速，可扩展的Python进度条
def txtToXml(txt_path):
    for txt_file in tqdm(glob.glob(txt_path + '/*.txt')):
        txt_name_ = txt_file.split('\\')[-1][:-4]
        data = {"shapes": []}
        n = 1
        #im = Image.open(image_path + '\\' + txt_name_ +'.jpg')
        width = 1280
        height = 720
        tree = open(txt_file, 'r', encoding='UTF-8')
        node_root = Element('annotation')
        node_folder = SubElement(node_root, 'folder')
        node_folder.text = 'traffic'
        node_filename = SubElement(node_root, 'filename')
        node_filename.text = txt_name_+ '.jpg'
        
        source = SubElement(node_root, 'source')
        database = SubElement(source, 'database')
        database.text = 'QL traffic database'
        annotation = SubElement(source, 'annotation')
        annotation.text = 'QL traffic'
        image = SubElement(source, 'image')
        image.text = 'traffic'
        flickrid = SubElement(source, 'flickrid')
        flickrid.text = str(n) 
        
        node_size = SubElement(node_root, 'size')
        node_width = SubElement(node_size, 'width')
        node_width.text = str(width)
        node_height = SubElement(node_size, 'height')
        node_height.text = str(height)
        node_depth = SubElement(node_size, 'depth')
        node_depth.text = '3'
        
        segmented = SubElement(node_root, 'segmented')
        segmented.text = '0'
        
        root = tree.readlines()
        for i, line in enumerate(root):
            column = line.split(' ')        
            labal = {'0':'trafficsigns','1':'car'}#按标签
            labal = labal[column[0]]
            for i in range(1,len(column)):
                column[i] = float(column[i])
            node_object = SubElement(node_root, 'object')
            node_name = SubElement(node_object, 'name')
            node_name.text = labal 
            
            node_pose = SubElement(node_object, 'pose')
            node_pose.text = 'Unspecified'
            node_truncated = SubElement(node_object, 'truncated')
            node_truncated.text = '0'
            
            
            node_difficult = SubElement(node_object, 'difficult')
            node_difficult.text = '0'
            node_bndbox = SubElement(node_object, 'bndbox')
            node_xmin = SubElement(node_bndbox, 'xmin')
            node_xmin.text = str(round(width*(column[1] - column[3]/2)))
            node_ymin = SubElement(node_bndbox, 'ymin')
            node_ymin.text = str(round(height*(column[2] - column[4]/2)))
            node_xmax = SubElement(node_bndbox, 'xmax')
            node_xmax.text = str(round(width*(column[1] + column[3]/2)))
            node_ymax = SubElement(node_bndbox, 'ymax')
            node_ymax.text = str(round(height*(column[2] + column[4]/2)))
#            node_xmin = SubElement(node_bndbox, 'x2')
#            node_xmin.text = column[4]
#            node_ymin = SubElement(node_bndbox, 'y2')
#            node_ymin.text = column[5]
#            node_xmax = SubElement(node_bndbox, 'x3')
#            node_xmax.text = column[6]
#            node_ymax = SubElement(node_bndbox, 'y3')
#            node_ymax.text = column[7]
            n = n + 1
        xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
        dom = parseString(xml)
        with open(txt_name_ + '.xml', 'w') as f:
            dom.writexml(f, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
 
 
if __name__ == "__main__":
    data_path = 'F:\\VOC2018\\twotxt'
    #pic_path = 'C:\\Users\\QinLong\\Desktop\\image'
    txtToXml(data_path )
