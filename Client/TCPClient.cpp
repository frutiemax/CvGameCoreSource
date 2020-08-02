#include "TCPClient.h"
#include "DummyStruct.h"

#include <string>
#include <sstream>
#include <boost/bind/bind.hpp>
#include <iostream>
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/xml_oarchive.hpp>

using namespace AI;
TCPClient::TCPClient()
{
	_connected = false;
}

TCPClient::~TCPClient()
{
	if (_connected)
	{
		_socket->close();
	}
	delete _socket;
}

void TCPClient::Connect()
{
	using namespace boost::asio;
	using ip::tcp;

	tcp::resolver resolver(_Context);

	//tcp::resolver::results_type endpoints = resolver.resolve("", "101");
	tcp::resolver::results_type endpoints = resolver.resolve("127.0.0.1", "11750");

	_socket = new tcp::socket(_Context);
	boost::system::error_code err;

	boost::asio::connect(*_socket, endpoints, err);
	if (!err.failed())
	{
		/*RequestMessage message(MessageType::REQ_PLAYER_AI_INIT);
		std::string toSend = SerializeMessage(message);

		size_t len = _socket->write_some(boost::asio::buffer(toSend));

		boost::array<char, 1024> buf;

		len = _socket->read_some(boost::asio::buffer(buf), err);
		std::string inPacket;
		inPacket.assign(buf.begin(), buf.begin() + len);

		boost::shared_ptr<IMessage> deserialized = AI::DeserializeMessage(inPacket);
		IMessage* m = deserialized.get();
		std::cout << m->GetType();*/

		_connected = true;
	}
	else
	{
		std::cout << "Couldn't connect" << std::endl;
	}
}

bool TCPClient::OnPlayerAIInit()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_INIT);
}

bool TCPClient::OnPlayerAIReset()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_RESET);
}

bool TCPClient::OnPlayerAIDoTurnPre()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_DOTURNPRE);
}

bool TCPClient::OnPlayerAIDoTurnPost()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_DOTURNPOST);
}

bool TCPClient::OnPlayerAIDoTurnUnitsPre()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_DOTURN_UNITSPRE);
}

bool TCPClient::OnPlayerAIDoTurnUnitsPost()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_DOTURN_UNITSPOST);
}

bool TCPClient::OnPlayerAIUpdateFoundValues()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_FOUNDVALUES);
}

bool TCPClient::OnPlayerAIUnitUpdate()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_UNITUPDATE);
}

bool TCPClient::OnPlayerAIConquerCity()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_CONQUERCITY);
}

bool TCPClient::OnPlayerAIFoundValue()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_FOUNDVALUE);
}

bool TCPClient::OnPlayerAIChooseFreeGreatPerson()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_CHOOSE_FREE_GREATPERSON);
}

bool TCPClient::OnPlayerAIChooseResearch()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_CHOOSE_RESEARCH);
}

bool TCPClient::OnPlayerAIPlotTargetMissionAIs()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_PLOTTARGETMISSIONS);
}

bool TCPClient::OnPlayerAILaunch()
{
	return onAIRequest(MessageType::REQ_PLAYER_AI_LAUNCH);
}

bool TCPClient::OnCityAIInit()
{
	return onAIRequest(MessageType::REQ_CITY_AI_INIT);
}

bool TCPClient::OnCityAIReset()
{
	return onAIRequest(MessageType::REQ_CITY_AI_RESET);
}

bool TCPClient::OnCityAIDoTurn()
{
	return onAIRequest(MessageType::REQ_CITY_AI_DOTURN);
}

bool TCPClient::OnCityAIChooseProduction()
{
	return onAIRequest(MessageType::REQ_CITY_AI_CHOOSEPRODUCTION);
}

bool TCPClient::OnCityAIIsChooseProductionDirty()
{
	return onAIRequest(MessageType::REQ_CITY_AI_ISCHOOSEPRODUCTION_DIRTY);
}

bool TCPClient::OnCityAISetChooseProductionDirty()
{
	return onAIRequest(MessageType::REQ_CITY_AI_SETCHOOSEPRODUCTION_DIRTY);
}

bool AI::TCPClient::onAIRequest(MessageType messageType)
{
	//send the onPlayerAIInit request message
	boost::system::error_code err;

	//request the AI behavior
	RequestMessage request(messageType);
	std::string toWrite = SerializeMessage(request);
	_socket->write_some(boost::asio::buffer(toWrite), err);
	if (err.failed())
		return false;

	bool finished = false;
	boost::array<char, 1024> buf;

	while (!finished)
	{
		//get a message
		unsigned int len = _socket->read_some(boost::asio::buffer(buf), err);
		if (err.failed())
			return false;
		std::string inPacket;
		inPacket.assign(buf.begin(), buf.begin() + len);
		boost::shared_ptr<IMessage> aiMessage = AI::DeserializeMessage(inPacket);

		/*if (aiMessage->GetType() == AI::MessageType::SEND_PLAYER_AI_INIT)
			finished = true;
		else
		{
			//process the request from the server
		}*/

		std::cout << "Received acknowledge of type " << aiMessage->GetType() << std::endl;
		finished = true;

	}
	return finished;
}

bool AI::TCPClient::onGameRequest(AI::MessageType messageType)
{
	return false;
}
