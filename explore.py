from classes.ExploreFog import ExploreFog
# from classes.Commands import GoHome, MoveToScoutCampAndClick, ClickDurbin

try:
    while True:
        ExploreFog.start()
except:
    pass

# go_home = GoHome()
# move_to_scout_camp_and_click = MoveToScoutCampAndClick()
# click_monocular = ClickDurbin()
# go_home.set_successor(move_to_scout_camp_and_click)
# move_to_scout_camp_and_click.set_successor(click_monocular)
# go_home.do_work()
