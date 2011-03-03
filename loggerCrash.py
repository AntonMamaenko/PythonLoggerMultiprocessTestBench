import logging
import logging.config
import multiprocessing
import threading
import time

# create logger
#logging.config.fileConfig("logging.conf")

def loop():
	logger = logging.getLogger("simpleExample")	
	while True:
		logger.info("hi")    

def parallelrun(x):
	p = multiprocessing.Pool()
	for i in xrange(x):		
		p.apply_async(loop)
	p.close()
	p.join()

def threadedrun(x):
	threadlist = []
	for i in xrange(x):
		t = threading.Thread(target=loop)
		threadlist.append(t)
		t.start()

	for i in threadlist:
		i.join()

def main():
	#parallelrun(1)
	threadedrun(5)

if __name__ == '__main__':
    main()