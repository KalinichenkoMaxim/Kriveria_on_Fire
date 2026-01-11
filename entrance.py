import arcade
from arcade import SpriteList
from arcade.examples.drawing_primitives import scale, texture
from arcade.gui import UIManager, UILabel
from arcade.gui.widgets.layout import UIAnchorLayout, UIBoxLayout
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class Enterance(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)
        self.m = random.randint(1, 19)
        self.background = arcade.load_texture(f"background_images/{self.m}.jpg")
        self.sound = arcade.load_sound(f"soundtrack/{random.randint(1, 9)}.mp3")
        self.logo = arcade.load_texture("background_images/Kriveria on Fire.png")
        self.choice_texture = arcade.load_texture('background_images/choice.png')
        self.texture_dnk = arcade.load_texture("background_images/DNK.png")
        self.texture_gak = arcade.load_texture("background_images/GAK.png")
        self.dnk_ico = arcade.Sprite(self.texture_dnk, scale=1.0)
        self.gak_ico = arcade.Sprite(self.texture_gak, scale=1.0)
        self.manager = UIManager()
        self.manager.enable()

        self.anchor_layout = UIAnchorLayout()
        self.box_layout = UIBoxLayout(vertical=True, space_between=10)
        self.show_choice_flag = False

        self.choosing_buttons = SpriteList()
        self.choosing_buttons.append(self.dnk_ico)
        self.choosing_buttons.append(self.gak_ico)

        self.setup_widgets()

        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)

    def setup_widgets(self):
        arcade.play_sound(self.sound, volume=0.05)
        self.label = UILabel(
            x=1000,
            y=100,
            text="Press any key...",
            font_size=50,
            text_color=arcade.color.WHITE,
            width=300
        )
        self.manager.add(self.label)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.rect.XYWH(960, 540, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_texture_rect(self.logo, arcade.rect.XYWH(500, 1000, 700, 50))
        if self.show_choice_flag:
            arcade.draw_texture_rect(self.texture_dnk,
                                     arcade.rect.XYWH(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2, 300, 300))
            arcade.draw_texture_rect(self.texture_gak,
                                     arcade.rect.XYWH(SCREEN_WIDTH // 2 + 250, SCREEN_HEIGHT // 2, 300, 300))
            arcade.draw_text(
                "Выберете сторону для игры",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT - 200,
                arcade.color.BLACK,
                font_size=50,
                anchor_x="center",
                anchor_y="top"
            )

        self.manager.draw()

    def on_key_press(self, key, modifiers):
        if key:
            if self.label:
                self.manager.remove(self.label)
                self.label = None
                self.show_choice_flag = self.choosing_text = UILabel(
                    x=SCREEN_WIDTH // 2,
                    y=SCREEN_HEIGHT - 200,
                    text="Выберете сторону для игры",
                    font_size=50,
                    text_color=arcade.color.WHITE,
                    width=300
                )
            return

        if key == arcade.key.F4 and (modifiers & arcade.key.MOD_ALT):
            arcade.close_window()
            return


def setup_game(width=800, height=600, title="Kriveria on Fire"):
    game = Enterance(width, height, title)
    return game


def main():
    game = setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, "Kriveria on Fire")
    arcade.run()


if __name__ == "__main__":
    main()