import menu_class
from discord_mods import openasar, betterdiscord

menu = menu_class.Menu('Discord mods', {betterdiscord: betterdiscord.install, openasar: openasar.install})
