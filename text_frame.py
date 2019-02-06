import pygame
import pygame.font


class TextFrame:

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 450, 300
        self.frame_color = (255, 204, 203)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.high_scores = [str("{:,}".format(round(x, -1))) for x in stats.high_score]
        self.msg = ['High scores:'] + self.high_scores
        self.prepared_msg = []
        self.y = self.rect.top + 25
        self.add_to_y = 0
        self.prep_msg(self.msg)

    def prep_msg(self, msg):
        for line in msg:
            self.prepared_msg.append(self.font.render(line, True, self.text_color))

    def draw_frame(self):
        self.screen.fill(self.frame_color, self.rect)
        for line in range(len(self.prepared_msg)):
            self.line_rect = self.prepared_msg[line].get_rect()
            self.line_rect.centerx = self.rect.centerx
            self.line_rect.centery = self.y + self.add_to_y
            self.screen.blit(self.prepared_msg[line], self.line_rect)
            self.add_to_y += 50

