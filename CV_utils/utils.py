import cv2

# data type 
def print_matInfo(name, Image): 

    # U : unsigned
    # S : Signed
    # F : Float
    if Image.dtype == 'uint8':
        mat_type = 'CV_8U' 
    elif Image.dtype == 'int8':
        mat_type = 'CV_8S'
    elif Image.dtype == 'uint16':
        mat_type = 'CV_16U'
    elif Image.dtype == 'int16':
        mat_type = 'CV_16S'
    elif Image.dtype == 'float32':
        mat_type = 'CV_32F'
    elif Image.dtype == 'float64':
        mat_type = 'CV_64F'

    if Image.ndim == 3:
        nchannel = 3
    else:
        nchannel = 1

    print("%12s : depth(%s), channels(%s) --> mat_type(%sC%d)" % (name, Image.dtype, nchannel, mat_type, nchannel))