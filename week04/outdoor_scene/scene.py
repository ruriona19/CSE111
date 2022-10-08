"""
File: scene.py
Author: Roberto Uriona
Purpose: Prove that I can write functions with parameters and call those functions multiple times with arguments.
"""
# Standard library imports
import random

# local library imports
import draw2d


def main():
    # Width and height of the scene in pixels
    scene_width = 1000
    scene_height = 600

    # Call the start_drawing function in the draw2d.py library which will open a window and create a canvas.
    canvas = draw2d.start_drawing("Scene", scene_width, scene_height)
    
    # Draw the sky and all the objects in the sky.
    draw_sky(canvas, scene_width, scene_height)
    draw_sun(canvas, "yellow")
    draw_clouds(canvas, "white")
    draw_birds(canvas, "blue")
                
    # Draw the mountains
    draw_mountains(canvas, "slateGray")        

    # Draw the ground and all the objects on the ground.
    draw_ground(canvas, scene_width, scene_height)
    draw_lake(canvas, "deepSkyBlue")
    draw_forest(canvas)    

    # Call the finish_drawing function in the draw2d.py library.
    draw2d.finish_drawing(canvas)
    
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky
    Parameters
        canvas: The new canvas where this program can draw 2-dimensional shapes.
        scene_width: the width in pixels of the canvas
        scene_height: the height in pixels of the canvas
    Return: Nothing.
    """   
    draw2d.draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")

def draw_sun(canvas, color):
    """Draw the sun in a random location over the sky
    Parameters
        canvas: The new canvas where this program can draw 2-dimensional shapes.
        color: The color of the sun.
    Return: Nothing.
    """   
    x = random.randrange(50, 900)
    y = random.randrange(400, 500)  
    draw2d.draw_oval(canvas, x, y, x + 100, y + 100, fill=color)

def draw_clouds(canvas, color):
    """Draw clouds in a random location over the sky
    Parameters
        canvas: The new canvas where this program can draw 2-dimensional shapes.
        color: The color of the clouds        
    Return: Nothing.
    """       
    draw_cloud(canvas, 100, color)
    draw_cloud(canvas, 20, color)
    draw_cloud(canvas, 100, color)

def draw_birds(canvas, color):
    """Draw birds in a random location over the sky
    Parameters
        canvas: The new canvas where this program can draw 2-dimensional shapes.
        color: The color of the birds
    Return: Nothing.
    """       
    draw_bird(canvas, 0, color)
    draw_bird(canvas, 40, color)
    draw_bird(canvas, -30, color)
    draw_bird(canvas, 0, color)
    draw_bird(canvas,-50, color)
    draw_bird(canvas, -40, color)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground."""
    draw2d.draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="green")

def draw_mountains(canvas, color):
    """Draw the mountains.
    Parameters
        canvas: The new canvas where this program can draw 2-dimensional shapes.
        color: The color of the mountains
    Return: Nothing.
    """       
    draw_mountain(canvas, 0, 0, color)
    draw_mountain(canvas, 200, 30, color)
    draw_mountain(canvas, 550, 35, color)
    draw_mountain(canvas, 750, 15, color)
    draw_mountain(canvas, 350, 50, color)

def draw_lake(canvas, color):
    """Draw the lake.
    Parameters
        canvas: The new canvas where this program can draw 2-dimensional shapes.        
        color: The color of the lake.
    Return: Nothing.
    """
    draw2d.draw_oval(canvas, 450, 50, 850, 180, outline=color, fill=color)
    draw2d.draw_oval(canvas, 650, 30, 1050, 150, outline=color, fill=color)
    draw2d.draw_oval(canvas, 650, 95, 950, 195, outline=color, fill=color)
       
def draw_forest(canvas):
    """Draw the forest.
    Parameters
        canvas: The new canvas where this program can draw 2-dimensional shapes.        
    Return: Nothing.
    """
    # Draw 20 small trees in a random location just below the mountains 
    # and with a high between 40 and 50 pixels
    for x in range(0, 400, 20):
        y = random.randrange(150, 180)
        z = random.randrange(40, 50)
        draw_pine_tree(canvas, x, y, z)
    
    # Draw 20 mediuim trees in a random location around the middle of the ground
    # and with a high between 60 and 70 pixels
    for x in range(0, 400, 20):
        y = random.randrange(80, 150)
        z = random.randrange(60, 70)
        draw_pine_tree(canvas, x, y, z)

    # Draw 20 big trees in a random location to the bottm of the scene
    # and with a high between 80 and 100 pixels
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
    draw2d.draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw2d.draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")
    
def draw_cloud(canvas, startY, color):
    """Draw a cloud in a random location in the sky.
    Parameters
        canvas: The canvas where this function will draw a cloud.
        startY: The y location in pixels where this function will start drawing the cloud.
        color: THe color of the cloud.
    Return: nothing
    """
    # The start x location where this function will start drawing the cloud.
    startX = random.randrange(100, 800) 
    draw2d.draw_oval(canvas, startX + 100, startY + 480, startX + 240, startY + 400, outline=color, fill=color)
    draw2d.draw_oval(canvas, startX + 130, startY + 430, startX + 280, startY + 400, outline=color, fill=color)
    draw2d.draw_oval(canvas, startX + 40, startY + 490, startX + 150, startY + 430, outline=color, fill=color)

def draw_bird(canvas, startY, color):
    """Draw a bird in a random location in the sky.
    Parameters
        canvas: The canvas where this function will draw a bird.
        startY: The y location in pixels where this function will start drawing a bird.
        color: The color of the bird
    Return: nothing
    """
    startX = random.randrange(0, 800)
    draw2d.draw_arc(canvas, 50 + startX, 450 + startY, 100 + startX, 550 + startY, start=50, extent=70, width=3, outline=color)  
    draw2d.draw_arc(canvas, 75 + startX, 450 + startY, 125 + startX, 550 + startY, start=50, extent=70, width=3, outline=color)

def draw_mountain(canvas, startX, startY, color):
    """Draw a bird in a random location in the sky.
    Parameters
        canvas: The canvas where this function will draw a mountain.
        startX: The x location in pixels where this function will start drawing a mountain.
        startY: The y location in pixels where this function will start drawing a mountain.
        color: The color of the mountain        
    Return: nothing
    """
    draw2d.draw_polygon(canvas, startX + 0, 200, startX + 100, startY + 300, startX + 200, startY + 300, startX + 300, 200, fill=color)
    draw2d.draw_polygon(canvas, startX + 100, startY + 300, startX + 140, startY + 340, startX + 148, startY + 345, startX + 152, startY + 345, startX + 160, startY + 340, startX + 200, startY + 300, fill="white")


# Call the main function so that this program will start executing.
main()