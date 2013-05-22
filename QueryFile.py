__auther__ = 'shuson'
__version__ = 1.0

import os, glob

i = 0
def QueryFile(fileName):
  roots = []
	dirs = []
	subdirs=[]
	files = []

	for f in glob.glob('*.%s' %fileName):
		files.append('%s%s' %(os.getcwd(),f))

	for r in os.listdir(os.getcwd()):
		if os.path.isdir(r):
				roots.append(r)

	roots.remove('$RECYCLE.BIN')
	roots.remove('System Volume Information')

	for root in roots:
		for root,dir,file in os.walk(root):	
			dirs.append(root)

	for d in dirs:
		p = r'%s%s' %(os.getcwd()[:3],d)
		os.chdir(p)
		for f in glob.glob('*.%s' %fileName):
			files.append('%s%s\%s' %(os.getcwd()[:3],d,f))

	os.chdir(os.getcwd()[:3])
	song = open('files.txt','w')
	global i
	for f in files:
		song.write(f)
		song.write('\n')
		i +=1
	song.write("total files %d" %i)

QueryFile(raw_input('Type in the file extension to query: '))
raw_input("%d files are recorded to files.txt.\nAny KeyDown to Exit!!" %i)
