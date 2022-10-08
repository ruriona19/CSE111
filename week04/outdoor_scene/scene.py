import random
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing, draw_circle_with_vert_grad


def main():
    # Width and height of the scene in pixels
    scene_width = 1000
    scene_height = 600

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)

    # draw mountains
    #draw_polygon(canvas,0 , 200, 100, 300, 200, 300, 300, 200, fill="slateGray")
    #draw_polygon(canvas,100, 300, 140, 340, 148, 345, 152, 345, 160, 340, 200, 300, fill="white")
    draw_mountain(canvas, 0, 0)
    draw_mountain(canvas, 200, 30)
    draw_mountain(canvas, 550, 35)
    draw_mountain(canvas, 750, 15)
    draw_mountain(canvas, 350, 50)

    draw_ground(canvas, scene_width, scene_height)
    # drawing lake
    draw_oval(canvas, 450, 50, 850, 180, outline="deepSkyBlue", fill="deepSkyBlue")
    draw_oval(canvas, 650, 30, 1050, 150, outline="deepSkyBlue", fill="deepSkyBlue")
    draw_oval(canvas, 650, 95, 950, 195, outline="deepSkyBlue", fill="deepSkyBlue")

    draw_forest(canvas)
    # drawing sun
    draw_oval(canvas, 450, 450, 550, 550, fill="yellow")
    # drawing clouds
    draw_cloud(canvas, 25, 100)
    draw_cloud(canvas, 270, 20)
    draw_cloud(canvas, 425, 100)  
    # drawing birdds
    draw_bird(canvas, 0, 0)
    draw_bird(canvas, -50, 40)
    draw_bird(canvas, -50, -30)
    draw_bird(canvas, -100, 0)
    draw_bird(canvas, -80, -50)
    draw_bird(canvas, -150, -40)



    #draw_circle_with_vert_grad(canvas, 850, 500, 30, [226, 156, 175], [105, 182, 174])
    
    #draw_polygon(canvas,0 , 200, 100, 300, 200, 300, 300, 200, fill="slateGray")
    #draw_polygon(canvas,100, 300, 140, 340, 148, 345, 152, 345, 160, 340, 200, 300, fill="white")
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")
       
def draw_forest(canvas):
    for x in range(0, 400, 20):
        y = random.randrange(150, 180)
        z = random.randrange(40, 50)
        draw_pine_tree(canvas, x, y, z)
    
    for x in range(0, 400, 20):
        y = random.randrange(80, 150)
        z = random.randrange(60, 70)
        draw_pine_tree(canvas, x, y, z)

    for x in range(0, 500, 40):
        y = random.randrange(0, 80)
        z = random.randrange(80, 100)
        draw_pine_tree(canvas, x, y, z)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")
    
def draw_cloud(canvas, startX, startY):
    draw_oval(canvas, startX + 100, startY + 480, startX + 240, startY + 400, outline="white", fill="white")
    draw_oval(canvas, startX + 130, startY + 430, startX + 280, startY + 400, outline="white", fill="white")
    draw_oval(canvas, startX + 40, startY + 490, startX + 150, startY + 430, outline="white", fill="white")
# Define your functions such as
# draw_sky and draw_ground here.

def draw_bird(canvas, startX, startY):
    draw_arc(canvas, 850 + startX, 450 + startY, 900 + startX, 550 + startY, start=50, extent=70, width=3)  
    draw_arc(canvas, 875 + startX, 450 + startY, 925 + startX, 550 + startY, start=50, extent=70, width=3)

def draw_mountain(canvas, x, y):
    draw_polygon(canvas, 0 + x, 200, 100 + x, 300 + y, 200 + x, 300 + y, 300 + x, 200, fill="slateGray")
    draw_polygon(canvas, 100 + x, 300 + y, 140 + x, 340 + y, 148 + x, 345 + y, 152 + x, 345 + y, 160 + x, 340 + y, 200 + x, 300 + y, fill="white")


# Call the main function so that
# this program will start executing.
main()