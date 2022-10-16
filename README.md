# SkinRandomizer
An [UnrealEngine PythonSDK](https://github.com/bl-sdk/PythonSDK) mod for Borderlands 2 that does the following:
* Add an option to remove customization elegibility (Allows Maya to use Zer0 heads/skins, etc) This does not unlock all customization 
* Press F2 to randomize the customization in the Quick Change, New Character, and Vehicle spawn menus

## Installations

Begin by [downloading `SkinRandomizer.zip` here](https://github.com/Cae-l/SkinRandomizer/archive/refs/tags/1.0.zip).

1. [Install/update UnrealEngine PythonSDK](https://bl-sdk.github.io/) if you have not already. *Note that your Mode Menu must be version 2.5 or later* (check MODS > General from the main menu)
2. Locate the SDK's `Mods` folder (located `BL2 instalation` > `Binaries` > `Win32`)
3. Copy the `SkinRandomizer` folder from `SkinRandomizer.zip` to `Mods` 
4. Launch the game, select the "MODS" option from the main menu, then select "Skin Randomzer" to enable it


## Usage

Skin Randomizer operates using the `F2` key during certain interactive menus.
| Menu                  | Description                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------|
| Quick change station  | Selects random head & skin from the available pool                                                          |
| Character creation    | Selects random head & skin from the available pool                                                          |
| Catch-a-ride          | Selects a random vehicle skin form the available pool (Preview does not update and not all skins are valid) |


Skin Ransomer has an option that can be configured in game "OPTIONS" > "MODS":
| Option                         | Description                                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------------------|
| Use All Skins - Allow          | Allows all customizations to be available in for all characters (ie. Maya can use Zer0's heads/skins freely). |
| Use All Skins - Default        | Turns off the option. (Swaps current character to default customizations if current selection isn't eligible) |
