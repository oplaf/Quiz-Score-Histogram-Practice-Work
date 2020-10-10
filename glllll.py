import arcade
import random

def main():
    arcade.open_window(700, 700, "String Split Demo")
    data = ["100,200,200",
            "200,200,600",
            "300,200,300",
            "400,200,250"]

    our_colors = [arcade.color.HEART_GOLD,
                  arcade.color.APPLE_GREEN,
                  arcade.color.RED_DEVIL,
                  arcade.color.ALICE_BLUE,
                  arcade.color.SALMON,
                  arcade.color.DARK_VANILLA]

    arcade.start_render()
    for item in data:
        split_item = item.split(',')
        x_pos = int(split_item[0])
        y_pos = int(split_item[1])
        height = int(split_item[2])
        current_color = random.choice(our_colors)
        center_y = (y_pos+height)/2
        arcade.draw_rectangle_filled(x_pos,center_y,50, height, current_color)

    arcade.draw_text("String Split Demo", 200, 600, arcade.color.ELECTRIC_CRIMSON,20)
    arcade.finish_render()


    arcade.run()

main()