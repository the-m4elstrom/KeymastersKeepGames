from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class GunfireRebornArchipelagoOptions:
    gunfire_reborn_dlc_owned: GunfireRebornDLCOwned
    gunfire_reborn_include_spiritual_assault: GunfireRebornIncludeSpiritualAssault

class GunfireRebornGame(Game):
    name = "Gunfire Reborn"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.AND
    ]

    is_adult_only_or_unrated = False

    options_cls = GunfireRebornArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Cannot use the following weapons (unless required): WEAPONS",
                data={
                    "WEAPONS": (self.all_weapons, 5),
                },
            ),
            GameObjectiveTemplate(
                label="Play on difficulty DIFFICULTY or higher",
                data={
                    "DIFFICULTY": (self.all_difficulties, 1)
                },
            ),
            GameObjectiveTemplate(
                label="Finish all runs at Hyperborean Jokul",
                data=dict()
            ),
            GameObjectiveTemplate(
                label="Finish all runs at Duo Fjord",
                data=dict()
            ),
            GameObjectiveTemplate(
                label="Can only pickup Normal rarity scrolls",
                data=dict()
            ),
            GameObjectiveTemplate(
                label="Cannot pickup Normal rarity scrolls",
                data=dict()
            ),
            GameObjectiveTemplate(
                label="Open every Peculiar Chest",
                data=dict()
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Win a run as CHARACTER",
                data={
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a run as CHARACTER using a WEAPON_TYPE",
                data={
                    "CHARACTER": (self.characters, 1),
                    "WEAPON_TYPE": (self.weapon_types, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
                GameObjectiveTemplate(
                label="Win a run as CHARACTER on DIFFICULTY",
                data={
                    "CHARACTER": (self.characters, 1),
                    "DIFFICULTY": (self.difficulty_normal, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a run as CHARACTER on DIFFICULTY",
                data={
                    "CHARACTER": (self.characters, 1),
                    "DIFFICULTY": (self.difficulty_hard, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a run as CHARACTER using one of the following weapons: WEAPON",
                data={
                    "CHARACTER": (self.characters, 1),
                    "WEAPON": (self.all_weapons, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a run on Reincarnation Difficulty with the following Bizarre Dream enabled: BIZARRE_DREAM",
                data={
                    "BIZARRE_DREAM": (self.bizarre_dreams, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a run on Reincarnation Difficulty with the following Bizarre Dreams enabled: BIZARRE_DREAM",
                data={
                    "BIZARRE_DREAM": (self.bizarre_dreams, 3),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a run on Reincarnation Difficulty with the following Bizarre Dreams enabled: Boundless Dream",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

        if self.spiritual_assault_enabled:
            templates.extend( 
                [
                    GameObjectiveTemplate(
                        label="Win a round of Spiritual Assault as CHARACTER",
                        data={
                            "CHARACTER": (self.characters, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Win a round of Spiritual Assault on MAP",
                        data={
                            "MAP": (self.spiritual_assault_maps, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ]
            )

        return templates

    @property
    def dlc_owned(self) -> List[str]:
        return sorted(self.archipelago_options.gunfire_reborn_dlc_owned.value)
    
    @property
    def has_dlc_1(self) -> bool:
        return "Visitors of Spirit Realm" in self.dlc_owned
    
    @property
    def has_dlc_2(self) -> bool:
        return "Artisan and Magician" in self.dlc_owned
    
    @property
    def has_dlc_3(self) -> bool:
        return "Realm of Frost and Inkwash" in self.dlc_owned

    @property
    def spiritual_assault_enabled(self) -> bool:
        return bool(self.archipelago_options.gunfire_reborn_include_spiritual_assault.value)
    
    @staticmethod
    def difficulty_normal() -> List[str]:
        return [
            "Normal",
            "Expert",
        ]
    
    @staticmethod
    def difficulty_hard() -> List[str]:
        return [
            "Nightmare",
            "Reincarnation"
        ]
    
    @staticmethod
    def all_difficulties() -> List[str]:
        return [
            "Normal",
            "Expert",
            "Nightmare",
            "Reincarnation"
        ]

    @staticmethod
    def bizarre_dreams() -> List[str]:
        return [
            "Spiritual Link",
            "Mysterious Jokul",
            "Lone Wolf",
            "Interdependent Fortunes",
            "Transcendent Arsenal",
            "Ascension Fusion",
            "Mission From Above",
        ]
    
    @staticmethod
    def spiritual_assault_maps() -> List[str]:
        return [
            "Desert Frontier",
            "Mid Fjord"
        ]

    @functools.cached_property
    def characters_base(self) -> List[str]:
        return [
            "Crown Prince",
            "Ao Bai",
            "Qing Yan",
            "Lei Luo",
            "Tao",
            "Qian Sui",
        ]
    
    @functools.cached_property
    def characters_dlc_1(self) -> List[str]:
        return [
            "Xing Zhe",
            "Li",
        ]
    
    @functools.cached_property
    def characters_dlc_2(self) -> List[str]:
        return [
            "Zi Xiao",
            "Nona",
        ]
    
    @functools.cached_property
    def characters_dlc_3(self) -> List[str]:
        return [
            "Lyn",
            "Momo",
        ]

    def characters(self) -> List[str]:
        characters: List[str] = self.characters_base

        if self.has_dlc_1:
            characters.extend(self.characters_dlc_1)

        if self.has_dlc_2:
            characters.extend(self.characters_dlc_2)

        if self.has_dlc_3:
            characters.extend(self.characters_dlc_3)
        
        return sorted(characters)
    

    @staticmethod
    def weapon_types() -> List[str]:
        return [
            "Rifle",
            "Submachine Gun",
            "Pistol",
            "Shotgun",
            "Sniper",
            "Launcher",
            "Injector",
            "Melee",
            "Staff"
        ]

    @functools.cached_property
    def weapons_rifle_base(self) -> List[str]:
        return [
            "Big Hippo",
            "Cavalry",
            "Crimson Firescale",
            "Dragonchaser",
            "Lightning Blast",
            "Rainbow Arch",
        ]
    
    @functools.cached_property
    def weapons_rifle_dlc_1(self) -> List[str]:
        return [
            "Hexagon"
        ]
    
    @functools.cached_property
    def weapons_rifle_dlc_2(self) -> List[str]:
        return list()

    @functools.cached_property
    def weapons_rifle_dlc_3(self) -> List[str]:
        return [
            "Tracker"
        ]
    
    def weapons_rifle(self) -> List[str]:
        weapons: List[str] = self.weapons_rifle_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_rifle_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_rifle_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_rifle_dlc_3)

        return sorted(weapons)
    
    @functools.cached_property
    def weapons_smg_base(self) -> List[str]:
        return [
            "Angelic Aura",
            "Concealed Ammo",
            "Demonlore",
            "Dual Fang",
            "Scalpel",
            "Star Devourer"
        ]
    
    @functools.cached_property
    def weapons_smg_dlc_1(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_smg_dlc_2(self) -> List[str]:
        return [
            "Wolf Gaze"
        ]
    
    @functools.cached_property
    def weapons_smg_dlc_3(self) -> List[str]:
        return list()

    def weapons_smg(self) -> List[str]:
        weapons: List[str] = self.weapons_smg_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_smg_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_smg_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_smg_dlc_3)

        return sorted(weapons)
    
    @functools.cached_property
    def weapons_pistol_base(self) -> List[str]:
        return[
            "Aura of Venom",
            "Glimmering",
            "Icy Spear",
            "Prism",
            "Scorching Rounds",
            "Sunder",
            "Talisman"
        ]
    
    @functools.cached_property
    def weapons_pistol_dlc_1(self) -> List[str]:
        return [
            "Arc Light",
            "Cloud Weaver"
        ]
    
    @functools.cached_property
    def weapons_pistol_dlc_2(self) -> List[str]:
        return [
            "Star Ring"
        ]
    
    @functools.cached_property
    def weapons_pistol_dlc_3(self) -> List[str]:
        return list()
    
    def weapons_pistol(self) -> List[str]:
        weapons: List[str] = self.weapons_pistol_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_pistol_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_pistol_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_pistol_dlc_3)

        return sorted(weapons)

    @functools.cached_property
    def weapons_shotgun_base(self) -> List[str]:
        return [
            "Argus",
            "Hell",
            "Illusion",
            "Porcupine",
            "Pupil",
            "Wheel Saw",
            "Wild Hunt",
        ]
    
    @functools.cached_property
    def weapons_shotgun_dlc_1(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_shotgun_dlc_2(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_shotgun_dlc_3(self) -> List[str]:
        return list()

    def weapons_shotgun(self) -> List[str]:
        weapons: List[str] = self.weapons_shotgun_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_shotgun_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_shotgun_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_shotgun_dlc_3)

        return sorted(weapons)
    
    @functools.cached_property
    def weapons_sniper_base(self) -> List[str]:
        return [
            "Bloody Drill",
            "Double Caliber",
            "Golden Bow",
            "Goshawk",
            "Piercing Flame",
            "Sting",
            "Strike Wing",
            "Woodpecker",
        ]
    
    @functools.cached_property
    def weapons_sniper_dlc_1(self) -> List[str]:
        return [
            "Lighting Ksana"
        ]
    
    @functools.cached_property
    def weapons_sniper_dlc_2(self) -> List[str]:
        return [
            "Brick"
        ]
    
    @functools.cached_property
    def weapons_sniper_dlc_3(self) -> List[str]:
        return list()
    
    def weapons_sniper(self) -> List[str]:
        weapons: List[str] = self.weapons_sniper_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_sniper_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_sniper_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_sniper_dlc_3)

        return sorted(weapons)

    @functools.cached_property
    def weapons_launcher_base(self) -> List[str]:
        return [
            "Bone Dragon",
            "Deafening Mortar",
            "Dragon Breath",
            "Frenzied Shark",
            "Justice",
            "Shrieker",
            "Thunder Storm",
            "Tiger Cannon",
        ]
    
    @functools.cached_property
    def weapons_launcher_dlc_1(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_launcher_dlc_2(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_launcher_dlc_3(self) -> List[str]:
        return [
            "Tempest"
        ]
    
    def weapons_launcher(self) -> List[str]:
        weapons: List[str] = self.weapons_launcher_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_launcher_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_launcher_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_launcher_dlc_3)

        return sorted(weapons)

    @functools.cached_property
    def weapons_injector_base(self) -> List[str]:
        return [
            "Clawspray",
            "Fire Dragon",
            "Laser Gloves",
            "Radioactive Gauntlet",
            "Rainbow",
            "Thunderclap Gloves"
        ]
    
    @functools.cached_property
    def weapons_injector_dlc_1(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_injector_dlc_2(self) -> List[str]:
        return [
            "Jet Octopus"
        ]
    
    @functools.cached_property
    def weapons_injector_dlc_3(self) -> List[str]:
        return list()
    
    def weapons_injector(self) -> List[str]:
        weapons: List[str] = self.weapons_injector_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_injector_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_injector_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_injector_dlc_3)

        return sorted(weapons)

    @functools.cached_property
    def weapons_melee_base(self) -> List[str]:
        return [
            "Fire Tower",
            "Flowing Light",
            "Poisonous Ghost",
            "Storm Chaser"
        ]
    
    @functools.cached_property
    def weapons_melee_dlc_1(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_melee_dlc_2(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_melee_dlc_3(self) -> List[str]:
        return list()
    
    def weapons_melee(self) -> List[str]:
        weapons: List[str] = self.weapons_melee_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_melee_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_melee_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_melee_dlc_3)

        return sorted(weapons)

    @functools.cached_property
    def weapons_staff_base(self) -> List[str]:
        return [
            "Crane Chant"
        ]
    
    @functools.cached_property
    def weapons_staff_dlc_1(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_staff_dlc_2(self) -> List[str]:
        return list()
    
    @functools.cached_property
    def weapons_staff_dlc_3(self) -> List[str]:
        return [
            "Phoenix Roar",
            "Starfly"
        ]
    
    def weapons_staff(self) -> List[str]:
        weapons: List[str] = self.weapons_staff_base[:]

        if self.has_dlc_1:
            weapons.extend(self.weapons_staff_dlc_1)
        if self.has_dlc_2:
            weapons.extend(self.weapons_staff_dlc_2)
        if self.has_dlc_3:
            weapons.extend(self.weapons_staff_dlc_3)

        return sorted(weapons)
    
    def all_weapons(self) -> List[str]:
        weapons: List[str] = list()

        weapons.extend(self.weapons_rifle())
        weapons.extend(self.weapons_smg())
        weapons.extend(self.weapons_pistol())
        weapons.extend(self.weapons_shotgun())
        weapons.extend(self.weapons_sniper())
        weapons.extend(self.weapons_launcher())
        weapons.extend(self.weapons_injector())
        weapons.extend(self.weapons_melee())
        weapons.extend(self.weapons_staff())
        
        return sorted(weapons)
   

#####################
# Archipelago Options
#####################

class GunfireRebornDLCOwned(OptionSet):
    """
    Indicates which Gunfire Reborn DLC the player owns, if any.
    """
    display_name = "Gunfire Reborn DLC Owned"
    valid_keys = [
        "Visitors of Spirit Realm",
        "Artisan and Magician",
        "Realm of Frost and Inkwash",
    ]

    default = valid_keys

class GunfireRebornIncludeSpiritualAssault(Toggle):
    """
    Indicates whether or not to include Gunfire Reborn Spiritual Assault when generating objectives.
    """
    display_name = "Gunfire Reborn Include Spiritual Assault"