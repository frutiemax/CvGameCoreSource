#pragma once

#include <iostream>
#include <boost/asio.hpp>
#include <boost/array.hpp>
#include <boost/asio/ip/tcp.hpp>

namespace AI
{
	class TCPClient
	{
	public:
		TCPClient();
		virtual ~TCPClient();

		void Connect();

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
		bool sendMessage(class IMessage* message);

		bool _connected;
		boost::asio::ip::tcp::socket* _socket;
		boost::asio::io_context _Context;
	};
}

