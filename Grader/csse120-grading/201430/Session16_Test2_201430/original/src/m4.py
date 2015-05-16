"""
Test 2, problem 4.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and PUT YOUR NAME HERE.  April 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import zellegraphics as zg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem4a()
    test_problem4b()


def test_problem4a():
    """ Tests the   problem4a   function. """
    # TODO:  READ and use the following tests that we have supplied
    #        for you.  The tests produce the same pictures shown in
    #            problem4a_picture.pdf.
    window1 = zg.GraphWin('Problem 4a, tests 1 and 2', 600, 300)
    
    # Test 1:
    center = zg.Point(50, 50)
    circle = zg.Circle(center, 20)
    
    corner1 = zg.Point(150, 120)
    corner2 = zg.Point(210, 200)
    rectangle = zg.Rectangle(corner1, corner2)
    
    problem4a(window1, circle, rectangle, 'blue', 'red')
    
    # Test 2:
    center = zg.Point(350, 200)
    circle = zg.Circle(center, 60)
    
    corner1 = zg.Point(400, 80)
    corner2 = zg.Point(500, 140)
    rectangle = zg.Rectangle(corner1, corner2)
    
    problem4a(window1, circle, rectangle, 'yellow', 'green')
    
    window1.closeOnMouseClick()
    
    # Test 3:
    window2 = zg.GraphWin('problem 4a, test 3', 300, 200)
    
    center = zg.Point(250, 80)
    circle = zg.Circle(center, 25)
    
    corner1 = zg.Point(50, 30)
    corner2 = zg.Point(150, 130)
    rectangle = zg.Rectangle(corner1, corner2)
    
    problem4a(window2, circle, rectangle, 'cyan', 'black')
    
    window2.closeOnMouseClick()


def problem4a(window, circle, rectangle, circle_color, rectangle_color):
    """
    See   problem4a_picture.pdf   in this project for pictures that may
    help you better understand the following specification:
    
    Draws a circle, a rectangle and 4 lines as follows:
      -- All the shapes should have their width (i.e., line thickness)
           set to 3 (instead of the default 1).
      -- The circle should be the given circle,
           but with its FILL color set to the given  circle_color.
      -- The rectangle should be the given rectangle,
           but with its OUTLINE color set to the given   rectangle_color.
      -- The 4 lines each have one end at the center of the given circle
           and the other end at a corner of the rectangle.
           (The rectangle has 4 corners; one line to each.)
           The lines should be drawn AFTER drawing the circle and rectangle
           so that the lines are on TOP of the circle and rectangle.
     
    See   problem4a_picture.pdf   for examples.
    
    Preconditions: The first argument is a zg.GraphWin,
                   the second and third arguments are a zg.Circle
                   and zg.Rectangle, respectively, and the fourth and fifth
                   arguments are colors appropriate for zellegraphics.
    """
    # TODO: Implement and test this function.
    # NOTE: Partial credit is available if you can draw
    #       only parts of what is asked for.


def test_problem4b():
    """ Tests the   problem4b   function. """
    # TODO:  READ and use the following tests that we have supplied
    #        for you.  The tests produce the same pictures shown in
    #            problem4b_picture.pdf.
    window1 = zg.GraphWin('Problem 4b, test 1', 300, 650)
    
    # Test 1:
    point1 = zg.Point(250, 80)
    rectangle1 = zg.Rectangle(zg.Point(50, 30), zg.Point(100, 60))
    colors1 = ['blue', 'red', 'green', 'white', 'cyan', 'yellow', 'brown', 'pink']
    
    problem4b(window1, 7, point1, rectangle1, colors1)
    
    window1.closeOnMouseClick()
    
    window2 = zg.GraphWin('Problem 4b, tests 2 and 3', 500, 650)
    
    # Test 2:
    point2 = zg.Point(40, 40)
    rectangle2 = zg.Rectangle(zg.Point(100, 20), zg.Point(140, 30))
    colors2 = ['blue', 'red', 'green']
    
    problem4b(window2, 8, point2, rectangle2, colors2)
    
    # Test 3:
    point3 = zg.Point(200, 80)
    rectangle3 = zg.Rectangle(zg.Point(400, 100), zg.Point(480, 150))
    
    problem4b(window2, 6, point3, rectangle3, colors2)
    
    window2.closeOnMouseClick()

    
def problem4b(window, n, point, rectangle, colors):
    """
    See   problem4b_picture.pdf   in this project for pictures that may
    help you better understand the following specification:
    
    Draws  n  "things" as follows:
      -- Each "thing" consists of a circle, a rectangle, and 4 lines,
           as in problem3a.
      -- The first "thing" has:
           -- Its rectangle is the given rectangle.
           -- Its circle is centered at the given point.
           -- The radius of the circle is half of the width of the rectangle.
           -- Its 4 lines go from the center of the circle to the 4 corners
                of the rectangle, as in problem3a.
           -- The fill color of the circle is the first (beginning) color
                in the given list of colors.
           -- The outline color of the rectangle is the second color
                in the given list of colors.
      -- Each succeeding "thing" has the same size and relationships
           as the first thing, but is shifted 70 pixels down
           from the previous "thing".
      -- Also, the circles have fill colors per the given list of colors,
           one after the other, starting at the first (beginning) color,
           wrapping as necessary.
      -- Also, the rectangles have outline colors per the given
           list of colors, one after the other, wrapping as necessary,
           but starting at the second color.

    See   problem4b_picture.pdf   for examples.

    Preconditions: The first argument is a zg.GraphWin,
                   the second argument is a non-negative integer,
                   the third argument is a zg.Point,
                   the fourth argument is zg.Rectangle,
                   and the fifth argument is a list of colors
                   appropriate for zellegraphics.
    """
    # TODO: Implement and test this function.  Partial credit
    #       is available if you get only part of this to work.
    # IMPLEMENTATION REQUIREMENTS:
    #   Use (call)   problem4a   appropriately in solving problem4b.
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
