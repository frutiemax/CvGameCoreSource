#include  "TCPClient.h"

int main()
{
	AI::TCPClient client;

	client.Connect();

	if (client.IsConnected())
	{
		//stimulating the network commands for 50 turns
		for (int i = 0; i < 50; i++)
		{
			client.OnCityAIChooseProduction();
			client.OnCityAIDoTurn();
			client.OnCityAIInit();
			client.OnCityAIIsChooseProductionDirty();
			client.OnCityAIReset();
			client.OnCityAISetChooseProductionDirty();
			client.OnPlayerAIChooseFreeGreatPerson();
			client.OnPlayerAIChooseResearch();
			client.OnPlayerAIConquerCity();
			client.OnPlayerAIDoTurnPost();
			client.OnPlayerAIDoTurnPre();
			client.OnPlayerAIDoTurnUnitsPost();
			client.OnPlayerAIDoTurnUnitsPre();
			client.OnPlayerAIFoundValue();
			client.OnPlayerAIInit();
			client.OnPlayerAILaunch();
			client.OnPlayerAIPlotTargetMissionAIs();
			client.OnPlayerAIReset();
			client.OnPlayerAIUnitUpdate();
			client.OnPlayerAIUpdateFoundValues();
			client.OnCityAIChooseProduction();
			client.OnCityAIDoTurn();
			client.OnCityAIInit();
			client.OnCityAIIsChooseProductionDirty();
			client.OnCityAIReset();
			client.OnCityAISetChooseProductionDirty();
		}
	}
	
	
	return 0;
}