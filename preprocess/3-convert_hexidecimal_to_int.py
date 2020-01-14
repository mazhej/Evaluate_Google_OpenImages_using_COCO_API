import json

#real coco json
# with open('/home/maziar/WA/eval_res/distiller/data/annotations/instances_val2017.json') as f:
#   data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print(data)

#converted OI to coco
with open("/home/maziar/WA/OI/convert_openIm_coco/annotations/val-annotations-bbox.json") as f:
  conv = json.load(f)




for i in range(len(conv['annotations'])):
  if 'segmentation' not in conv['annotations']:
    conv['annotations'][i]['segmentation'] = []

for i in range(len(conv['annotations'])):
  conv['annotations'][i]['image_id'] = int(conv['annotations'][i]['image_id'][:15],16)

for i in range(len(conv['images'])):
  conv['images'][i]['id'] = int(conv['images'][i]['id'][:15],16)

with open('data_test_convert.json', 'w') as fp:
    json.dump(conv, fp)



print(conv)