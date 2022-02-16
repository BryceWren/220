from graphics import *

def convert():
   win = GraphWin("Converter", 700, 500)
   win.setCoords((0, 0, 10, 10))
   celsius_text = Text(Point(3, 8), "Celsius")
   celsius_entry = Entry(Point(7, 8), 30)
   click_text = Text(Point(5, 5), "Click to Convert")
   result_text = Text(Point(3, 1), " ")

   celsius_text.draw(win)
   celsius_entry.draw(win)
   click_text.draw(win)
   result_text.draw(win)
   win.getMouse()
   celsius = eval(celsius_entry.getText())
   farenheit = celsius * 9 / 5 + 32
   result_text.setText(farenheit)
   click_text.setText("Click to Close!")

   win.getMouse()


