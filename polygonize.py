import os, fnmatch
from subprocess import call
call(["ls", "-l"])

inFolder= 'C:/Users/unimi/Documents/Umberto/Universita/PhD/Guglielmin/Permafrost/Alta_Valtellina/Landsat_ita/LE71930282000259EDC00/DNs2Reflectance_LE71930282000259EDC00/'
outFolder= 'C:/Users/unimi/Documents/Umberto/Universita/PhD/Guglielmin/Permafrost/Alta_Valtellina/Landsat_ita/Cloud_mask_AltaValtellina/clip_2_foscagno/'

os.chdir (inFolder)

def findRasters (path, filter):
    for root, dirs, files in os.walk(path, filter):
        for file in fnmatch.filter(files, filter):
            yield os.path.join (root, file)

for raster in findRasters (inFolder, '*.tif'):
    (infilepath, infilename)= os.path.split (raster)
    print infilename
    outRaster= outFolder+ 'clip_'+ infilename
    print outRaster
    warp= 'gdalwarp -dstnodata 0 -q -cutline %s -crop_to_cutline -of GTiff %s %s' % ('study_area_foscagno.shp', raster, outRaster)
    call (warp)