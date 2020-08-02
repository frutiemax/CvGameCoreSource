
import enum
import xml.etree.ElementTree as xml


REQ_PLAYER_AI_INIT                      = 0
REQ_PLAYER_AI_RESET                     = 1
REQ_PLAYER_AI_DOTURNPRE                 = 2
REQ_PLAYER_AI_DOTURNPOST                = 3
REQ_PLAYER_AI_DOTURN_UNITSPRE           = 4
REQ_PLAYER_AI_DOTURN_UNITSPOST          = 5
REQ_PLAYER_AI_FOUNDVALUES               = 6
REQ_PLAYER_AI_UNITUPDATE                = 7
REQ_PLAYER_AI_CONQUERCITY               = 8
REQ_PLAYER_AI_FOUNDVALUE                = 9
REQ_PLAYER_AI_CHOOSE_FREE_GREATPERSON   = 10
REQ_PLAYER_AI_CHOOSE_RESEARCH           = 11
REQ_PLAYER_AI_PLOTTARGETMISSIONS        = 12

SEND_PLAYER_AI_INIT                     = 13
SEND_PLAYER_AI_RESET                    = 14
SEND_PLAYER_AI_DOTURNPRE                = 15
SEND_PLAYER_AI_DOTURNPOST               = 16
SEND_PLAYER_AI_DOTURN_UNITSPRE          = 17
SEND_PLAYER_AI_DOTURN_UNITSPOST         = 18
SEND_PLAYER_AI_FOUNDVALUES              = 19
SEND_PLAYER_AI_UNITUPDATE               = 20
SEND_PLAYER_AI_CONQUERCITY              = 21
SEND_PLAYER_AI_FOUNDVALUE               = 22
SEND_PLAYER_AI_CHOOSE_FREE_GREATPERSON  = 23
SEND_PLAYER_AI_CHOOSE_RESEARCH          = 24
SEND_PLAYER_AI_PLOTTARGETMISSIONS       = 25

REQ_CITY_AI_INIT                        = 26
REQ_CITY_AI_RESET                       = 27
REQ_CITY_AI_DOTURN                      = 28
REQ_CITY_AI_CHOOSEPRODUCTION            = 29
REQ_CITY_AI_ISCHOOSEPRODUCTION_DIRTY    = 30
REQ_CITY_AI_SETCHOOSEPRODUCTION_DIRTY   = 31

SEND_CITY_AI_INIT                       = 32
SEND_CITY_AI_RESET                      = 33
SEND_CITY_AI_DOTURN                     = 34
SEND_CITY_AI_CHOOSEPRODUCTION           = 35
SEND_CITY_AI_ISCHOOSEPRODUCTION_DIRTY   = 36
SEND_CITY_AI_SETCHOOSEPRODUCTION_DIRTY  = 37

DUMMY                                   = 38



class DummyMessage:
    def __init__(self):
        self.MessageType = DUMMY
        self.Message = "hello from server"

def serializeDummy(m):
    pythonSerialization = xml.Element('boost_serialization')
    pythonSerialization.set('signature','serialization::archive')
    pythonSerialization.set('version','18')

    messageType = xml.SubElement(pythonSerialization,'MessageType')
    messageType.text = str(m.MessageType)

    message = xml.SubElement(pythonSerialization,'Message')
    message.text = m.Message

    return xml.tostring(pythonSerialization)

def deserializeDummy(myString):
    ret = DummyMessage()
    root = xml.fromstring(myString)
    for child in root:
        if child.tag == 'Message':
            ret.Message = child.text
            return ret

serializeFunction = {DUMMY : serializeDummy}
def serialize(m):
    return serializeFunction[m.MessageType](m)

deserializeFunction = {DUMMY : deserializeDummy}
def deserialize(myString):
    root = xml.fromstring(myString)
    for child in root:
        if child.tag == 'MessageType':
            messageType = child.text
            return deserializeFunction[int(messageType)](myString)
            
