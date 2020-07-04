#include "CvGameCoreDLLPCH.h"
#include "CvPlayerCustomAI.h"

void CvPlayerCustomAI::AI_init()
{
}

void CvPlayerCustomAI::AI_reset()
{
}

void CvPlayerCustomAI::AI_doTurnPre()
{
}

void CvPlayerCustomAI::AI_doTurnPost()
{
}

void CvPlayerCustomAI::AI_doTurnUnitsPre()
{
}

void CvPlayerCustomAI::AI_doTurnUnitsPost()
{
}

void CvPlayerCustomAI::AI_updateFoundValues(bool bStartingLoc)
{
}

void CvPlayerCustomAI::AI_unitUpdate()
{
}

void CvPlayerCustomAI::AI_conquerCity(CvCity* pCity, PlayerTypes eOldOwner)
{
}

int CvPlayerCustomAI::AI_foundValue(int iX, int iY, int iMinUnitRange, bool bStartingLoc)
{
    return 0;
}

void CvPlayerCustomAI::AI_chooseFreeGreatPerson()
{
}

void CvPlayerCustomAI::AI_chooseFreeTech()
{
}

void CvPlayerCustomAI::AI_chooseResearch()
{
}

int CvPlayerCustomAI::AI_plotTargetMissionAIs(CvPlot* pPlot, MissionAITypes eMissionAI, int iRange)
{
    return 0;
}

void CvPlayerCustomAI::AI_launch(VictoryTypes eVictory)
{
}

bool CvPlayerCustomAI::AI_captureUnit(UnitTypes eUnit, CvPlot* pPlot)
{
    return false;
}

void CvPlayerCustomAI::AI_City_doTurn(CvCity* city)
{
}

void CvPlayerCustomAI::AI_City_chooseProduction(CvCity* city, bool bInterruptWonders)
{
}

bool CvPlayerCustomAI::AI_City_isChooseProductionDirty(CvCity* city)
{
    return false;
}

void CvPlayerCustomAI::AI_City_setChooseProductionDirty(CvCity* city, bool bNewValue)
{
}

int CvPlayerCustomAI::AI_City_GetNumPlotsAcquiredByOtherPlayer(CvCity* city, PlayerTypes ePlayer) const
{
    return 0;
}

void CvPlayerCustomAI::AI_City_ChangeNumPlotsAcquiredByOtherPlayer(CvCity* city, PlayerTypes ePlayer, int iChange)
{
}

OperationSlot CvPlayerCustomAI::PeekAtNextUnitToBuildForOperationSlot(int iAreaID)
{
    return OperationSlot();
}

OperationSlot CvPlayerCustomAI::CityCommitToBuildUnitForOperationSlot(int iAreaID, int iTurns, CvCity* pCity)
{
    return OperationSlot();
}

void CvPlayerCustomAI::CityUncommitToBuildUnitForOperationSlot(OperationSlot thisSlot)
{
}

void CvPlayerCustomAI::CityFinishedBuildingUnitForOperationSlot(OperationSlot thisSlot, CvUnit* pThisUnit)
{
}

int CvPlayerCustomAI::GetNumUnitsNeededToBeBuilt()
{
    return 0;
}
