import requests
values = [#"Araxys Bio Harvester",
#"Black Market Butterfly",
"Blade of Chaos",
"Blade of Imperium",
"Bound",
"Caeruleus",
"Champions 2022",
"Champions 2023",
"Composite Knife",
"Crimsonbeast Hammer",
"Cryostasis Impact",
"VCT LOCK//IN Misericórdia",
"Equilibrium",
"Gaias Vengeance",
"Glitchpop axe",
"Idian Thorn Blade",
"Ignite fan",
"Ion Karambit",
"Lunas Descent",
"Magepunk Sparkswitch",
"Neo Frontier Axe",
"Neptune Anchor",
"No Limits Bat",
"Obsidiana",
"Onimaru Kunitsu",
"Powerfist",
"Reaver Karambit",
"Relic Stone Daggers",
"Reverie",
"Altitude Knuckle",
"Ruyi Staff",
"Sandswept Dagg",
"Hu Else",
"Hack",
"Strike",
"Gaia Wrath",
"RGX 11z Pro Firefly",
".SYS Melee",
"Blade of Serket",
"VALORANT GO! Vol. 1",
"Prime 2.0 Karambit",
"Prism III",
"Outpost",
"Magepunk Electroblade",
"Song Steel",
"Forsaken Ritual blade",
"Origin",
"Tethered Realms prosperity",
"K/TAC",
"Reaver",
"Luxe",
"Prism",
"Sovereign",
"Prime Axe",
"Kingdom",
"Elderflame",
"Oni",
"Hivemind",
"Glitchpop",
"Nebula",
"Spline",
"Smite",
"EGO",
"Gravitational Uranium Neuroblaster",
"Ruin",
"Singularity",
"Ion Energy",
"Winterwunderland candy cane",
"Blastx polymer knifetech",
"Blade of the Ruined King",
"Relic of the Sentinel",
"Artisan Foil",
"Waveform",
"Yoru’s Stylish Butterfly Comb",
"RGX 11Z Pro Blade",
"Catrina",
"Radiant Crisis 001 Baseball Bat",
"Velocity Karambit",
"Personal Administrative Melee Unit",
"Snowfall Wand",
"Soulstrife Scythe",
"Task Force 809 Knife",
"Terminus A Quo",
"Tilde",
"TitanMail Mace",
"Transition",
"Magepunk 2.0",
"Recon",
"Venturi",
"Xenohunter"]

url = "https://skinrating.up.railway.app/api/v1/skin"


for element in values:
    data = {'name': element, 'elo': 1500}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('Success!')
        print(response.json())
    else:
        print(f'Error: {response.status_code}')
        print(response.text)


    