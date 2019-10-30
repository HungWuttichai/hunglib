import json
import xmltodict


def readClasses(filepath):
    with open(filepath, 'r') as file:
        line = file.readline()
        cnt = 0
        classes = []
        class_idx = []
        while line:
            class_now = line.strip()
            cnt += 1
            classes.append(class_now.lower())
            class_idx.append(cnt)
            line = file.readline()
        return classes


def readXML(filepath):
    with open(filepath, 'r') as file:
        data_xml = file.read()
        input_dict = xmltodict.parse(data_xml)
        data_json = json.loads(json.dumps(input_dict))

        img_size = data_json['annotation']['size']
        img_object = data_json['annotation']['object']
        img_width, img_height, img_depth = (
            img_size['width'], img_size['height'], img_size['depth'])
        return img_object, int(img_width), int(img_height), int(img_depth)


def xml2yolo(path_xml, path_classes):

    classes = readClasses(path_classes)
    img_object, img_width, img_height, img_depth = readXML(path_xml)
    yolo_file = open(path_xml+".txt", "w")

    for obj in img_object:
        obj_class = obj['name']
        obj_pos = obj['bndbox']
        xmin = float(obj_pos['xmin'])
        ymin = float(obj_pos['ymin'])
        xmax = float(obj_pos['xmax'])
        ymax = float(obj_pos['ymax'])
        obj_idx = classes.index(obj_class)
        x = (xmax + xmin) / img_width/2
        y = (ymax + ymin) / img_height/2
        w = (xmax - xmin) / img_width
        h = (ymax - ymin) / img_height
        L = str(obj_idx) + " " + str(format(x, '.6f')) + " " + str(format(y, '.6f')
                                                                   ) + " " + str(format(w, '.6f')) + " " + str(format(h, '.6f')) + "\n"
        yolo_file.writelines(L)
    yolo_file.close()
