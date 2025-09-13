from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class TeamFortress2ArchipelagoOptions:
    team_fortress_2_include_alternate_game_modes: TeamFortress2IncludeAlternateGameModes
    team_fortress_2_include_mann_vs_machine: TeamFortress2IncludeMannVsMachine

class TeamFortress2Game(Game):
    name = "Team Fortress 2"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = TeamFortress2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Cannot use the following weapons (unless required): WEAPONS",
                data={
                    "WEAPONS": (self.all_weapons, 5),
                },
            ),
            GameObjectiveTemplate(
                label="Earn at least 15 points in each round",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Win a match as CLASS",
                data={
                    "CLASS": (self.classes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a match on MAP",
                data={
                    "MAP": (self.main_maps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a match as CLASS on MAP",
                data={
                    "CLASS": (self.classes, 1),
                    "MAP": (self.main_maps, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a match on any GAMEMODE map",
                data={
                    "GAMEMODE": (self.main_gamemodes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Get 5 kills as CLASS in a single life",
                data={
                    "CLASS": (self.classes, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Get 5 kills as CLASS on MAP in a single life",
                data={
                    "CLASS": (self.classes, 1),
                    "MAP": (self.main_maps, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Scout using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.scout_primary, 1),
                    "SECONDARY": (self.scout_secondary, 1),
                    "MELEE": (self.scout_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Soldier using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.soldier_primary, 1),
                    "SECONDARY": (self.soldier_secondary, 1),
                    "MELEE": (self.soldier_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Pyro using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.pyro_primary, 1),
                    "SECONDARY": (self.pyro_secondary, 1),
                    "MELEE": (self.pyro_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Demoman using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.demo_primary, 1),
                    "SECONDARY": (self.demo_secondary, 1),
                    "MELEE": (self.demo_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Heavy using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.heavy_primary, 1),
                    "SECONDARY": (self.heavy_secondary, 1),
                    "MELEE": (self.heavy_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Engineer using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.engineer_primary, 1),
                    "SECONDARY": (self.engineer_secondary, 1),
                    "MELEE": (self.engineer_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Medic using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.medic_primary, 1),
                    "SECONDARY": (self.medic_secondary, 1),
                    "MELEE": (self.medic_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Sniper using the following loadout: PRIMARY, SECONDARY, MELEE",
                data={
                    "PRIMARY": (self.sniper_primary, 1),
                    "SECONDARY": (self.sniper_secondary, 1),
                    "MELEE": (self.sniper_melee, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round as Spy using the following loadout: PRIMARY, SECONDARY, MELEE, WATCH",
                data={
                    "PRIMARY": (self.spy_primary, 1),
                    "SECONDARY": (self.spy_secondary, 1),
                    "MELEE": (self.spy_melee, 1),
                    "WATCH": (self.spy_watch, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
        ]

        if self.alternate_gamemodes_enabled:
            templates.extend( 
                [
                    GameObjectiveTemplate(
                        label="Win a round on any GAMEMODE map",
                        data={
                            "GAMEMODE": (self.alternate_gamemodes, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Win a round as CLASS on any GAMEMODE map",
                        data={
                            "CLASS": (self.classes, 1),
                            "GAMEMODE": (self.alternate_gamemodes, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Get 5 kills as CLASS in a single life on any GAMEMODE map",
                        data={
                            "CLASS": (self.classes, 1),
                            "GAMEMODE": (self.alternate_gamemodes, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    ),
                ]
            )

        if self.mann_vs_machine_enabled:
            templates.extend( 
                [
                    GameObjectiveTemplate(
                        label="Complete a Mann Vs. Machine mission on MAP",
                        data={
                            "MAP": (self.mann_vs_machine_main_maps, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Complete a Mann Vs. Machine tour of OPERATION",
                        data={
                            "OPERATION": (self.mann_vs_machine_main_tours, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Complete a Mann Vs. Machine mission on MAP",
                        data={
                            "MAP": (self.mann_vs_machine_expert_maps, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=1,
                    ),
                    GameObjectiveTemplate(
                        label="Complete a Mann Vs. Machine tour of OPERATION",
                        data={
                            "OPERATION": (self.mann_vs_machine_expert_tours, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                ]
            )

        return templates

    @property
    def alternate_gamemodes_enabled(self) -> bool:
        return bool(self.archipelago_options.team_fortress_2_include_alternate_game_modes.value)

    @property
    def mann_vs_machine_enabled(self) -> bool:
        return bool(self.archipelago_options.team_fortress_2_include_mann_vs_machine.value)

    
    def classes(self) -> List[str]:
        return [
            "Scout",
            "Soldier",
            "Pyro",
            "Demoman",
            "Heavy",
            "Engineer",
            "Medic",
            "Sniper",
            "Spy",
        ]

    
    def main_maps(self) -> List[str]:
        return [
            "2Fort",
            "2Fort Invasion",
            "Applejack",
            "Doublecross",
            "Frosty",
            "Landfall",
            "Pelican Peak",
            "Penguin Peak",
            "Sawmill (Capture the Flag)",
            "Turbine",
            "Well (Capture the Flag)",
            "Altitude",
            "Brew",
            "Dustbowl",
            "Egypt",
            "Fortezza",
            "Gorge (Attack/Defend)",
            "Gravelpit",
            "Haarp",
            "Hadal",
            "Hardwood",
            "Junction",
            "Mercenary Park",
            "Mossrock",
            "Mountain Lab",
            "Overgrown",
            "Snowplow",
            "Steelworks",
            "Sulfur",
            "5Gorge",
            "Badlands (Control Points)",
            "Canaveral",
            "Coldfront",
            "Fastlane",
            "Foundry (Control Points)",
            "Freight",
            "Granary",
            "Gullywash",
            "Metalworks",
            "Powerhouse",
            "Process",
            "Reckoner",
            "Snakewater",
            "Standin",
            "Sunshine",
            "Vanguard",
            "Well",
            "Yukon",
            "Badlands (King of the Hill)",
            "Brazil",
            "Cachoeira",
            "Cascade",
            "Harvest",
            "Highpass",
            "Kong King",
            "Lakeside",
            "Lazarus",
            "Megaton",
            "Nucleus",
            "Overcast",
            "Probed",
            "Rotunda",
            "Sawmill (King of the Hill)",
            "Sharkbay",
            "Snowtower",
            "Suijin",
            "Viaduct",
            "Badwater",
            "Barnblitz",
            "Borneo",
            "Bread Space",
            "Camber",
            "Cashworks",
            "Embargo",
            "Emerge",
            "Enclosure",
            "Frontier",
            "Goldrush",
            "Hoodoo",
            "Odyssey",
            "Patagonia",
            "Phoenix",
            "Pier",
            "Rumford",
            "Snowycoast",
            "Swiftwater",
            "Thunder Mountain (Payload)",
            "Upward",
            "Venice",
        ]

    
    def main_gamemodes(self) -> List[str]:
        return [
            "Attack/Defend",
            "Capture the Flag",
            "Control Points",
            "King of the Hill",
            "Payload",
        ]
    
    def alternate_gamemodes(self) -> List[str]:
        return [
            "Payload Race",
            "Misc.",
            "Mannpower",
            "PASS Time",
        ]

    
    def mann_vs_machine_main_maps(self) -> List[str]:
        return[
            "Bigrock",
            "Coal Town",
            "Decoy",
            "Mannhattan",
            "Rottenburg",
        ]

    
    def mann_vs_machine_main_tours(self) -> List[str]:
        return[
            "Operation Oil Spill",
            "Operation Steel Trap",
            "Operation Mecha Engie",
            "Operation Two Cities",
        ]

    
    def mann_vs_machine_expert_maps(self) -> List[str]:
        return [
            "Mannworks",
        ]

    
    def mann_vs_machine_expert_tours(self) -> List[str]:
        return [
            "Operation Gear Grinder",
        ]


    
    def scout_primary(self) -> List[str]:
        return [
            "Scattergun",
            "Force-A-Nature",
            "Shortstop",
            "Soda Popper",
            "Baby Face's Blaster",
            "Back Scatter",
        ]

    
    def scout_secondary(self) -> List[str]:
        return [
            "Pistol",
            "Winger",
            "Pretty Boy's Pocket Pistol",
            "Flying Guillotine",
            "Bonk! Atomic Punch",
            "Crit-a-Cola",
            "Mad Milk",
        ]


    
    def scout_melee(self) -> List[str]:
        return [
            "Bat",
            "Holy Mackerel",
            "Sandman",
            "Candy Cane",
            "Boston Basher",
            "Sun-on-a-Stick",
            "Fan O'War",
            "Atomizer",
            "Wrap Assassin",
        ]


    
    def soldier_primary(self) -> List[str]:
        return [
            "Rocket Launcher",
            "Original",
            "Direct Hit",
            "Black Box",
            "Rocket Jumper",
            "Liberty Launcher",
            "Cow Mangler 5000",
            "Beggar's Bazooka",
            "Air Strike",
        ]

    
    def soldier_secondary(self) -> List[str]:
        return [
            "Shotgun",
            "Reserve Shooter",
            "Buff Banner",
            "Gunboats",
            "Battalion's Backup",
            "Concheror",
            "Mantreads",
            "Righteous Bison",
            "B.A.S.E. Jumper",
        ]

    
    def soldier_melee(self) -> List[str]:
        return [
            "Shovel",
            "Equalizer",
            "Pain Train",
            "Half-Zatoichi",
            "Disciplinary Action",
            "Market Gardener",
            "Escape Plan",
        ]


    
    def pyro_primary(self) -> List[str]:
        return [
            "Flame Thrower",
            "Rainblower",
            "Backburner",
            "Degreaser",
            "Phlogistinator",
            "Dragon's Fury",
        ]

    
    def pyro_secondary(self) -> List[str]:
        return [
            "Shotgun",
            "Reserve Shooter",
            "Flare Gun",
            "Detonator",
            "Manmelter",
            "Scorch Shot",
            "Thermal Thruster",
            "Gas Passer",
        ]

    
    def pyro_melee(self) -> List[str]:
        return [
            "Fire Axe",
            "Lollichop",
            "Axtinguisher",
            "Postal Pummeler",
            "Homewrecker",
            "Powerjack",
            "Back Scratcher",
            "Sharpened Volcano Fragment",
            "Third Degree",
            "Neon Annihilator",
            "Hot Hand"
        ]


    
    def demo_primary(self) -> List[str]:
        return [
            "Grenade Launcher",
            "Loch-n-Load",
            "Ali Baba's Wee Booties",
            "Bootlegger",
            "Loose Cannon",
            "B.A.S.E. Jumper",
        ]

    
    def demo_secondary(self) -> List[str]:
        return [
            "Stickybomb Launcher",
            "Scottish Resistance",
            "Chargin' Targe",
            "Sticky Jumper",
            "Splendid Screen",
            "Tide Turner",
            "Quickiebomb Launcher",
        ]

    
    def demo_melee(self) -> List[str]:
        return [
            "Bottle",
            "Scottish Handshake",
            "Eyelander",
            "Nessie's Nine Iron",
            "Scotsman's Skullcutter",
            "Pain Train",
            "Ullapool Caber",
            "Claidheamh Mòr",
            "Half-Zatoichi",
            "Persian Persuader",
        ]


    
    def heavy_primary(self) -> List[str]:
        return [
            "Minigun",
            "Natascha",
            "Brass Beast",
            "Tomislav",
            "Huo-Long Heater",
        ]

    
    def heavy_secondary(self) -> List[str]:
        return [
            "Shotgun",
            "Family Business",
            "Sandvich",
            "Dalokohs Bar",
            "Buffalo Steak Sandvich",
            "Second Banana",
        ]

    
    def heavy_melee(self) -> List[str]:
        return [
            "Fists",
            "Killing Gloves of Boxing",
            "Gloves of Running Urgently",
            "Warrior's Spirit",
            "Fists of Steel",
            "Eviction Notice",
            "Holiday Punch",
        ]


    
    def engineer_primary(self) -> List[str]:
        return [
            "Shotgun",
            "Frontier Justice",
            "Widowmaker",
            "Pomson 6000",
            "Rescue Ranger",
        ]

    
    def engineer_secondary(self) -> List[str]:
        return [
            "Pistol",
            "Wrangler",
            "Short Circuit",
        ]

    
    def engineer_melee(self) -> List[str]:
        return [
            "Wrench",
            "Gunslinger",
            "Southern Hospitality",
            "Jag",
            "Eureka Effect",
        ]


    
    def medic_primary(self) -> List[str]:
        return [
            "Syringe Gun",
            "Blutsauger",
            "Crusader's Crossbow",
            "Overdose",
        ]

    
    def medic_secondary(self) -> List[str]:
        return [
            "Medi Gun",
            "Kritzkrieg",
            "Quick-Fix",
            "Vaccinator",
        ]

    
    def medic_melee(self) -> List[str]:
        return [
            "Bonesaw",
            "Ubersaw",
            "Vita-Saw",
            "Amputator",
            "Solemn Vow",
        ]


    
    def sniper_primary(self) -> List[str]:
        return [
            "Sniper Rifle",
            "Huntsman",
            "Fortified Compound",
            "Sydney Sleeper",
            "Bazaar Bargain",
            "Machina",
            "Hitman's Heatmaker",
            "Classic",
        ]

    
    def sniper_secondary(self) -> List[str]:
        return [
            "Submachine Gun",
            "Cleaner's Carbine",
            "Jarate",
            "Razorback",
            "Darwin's Danger Shield",
            "Cozy Camper",
        ]

    
    def sniper_melee(self) -> List[str]:
        return [
            "Kukri",
            "Tribalman's Shiv",
            "Bushwacka",
            "Shahanshah",
        ]

    
    def spy_primary(self) -> List[str]:
        return [
            "Revolver",
            "Ambassador",
            "L'Etranger",
            "Enforcer",
            "Diamondback", 
        ]

    
    def spy_secondary(self) -> List[str]:
        return [
            "Sapper",
            "Red-Tape Recorder",
        ]

    
    def spy_melee(self) -> List[str]:
        return [
            "Knife",
            "Your Eternal Reward",
            "Conniver's Kunai",
            "Big Earner",
            "Spy-cicle",
        ]

    
    def spy_watch(self) -> List[str]:
        return [
            "Invis Watch",
            "Cloak and Dagger",
            "Dead Ringer",
        ]


    
    def all_weapons(self) -> List[str]:
        weaponsList: List[str] = list()
        
        weaponsList.extend(self.scout_primary())
        weaponsList.extend(self.scout_secondary())
        weaponsList.extend(self.scout_melee())
        weaponsList.extend(self.soldier_primary())     
        weaponsList.extend(self.soldier_secondary())   
        weaponsList.extend(self.soldier_melee())       
        weaponsList.extend(self.pyro_primary())        
        weaponsList.extend(self.pyro_secondary())      
        weaponsList.extend(self.pyro_melee())          
        weaponsList.extend(self.demo_primary())        
        weaponsList.extend(self.demo_secondary())      
        weaponsList.extend(self.demo_melee())          
        weaponsList.extend(self.heavy_primary())       
        weaponsList.extend(self.heavy_secondary())     
        weaponsList.extend(self.heavy_melee())         
        weaponsList.extend(self.medic_primary())       
        weaponsList.extend(self.medic_secondary())     
        weaponsList.extend(self.medic_melee())         
        weaponsList.extend(self.sniper_primary())      
        weaponsList.extend(self.sniper_secondary())    
        weaponsList.extend(self.sniper_melee())        
        weaponsList.extend(self.spy_primary())         
        weaponsList.extend(self.spy_secondary())       
        weaponsList.extend(self.spy_melee())           
        weaponsList.extend(self.spy_watch())

        return sorted(weaponsList)

#####################
# Archipelago Options
#####################

class TeamFortress2IncludeAlternateGameModes(Toggle):
    """
    Indicates whether or not to include Team Fortress 2 alternate game modes when generating objectives.
    """
    display_name = "Team Fortress 2 Include Alternate Game Modes"

class TeamFortress2IncludeMannVsMachine(Toggle):
    """
    Indicates whether or not to include Team Fortress 2 Mann vs Machine when generating objectives.
    """
    display_name = "Team Fortress 2 Include Mann vs Machine"