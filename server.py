#!/usr/bin/python3

import tornado.ioloop
import tornado.web

import csv

def select_all(file):
  rijen = []

  with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for rij in csvreader: rijen.append(rij)

  return rijen


class MainHandler(tornado.web.RequestHandler):
  def get(self, i_dont_care):
    with open('index.html', 'r') as template:
      essences = select_all('Essences.csv')
      tips = select_all('tips.csv')
      todos = select_all('todos.csv')

      t = tornado.template.Template(template.read())

      self.write(t.generate(essences=essences, tips=tips, todos=todos))

def make_app():
  return tornado.web.Application([
    (r"/(|index.php)", MainHandler),
      (r"/(.*)", tornado.web.StaticFileHandler, {'path': "."}),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(5000)
  tornado.ioloop.IOLoop.current().start()