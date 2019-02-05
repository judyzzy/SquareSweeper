#!/usr/bin/env python

import yaml
import pyglet
"""
file containing all the geomtry displayed
"""
#https://www.programsinformationpeople.org/runestone/static/publicpy3/Pyglet/windowContents.html
"""
Vertex position
"""
class V:
	def __init__(self, x, y):
		self.x  = x
		self.y = y

	def add(self, vec):
		self.x += vec.x
		self.y += vec.y

	def sub(self, vec):
		self.x -= vec.x
		self.y -= vec.y

	def mult(self, scalar):
		self.x *= scalar
		self.y *= scalar

	def mag(self):
		return sqrt(self.x ** 2 + self.y ** 2)

	def copy(self):
		return Vec2(self.x, self.y)

	def coords(self):
		return (self.x, self.y)

	def __repr__(self):
		return str(self.coords())

"""
2D shapes
"""
class Shape(object):
	def __init__(self,type,v):
		if(len(v) == 0):
			raise ValueError("Empty Input")
		self.type = type
		self.v = v
	def __repr__(self):
		s = ""
		for vertex in self.v:
			s += str(vertex)
		return "type: " + self.type + " v: " + s

	def get_v(self):
		return self.v
	def get_type(self):
		return self.type
"""
circle
"""
class Circle(Shape):
	def __init__(self,c,r):
		if(r <= 0):
			raise ValueError("Invalid radius")
		Shape.__init__(self,"circle",[c])
		self.radius = r

	def get_radius(self):
		return self.radius

	def __repr__(self):
		s = Shape.__repr__(self)
		s += " rardius: "+ str(self.radius)
		return  s
"""
polygon
"""
class Polygon(Shape):
	def __init__(self,v):
		Shape.__init__(self,"polygon",v)

"""
Object properties:
1. how many pieces does it contain
2. can we move it? (is it heavy enough to move)
3. can we suck it in?/ Is it dust?
"""
class Object(object):
	def __init__(self, movable, dust, piece_num,pieces):
		self.movable = movable
		self.dust = dust
		self.num = piece_num
		self.pieces = pieces

	def get_pieces(self):
		return self.pieces

	def __repr__(self):
		s = "movable: "+str(self.movable) + " dust "+ str(self.dust)
		s += " piece num: "+str(self.num) + "\n"
		for shape in self.pieces:
			s += str(shape)+'\n'
		return s 


def main():
	c = Circle(V(1,1),1)
	print(c)
	p = Polygon([V(1,1),V(2,2),V(1,3)])
	print(p)
	print("first object")
	o = Object(True,True,1,[c])
	print(o)
	print("second object:")
	oo = Object(True,True,2,[c,p])
	print(oo)

	with open("./config/test.yaml", 'r') as stream:
	    info = yaml.load(stream)
	    print(info)
	pyglet.app.run()


if __name__ == '__main__':
	game_window = pyglet.window.Window()
	game_window.clear()
	main()