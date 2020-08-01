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
		std::string hello = "helloworld";
		std::ostringstream stream;

		DummyStruct d;
		boost::archive::xml_oarchive oArchive(stream);
		oArchive << BOOST_SERIALIZATION_NVP(d);

		size_t len = _socket->write_some(boost::asio::buffer(stream.str()));
		_connected = true;
	}
	else
	{
		std::cout << "Couldn't connect" << std::endl;
	}
}

bool TCPClient::OnPlayerAIInit()
{
	return false;
}

bool TCPClient::OnPlayerAIReset()
{
	return false;
}

bool TCPClient::OnPlayerAIDoTurnPre()
{
	return false;
}

bool TCPClient::OnPlayerAIDoTurnPost()
{
	return false;
}

bool TCPClient::OnPlayerAIDoTurnUnitsPre()
{
	return false;
}

bool TCPClient::OnPlayerAIDoTurnUnitsPost()
{
	return false;
}

bool TCPClient::OnPlayerAIUpdateFoundValues()
{
	return false;
}

bool TCPClient::OnPlayerAIUnitUpdate()
{
	return false;
}

bool TCPClient::OnPlayerAIConquerCity()
{
	return false;
}

bool TCPClient::OnPlayerAIFoundValue()
{
	return false;
}

bool TCPClient::OnPlayerAIChooseFreeGreatPerson()
{
	return false;
}

bool TCPClient::OnPlayerAIChooseResearch()
{
	return false;
}

bool TCPClient::OnPlayerAIPlotTargetMissionAIs()
{
	return false;
}

bool TCPClient::OnPlayerAILaunch()
{
	return false;
}

bool TCPClient::OnCityAIInit()
{
	return false;
}

bool TCPClient::OnCityAIReset()
{
	return false;
}

bool TCPClient::OnCityAIDoTurn()
{
	return false;
}

bool TCPClient::OnCityAIChooseProduction()
{
	return false;
}

bool TCPClient::OnCityAIIsChooseProductionDirty()
{
	return false;
}

bool TCPClient::OnCityAISetChooseProductionDirty()
{
	return false;
}
