# *****************************************************************************
# Shih-Chun Liu
# sl3497
# 3/10/2013
# file: ppm_changer.py
#
# This program allows a user to manipulate an image saved as a ppm file and
# and saves the manipulated copy as a new ppm file.
#******************************************************************************

def negate_red(x, maxvalue):
    '''Negates red. x = list of pixels. maxvalue = maximum color value.'''
    for i in range(len(x)):
        if i % 3 == 0:
            x[i] = str(maxvalue - int(x[i]))
    return x


def negate_green(x, maxvalue):
    '''Negates green. x = list of pixels. maxvalue = maximum color value.'''
    for i in range(len(x)):
        if i % 3 == 1:
            x[i] = str(maxvalue - int(x[i]))
    return x


def negate_blue(x, maxvalue):
    '''Negates blue. x = list of pixels. maxvalue = maximum color value.'''
    for i in range(len(x)):
        if i % 3 == 2:
            x[i] = str(maxvalue - int(x[i]))
    return x


def flatten_red(x):
    '''Flattens red. x = list of pixels.'''
    for i in range(len(x)):
        if i % 3 == 0:
            x[i] = '0'
    return x


def flatten_green(x):
    '''Flattens green. x = list of pixels.'''
    for i in range(len(x)):
        if i % 3 == 1:
            x[i] = '0'
    return x


def flatten_blue(x):
    '''Flattens blue. x = list of pixels.'''
    for i in range(len(x)):
        if i % 3 == 2:
            x[i] = '0'
    return x


def greyscale(x):
    '''Converts to greyscale. x = list of pixels.'''
    for i in range(len(x)/3):
        x[3*i] = x[3*i+1] = x[3*i+2] = str(int(round((int(x[3*i]) + \
                                      int(x[3*i+1]) + int(x[3*i+2])) / 3.)))
    return x


def flip_horizontal(x, columns, rows):
    '''Horizontally flips the image. x = list of pixels. \
columns = number of columns in image. rows = number of rows in image.'''
    y = []
    for i in range(rows):
        temp = x[(i*3*columns):((i+1)*3*columns)]
        newrow = []
        # Reverse each pixel and add into 'newrow' list.
        for j in range(columns):
            revpixel = [temp[3*j+2], temp[3*j+1], temp[3*j]]
            newrow += revpixel
        # Reverse 'newrow', effectively implementing horizontal flip in a row.
        newrow.reverse()
        y += newrow
    return y


def horizontal_blur(x):
    '''Blurs each trio of adjacent pixels. x = list of pixels.'''
    for i in range(len(x)/9):
        x[9*i] = x[9*i+3] = x[9*i+6] = str(int(round((int(x[9*i]) + \
                                        int(x[9*i+3]) + int(x[9*i+6])) / 3.)))
        x[9*i+1] = x[9*i+4] = x[9*i+7] = str(int(round((int(x[9*i+1]) + \
                                        int(x[9*i+4]) + int(x[9*i+7])) / 3.)))
        x[9*i+2] = x[9*i+5] = x[9*i+8] = str(int(round((int(x[9*i+2]) + \
                                        int(x[9*i+5]) + int(x[9*i+8])) / 3.)))
    return x


def extreme_contrast(x, maxvalue):
    '''Maximizes the color contrast. x = list of pixels. \
maxvalue = maximum color value.'''
    maxx = str(maxvalue)
    for i in range(len(x)):
        temp = int(x[i])
        if temp > (maxvalue / 2.):
            x[i] = maxx
        else:
            x[i] = '0'
    return x


def storefile(infilename, maxlength):
    '''Saves file information into variables and file content into lists.\
infilename = name of input file. maxlength = maximum number of columns.'''
    infile = open(infilename, 'r')

    # Save each header line into the 'head' list.
    head = []
    for i in range(3):
        header = infile.readline()
        head.append(header)
        # Save photo dimensions.
        if i == 1:
            info = header.split()
            length = int(info[0])
            width = int(info[1])
            # Check whether rowlength is too long.
            if length > maxlength or width > maxlength:
                import sys
                infile.close()
                sys.exit('File is too large: too many columns.') 
        # Save maximum color value.
        if i == 2:
            maxvalue = int(header)
            
    # Save the pixel values into the 'pixel' list.
    pixels = []
    for line in infile:
        line = line.split()
        for n in line:
            pixels.append(n)
            
    infile.close()
    return length, width, maxvalue, head, pixels


def createfile(head, pixels, outfilename):
    '''Creates and writes the outfile. head = header list. pixels = pixel \
list. outfilename = name of output file.'''
    copy = open(outfilename, 'w')

    # Write header lines.
    for m in head:
        copy.write(m)

    # Write pixel lines.    
    outpixels = ''
    for n in pixels:
        outpixels += n + ' '
    copy.write(outpixels.rstrip() + '\n')

    copy.close()
    print '\n', outfilename, 'created.'


def userinput():
    '''Displays title and manages the user's input for file to maniuplate.'''
    print 'Portable Pixmap (PPM) Image Editor \n'
    infilename =  raw_input('Enter name of image file: ')
    outfilename = raw_input('Enter name of output file: ')
    print ' '
    return infilename, outfilename


def menu():
    '''Displays the options for image manipulation'''
    print 'Here are your choices:'
    print '[1] Convert to greyscale\t [2] Flip horizontally'
    print '[3] Negative of red\t [4] Negative of green\t [5] Negative of blue'
    print '[6] Just the reds\t [7] Just the greens\t [8] Just the blues'
    print '[9] Extreme contrast\t [10] Horizontal blur \n'


def userchoice(opnumber):
    '''Manages the user's decision for an operation. opnumber = number \
representing the operation.'''
    question = 'Do you want ' + str(opnumber) + '? (y/n) '
    choice = raw_input(question)
    if choice == 'y':
        return True
    else:
        return False
