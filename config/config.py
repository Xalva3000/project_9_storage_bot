from environs import Env


class BotSettings:
    def __init__(self, token=None):
        if token is None:
            try:
                self.token = self.load_from_file()
            except Exception as error:
                print(error)
        else:
            self.token = token

    @staticmethod
    def load_from_file(path='.keys/.env'):
        env = Env()
        env.read_env(path)
        return BotSettings(env('BOT_TOKEN'))
