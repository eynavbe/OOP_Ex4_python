from Ex4.GraphAlgo import GraphAlgo
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
import time
import random


class GraphView:
    def __init__(self):
        self.run_move = True
        self.g_algo = GraphAlgo()
        self.client = Client()
        # self.r = False
        self.list_stop = []
        # For agents to see moving between move
        self.list_pos_agent = {}

        self.pos_to = ""
        self.stepx = 0
        self.stepy = 0
        self.x_pos = 0
        self.y_pos = 0
        self.draw()


    AZURE = (0, 204, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    time_start = time.time()
    # init pygame
    WIDTH, HEIGHT = 1080, 720
    time_end = time.time()
    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    num_pic = random.randint(1, 2)
    # dx, dy = (bx - ax, by - ay)
    # stepx, stepy = (dx / 25., dy / 25.)
    pos_agr = {}

    def reset_list_pos_agent(self, sum):
        for i in range(sum):
            # [stepx = 0, self.stepy = 0, self.x_pos = 0, self.y_pos = 0, pos_to]
            self.list_pos_agent[i] = [0, 0, 0, 0, []]

    def draw(self):
        pygame.init()
        self.screen = display.set_mode((self.WIDTH, self.HEIGHT), depth=32, flags=RESIZABLE)
        # font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('graph')
        self.screen.fill(self.white)
        button_stop = self.button_create("STOP", (self.screen.get_width() - 75, 0, 75, 40), self.black, self.AZURE,
                                         self.on_click_button_stop)
        background = pygame.image.load('../Ex4/pic/background.jpg').convert()
        pygame.display.flip()
        pygame.display.update()
        diamondPink = pygame.image.load('../Ex4/pic/diamondPink.png').convert_alpha()
        diamondWhite = pygame.image.load('../Ex4/pic/diamondWhite.png').convert_alpha()
        p1 = pygame.image.load('../Ex4/pic/p1.png').convert_alpha()
        p2 = pygame.image.load('../Ex4/pic/p2.png').convert_alpha()
        clock = pygame.time.Clock()
        pygame.font.init()
        self.client.start_connection(self.HOST, self.PORT)
        self.g_algo.load_from_json_graph(json.loads(self.client.get_graph()))
        self.g_algo.load_from_json_pokemons(json.loads(self.client.get_pokemons()))
        FONT = pygame.font.SysFont('Arial', 20, bold=True)
        self.min_x = float(self.g_algo.get_graph().get_node_x(
            min(list(self.g_algo.get_graph().get_all_v()), key=lambda n: self.g_algo.get_graph().get_node_x(n))))
        self.min_y = float(self.g_algo.get_graph().get_node_y(
            min(list(self.g_algo.get_graph().get_all_v()), key=lambda n: self.g_algo.get_graph().get_node_y(n))))
        self.max_x = float(self.g_algo.get_graph().get_node_x(
            max(list(self.g_algo.get_graph().get_all_v()), key=lambda n: self.g_algo.get_graph().get_node_x(n))))
        self.max_y = float(self.g_algo.get_graph().get_node_y(
            max(list(self.g_algo.get_graph().get_all_v()), key=lambda n: self.g_algo.get_graph().get_node_y(n))))
        radius = 15
        sort_poke = self.g_algo.get_graph().sort_pokemon_value()
        po = self.g_algo.get_graph().get_all_pokemons()
        for i in range(len(po)):
            f = po[sort_poke[i]]['src']
            self.client.add_agent("{\"id\":" + str(f) + "}")

        self.client.start()
        """
        The code below should be improved significantly:
        The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
        """
        self.run_move_count = 0
        # test = False
        # display.update()
        # display.update()
        # # refresh rate
        # clock.tick(30)
        self.count = 0
        try:
            while self.client.is_running() == 'true':
                try:

                    display.update()
                    # check events
                    self.screen.blit(pygame.transform.scale(background, (self.WIDTH, self.HEIGHT)), [0, 0])
                    for event_pygame in pygame.event.get():
                        if event_pygame.type == pygame.QUIT:
                            pygame.quit()
                            exit(0)
                        elif event_pygame.type == VIDEORESIZE:
                            self.screen = pygame.display.set_mode(
                                event_pygame.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                            self.screen.blit(pygame.transform.scale(background, event_pygame.dict['size']), [0, 0])
                        self.button_check(button_stop, event_pygame)
                    self.button_draw(self.screen, button_stop)
                    # Set up the text.
                    ttl = self.client.time_to_end()
                    self.g_algo.load_from_json_agents(json.loads(self.client.get_agents()))
                    self.g_algo.load_from_json_pokemons(json.loads(self.client.get_pokemons()))
                    text = FONT.render('time to end: ' + str(int(float(ttl) * 0.001)) + ' sec', True, self.white)
                    rect_info = text.get_rect()
                    rect_info.right = 160
                    self.screen.blit(text, rect_info)
                    info = json.loads(self.client.get_info())
                    text = FONT.render('moves: ' + str(int(info["GameServer"]["moves"])), True, self.white)
                    rect_info = text.get_rect()
                    rect_info.right = 280
                    self.screen.blit(text, rect_info)
                    text = FONT.render('level: ' + str(info["GameServer"]["game_level"]), True, self.white)
                    rect_info = text.get_rect()
                    rect_info.right = 400
                    self.screen.blit(text, rect_info)
                    agents = self.g_algo.get_graph().get_all_agents()
                    for agent in agents:
                        text = FONT.render('grade agent ' + str(agents[agent]['id'] + 1) + " :" + str(agents[agent]['value']),
                                           True, self.white)
                        rect_info = text.get_rect()
                        rect_info.right = 600 + ((agents[agent]['id']) * 200)
                        self.screen.blit(text, rect_info)

                    # draw edges
                    for s in self.g_algo.get_graph().get_all_v():
                        for e in self.g_algo.get_graph().all_out_edges_of_node(s):
                            src = next(n for n in self.g_algo.get_graph().get_all_v() if n == s)
                            dest = next(n for n in self.g_algo.get_graph().get_all_v() if n == e)
                            # scaled positions
                            src_x = self.my_scale(self.g_algo.get_graph().get_node_x(src), x=True)
                            src_y = self.my_scale(self.g_algo.get_graph().get_node_y(src), y=True)
                            dest_x = self.my_scale(self.g_algo.get_graph().get_node_x(dest), x=True)
                            dest_y = self.my_scale(self.g_algo.get_graph().get_node_y(dest), y=True)
                            # draw the line
                            pygame.draw.line(self.screen, self.white,
                                             (src_x, src_y), (dest_x, dest_y))
                    # draw nodes
                    for n in self.g_algo.get_graph().get_all_v():
                        x = self.my_scale(self.g_algo.get_graph().get_node_x(n), x=True)
                        y = self.my_scale(self.g_algo.get_graph().get_node_y(n), y=True)
                        gfxdraw.filled_circle(self.screen, int(x), int(y),
                                              radius, self.black)
                        gfxdraw.aacircle(self.screen, int(x), int(y),
                                         radius, Color(255, 255, 255))
                        # draw the node id
                        id_srf = FONT.render(str(n), True, Color(255, 255, 255))
                        rect_info = id_srf.get_rect(center=(x, y))
                        self.screen.blit(id_srf, rect_info)
                    # display.update()
                    # draw agents
                    self.g_algo.load_from_json_agents(json.loads(self.client.get_agents()))
                    agents = self.g_algo.get_graph().get_all_agents()
                    for agent in agents:
                        x, y = self.g_algo.get_graph().get_x_y(agents[agent]['pos'])
                        x = self.my_scale(float(x), x=True)
                        y = self.my_scale(float(y), y=True)

                        if self.num_pic == 1:
                            if agent not in self.list_pos_agent:
                                self.reset_list_pos_agent(len(agents))
                            if len(agents) == 1:
                                lis = self.list_pos_agent[agent]
                                x_pos = lis[2]
                                x_pos += lis[0]
                                y_pos = lis[3]
                                y_pos += lis[1]
                                lis = [lis[0],lis[1],x_pos,y_pos,lis[4]]
                                self.list_pos_agent[agent] = lis
                                if agent not in self.pos_agr:
                                    self.pos_agr[agent] = {"True":agents[agent]['pos']}
                                else:
                                    for i in self.pos_agr[agent]:
                                        if self.pos_agr[agent][i] != agents[agent]['pos']:
                                            self.pos_agr[agent] = {}
                                            self.pos_agr[agent] = {"True": agents[agent]['pos']}
                            else:
                                self.pos_agr[agent] = {"False": agents[agent]['pos']}
                                x_pos, y_pos = 0, 0
                            self.screen.blit(pygame.transform.scale(p1, (45, 65)), [int(x - 42 + x_pos), int(y - 60 + y_pos)])
                        else:
                            if agent not in self.list_pos_agent:
                                self.reset_list_pos_agent(len(agents))
                            if len(agents) == 1:
                                lis = self.list_pos_agent[agent]
                                x_pos = lis[2]
                                x_pos += lis[0]
                                y_pos = lis[3]
                                y_pos += lis[1]
                                lis = [lis[0], lis[1], x_pos, y_pos, lis[4]]
                                self.list_pos_agent[agent] = lis
                                if agent not in self.pos_agr:
                                    self.pos_agr[agent] = {"True": agents[agent]['pos']}
                                else:
                                    for i in self.pos_agr[agent]:
                                        if self.pos_agr[agent][i] != agents[agent]['pos']:
                                            self.pos_agr[agent] = {}
                                            self.pos_agr[agent] = {"True": agents[agent]['pos']}

                            else:
                                self.pos_agr[agent] = {"False": agents[agent]['pos']}
                                x_pos, y_pos = 0, 0
                            self.screen.blit(pygame.transform.scale(p2, (45, 65)), [int(x - 42 + x_pos), int(y - 60 + y_pos)])

                    pokemon1_all = self.g_algo.get_graph().get_all_pokemons()
                    for p in pokemon1_all:
                        x, y = self.g_algo.get_graph().get_x_y(pokemon1_all[p]['pos'])
                        x = self.my_scale(float(x), x=True)
                        y = self.my_scale(float(y), y=True)
                        if pokemon1_all[p]['type'] < 0:
                            self.screen.blit(pygame.transform.scale(diamondPink, (25, 25)), [int(x - 22), int(y - 22)])
                        else:
                            self.screen.blit(pygame.transform.scale(diamondWhite, (25, 25)), [int(x - 22), int(y - 22)])
                    # update screen changes
                    display.update()
                    # refresh rate
                    clock.tick(60)
                    if len(self.list_stop) > 1:
                        if self.list_stop[len(self.list_stop) - 1] + self.list_stop[0] <= time.time():
                            self.client.move()
                            self.list_stop[1] += self.list_stop[0]
                            self.list_stop.remove(self.list_stop[0])
                            for agent1 in agents:
                                for i in self.pos_agr[agent1]:
                                    if i == "True":
                                        list111 = self.list_pos_agent[agent1]
                                        list1 = [list111[0], list111[1], 0, 0, list111[4]]
                                        self.list_pos_agent[agent1] = list1
                                        h = self.pos_agr[agent1]["True"]
                                        self.pos_agr[agent1] = {}
                                        self.pos_agr[agent1] = {"False": h}
                    else:
                        self.reset_list_pos_agent(len(agents))
                        self.list_stop = []
                        self.move_agent()
                except:
                    exit(0)
            exit(0)
        except:
            exit(0)


    def button_create(self, text, rect, inactive_color, active_color, action):
        font = pygame.font.Font(None, 16)
        button_rect = pygame.Rect(rect)
        text = font.render(text, True, self.white)
        text_rect = text.get_rect(center=button_rect.center)
        return [text, text_rect, button_rect, inactive_color, active_color, action, False]

    # Draws the menu button
    def button_draw(self, screen, info):
        text, text_rect, rect_b, inactive_color, active_color, action, hover = info
        if hover:
            color_b = active_color
        else:
            color_b = inactive_color
        pygame.draw.rect(screen, color_b, rect_b)
        screen.blit(text, text_rect)

    def on_click_button_stop(self):
        self.client.stop()
        self.client.stop_connection()
        exit(0)

    def button_check(self, info, event_b):
        text, text_rect, rect_b, inactive_color, active_color, action, hover = info
        if event_b.type == pygame.MOUSEMOTION:
            info[-1] = rect_b.collidepoint(event_b.pos)
        elif event_b.type == pygame.MOUSEBUTTONDOWN:
            if hover and action:
                action()

    def move_agent(self):
        list_stops_more_agents = []
        agents = self.g_algo.get_graph().get_all_agents()
        self.reset_list_pos_agent(len(agents))
        for agent in agents:
            if agents[agent]['dest'] == -1:
                src = (agents[agent]['src'])
                if src == -1:
                    src = (agents[agent]['src'])
                lis, self.list_stop, list_pos_to = self.g_algo.pokemon_selection_for_agent(agents[agent]['id'], src,
                                                                               (agents[agent]['speed']))
                self.count = 0
                list_stops_more_agents.append(self.list_stop)
                for i in lis:
                    self.client.choose_next_edge(
                        '{"agent_id":' + str(agents[agent]['id']) + ', "next_node_id":' + str(i) + '}')
                x, y = self.g_algo.get_graph().get_x_y(agents[agent]['pos'])
                x = self.my_scale(float(x), x=True)
                y = self.my_scale(float(y), y=True)
                if len(list_pos_to) > 0:
                    x_pos_to, y_pos_to = self.g_algo.get_graph().get_x_y(list_pos_to[0])
                    x_pos_to = self.my_scale(float(x_pos_to), x=True)
                    y_pos_to = self.my_scale(float(y_pos_to), y=True)
                    dx, dy = (x_pos_to - x, y_pos_to - y)
                    stepx, stepy = (dx / ((self.list_stop[0] * 100) - (self.list_stop[0] * 40)), dy / ((self.list_stop[0] * 100) - (self.list_stop[0] * 40)))
                    self.list_pos_agent[agent] = [stepx,stepy,0,0,list_pos_to]
        if len(list_stops_more_agents) > 1:
            self.list_stop = []
            for one in list_stops_more_agents:
                for i in range(len(one) - 1):
                    if one[i + 1] != 0:
                        one[i + 1] = one[i + 1] + one[i]
            repeat = True
            while repeat:
                min_index = 0
                min_val = 111111111
                for i_in in range(len(list_stops_more_agents)):
                    list_stop_one_0 = list_stops_more_agents[i_in]
                    if list_stop_one_0[0] < min_val and len(list_stop_one_0) > 1 and list_stop_one_0[1] != 0:
                        min_val = list_stop_one_0[0]
                        min_index = i_in
                if min_val < 111111111:
                    self.list_stop.append(min_val)
                    list_stops_more_agents[min_index].remove(min_val)
                else:
                    max_val = 0
                    for i_in in range(len(list_stops_more_agents)):
                        list_stop_one_0 = list_stops_more_agents[i_in]
                        if list_stop_one_0[0] > max_val:
                            max_val = list_stop_one_0[0]
                    self.list_stop.append(max_val)
                    repeat = False

            for i_stop in range(len(self.list_stop) - 1):
                self.list_stop[len(self.list_stop) - 1 - i_stop] = self.list_stop[len(self.list_stop) - 1 - i_stop] - \
                                                                   self.list_stop[len(self.list_stop) - 2 - i_stop]
        if len(self.list_stop) > 1 and self.list_stop[len(self.list_stop) - 1] == 0:
            self.list_stop.remove(0)
        if len(self.list_stop) > 0:
            self.list_stop.append(time.time())
        self.client.move()






    def scale(self, data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimensions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    # decorate scale with the correct values
    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.min_y, self.max_y)
