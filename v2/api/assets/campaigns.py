#!/usr/bin/python2.7

from assets import monsters as monster_assets


#
#   This assets file is more complicated than others, since a lot of it drives
#   the business logic of campaigns, i.e. the rules and things that affect or
#   interact with lesser game assets.
#


#
#   default and baseline ("standard") campaign assets
#

default_timeline = [
    {"year": 0,  "settlement_event":    [{"handle": "core_first_day"}]              },
    {"year": 1,  "story_event":         [{"handle": "core_returning_survivors"}]    },
    {"year": 2,  "story_event":         [{"handle": "core_endless_screams"}]        },
    {"year": 3,  },
    {"year": 4,  "nemesis_encounter":   [{"name": "Nemesis Encounter: Butcher"}]    },
    {"year": 5,  "story_event":         [{"handle": "core_hands_of_heat"}]          },
    {"year": 6,  "story_event":         [{"handle": "core_armored_strangers"}]      },
    {"year": 7,  "story_event":         [{"handle": "core_phoenix_feather"}]        },
    {"year": 8,  },
    {"year": 9,  "nemesis_encounter":   [{"name": "Nemesis Encounter: King's Man"}] },
    {"year": 10, },
    {"year": 11, "story_event":         [{"handle": "core_regal_visit"}]            },
    {"year": 12, "story_event":         [{"handle": "core_conviction"}]             },
    {"year": 13, }, {"year": 14, }, {"year": 15, },
    {"year": 16, "nemesis_encounter":   [{"name": "Nemesis Encounter"}]             },
    {"year": 17, }, {"year": 18, },
    {"year": 19, "nemesis_encounter":   [{"name": "Nemesis Encounter"}]             },
    {"year": 20, "story_event":         [{"handle": "core_watched"}]                },
    {"year": 21, }, {"year": 22, },
    {"year": 23, "nemesis_encounter":   [{"name": "Nemesis Encounter: Level 3"}]    },
    {"year": 24, }, {"year": 25, },
    {"year": 26, "nemesis_encounter":   [{"name": "Nemesis Encounter: Watcher"}]    },
    {"year": 27, }, {"year": 28,}, {"year": 29,}, {"year": 30,}, {"year": 31,},
    {"year": 32, }, {"year": 33,}, {"year": 34,}, {"year": 35,}, {"year": 36,},
    {"year": 37, }, {"year": 38,}, {"year": 39,}, {"year": 40,},
]


default_survivor_attribute_milestones = {
    "hunt_xp": [
        {"values": [2,6,10,15], "handle": "core_age"},
    ],
    "Courage": [
        {"values": [3], "handle": "core_bold"},
        {"values": [9], "handle": "core_see_the_truth"},
    ],
    "Understanding": [
        {"values": [3], "handle": "core_insight"},
        {"values": [9], "handle": "core_white_secret"},
    ],
}


milestone_story_events = {
    "first_child": {
        "sort_order": 0,
        "name": "First child is born",
        "story_event": "Principle: New Life",
        "story_event_handle": "core_new_life",
    },
    "first_death": {
        "sort_order": 1,
        "name": "First time death count is updated",
        "story_event": "Principle: Death",
        "story_event_handle": "core_death",
        "add_to_timeline": 'int(self.settlement["death_count"]) >= 1',
    },
    "pop_15": {
        "sort_order": 2,
        "name": "Population reaches 15",
        "story_event": "Principle: Society",
        "story_event_handle": "core_society",
        "add_to_timeline": 'int(self.settlement["population"]) >= 15',
    },
    "innovations_5": {
        "sort_order": 3,
        "name": "Settlement has 5 innovations",
        "story_event": "Hooded Knight",
        "story_event_handle": "core_hooded_knight",
        "add_to_timeline": 'len(self.settlement["innovations"]) >= 5',
    },
    "innovations_8": {
        "sort_order": 2,
        "name": "Settlement has 8 innovations",
        "story_event": "Edged Tonometry",
        "story_event_handle": "ss_edged_tonometry",
        "add_to_timeline": 'len(self.settlement["innovations"]) >= 8',
    },
    "nemesis_defeat": {
        "sort_order": 6,
        "name": "Not Victorious against Nemesis",
        "story_event_handle": "core_game_over",
        "story_event": "Game Over",
    },
    "game_over": {
        "sort_order": 10,
        "name": "Population reaches 0",
        "story_event": "Game Over",
        "story_event_handle": "core_game_over",
        "add_to_timeline": 'int(self.settlement["population"]) == 0 and int(self.settlement["lantern_year"]) >= 1',
    },
}


campaign_definitions = {
    "people_of_the_lantern": {
        "default": True,
        "name": "People of the Lantern",
        "saviors": "1.3.1",
        "survival_actions": ["dodge","encourage","dash","surge"],
        "always_available": {
            "location": ["Lantern Hoard"],
            "innovation": ["Language"],
        },
        "forbidden": {
            "location": ["The Sun","Throne"],
            "innovation": ["Sun Language","Dragon Speech","Radiating Orb"],
        },
        "principles": ["new_life","death","society","conviction"],
        "milestones": ["first_child","first_death","pop_15","innovations_5","game_over"],
        "special_showdowns": ["watcher"],
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "survivor_attribute_milestones": default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "timeline": default_timeline,
        "settlement_sheet_init": {
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []}
        },
    },

    "the_green_knight": {
        "name": "The Green Knight",
        "subtitle": "A campaign following the 'People of the Lantern' timeline that includes all content required by the Green Knight Armor expansion.",
        "saviors": "1.3.1",
        "survival_actions": ["dodge","encourage","dash","surge"],
        "always_available": {
            "location": ["Lantern Hoard"],
            "innovation": ["Language"],
        },
        "forbidden": {
            "location": ["The Sun","Throne"],
            "innovation": ["Sun Language","Dragon Speech","Radiating Orb"],
        },
        "principles": ["new_life","death","society","conviction"],
        "milestones": ["first_child","first_death","pop_15","innovations_5","game_over"],
        "special_showdowns": ["watcher"],
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "survivor_attribute_milestones": default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "timeline": default_timeline,
        "settlement_sheet_init": {
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
            "expansions": ["green_knight_armor", "dung_beetle_knight","flower_knight","lion_knight","gorm"],
        },
    },

    "people_of_the_skull": {
        "name": "People of the Skull",
        "subtitle": "Always displays the alternate rules and endeavors on p.213 of the core game manual on the Campaign Summary view.",
        "saviors": "1.3.1",
        "survival_actions": ["dodge","encourage","dash","surge"],
        "always_available": {
            "location": ["Lantern Hoard"],
            "innovation": ["Language"],
        },
        "special_rules": [
            {"name": "People of the Skull",
             "desc": "Survivors can only place weapons and armor with the <b>bone</b> keyword in their gear grid. The people of the skull ignore the <b>Frail</b> rule.",
             "bg_color": "E3DAC9",
             "font_color": "333"},
            {"name": "People of the Skull",
             "desc": "When you name a survivor, if they have the word bone or skull in their name, in addition to +1 survival, players choose to gain +1 permanent accuracy, evasion, strength, luck or speed.",
             "bg_color": "E3DAC9",
             "font_color": "333"},
            {"name": "Black Skull",
             "desc": "If a weapon or armor is made with the Black Skull resource, a survivor may place it in their gear grid despite being iron.",
             "bg_color": "333",
             "font_color": "efefef"},
        ],
        "endeavors": {
            "Skull Ritual": {"cost": 1, "desc": "Costs one Skull resource. Nominate up to four survivors to consume the skull. They gain a permanent +1 to all their attributes."},
        },
        "principles": ["new_life","death","society","conviction"],
        "milestones": ["first_child","first_death","pop_15","innovations_5","game_over"],
        "special_showdowns": ["watcher"],
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "survivor_attribute_milestones": default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "timeline": default_timeline,
        "settlement_sheet_init": {
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
        },
    },

    "the_bloom_people": {
        "name": "The Bloom People",
        "saviors": "1.3.1",
        "survival_actions": ["dodge","encourage","dash","surge"],
        "always_available": {
            "location": ["Lantern Hoard"],
            "innovation": ["Language"],
        },
        "forbidden": {
            "abilities_and_impairments": ["Flower Addiction"],
            "quarries": ["flower_knight"],
        },
        "principles": ["new_life","death","society","conviction"],
        "milestones": ["first_child","first_death","pop_15","innovations_5","game_over"],
        "endeavors": {
            "Forest Run": {"cost": 1, "desc": "You may exchange any number of monster resources for that number of random Flower resources."},
        },
        "settlement_buff": "All survivors are born with +1 permanent luck, +1 permanent green affinity and -2 permanent red affinities.",
        "newborn_survivor": {
            "affinities": {"red": -2, "green": 1,},
            "Luck": 1,
        },
        "timeline": default_timeline,
        "special_showdowns": ["watcher"],
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "survivor_attribute_milestones": default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "settlement_sheet_init": {
            "storage": ["Sleeping Virus Flower"],
            "expansions": ["flower_knight"],
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
        },
    },

    "people_of_the_sun": {
        "name": "People of the Sun",
        "survivor_attribs": ["Purified","Sun Eater","Child of the Sun"],
        "survival_actions": ["dodge","overcharge","embolden"],
        "always_available": {
            "location": ["The Sun","Sacred Pool"],
            "innovation": ["Sun Language", "Umbilical Bank"],
        },
        "forbidden": {
            "location": ["Lantern Hoard"],
            "innovation": ["Leader", "Language"],
        },
        "principles": ["potsun_new_life","death","society","conviction"],
        "milestones": ["first_child","first_death","pop_15","innovations_8","nemesis_defeat","game_over"],
        "timeline": [
            {"year": 0,  "settlement_event":    [{"handle": "core_first_day"}]              },
            {"year": 1,  "story_event":         [{"handle": "ss_pool_and_sun"}]             },
            {"year": 2,  "story_event":         [{"handle": "core_endless_screams"}]        },
            {"year": 3,  },
            {"year": 4,  "story_event":         [{"handle": "ss_sun_dipping"}]              },
            {"year": 5,  "story_event":         [{"handle": "ss_great_sky_gift"}]           },
            {"year": 6,  },
            {"year": 7,  "story_event":         [{"handle": "core_phoenix_feather"}]        },
            {"year": 8,  }, {"year": 9, },
            {"year": 10, "story_event":         [{"handle": "ss_birth_of_color"}]           },
            {"year": 11, "story_event":         [{"handle": "core_conviction"}]             },
            {"year": 12, "story_event":         [{"handle": "ss_sun_dipping"}]              },
            {"year": 13, "story_event":         [{"handle": "ss_great_sky_gift"}]           },
            {"year": 14, }, {"year": 15, }, {"year": 16, }, {"year": 17, }, {"year": 18, },
            {"year": 19, "story_event":         [{"handle": "ss_sun_dipping"}]              },
            {"year": 20, "story_event":         [{"handle": "ss_final_gift"}]               },
            {"year": 21, "nemesis_encounter":   [{"name": "Nemesis Encounter: Kings Man Level 2"}]  },
            {"year": 22, "nemesis_encounter":   [{"name": "Nemesis Encounter: Butcher Level 3"}]    },
            {"year": 23, "nemesis_encounter":   [{"name": "Nemesis Encounter: Kings Man Level 3"}]  },
            {"year": 24, "nemesis_encounter":   [{"name": "Nemesis Encounter: The Hand Level 3"}]   },
            {"year": 25, "story_event":         [{"handle": "ss_great_devourer"}]           },
            {"year": 26,}, {"year": 27,}, {"year": 28,}, {"year": 29,}, {"year": 30,}, {"year": 31,},
            {"year": 32,}, {"year": 33,}, {"year": 34,}, {"year": 35,}, {"year": 36,},
            {"year": 37,}, {"year": 38,}, {"year": 39,}, {"year": 40,},
        ],
        "special_showdowns": ["ancient_sunstalker"],
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "survivor_attribute_milestones": default_survivor_attribute_milestones,
        "quarries": monster_assets.base_game_quarries,
        "settlement_sheet_init": {
            "expansions": ["sunstalker"],
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher"],
            "nemesis_encounters": {'butcher': []},
        },
    },

    "people_of_the_stars": {
        "name": "People of the Stars",
        "dragon_traits": "1.3.1",
        "survivor_attribs": ["Scar","Noble surname","Reincarnated surname"],
        "survival_actions": ["dodge","encourage","dash","surge"],
        "always_available": {
            "location": ["Throne"],
            "innovation": ["Dragon Speech","Radiating Orb"],
        },
        "forbidden": {
            "location": ["Lantern Hoard", "Dragon Armory"],
            "innovation": ["Language","Lantern Oven","Clan of Death","Family"],
        },
        "founder_epithet": "foundling",
        "replaced_story_events": {
            "Bold": "Awake",
            "Insight": "Awake",
        },
        "survivor_attribs": ["Scar","Noble surname","Reincarnated surname"],
        "special_rules": [
            {"name": "Removed Story Events", "desc": "If an event or card would cause you to add/trigger <b>Hands of Heat</b>, <b>Regal Visit</b>, <b>Armored Strangers</b>, <b>Watched</b>, or <b>Nemesis Encounter - Watcher</b>, do nothing instead.", "bg_color": "673AB7", "font_color": "FFF"},
        ],
        "principles": ["new_life","death","society","conviction"],
        "milestones": ["first_child","first_death","pop_15","game_over"],
        "timeline": [
            {"year": 0,  "settlement_event":    [{"handle": "core_first_day"}]              },
            {"year": 1,  "story_event":         [{"handle": "dk_foundlings"}]               },
            {"year": 2,  "story_event":         [{"handle": "core_endless_screams"}]        },
            {"year": 3,  },
            {"year": 4,  "nemesis_encounter":   [{"name": "Nemesis Encounter - Dragon King Human Lvl 1"}]   },
            {"year": 5,  "story_event":         [{"handle": "dk_midnights_children"}]     },
            {"year": 6,  },
            {"year": 7,  "story_event":         [{"handle": "core_phoenix_feather"}]        },
            {"year": 8,  },
            {"year": 9,  "nemesis_encounter":   [{"name": "Nemesis Encounter - Dragon King Human Lvl 2"}]   },
            {"year": 10, "story_event":         [{"handle": "dk_unveil_the_sky"}]           },
            {"year": 11, },
            {"year": 12, "story_event":         [{"handle": "core_conviction"}]             },
            {"year": 13, "nemesis_encounter":   [{"name": "Nemesis Encounter - Butcher Lvl 2"}] },
            {"year": 14, }, {"year": 15, },
            {"year": 16, "nemesis_encounter":   [{"name": "Nemesis Encounter - Lvl 2"}]     },
            {"year": 17, }, {"year": 18, },
            {"year": 19, "nemesis_encounter":   [{"name": "Nemesis Encounter - Dragon King Human Lvl 3"}]   },
            {"year": 20, "story_event":         [{"handle": "dk_tomb"}]                     },
            {"year": 21, }, {"year": 22, },
            {"year": 23, "nemesis_encounter":   [{"name": "Nemesis Encounter - Lvl 3"}]     },
            {"year": 24, },
            {"year": 25, "nemesis_encounter":   [{"handle": "dk_death_of_the_dragon_king"}] },
            {"year": 26, }, {"year": 27, }, {"year": 28, }, {"year": 29, }, {"year": 30, }, {"year": 31, },
            {"year": 32, }, {"year": 33, }, {"year": 34, }, {"year": 35, }, {"year": 36, },
            {"year": 37, }, {"year": 38, }, {"year": 39, }, {"year": 40, },
        ],
        "survivor_attribute_milestones": {
            "hunt_xp": [
                {"values": [2,6,10,15], "handle": "core_age"},
            ],
            "Courage": [
                {"values": [3], "handle": "dk_awake"},
                {"values": [9], "handle": "core_see_the_truth"},
            ],
            "Understanding": [
                {"values": [3], "handle": "dk_awake"},
                {"values": [9], "handle": "core_white_secret"},
            ],
        },
        "quarries": monster_assets.base_game_quarries,
        "special_showdowns": ["the_tyrant","dragon_king_lv3"],
        "nemesis_monsters": ["butcher","kings_man","the_hand"],
        "settlement_sheet_init": {
            "expansions": ["dragon_king"],
            "quarries": ["white_lion"],
            "nemesis_monsters": ["butcher","kings_man","the_hand"],
            "nemesis_encounters": {"butcher":[1], "kings_man":[1], "the_hand":[1]},
        },
    },
}

