import ppm_changer as p

def main():
    '''Performs the desired manipulations to an image file.'''
    picname, copyname = p.userinput()
    columns, rows, scale, header, outfile = p.storefile(picname, 1000)
    
    p.menu()    
    if p.userchoice([1]):
        outfile = p.greyscale(outfile)
    if p.userchoice([2]):
        outfile = p.flip_horizontal(outfile, columns, rows)
    if p.userchoice([3]):
        outfile = p.negate_red(outfile, scale)
    if p.userchoice([4]):
        outfile = p.negate_green(outfile, scale)
    if p.userchoice([5]):
        outfile = p.negate_blue(outfile, scale)
    # To accomplish 'just [color]', flatten the other two colors.
    if p.userchoice([6]):
        outfile = p.flatten_green(outfile)
        outfile = p.flatten_blue(outfile)
    if p.userchoice([7]):
        outfile = p.flatten_red(outfile)
        outfile = p.flatten_blue(outfile)
    if p.userchoice([8]):
        outfile = p.flatten_red(outfile)
        outfile = p.flatten_green(outfile)
    if p.userchoice([9]):
        outfile = p.extreme_contrast(outfile, scale)
    if p.userchoice([10]):
        outfile = p.horizontal_blur(outfile)
    
    p.createfile(header, outfile, copyname)


main()
