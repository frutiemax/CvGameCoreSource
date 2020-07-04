#pragma once
#include "CvCity.h"
class CvCityCustomAI :
    public CvCity
{
	void AI_init();
	void AI_reset();
	void AI_doTurn();
	void AI_chooseProduction(bool bInterruptWonders);
	bool AI_isChooseProductionDirty();
	void AI_setChooseProductionDirty(bool bNewValue);

	int AI_GetNumPlotsAcquiredByOtherPlayer(PlayerTypes ePlayer) const;
	void AI_ChangeNumPlotsAcquiredByOtherPlayer(PlayerTypes ePlayer, int iChange);
};

