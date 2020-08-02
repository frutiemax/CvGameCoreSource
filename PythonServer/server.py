import socketserver
import socket
import xml.etree.ElementTree as xml
import Message
import AI

class Server:
    def __init__(self):
        self._socket = socket.socket()
        
    def SetAI(self, ai):
        self._ai = ai
        self.HandleAIFunctionTable = {
            Message.REQ_PLAYER_AI_INIT                          : self._ai.OnPlayerAIInit,
            Message.REQ_PLAYER_AI_RESET                         : self._ai.OnPlayerAIReset,
            Message.REQ_PLAYER_AI_DOTURNPRE                     : self._ai.OnPlayerAIDoTurnPre,
            Message.REQ_PLAYER_AI_DOTURNPOST                    : self._ai.OnPlayerAIDoTurnPost,
            Message.REQ_PLAYER_AI_DOTURN_UNITSPRE               : self._ai.OnPlayerAIDoTurnUnitsPre,
            Message.REQ_PLAYER_AI_DOTURN_UNITSPOST              : self._ai.OnPlayerAIDoTurnUnitsPost,
            Message.REQ_PLAYER_AI_FOUNDVALUES                   : self._ai.OnPlayerAIFoundValues,
            Message.REQ_PLAYER_AI_UNITUPDATE                    : self._ai.OnPlayerAIUnitUpdate,
            Message.REQ_PLAYER_AI_CONQUERCITY                   : self._ai.OnPlayerAIConquerCity,
            Message.REQ_PLAYER_AI_FOUNDVALUE                    : self._ai.OnPlayerAIFoundValue,
            Message.REQ_PLAYER_AI_CHOOSE_FREE_GREATPERSON       : self._ai.OnPlayerAIChooseFreeGreatePerson,
            Message.REQ_PLAYER_AI_CHOOSE_RESEARCH               : self._ai.OnPlayerAIChooseResearch,
            Message.REQ_PLAYER_AI_PLOTTARGETMISSIONS            : self._ai.OnPlayerAIPlotTargetMissionAIs,
            Message.REQ_PLAYER_AI_LAUNCH                        : self._ai.OnPlayerAILaunch,

            Message.REQ_CITY_AI_INIT                            : self._ai.OnCityAIInit,
            Message.REQ_CITY_AI_RESET                           : self._ai.OnCityAIReset,
            Message.REQ_CITY_AI_DOTURN                          : self._ai.OnCityAIDoTurn,
            Message.REQ_CITY_AI_CHOOSEPRODUCTION                : self._ai.OnCityAIChooseProduction,
            Message.REQ_CITY_AI_ISCHOOSEPRODUCTION_DIRTY        : self._ai.OnCityAIIsChooseProductionDirty,
            Message.REQ_CITY_AI_SETCHOOSEPRODUCTION_DIRTY       : self._ai.OnCityAISetChooseProductionDirty,
        }
    
    def Run(self, host, port):
        self._socket.bind((host,port))
        self._socket.listen(1)

        while True:
            self.conn, self.addr = self._socket.accept()

            with self.conn:
                while True:
                    #get the request command from CIV5
                    data = self.conn.recv(1024)
                    if not data: break

                    reqCommand = Message.deserialize(data.decode("utf-8"))

                    #execute the AI commands
                    self.HandleAIFunctionTable[reqCommand.MessageType]()

                    #send an acknowledge that the AI commands have been completed
                    ackType = Message.ToAcknowledge[reqCommand.MessageType]
                    self.AcknowledgeAIRequest(ackType)

    def HandleDummy(self):
        print('This is a dummy message \n')

    def AcknowledgeAIRequest(self, messageType):
        #send the acknowledge message
        m = Message.AcknowledgeMessage(messageType)
        self.conn.sendall(bytes(Message.serialize(m)))

if __name__ == "__main__":
    HOST, PORT = "localhost", 11750
    server = Server()
    ai = AI.AI()
    server.SetAI(ai)
    server.Run(HOST,PORT)

            

