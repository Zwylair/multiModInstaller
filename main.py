import menu_class
import discord_mods
import spotify_mods

mods_menus = {
    discord_mods: discord_mods.menu,
    spotify_mods: spotify_mods.menu,
}

main_menu = menu_class.Menu('Main', mods_menus)
main_menu.run()
