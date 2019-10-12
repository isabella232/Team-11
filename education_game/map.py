# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter,
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
    # word_list = ['Budget', 'Income']
    scenes = {
    'starting_out': S.StartingOut(),
    'budget': S.Budget(),
    'income': S.Income()}
    # for word in word_list:
    #     words_scene = "".join(word.capitalize().split(" "))
    #     scene_name = ['S', words_scene]
    #     scene = ".".join(scene_name)
        # scenes[word] = scene
    # initializes to a starting scene
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # gets the specified scene from the scenes dictionary list.
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    # gets the first scene of the map from the dictionary list
    def opening_scene(self):
        return self.next_scene(self.start_scene)
