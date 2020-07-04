#pragma once
#include "CvPlayer.h"
class CvPlayerCustomAI :
    public CvPlayer
{
	void AI_init();
	void AI_reset();
	void AI_doTurnPre();
	void AI_doTurnPost();
	void AI_doTurnUnitsPre();
	void AI_doTurnUnitsPost();
	void AI_updateFoundValues(bool bStartingLoc = false);
	void AI_unitUpdate();
	void AI_conquerCity(CvCity* pCity, PlayerTypes eOldOwner);
	int AI_foundValue(int iX, int iY, int iMinUnitRange = -1, bool bStartingLoc = false);
	void AI_chooseFreeGreatPerson();
	void AI_chooseFreeTech();
	void AI_chooseResearch();
	int AI_plotTargetMissionAIs(CvPlot* pPlot, MissionAITypes eMissionAI, int iRange = 0);
	void AI_launch(VictoryTypes eVictory);
	bool AI_captureUnit(UnitTypes eUnit, CvPlot* pPlot);

	OperationSlot PeekAtNextUnitToBuildForOperationSlot(int iAreaID);
	OperationSlot CityCommitToBuildUnitForOperationSlot(int iAreaID, int iTurns, CvCity* pCity);
	void CityUncommitToBuildUnitForOperationSlot(OperationSlot thisSlot);
	void CityFinishedBuildingUnitForOperationSlot(OperationSlot thisSlot, CvUnit* pThisUnit);
	int GetNumUnitsNeededToBeBuilt();
};

