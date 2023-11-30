class text:
    def __init__(self, position, text, font):
        self.position = position
        self.text = text
        self.font = font

    def textrender(self, surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, self.position)