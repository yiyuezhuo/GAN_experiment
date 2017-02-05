from shutil import copyfile
import os

def sample(root, target, form, target_form = None, start = 1, end = None, step = 10):
    '''
    root: file location
    form: format string i.e convert{}.jpg
    '''
    
    if target_form is None:
        target_form = '{}'
    
    if not os.path.exists(target):
        os.mkdir(target)
    
    idx = start
    while(end is None or idx <= end):
        
        name = form.format(idx)
        path = os.path.join(root, name)
        
        #print(path)
        if not os.path.exists(path):
            break
        
        target_name = target_form.format(name)
        target_path = os.path.join(target, target_name)
        copyfile(path, target_path)
        
        idx += step
    