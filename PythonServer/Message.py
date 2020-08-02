
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
REQ_PLAYER_AI_LAUNCH                    = 13

SEND_PLAYER_AI_INIT                     = 14
SEND_PLAYER_AI_RESET                    = 15
SEND_PLAYER_AI_DOTURNPRE                = 16
SEND_PLAYER_AI_DOTURNPOST               = 17
SEND_PLAYER_AI_DOTURN_UNITSPRE          = 18
SEND_PLAYER_AI_DOTURN_UNITSPOST         = 19
SEND_PLAYER_AI_FOUNDVALUES              = 20
SEND_PLAYER_AI_UNITUPDATE               = 21
SEND_PLAYER_AI_CONQUERCITY              = 22
SEND_PLAYER_AI_FOUNDVALUE               = 23
SEND_PLAYER_AI_CHOOSE_FREE_GREATPERSON  = 24
SEND_PLAYER_AI_CHOOSE_RESEARCH          = 25
SEND_PLAYER_AI_PLOTTARGETMISSIONS       = 26
SEND_PLAYER_AI_LAUNCH                   = 27

REQ_CITY_AI_INIT                        = 28
REQ_CITY_AI_RESET                       = 29
REQ_CITY_AI_DOTURN                      = 30
REQ_CITY_AI_CHOOSEPRODUCTION            = 31
REQ_CITY_AI_ISCHOOSEPRODUCTION_DIRTY    = 32
REQ_CITY_AI_SETCHOOSEPRODUCTION_DIRTY   = 33

SEND_CITY_AI_INIT                       = 34
SEND_CITY_AI_RESET                      = 35
SEND_CITY_AI_DOTURN                     = 36
SEND_CITY_AI_CHOOSEPRODUCTION           = 37
SEND_CITY_AI_ISCHOOSEPRODUCTION_DIRTY   = 38
SEND_CITY_AI_SETCHOOSEPRODUCTION_DIRTY  = 39

DUMMY                                   = 40
BASE_MESSAGE                            = 41

ToAcknowledge = {
    REQ_PLAYER_AI_INIT                          : SEND_PLAYER_AI_INIT,
    REQ_PLAYER_AI_RESET                         : SEND_PLAYER_AI_RESET,
    REQ_PLAYER_AI_DOTURNPRE                     : SEND_PLAYER_AI_DOTURNPRE,
    REQ_PLAYER_AI_DOTURNPOST                    : SEND_PLAYER_AI_DOTURNPOST,
    REQ_PLAYER_AI_DOTURN_UNITSPRE               : SEND_PLAYER_AI_DOTURN_UNITSPRE,
    REQ_PLAYER_AI_DOTURN_UNITSPOST              : SEND_PLAYER_AI_DOTURN_UNITSPOST,
    REQ_PLAYER_AI_FOUNDVALUES                   : SEND_PLAYER_AI_FOUNDVALUES,
    REQ_PLAYER_AI_UNITUPDATE                    : SEND_PLAYER_AI_UNITUPDATE,
    REQ_PLAYER_AI_CONQUERCITY                   : SEND_PLAYER_AI_CONQUERCITY,
    REQ_PLAYER_AI_FOUNDVALUE                    : SEND_PLAYER_AI_FOUNDVALUE,
    REQ_PLAYER_AI_CHOOSE_FREE_GREATPERSON       : SEND_PLAYER_AI_CHOOSE_FREE_GREATPERSON,
    REQ_PLAYER_AI_CHOOSE_RESEARCH               : SEND_PLAYER_AI_CHOOSE_RESEARCH,
    REQ_PLAYER_AI_PLOTTARGETMISSIONS            : SEND_PLAYER_AI_PLOTTARGETMISSIONS,
    REQ_PLAYER_AI_LAUNCH                        : SEND_PLAYER_AI_LAUNCH,

    REQ_CITY_AI_INIT                            : SEND_CITY_AI_INIT,
    REQ_CITY_AI_RESET                           : SEND_CITY_AI_RESET,
    REQ_CITY_AI_DOTURN                          : SEND_CITY_AI_DOTURN,
    REQ_CITY_AI_CHOOSEPRODUCTION                : SEND_CITY_AI_CHOOSEPRODUCTION,
    REQ_CITY_AI_ISCHOOSEPRODUCTION_DIRTY        : SEND_CITY_AI_ISCHOOSEPRODUCTION_DIRTY,
    REQ_CITY_AI_SETCHOOSEPRODUCTION_DIRTY       : SEND_CITY_AI_SETCHOOSEPRODUCTION_DIRTY,
}

class Message:
    def __init__(self):
        self.MessageType = BASE_MESSAGE

class DummyMessage(Message):
    def __init__(self):
        self.MessageType = DUMMY
        self.Message = "hello from server"

class RequestMessage(Message):
    def __init__(self, messageType):
        self.MessageType = messageType

class AcknowledgeMessage(Message):
    def __init__(self, messageType):
        self.MessageType = messageType


def serializeDummy(m):
    messageElement = xml.Element('Message')
    messageElement.set('MessageType', str(m.MessageType))
    messageStringElement = xml.SubElement(messageElement, 'Message')
    messageStringElement.text = m.Message
    return xml.tostring(messageElement)

def serializeRequest(m):
    messageElement = xml.Element('Message')
    messageElement.set('MessageType', str(m.MessageType))
    return xml.tostring(messageElement)

def serializeAcknowledge(m):
    messageElement = xml.Element('Message')
    messageElement.set('MessageType', str(m.MessageType))
    return xml.tostring(messageElement)

def deserializeDummy(myString):
    root = xml.fromstring(myString)
    message = root[0].text
    m = DummyMessage()
    m.Message = message
    return m

def deserializeRequest(myString):
    root = xml.fromstring(myString)
    messageType = root.attrib['MessageType']
    messageType = int(messageType)
    message = RequestMessage(messageType)
    return message

def deserializeAcknowledge(myString):
    root = xml.fromstring(myString)
    messageType = root.attrib['MessageType']
    messageType = int(messageType)
    message = RequestMessage(messageType)
    return message

serializeFunction = {
    DUMMY : serializeDummy,
    REQ_PLAYER_AI_INIT                      : serializeRequest,
    REQ_PLAYER_AI_RESET                     : serializeRequest,
    REQ_PLAYER_AI_DOTURNPRE                 : serializeRequest,
    REQ_PLAYER_AI_DOTURNPOST                : serializeRequest,
    REQ_PLAYER_AI_DOTURN_UNITSPRE           : serializeRequest,
    REQ_PLAYER_AI_DOTURN_UNITSPOST          : serializeRequest,
    REQ_PLAYER_AI_FOUNDVALUES               : serializeRequest,
    REQ_PLAYER_AI_UNITUPDATE                : serializeRequest,
    REQ_PLAYER_AI_CONQUERCITY               : serializeRequest,
    REQ_PLAYER_AI_FOUNDVALUE                : serializeRequest,
    REQ_PLAYER_AI_CHOOSE_FREE_GREATPERSON   : serializeRequest,
    REQ_PLAYER_AI_CHOOSE_RESEARCH           : serializeRequest,
    REQ_PLAYER_AI_PLOTTARGETMISSIONS        : serializeRequest,
    REQ_PLAYER_AI_LAUNCH                    : serializeRequest,

    SEND_PLAYER_AI_INIT                      : serializeAcknowledge,
    SEND_PLAYER_AI_RESET                     : serializeAcknowledge,
    SEND_PLAYER_AI_DOTURNPRE                 : serializeAcknowledge,
    SEND_PLAYER_AI_DOTURNPOST                : serializeAcknowledge,
    SEND_PLAYER_AI_DOTURN_UNITSPRE           : serializeAcknowledge,
    SEND_PLAYER_AI_DOTURN_UNITSPOST          : serializeAcknowledge,
    SEND_PLAYER_AI_FOUNDVALUES               : serializeAcknowledge,
    SEND_PLAYER_AI_UNITUPDATE                : serializeAcknowledge,
    SEND_PLAYER_AI_CONQUERCITY               : serializeAcknowledge,
    SEND_PLAYER_AI_FOUNDVALUE                : serializeAcknowledge,
    SEND_PLAYER_AI_CHOOSE_FREE_GREATPERSON   : serializeAcknowledge,
    SEND_PLAYER_AI_CHOOSE_RESEARCH           : serializeAcknowledge,
    SEND_PLAYER_AI_PLOTTARGETMISSIONS        : serializeAcknowledge,
    SEND_PLAYER_AI_LAUNCH                    : serializeAcknowledge,

    REQ_CITY_AI_INIT                        : serializeRequest,
    REQ_CITY_AI_RESET                       : serializeRequest,
    REQ_CITY_AI_DOTURN                      : serializeRequest,
    REQ_CITY_AI_CHOOSEPRODUCTION            : serializeRequest,
    REQ_CITY_AI_ISCHOOSEPRODUCTION_DIRTY    : serializeRequest,
    REQ_CITY_AI_SETCHOOSEPRODUCTION_DIRTY   : serializeRequest,

    SEND_CITY_AI_INIT                        : serializeAcknowledge,
    SEND_CITY_AI_RESET                       : serializeAcknowledge,
    SEND_CITY_AI_DOTURN                      : serializeAcknowledge,
    SEND_CITY_AI_CHOOSEPRODUCTION            : serializeAcknowledge,
    SEND_CITY_AI_ISCHOOSEPRODUCTION_DIRTY    : serializeAcknowledge,
    SEND_CITY_AI_SETCHOOSEPRODUCTION_DIRTY   : serializeAcknowledge,
}

def serialize(m):
    return serializeFunction[m.MessageType](m)

deserializeFunction = {
    DUMMY                                   : deserializeDummy,
    REQ_PLAYER_AI_INIT                      : deserializeRequest,
    REQ_PLAYER_AI_RESET                     : deserializeRequest,
    REQ_PLAYER_AI_DOTURNPRE                 : deserializeRequest,
    REQ_PLAYER_AI_DOTURNPOST                : deserializeRequest,
    REQ_PLAYER_AI_DOTURN_UNITSPRE           : deserializeRequest,
    REQ_PLAYER_AI_DOTURN_UNITSPOST          : deserializeRequest,
    REQ_PLAYER_AI_FOUNDVALUES               : deserializeRequest,
    REQ_PLAYER_AI_UNITUPDATE                : deserializeRequest,
    REQ_PLAYER_AI_CONQUERCITY               : deserializeRequest,
    REQ_PLAYER_AI_FOUNDVALUE                : deserializeRequest,
    REQ_PLAYER_AI_CHOOSE_FREE_GREATPERSON   : deserializeRequest,
    REQ_PLAYER_AI_CHOOSE_RESEARCH           : deserializeRequest,
    REQ_PLAYER_AI_PLOTTARGETMISSIONS        : deserializeRequest,
    REQ_PLAYER_AI_LAUNCH                    : deserializeRequest,

    SEND_PLAYER_AI_INIT                     : deserializeAcknowledge,
    SEND_PLAYER_AI_RESET                    : deserializeAcknowledge,
    SEND_PLAYER_AI_DOTURNPRE                : deserializeAcknowledge,
    SEND_PLAYER_AI_DOTURNPOST               : deserializeAcknowledge,
    SEND_PLAYER_AI_DOTURN_UNITSPRE          : deserializeAcknowledge,
    SEND_PLAYER_AI_DOTURN_UNITSPOST         : deserializeAcknowledge,
    SEND_PLAYER_AI_FOUNDVALUES              : deserializeAcknowledge,
    SEND_PLAYER_AI_UNITUPDATE               : deserializeAcknowledge,
    SEND_PLAYER_AI_CONQUERCITY              : deserializeAcknowledge,
    SEND_PLAYER_AI_FOUNDVALUE               : deserializeAcknowledge,
    SEND_PLAYER_AI_CHOOSE_FREE_GREATPERSON  : deserializeAcknowledge,
    SEND_PLAYER_AI_CHOOSE_RESEARCH          : deserializeAcknowledge,
    SEND_PLAYER_AI_PLOTTARGETMISSIONS       : deserializeAcknowledge,
    SEND_PLAYER_AI_LAUNCH                   : deserializeAcknowledge,

    REQ_CITY_AI_INIT                        : deserializeRequest,
    REQ_CITY_AI_RESET                       : deserializeRequest,
    REQ_CITY_AI_DOTURN                      : deserializeRequest,
    REQ_CITY_AI_CHOOSEPRODUCTION            : deserializeRequest,
    REQ_CITY_AI_ISCHOOSEPRODUCTION_DIRTY    : deserializeRequest,
    REQ_CITY_AI_SETCHOOSEPRODUCTION_DIRTY   : deserializeRequest,

    SEND_CITY_AI_INIT                       : deserializeAcknowledge,
    SEND_CITY_AI_RESET                      : deserializeAcknowledge,
    SEND_CITY_AI_DOTURN                     : deserializeAcknowledge,
    SEND_CITY_AI_CHOOSEPRODUCTION           : deserializeAcknowledge,
    SEND_CITY_AI_ISCHOOSEPRODUCTION_DIRTY   : deserializeAcknowledge,
    SEND_CITY_AI_SETCHOOSEPRODUCTION_DIRTY  : deserializeAcknowledge
}
def deserialize(myString):
    root = xml.fromstring(myString)
    if(root.tag == 'Message'):
        messageType = root.attrib['MessageType']
        return deserializeFunction[int(messageType)](myString)
            
            
