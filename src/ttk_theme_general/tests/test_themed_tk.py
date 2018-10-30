"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2017-2018 RedFantom
"""
from ttkthemes._tkinter import tk, ttk
from ttkthemes.themed_tk import ThemedTk
import unittest


class TestThemedTk(unittest.TestCase):
    def setUp(self):
        self.tk = ThemedTk()
        self.themes = ["blue", "plastik", "keramik", "aquativo",
                       "clearlooks", "elegance", "kroc", "radiance",
                       "winxpblue", "keramik_alt", "black", "arc"]

    def tearDown(self):
        self.tk.destroy()

    def test_themes_available(self):
        available_themes = self.tk.get_themes()
        for theme in self.themes:
            self.assertTrue(theme in available_themes)

    def test_theme_setting(self):
        button = ttk.Button(self.tk)
        label = ttk.Label(self.tk)
        button.pack()
        label.pack()
        self.tk.update()
        for theme in self.tk.get_themes():
            self.tk.set_theme(theme)
            self.tk.update()

    def test_custom_theme(self):
        if not self.tk.png_support:
            return
        for theme in self.tk.pixmap_themes:
            tk = ThemedTk()
            tk.set_theme_advanced(theme, brightness=0.2, saturation=1.4, hue=1.8)
            tk.destroy()
        return

    def test_toplevel_hook(self):
        __init__toplevel = tk.Toplevel.__init__
        self.tk.set_theme("black", True, False)
        self.assertNotEqual(__init__toplevel, tk.Toplevel.__init__)
        top = tk.Toplevel(self.tk)
        color = ttk.Style(self.tk).lookup("TFrame", "background")
        self.assertIsNotNone(color)
        self.assertEqual(top.cget("background"), color)
        top.destroy()

    def test_tk_background(self):
        self.tk.config(background="white")
        self.tk.set_theme("black", False, True)
        self.assertNotEqual(self.tk.cget("background"), "white")
