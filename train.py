from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import os

bot = ChatBot('Bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              trainer='chatterbot.trainers.ChatterBotCorpusTrainer')


# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train('chatterbot.corpus.english')
