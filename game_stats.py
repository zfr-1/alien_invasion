class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于非活跃状态
        self.game_active = False
        # 在任何情况下都不应重置最高分,从文件high_score.txt文件读出最高分
        try:
            with open("high_score.txt") as file_object:
                high_score = file_object.readline()
                if high_score:
                    high_score = int(high_score)
                else:
                    high_score = 0
        except FileNotFoundError:
            self.high_score = 0
        else:
            self.high_score = high_score



    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1