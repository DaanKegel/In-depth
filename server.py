#!/usr/bin/python3

import tornado.ioloop
import tornado.web

import csv

class MainHandler(tornado.web.RequestHandler):
    def get(self, i_dont_care):
    	with open('index.html', 'r') as template:
	    	with open('Essences.csv', 'r') as csvfile:
	    		csvreader = csv.reader(csvfile)

	    		rijen = []
	    		for rij in csvreader: rijen.append(rij)

	    		t = tornado.template.Template(template.read())

	    		self.write(t.generate(csv=rijen))

def make_app():
    return tornado.web.Application([
    	(r"/(|index.php)", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': "."}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()