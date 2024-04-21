import os
import subprocess

base_dir_name='/home/satyukt/Sarthak/oil_well_saturn/'
l1_dir_list=['Intermediate','Models','Runtime','SampleData','Utils']
l2_dir_list=['Input','Output']
for item in l1_dir_list:
  os.makedirs(os.path.join(base_dir_name,item), exist_ok=True)
  if item=='SampleData':
    for item_l2 in l2_dir_list:
      os.mkdir(os.path.join(base_dir_name,item,item_l2))
  if item=='Runtime':
    if not os.path.exists(os.path.join(base_dir_name,item,'.gitkeep')):
      with open(os.path.join(base_dir_name,item,'.gitkeep'), 'w'): pass