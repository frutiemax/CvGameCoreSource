#pragma once

#include <iostream>
#include <boost/asio.hpp>
#include <boost/array.hpp>
#include <boost/asio/ip/tcp.hpp>

#include "Message.h"

namespace AI
{
	class TCPClient
	{
	public:
		TCPClient();
		virtual ~TCPClient();

		void Connect();
		bool IsConnected() const { return _connected; };

		//PlayerAI
		bool OnPlayerAIInit();
		bool OnPlayerAIReset();
		bool OnPlayerAIDoTurnPre();
		bool OnPlayerAIDoTurnPost();
		bool OnPlayerAIDoTurnUnitsPre();
		bool OnPlayerAIDoTurnUnitsPost();
		bool OnPlayerAIUpdateFoundValues();
		bool OnPlayerAIUnitUpdate();
		bool OnPlayerAIConquerCity();
		bool OnPlayerAIFoundValue();
		bool OnPlayerAIChooseFreeGreatPerson();
		bool OnPlayerAIChooseResearch();
		bool OnPlayerAIPlotTargetMissionAIs();
		bool OnPlayerAILaunch();

		//CityAI
		bool OnCityAIInit();
		bool OnCityAIReset();
		bool OnCityAIDoTurn();
		bool OnCityAIChooseProduction();
		bool OnCityAIIsChooseProductionDirty();
		bool OnCityAISetChooseProductionDirty();
	private:
		//AI requests block the AI flow (it expects an acknowledge message)
		bool onAIRequest(AI::MessageType messageType);

		//Game requests do not block the flow, the client sends game data to the server
		bool onGameRequest(AI::MessageType messageType);

		bool _connected;
		boost::asio::ip::tcp::socket* _socket;
		boost::asio::io_context _Context;
	};
}

