import random
from typing import List, Tuple

import unrealsdk
from unrealsdk import *
from Mods import ModMenu
from ..ModMenu import EnabledSaveType, Hook, SDKMod


allSkins = ModMenu.Options.Spinner(
    Caption="Use All Skins",
    Description="Enables the use of all skins regardless of character selection.",
    Choices=["Default", "All Skins"],
    StartingValue="Default"
)

class skinRando(SDKMod):
    Name = "Skin Randomizer"
    Version = "1.4"
    Author = "Cael"
    Description: str = ("<strong><u><font size='18' color='#8a0087'>Skin Randomizer</font></u></strong>\n"\
                        "<font size='16'>Features:</font>\n"\
                        "<font size='12'>1.Press F2 to randomize any customization in UI</font>\n"
                        "<font size='12'>[Quick Change, New Characters creation, and Catch-a-Ride]</font>\n"\
                        "<font size='12'>2.Turn on/off character customization eligibility</font>\n"
                        "<font size='12'>[Allows Maya heads/skins on Zer0, etc]</font>\n")
 
    Options: List[ModMenu.Options.Base] = [
        allSkins
    ]

    SaveEnabledState = EnabledSaveType.LoadOnMainMenu

    def Enable(self) -> None:
        super().Enable()
        if allSkins.CurrentValue == "All Skins":
            self.enableAllSkins()

    def Disable(self) -> None:
        super().Disable()
        self.disableAllSkins()

    def ModOptionChanged(self, option: ModMenu.Options.Base, new_value) -> None:
        if option == allSkins:
            if new_value == "All Skins":
                self.enableAllSkins()
            else: 
                self.disableAllSkins()

    def enableAllSkins(self) -> None:
        PC = unrealsdk.GetEngine().GamePlayers[0].Actor
        PC.ConsoleCommand("set GD_Soldier.Character.CharClass_Soldier EligibleUsage (0)")
        PC.ConsoleCommand("set GD_Assassin.Character.CharClass_Assassin EligibleUsage (0)")
        PC.ConsoleCommand("set GD_Siren.Character.CharClass_Siren EligibleUsage (0)")
        PC.ConsoleCommand("set GD_Mercenary.Character.CharClass_Mercenary EligibleUsage (0)")
        PC.ConsoleCommand("set GD_Tulip_Mechromancer.Character.CharClass_Mechromancer EligibleUsage (0)")
        PC.ConsoleCommand("set GD_Lilac_PlayerClass.Character.CharClass_LilacPlayerClass EligibleUsage (0)")
        PC.ConsoleCommand("set VSSUIDefinition EligibleUsage (0)")

    def disableAllSkins(self) -> None:
        PC = unrealsdk.GetEngine().GamePlayers[0].Actor
        PC.ConsoleCommand("set GD_Soldier.Character.CharClass_Soldier (Class'WillowGame.CustomizationUsage_Soldier')")
        PC.ConsoleCommand("set GD_Assassin.Character.CharClass_Assassin EligibleUsage (Class'WillowGame.CustomizationUsage_Assassin')")
        PC.ConsoleCommand("set GD_Siren.Character.CharClass_Siren EligibleUsage (Class'WillowGame.CustomizationUsage_Siren')")
        PC.ConsoleCommand("set GD_Mercenary.Character.CharClass_Mercenary EligibleUsage (Class'WillowGame.CustomizationUsage_Mercenary')")
        PC.ConsoleCommand("set GD_Tulip_Mechromancer.Character.CharClass_Mechromancer EligibleUsage (Class'WillowGame.CustomizationUsage_ExtraPlayerA')")
        PC.ConsoleCommand("set GD_Lilac_PlayerClass.Character.CharClass_LilacPlayerClass EligibleUsage (Class'WillowGame.CustomizationUsage_ExtraPlayerB')")
        PC.ConsoleCommand("set GD_SagePackageDef.Vehicles.VSSUI_ShockFanBoat EligibleUsage (Class'WillowGame.CustomizationUsage_FanBoat')")
        PC.ConsoleCommand("set GD_SagePackageDef.Vehicles.VSSUI_IncendiaryFanBoat EligibleUsage (Class'WillowGame.CustomizationUsage_FanBoat')")
        PC.ConsoleCommand("set GD_SagePackageDef.Vehicles.VSSUI_CorrosiveFanBoat EligibleUsage (Class'WillowGame.CustomizationUsage_FanBoat')")
        PC.ConsoleCommand("set GD_OrchidPackageDef.Vehicles.VSSUI_SawBladeHovercraft EligibleUsage (Class'WillowGame.CustomizationUsage_Hovercraft')")
        PC.ConsoleCommand("set GD_OrchidPackageDef.Vehicles.VSSUI_RocketHovercraft EligibleUsage (Class'WillowGame.CustomizationUsage_Hovercraft')")
        PC.ConsoleCommand("set GD_OrchidPackageDef.Vehicles.VSSUI_HarpoonHovercraft EligibleUsage (Class'WillowGame.CustomizationUsage_Hovercraft')")
        PC.ConsoleCommand("set GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical EligibleUsage (Class'WillowGame.CustomizationUsage_BanditTech')")
        PC.ConsoleCommand("set GD_Globals.VehicleSpawnStation.VSSUI_RocketRunner EligibleUsage (Class'WillowGame.CustomizationUsage_Runner')")
        PC.ConsoleCommand("set GD_Globals.VehicleSpawnStation.VSSUI_MGRunner EligibleUsage (Class'WillowGame.CustomizationUsage_Runner')")
        PC.ConsoleCommand("set GD_Globals.VehicleSpawnStation.VSSUI_CatapultTechnical EligibleUsage (Class'WillowGame.CustomizationUsage_BanditTech')")

    @Hook("WillowGame.CustomizationGFxMovie.MainInputKey")
    def MainInputKey(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        if params.ukey == "F2" and params.uevent == 1:
            _heads: List[UObject] = list(caller.HeadCustomizations)
            choiceHead: UObject = random.choice(_heads)
            caller.EquippedHeadCustomization = choiceHead
            caller.UpdateHeadPreview(choiceHead)
            caller.CommitHeadCustomization(choiceHead)


            _skins: List[UObject] = list(caller.SkinCustomizations)
            choiceSkin: UObject = random.choice(_skins)
            caller.EquippedSkinCustomization = choiceSkin
            caller.UpdateSkinPreview(choiceSkin)
            caller.CommitSkinCustomization(choiceSkin)

        return True

    @Hook("WillowGame.CharacterSelectionReduxGFxMovie.HandleCustomizeCharacterInput")
    def HandleCustomizeCharacterInput(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        if params.Key =="F2" and params.Event == 1:
            _heads: List[UObject] = list(caller.PrimaryPlayerHeadCustomizations)
            choiceHead: UObject = random.choice(_heads)
            caller.EquippedHeadCustomization[0] = choiceHead
            caller.UpdateHeadPreview(0, choiceHead)
            caller.CommitHeadCustomization(0)

            _skins: List[UObject] = list(caller.PrimaryPlayerSkinCustomizations)
            choiceSkin: UObject = random.choice(_skins)
            caller.EquippedSkinCustomization[0] = choiceSkin
            caller.UpdateSkinPreview(0, choiceSkin)
            caller.CommitSkinCustomization(0)
        return True

    @Hook("WillowGame.VehicleSpawnStationGFxMovie.HandleKeyDefaults")
    def HandleKeyDefaults(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        if params.ukey == "F2" and params.uevent == 1:
            caller.SelectedModuleIndex = 0
            _skins: List[UObject] = list(caller.AvailableVehicleSkinDefinitions)
            choiceSkin: UObject = random.choice(_skins)
            caller.UpdatePreview(choiceSkin)
            caller.VehicleChoiceModule[0].EquippedVehicleCustomizationDefinition = choiceSkin
            caller.VehicleChoiceModule[0].PreviewVehicleCustomizationDefinition = choiceSkin
            caller.CommitCustomization()

            caller.SelectedModuleIndex = 1
            _skins: List[UObject] = list(caller.AvailableVehicleSkinDefinitions)
            choiceSkin: UObject = random.choice(_skins)
            caller.UpdatePreview(choiceSkin)
            caller.VehicleChoiceModule[1].EquippedVehicleCustomizationDefinition = choiceSkin
            caller.VehicleChoiceModule[1].PreviewVehicleCustomizationDefinition = choiceSkin
            caller.CommitCustomization()
            caller.CancelCustomization()
        return True

unrealsdk.RegisterMod(skinRando())
ModMenu.SaveModSettings(skinRando())
