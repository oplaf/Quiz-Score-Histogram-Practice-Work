import arcade
import random

def main():
    arcade.open_window(800,800, "Bar Graph")
    arcade.set_background_color(arcade.color.WHITE)

    #asking for input from user
    file_picker = input("What file should I graph?")
    #open and read .txt file
    infile1 = open(file_picker)
    #infile1 = open("input1.txt", 'r')
    readfile1 = infile1.readlines()


    arcade.start_render()

    colors_list = [arcade.color.BLACK, arcade.color.GREEN, arcade.color.RED, arcade.color.BLUE, arcade.color.YELLOW,
                   arcade.color.ORANGE, arcade.color.PURPLE, arcade.color.TURQUOISE, arcade.color.BROWN,
                   arcade.color.GRAY]


    bar_sep = 0
    for item in readfile1:
        split_item = item.split(':')
        xpos = int(split_item[1])
        name = split_item[0]
        #height = int(split_item[2])
        current_color = random.choice(colors_list)
        #center_y = int(ypos+height)/2
        #arcade.draw_rectangle_filled(xpos, center_y, 50, height, current_color)
        from_bottom = 200
        rectangle_height = xpos*10
        rectangle_width = 50
        print(name)
        bar_sep = bar_sep+100
        #foo = arcade.create_rectangle_filled(counter, upstart + (xpos*10), 50, upstart, current_color)
        foo = arcade.create_rectangle_filled(bar_sep, from_bottom+rectangle_height/2, rectangle_width, rectangle_height, current_color)
        foo.draw()
        arcade.draw_text(name, bar_sep-(rectangle_width/2), from_bottom-30, arcade.color.DARK_GRAY, 15)


    xaxis = arcade.create_line(50, from_bottom, 750,from_bottom, arcade.color.BLACK)
    yaxis = arcade.create_line(50, from_bottom, 50, 700, arcade.color.BLACK)


    xaxis.draw()
    yaxis.draw()
    arcade.finish_render()
    arcade.run()



main()

