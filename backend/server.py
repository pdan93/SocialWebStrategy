from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import twitter

api = twitter.Api(consumer_key='lt55UgMDpa2YQ02goLjCzn6EP',
                  consumer_secret='Zet0ja2fyNLvvEZp0v1LifT1pRtlUkxG7YqrG15naFIyWBEwMD',
                  access_token_key='183581455-Ze5AGzj8j7uc8UyaZmu12s2rx9jganamFvOixpfo',
                  access_token_secret='EHElVjh8aywRwGBr1gVbp5lsQUP2RpXopNGeEpnizyI8u')
import json
from pprint import pprint

cachedTwitterUsers = {
    "HamillHimself": {
        "image": "http://pbs.twimg.com/profile_images/822714806117363712/4Q-zC2vR_normal.jpg",
        "followers": ["http://pbs.twimg.com/profile_images/489587192692346880/JTzsjAUU_normal.jpeg",
                      "http://pbs.twimg.com/profile_images/686340861496541184/AERaA2hT_normal.jpg",
                      "http://pbs.twimg.com/profile_images/867559602853904384/81S_Y1jr_normal.jpg",
                      "http://pbs.twimg.com/profile_images/2053042113/MonkeyRiver_gif_200x200_crop_upscale_q85_normal.jpg",
                      "http://pbs.twimg.com/profile_images/737658149726003200/K6Dsdf9k_normal.jpg",
                      "http://pbs.twimg.com/profile_images/864247471886741505/P2i_nF7I_normal.jpg",
                      "http://pbs.twimg.com/profile_images/844561070870183936/_poh20Qt_normal.jpg",
                      "http://pbs.twimg.com/profile_images/854725589877612544/retvrcnI_normal.jpg",
                      "http://pbs.twimg.com/profile_images/854802637526585344/R27tECEQ_normal.jpg",
                      "http://pbs.twimg.com/profile_images/616619172139823104/wESXkmbX_normal.jpg",
                      "http://pbs.twimg.com/profile_images/694029423855554560/HCgxl9pA_normal.jpg",
                      "http://pbs.twimg.com/profile_images/867086244269961217/Aw2-rWpe_normal.jpg",
                      "http://pbs.twimg.com/profile_images/729666545094303744/0hTu_MZs_normal.jpg",
                      "http://pbs.twimg.com/profile_images/859946933108039680/6W5UcpRg_normal.jpg",
                      "http://pbs.twimg.com/profile_images/749694550332014592/UZBBHbS6_normal.jpg"],
        "name": "Mark Hamill",
        "followers_count": 1814887
    },
    "starwars": {
        "image": "http://pbs.twimg.com/profile_images/783419325830934528/7Ad49etX_normal.jpg",
        "followers": ["http://pbs.twimg.com/profile_images/823053194859343872/MmIE-fhI_normal.jpg",
                      "http://pbs.twimg.com/profile_images/543894430156337152/jF2H3Z7__normal.jpeg",
                      "http://pbs.twimg.com/profile_images/858713043227656194/JaT15_7z_normal.jpg",
                      "http://pbs.twimg.com/profile_images/855823431983607809/QIN_QUmc_normal.jpg",
                      "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                      "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                      "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                      "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                      "http://pbs.twimg.com/profile_images/869291208782127104/QlCJbdYS_normal.jpg",
                      "http://pbs.twimg.com/profile_images/823252347581267968/K6gn2QDT_normal.jpg",
                      "http://pbs.twimg.com/profile_images/869291275828252678/vYsM6Vvh_normal.jpg",
                      "http://pbs.twimg.com/profile_images/760206613596803074/RHTPx0pO_normal.jpg",
                      "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                      "http://pbs.twimg.com/profile_images/680976058884206592/XOt6FvxY_normal.jpg",
                      "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png"],
        "name": "Star Wars",
        "followers_count": 3254261
    }
}

testClients = [
    {"status": "hex_selected", "pair": 1, "data": {"lifePerHex": 180792, "name": "Star Wars",
                                                   "image": "http://pbs.twimg.com/profile_images/783419325830934528/7Ad49etX_normal.jpg",
                                                   "gameboard": {"hexagons": [{"life": 0, "surroundings": [1, 4],
                                                                               "image": "http://pbs.twimg.com/profile_images/823053194859343872/MmIE-fhI_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 7, "x": 20},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [0, 4, 5],
                                                                               "image": "http://pbs.twimg.com/profile_images/543894430156337152/jF2H3Z7__normal.jpeg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 21.3, "x": 20},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [7, 8, 3],
                                                                               "image": "http://pbs.twimg.com/profile_images/858713043227656194/JaT15_7z_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 64.2, "x": 20},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [2, 8],
                                                                               "image": "http://pbs.twimg.com/profile_images/855823431983607809/QIN_QUmc_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 78.5, "x": 20},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [0,
                                                                                                                     1,
                                                                                                                     5,
                                                                                                                     9,
                                                                                                                     10],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 14.3,
                                                                                                        "x": 27.5},
                                                                                                    "dragging": False},
                                                                              {"life": 180792,
                                                                               "surroundings": [1, 4, 6, 10, 11],
                                                                               "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                               "selected": True, "mark": "",
                                                                               "player": 1,
                                                                               "position": {"y": 28.6, "x": 27.5},
                                                                               "dragging": False}, {"life": 180792,
                                                                                                    "surroundings": [5,
                                                                                                                     7,
                                                                                                                     11,
                                                                                                                     12],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 1,
                                                                                                    "position": {
                                                                                                        "y": 42.9,
                                                                                                        "x": 27.5},
                                                                                                    "dragging": False},
                                                                              {"life": 180792,
                                                                               "surroundings": [2, 6, 8, 12, 13],
                                                                               "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                               "selected": True, "mark": "",
                                                                               "player": 1,
                                                                               "position": {"y": 57.2, "x": 27.5},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [2,
                                                                                                                     3,
                                                                                                                     7,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/869291208782127104/QlCJbdYS_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 71.5,
                                                                                                        "x": 27.5},
                                                                                                    "dragging": False},
                                                                              {"life": 180792,
                                                                               "surroundings": [4, 10, 24, 25, 26, 27,
                                                                                                28, 29],
                                                                               "image": "http://pbs.twimg.com/profile_images/823252347581267968/K6gn2QDT_normal.jpg",
                                                                               "selected": True, "mark": "",
                                                                               "player": 1,
                                                                               "position": {"y": 7, "x": 35},
                                                                               "dragging": False}, {"life": 180792,
                                                                                                    "surroundings": [9,
                                                                                                                     4,
                                                                                                                     5,
                                                                                                                     24,
                                                                                                                     25,
                                                                                                                     26,
                                                                                                                     27,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/869291275828252678/vYsM6Vvh_normal.jpg",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 1,
                                                                                                    "position": {
                                                                                                        "y": 21.3,
                                                                                                        "x": 35},
                                                                                                    "dragging": False},
                                                                              {"life": 180792,
                                                                               "surroundings": [5, 6, 10, 12, 24, 25,
                                                                                                26, 27, 28, 29],
                                                                               "image": "http://pbs.twimg.com/profile_images/760206613596803074/RHTPx0pO_normal.jpg",
                                                                               "selected": True, "mark": "",
                                                                               "player": 1,
                                                                               "position": {"y": 35.6, "x": 35},
                                                                               "dragging": False}, {"life": 180792,
                                                                                                    "surroundings": [6,
                                                                                                                     7,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     24,
                                                                                                                     25,
                                                                                                                     26,
                                                                                                                     27,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 1,
                                                                                                    "position": {
                                                                                                        "y": 49.9,
                                                                                                        "x": 35},
                                                                                                    "dragging": False},
                                                                              {"life": 180792,
                                                                               "surroundings": [7, 8, 12, 14, 24, 25,
                                                                                                26, 27, 28, 29],
                                                                               "image": "http://pbs.twimg.com/profile_images/680976058884206592/XOt6FvxY_normal.jpg",
                                                                               "selected": True, "mark": "",
                                                                               "player": 1,
                                                                               "position": {"y": 64.2, "x": 35},
                                                                               "dragging": False}, {"life": 180792,
                                                                                                    "surroundings": [8,
                                                                                                                     13,
                                                                                                                     24,
                                                                                                                     25,
                                                                                                                     26,
                                                                                                                     27,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 1,
                                                                                                    "position": {
                                                                                                        "y": 78.5,
                                                                                                        "x": 35},
                                                                                                    "dragging": False},
                                                                              {"life": 0, "surroundings": [16, 19],
                                                                               "image": "http://pbs.twimg.com/profile_images/489587192692346880/JTzsjAUU_normal.jpeg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 7, "x": 70},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [15, 19, 20],
                                                                               "image": "http://pbs.twimg.com/profile_images/686340861496541184/AERaA2hT_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 21.3, "x": 70},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [18, 22, 23],
                                                                               "image": "http://pbs.twimg.com/profile_images/867559602853904384/81S_Y1jr_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 64.2, "x": 70},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [17, 23],
                                                                               "image": "http://pbs.twimg.com/profile_images/2053042113/MonkeyRiver_gif_200x200_crop_upscale_q85_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 78.5, "x": 70},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [15,
                                                                                                                     16,
                                                                                                                     20,
                                                                                                                     24,
                                                                                                                     25],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/737658149726003200/K6Dsdf9k_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 14.3,
                                                                                                        "x": 62.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [16, 19, 21, 25, 26],
                                                                               "image": "http://pbs.twimg.com/profile_images/864247471886741505/P2i_nF7I_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 28.6, "x": 62.5},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [20,
                                                                                                                     22,
                                                                                                                     26,
                                                                                                                     27],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/844561070870183936/_poh20Qt_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 42.9,
                                                                                                        "x": 62.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [17, 21, 23, 27, 28],
                                                                               "image": "http://pbs.twimg.com/profile_images/854725589877612544/retvrcnI_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 57.2, "x": 62.5},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [17,
                                                                                                                     18,
                                                                                                                     22,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/854802637526585344/R27tECEQ_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 71.5,
                                                                                                        "x": 62.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [19, 25, 9, 10, 11, 12,
                                                                                                13, 14],
                                                                               "image": "http://pbs.twimg.com/profile_images/616619172139823104/wESXkmbX_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 7, "x": 55},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [19,
                                                                                                                     20,
                                                                                                                     24,
                                                                                                                     26,
                                                                                                                     9,
                                                                                                                     10,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/694029423855554560/HCgxl9pA_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 21.3,
                                                                                                        "x": 55},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [20, 21, 25, 27, 9, 10,
                                                                                                11, 12, 13, 14],
                                                                               "image": "http://pbs.twimg.com/profile_images/867086244269961217/Aw2-rWpe_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 35.6, "x": 55},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [21,
                                                                                                                     22,
                                                                                                                     26,
                                                                                                                     28,
                                                                                                                     9,
                                                                                                                     10,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/729666545094303744/0hTu_MZs_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 49.9,
                                                                                                        "x": 55},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [22, 23, 27, 29, 9, 10,
                                                                                                11, 12, 13, 14],
                                                                               "image": "http://pbs.twimg.com/profile_images/859946933108039680/6W5UcpRg_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 64.2, "x": 55},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [23,
                                                                                                                     28,
                                                                                                                     9,
                                                                                                                     10,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/749694550332014592/UZBBHbS6_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 78.5,
                                                                                                        "x": 55},
                                                                                                    "dragging": False}],
                                                                 "playerLife": 1627133}, "player": 1,
                                                   "followers_count": 3254261, "followers": [
            "http://pbs.twimg.com/profile_images/823053194859343872/MmIE-fhI_normal.jpg",
            "http://pbs.twimg.com/profile_images/543894430156337152/jF2H3Z7__normal.jpeg",
            "http://pbs.twimg.com/profile_images/858713043227656194/JaT15_7z_normal.jpg",
            "http://pbs.twimg.com/profile_images/855823431983607809/QIN_QUmc_normal.jpg",
            "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
            "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
            "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
            "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
            "http://pbs.twimg.com/profile_images/869291208782127104/QlCJbdYS_normal.jpg",
            "http://pbs.twimg.com/profile_images/823252347581267968/K6gn2QDT_normal.jpg",
            "http://pbs.twimg.com/profile_images/869291275828252678/vYsM6Vvh_normal.jpg",
            "http://pbs.twimg.com/profile_images/760206613596803074/RHTPx0pO_normal.jpg",
            "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
            "http://pbs.twimg.com/profile_images/680976058884206592/XOt6FvxY_normal.jpg",
            "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png"]}},
    {"status": "hex_selected", "pair": 0, "data": {"lifePerHex": 113430, "name": "Mark Hamill",
                                                   "image": "http://pbs.twimg.com/profile_images/822714806117363712/4Q-zC2vR_normal.jpg",
                                                   "gameboard": {"hexagons": [{"life": 0, "surroundings": [1, 4],
                                                                               "image": "http://pbs.twimg.com/profile_images/823053194859343872/MmIE-fhI_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 7, "x": 20},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [0, 4, 5],
                                                                               "image": "http://pbs.twimg.com/profile_images/543894430156337152/jF2H3Z7__normal.jpeg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 21.3, "x": 20},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [7, 8, 3],
                                                                               "image": "http://pbs.twimg.com/profile_images/858713043227656194/JaT15_7z_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 64.2, "x": 20},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [2, 8],
                                                                               "image": "http://pbs.twimg.com/profile_images/855823431983607809/QIN_QUmc_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 78.5, "x": 20},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [0,
                                                                                                                     1,
                                                                                                                     5,
                                                                                                                     9,
                                                                                                                     10],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 14.3,
                                                                                                        "x": 27.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [1, 4, 6, 10, 11],
                                                                               "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 28.6, "x": 27.5},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [5,
                                                                                                                     7,
                                                                                                                     11,
                                                                                                                     12],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 42.9,
                                                                                                        "x": 27.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [2, 6, 8, 12, 13],
                                                                               "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 57.2, "x": 27.5},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [2,
                                                                                                                     3,
                                                                                                                     7,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/869291208782127104/QlCJbdYS_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 71.5,
                                                                                                        "x": 27.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [4, 10, 24, 25, 26, 27,
                                                                                                28, 29],
                                                                               "image": "http://pbs.twimg.com/profile_images/823252347581267968/K6gn2QDT_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 7, "x": 35},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [9,
                                                                                                                     4,
                                                                                                                     5,
                                                                                                                     24,
                                                                                                                     25,
                                                                                                                     26,
                                                                                                                     27,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/869291275828252678/vYsM6Vvh_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 21.3,
                                                                                                        "x": 35},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [5, 6, 10, 12, 24, 25,
                                                                                                26, 27, 28, 29],
                                                                               "image": "http://pbs.twimg.com/profile_images/760206613596803074/RHTPx0pO_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 35.6, "x": 35},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [6,
                                                                                                                     7,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     24,
                                                                                                                     25,
                                                                                                                     26,
                                                                                                                     27,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 49.9,
                                                                                                        "x": 35},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [7, 8, 12, 14, 24, 25,
                                                                                                26, 27, 28, 29],
                                                                               "image": "http://pbs.twimg.com/profile_images/680976058884206592/XOt6FvxY_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 64.2, "x": 35},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [8,
                                                                                                                     13,
                                                                                                                     24,
                                                                                                                     25,
                                                                                                                     26,
                                                                                                                     27,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 78.5,
                                                                                                        "x": 35},
                                                                                                    "dragging": False},
                                                                              {"life": 0, "surroundings": [16, 19],
                                                                               "image": "http://pbs.twimg.com/profile_images/489587192692346880/JTzsjAUU_normal.jpeg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 7, "x": 70},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [15, 19, 20],
                                                                               "image": "http://pbs.twimg.com/profile_images/686340861496541184/AERaA2hT_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 21.3, "x": 70},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [18, 22, 23],
                                                                               "image": "http://pbs.twimg.com/profile_images/867559602853904384/81S_Y1jr_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 64.2, "x": 70},
                                                                               "dragging": False},
                                                                              {"life": 0, "surroundings": [17, 23],
                                                                               "image": "http://pbs.twimg.com/profile_images/2053042113/MonkeyRiver_gif_200x200_crop_upscale_q85_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 78.5, "x": 70},
                                                                               "dragging": False}, {"life": 113430,
                                                                                                    "surroundings": [15,
                                                                                                                     16,
                                                                                                                     20,
                                                                                                                     24,
                                                                                                                     25],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/737658149726003200/K6Dsdf9k_normal.jpg",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 2,
                                                                                                    "position": {
                                                                                                        "y": 14.3,
                                                                                                        "x": 62.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [16, 19, 21, 25, 26],
                                                                               "image": "http://pbs.twimg.com/profile_images/864247471886741505/P2i_nF7I_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 28.6, "x": 62.5},
                                                                               "dragging": False}, {"life": 0,
                                                                                                    "surroundings": [20,
                                                                                                                     22,
                                                                                                                     26,
                                                                                                                     27],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/844561070870183936/_poh20Qt_normal.jpg",
                                                                                                    "selected": False,
                                                                                                    "mark": "",
                                                                                                    "player": 0,
                                                                                                    "position": {
                                                                                                        "y": 42.9,
                                                                                                        "x": 62.5},
                                                                                                    "dragging": False},
                                                                              {"life": 0,
                                                                               "surroundings": [17, 21, 23, 27, 28],
                                                                               "image": "http://pbs.twimg.com/profile_images/854725589877612544/retvrcnI_normal.jpg",
                                                                               "selected": False, "mark": "",
                                                                               "player": 0,
                                                                               "position": {"y": 57.2, "x": 62.5},
                                                                               "dragging": False}, {"life": 113430,
                                                                                                    "surroundings": [17,
                                                                                                                     18,
                                                                                                                     22,
                                                                                                                     28,
                                                                                                                     29],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/854802637526585344/R27tECEQ_normal.jpg",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 2,
                                                                                                    "position": {
                                                                                                        "y": 71.5,
                                                                                                        "x": 62.5},
                                                                                                    "dragging": False},
                                                                              {"life": 113430,
                                                                               "surroundings": [19, 25, 9, 10, 11, 12,
                                                                                                13, 14],
                                                                               "image": "http://pbs.twimg.com/profile_images/616619172139823104/wESXkmbX_normal.jpg",
                                                                               "selected": True, "mark": "",
                                                                               "player": 2,
                                                                               "position": {"y": 7, "x": 55},
                                                                               "dragging": False}, {"life": 113430,
                                                                                                    "surroundings": [19,
                                                                                                                     20,
                                                                                                                     24,
                                                                                                                     26,
                                                                                                                     9,
                                                                                                                     10,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/694029423855554560/HCgxl9pA_normal.jpg",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 2,
                                                                                                    "position": {
                                                                                                        "y": 21.3,
                                                                                                        "x": 55},
                                                                                                    "dragging": False},
                                                                              {"life": 113430,
                                                                               "surroundings": [20, 21, 25, 27, 9, 10,
                                                                                                11, 12, 13, 14],
                                                                               "image": "http://pbs.twimg.com/profile_images/867086244269961217/Aw2-rWpe_normal.jpg",
                                                                               "selected": True, "mark": "",
                                                                               "player": 2,
                                                                               "position": {"y": 35.6, "x": 55},
                                                                               "dragging": False}, {"life": 113430,
                                                                                                    "surroundings": [21,
                                                                                                                     22,
                                                                                                                     26,
                                                                                                                     28,
                                                                                                                     9,
                                                                                                                     10,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/729666545094303744/0hTu_MZs_normal.jpg",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 2,
                                                                                                    "position": {
                                                                                                        "y": 49.9,
                                                                                                        "x": 55},
                                                                                                    "dragging": False},
                                                                              {"life": 113430,
                                                                               "surroundings": [22, 23, 27, 29, 9, 10,
                                                                                                11, 12, 13, 14],
                                                                               "image": "http://pbs.twimg.com/profile_images/859946933108039680/6W5UcpRg_normal.jpg",
                                                                               "selected": True, "mark": "",
                                                                               "player": 2,
                                                                               "position": {"y": 64.2, "x": 55},
                                                                               "dragging": False}, {"life": 113430,
                                                                                                    "surroundings": [23,
                                                                                                                     28,
                                                                                                                     9,
                                                                                                                     10,
                                                                                                                     11,
                                                                                                                     12,
                                                                                                                     13,
                                                                                                                     14],
                                                                                                    "image": "http://pbs.twimg.com/profile_images/749694550332014592/UZBBHbS6_normal.jpg",
                                                                                                    "selected": True,
                                                                                                    "mark": "",
                                                                                                    "player": 2,
                                                                                                    "position": {
                                                                                                        "y": 78.5,
                                                                                                        "x": 55},
                                                                                                    "dragging": False}],
                                                                 "playerLife": 107447}, "player": 2,
                                                   "followers_count": 1814887, "followers": [
            "http://pbs.twimg.com/profile_images/489587192692346880/JTzsjAUU_normal.jpeg",
            "http://pbs.twimg.com/profile_images/686340861496541184/AERaA2hT_normal.jpg",
            "http://pbs.twimg.com/profile_images/867559602853904384/81S_Y1jr_normal.jpg",
            "http://pbs.twimg.com/profile_images/2053042113/MonkeyRiver_gif_200x200_crop_upscale_q85_normal.jpg",
            "http://pbs.twimg.com/profile_images/737658149726003200/K6Dsdf9k_normal.jpg",
            "http://pbs.twimg.com/profile_images/864247471886741505/P2i_nF7I_normal.jpg",
            "http://pbs.twimg.com/profile_images/844561070870183936/_poh20Qt_normal.jpg",
            "http://pbs.twimg.com/profile_images/854725589877612544/retvrcnI_normal.jpg",
            "http://pbs.twimg.com/profile_images/854802637526585344/R27tECEQ_normal.jpg",
            "http://pbs.twimg.com/profile_images/616619172139823104/wESXkmbX_normal.jpg",
            "http://pbs.twimg.com/profile_images/694029423855554560/HCgxl9pA_normal.jpg",
            "http://pbs.twimg.com/profile_images/867086244269961217/Aw2-rWpe_normal.jpg",
            "http://pbs.twimg.com/profile_images/729666545094303744/0hTu_MZs_normal.jpg",
            "http://pbs.twimg.com/profile_images/859946933108039680/6W5UcpRg_normal.jpg",
            "http://pbs.twimg.com/profile_images/749694550332014592/UZBBHbS6_normal.jpg"]}}
]

clients = []
clientsData = []
testing = 0


class SimpleEcho(WebSocket):
    def testDirectTo(self):
        c1 = None
        c2 = None
        i = 0
        for client in clients:
            if clientsData[i]["status"] == "zero":
                if c1 is None:
                    c1 = i
                else:
                    c2 = i
                    break
            i += 1
        print "HERE", c1, c2
        if c1 is not None and c2 is not None:
            clientsData[c1] = testClients[0]
            clientsData[c1]["pair"] = c2
            clientsData[c2] = testClients[1]
            clientsData[c2]["pair"] = c1
            clients[c1].sendMessage(u'' + json.dumps({
                "type": "DIRECTLY_TO",
                "data": {
                    "mine": clientsData[c1]["data"],
                    "his": clientsData[c2]["data"],
                    "player": 1
                }
            }))
            clients[c2].sendMessage(u'' + json.dumps({
                "type": "DIRECTLY_TO",
                "data": {
                    "mine": clientsData[c2]["data"],
                    "his": clientsData[c1]["data"],
                    "player": 2
                }
            }))
            clientsData[c1]["status"] = "game_phase"
            clientsData[c2]["status"] = "game_phase"

    def getTwitterUser(self, name, player):
        if name in cachedTwitterUsers.keys():
            user_data = {"player": player}
            user_data.update(cachedTwitterUsers[name])
        else:
            user = api.GetUser(screen_name=name)
            followers = api.GetFollowers(screen_name=name, total_count=15)

            followers_data = []
            for follower in followers:
                followers_data.append(follower.profile_image_url)
            user_data = {
                "player": player,
                "name": user.name,
                "image": user.profile_image_url,
                "followers_count": user.followers_count,
                "followers": followers_data
            }
        clientsData[self.getClientIndex()]["status"] = "selected_user"
        clientsData[self.getClientIndex()]["data"] = user_data
        return user_data

    def getClientPlayer(self):
        i = 0
        for c in clients:
            if c == self:
                return (i % 2) + 1
            i += 1
        return 1

    def getClientIndex(self):
        i = 0
        for c in clients:
            if c == self:
                return i
            i += 1
        return 0

    def verifyForMatchup(self):
        c1 = None
        c1i = 0
        c2 = None
        c2i = 0
        i = 0
        for client in clients:
            if clientsData[i]["status"] == "selected_user":
                if c1 is None:
                    c1 = clients[i]
                    c1i = i
                else:
                    c2 = clients[i]
                    c2i = i
                    break
            i += 1
        if c1 and c2:
            c1.sendMessage(u'' + json.dumps({
                "type": "SET_OPPONENT",
                "data": clientsData[c2i]["data"]
            }))
            c2.sendMessage(u'' + json.dumps({
                "type": "SET_OPPONENT",
                "data": clientsData[c1i]["data"]
            }))
            clientsData[c1i]["status"] = "waiting_hex_selection"
            clientsData[c1i]["pair"] = c2i
            clientsData[c2i]["status"] = "waiting_hex_selection"
            clientsData[c2i]["pair"] = c1i
            # pprint(clientsData, indent=4)


    def verifyHexSelected(self):
        myIndex = self.getClientIndex()
        pairIndex = clientsData[myIndex]["pair"]
        if clientsData[pairIndex]["status"] == "hex_selected":
            self.sendMessage(u'' + json.dumps({
                "type": "OPPONENT_SELECTED",
                "data": clientsData[pairIndex]["data"]["gameboard"]
            }))
            clients[pairIndex].sendMessage(u'' + json.dumps({
                "type": "OPPONENT_SELECTED",
                "data": clientsData[myIndex]["data"]["gameboard"]
            }))
            clientsData[myIndex]["status"] = "game_phase"
            clientsData[pairIndex]["status"] = "game_phase"


    def verifyEndGame(self, c1, c2):
        response = {}
        if clientsData[c1]["attack"]["playerLife"] == 0:
            response = {
                "type": "GAME_OVER",
                "data": "Player "+str(clientsData[c2]["attack"]["me"])+" won!"
            }
        if clientsData[c2]["attack"]["playerLife"] == 0:
            response = {
                "type": "GAME_OVER",
                "data": "Player "+str(clientsData[c1]["attack"]["me"])+" won!"
            }
        if response:
            print "GAME OVEEEEEEERRRRRRRRRRRR"
            clients[c1].sendMessage(u'' + json.dumps(response))
            clients[c2].sendMessage(u'' + json.dumps(response))

    def verifyGamePhase(self):
        pairIndex = self.getClientIndex()
        myIndex = clientsData[pairIndex]["pair"]
        response = {}
        #import pdb; pdb.set_trace()
        if clientsData[myIndex]["status"] == "attacking" or clientsData[myIndex]["status"] == "defending":
            my = clientsData[myIndex]["attack"]
            pair = clientsData[pairIndex]["attack"]
            hexas = my["hexagons"]
            for hex in hexas:
                hex["mark"] = ''
            if clientsData[myIndex]["status"] == "attacking" and clientsData[pairIndex]["status"] == "attacking":
                if my["attacked"] == pair["attacker"] or my["attacker"] == pair["attacked"]:
                    #classssssssssssssssssssssssshhhhhhhhhhhh
                    if hexas[my["attacker"]]["life"] > hexas[pair["attacker"]]["life"]:
                        hexas[my["attacker"]]["life"] -= hexas[pair["attacker"]]["life"]
                        if my["playerLife"] > my["lifePerHex"]:
                            newLife = my["lifePerHex"]
                            my["playerLife"] -= my["lifePerHex"]
                        else:
                            newLife = my["playerLife"]
                            my["playerLife"] = 1
                        hexas[pair["attacker"]]["life"] = newLife
                        hexas[pair["attacker"]]["player"] = my["me"]
                    else:
                        hexas[pair["attacker"]]["life"] -= hexas[my["attacker"]]["life"]
                        if pair["playerLife"] > pair["lifePerHex"]:
                            newLife = pair["lifePerHex"]
                            pair["playerLife"] -= pair["lifePerHex"]
                        else:
                            newLife = pair["playerLife"]
                            pair["playerLife"] = 1
                        hexas[my["attacker"]]["life"] = newLife
                        hexas[my["attacker"]]["player"] = pair["me"]
                    response = {
                        "type": "1_STEP_PHASE_CLASH",
                        "data": {
                            "attacker1": my["attacker"],
                            "attacker2": pair["attacker"],
                            "attacked1": my["attacked"],
                            "attacked2": pair["attacked"],
                            "hexagons": hexas,
                            "player" + str(my["me"]) + "Life": my["playerLife"],
                            "player" + str(pair["me"]) + "Life": pair["playerLife"],
                        }
                    }
                elif my["directAttack"]==0 and pair["directAttack"]==0:
                    # import pdb;pdb.set_trace()
                    self.attack_process(my,pair,hexas)
                    self.attack_process(pair,my,hexas)
                    response = {
                        "type": "2_STEP_PHASE",
                        "data": {
                            "STEP_1": {
                                "attacker": my["attacker"],
                                "attacked": my["attacked"],
                                "hexagons": hexas,
                                "playerLife": my["playerLife"],
                                "player": my["me"],
                                "directAttack": 0
                            },
                            "STEP_2": {
                                "attacker": pair["attacker"],
                                "attacked": pair["attacked"],
                                "hexagons": hexas,
                                "playerLife": pair["playerLife"],
                                "player": pair["me"],
                                "directAttack": 0
                            }
                        }
                    }
                else:
                    if my["directAttack"]==1 and pair["directAttack"]==0:
                        self.attack_process(pair,my,hexas)
                        if hexas[my["attacker"]]["life"] > pair["playerLife"]:
                            pair["playerLife"] = 0
                        else:
                            pair["playerLife"] -= hexas[my["attacker"]]["life"]
                    if pair["directAttack"]==1 and my["directAttack"]==0:
                        self.attack_process(my,pair,hexas)
                        if hexas[pair["attacker"]]["life"] > my["playerLife"]:
                            my["playerLife"] = 0
                        else:
                            my["playerLife"] -= hexas[pair["attacker"]]["life"]
                    if pair["directAttack"]==1 and my["directAttack"]==1:
                        if hexas[pair["attacker"]]["life"] > my["playerLife"]:
                            my["playerLife"] = 0
                        else:
                            my["playerLife"] -= hexas[pair["attacker"]]["life"]
                        if hexas[my["attacker"]]["life"] > pair["playerLife"]:
                            pair["playerLife"] = 0
                        else:
                            pair["playerLife"] -= hexas[my["attacker"]]["life"]
                    response = {
                        "type": "2_STEP_PHASE",
                        "data": {
                            "STEP_1": {
                                "attacker": my["attacker"],
                                "attacked": my["attacked"],
                                "hexagons": hexas,
                                "playerLife": my["playerLife"],
                                "otherPlayerLife": pair["playerLife"],
                                "player": my["me"],
                                "directAttack": my["directAttack"]
                            },
                            "STEP_2": {
                                "attacker": pair["attacker"],
                                "attacked": pair["attacked"],
                                "hexagons": hexas,
                                "playerLife": pair["playerLife"],
                                "otherPlayerLife": my["playerLife"],
                                "player": pair["me"],
                                "directAttack": pair["directAttack"]
                            }
                        }
                    }


            elif clientsData[myIndex]["status"] == "attacking" and clientsData[pairIndex]["status"] == "defending":
                response = self.defense_process(my, pair, hexas)
            elif clientsData[myIndex]["status"] == "defending" and clientsData[pairIndex]["status"] == "attacking":
                response = self.defense_process(pair, my, hexas)

            clients[myIndex].sendMessage(u'' + json.dumps(response))
            clients[pairIndex].sendMessage(u'' + json.dumps(response))
            clientsData[myIndex]["status"] = "game_phase"
            clientsData[pairIndex]["status"] = "game_phase"
            self.verifyEndGame(myIndex,pairIndex)

    def attack_process(self, my, pair, hexas):
        if hexas[my["attacker"]]["life"] > hexas[my["attacked"]]["life"]:
            if my["playerLife"] > my["lifePerHex"]:
                newLife = my["lifePerHex"]
                my["playerLife"] -= my["lifePerHex"]
            else:
                newLife = my["playerLife"]
                my["playerLife"] = 1
            hexas[my["attacked"]]["life"] = newLife
            hexas[my["attacked"]]["player"] = my["me"]
        else:
            hexas[my["attacked"]]["life"] -= hexas[my["attacker"]]["life"]

    def defense_process(self, my, pair, hexas):
        attack = hexas[my["attacker"]]["life"]
        if my["attacked"] in pair["defenders"]:
            attackEach = round(attack / len(pair["defenders"]))
            for defInd in pair["defenders"]:
                if hexas[defInd]["life"] > attackEach:
                    hexas[defInd]["life"] -= attackEach
                else:
                    if my["playerLife"] > my["lifePerHex"]:
                        newLife = my["lifePerHex"]
                        my["playerLife"] -= my["lifePerHex"]
                    else:
                        newLife = my["playerLife"]
                        my["playerLife"] = 1
                    hexas[defInd]["life"] = newLife
                    hexas[defInd]["player"] = my["me"]
        else:
            defInd = my["attacked"]
            if hexas[defInd]["life"] > attack:
                hexas[defInd]["life"] -= attack
            else:
                if my["playerLife"] > my["lifePerHex"]:
                    newLife = my["lifePerHex"]
                    my["playerLife"] -= my["lifePerHex"]
                else:
                    newLife = my["playerLife"]
                    my["playerLife"] = 1
                hexas[defInd]["life"] = newLife
                hexas[defInd]["player"] = my["me"]
        response = {
            "type": "1_STEP_ATTACK_DEFENSE",
            "data": {
                "attacker": my["attacker"],
                "attacked": my["attacked"],
                "defenders": pair["defenders"],
                "hexagons": hexas,
                "playerLife": my["playerLife"],
                "player": my["me"]
            }
        }
        return response

    def handleMessage(self):
        data = json.loads(self.data)
        if data['type'] == 'getTwitterUser':
            self.sendMessage(u'' + json.dumps({
                "type": "SET_TWITTER_USER",
                "data": self.getTwitterUser(name=data['data'], player=self.getClientPlayer())
            }))
            self.verifyForMatchup()
        if data['type'] == 'lifeDistributed':
            clientsData[self.getClientIndex()]["data"]["gameboard"] = data['data']
            clientsData[self.getClientIndex()]["status"] = "hex_selected"
            self.verifyHexSelected()
        if data['type'] == 'attacking':
            clientsData[self.getClientIndex()]["attack"] = data['data']
            clientsData[self.getClientIndex()]["status"] = "attacking"
            self.verifyGamePhase()
        if data['type'] == 'defending':
            clientsData[self.getClientIndex()]["attack"] = data['data']
            clientsData[self.getClientIndex()]["status"] = "defending"
            self.verifyGamePhase()

        print(self.address[1], data['type'])

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)
        clientsData.append({"status": "zero"})
        # pprint(clientsData, indent=4)
        if testing == 1:
            self.testDirectTo()
        else:
            self.sendStart()

    def sendStart(self):
        # for client in clients:
        self.sendMessage(u'' + json.dumps({"type": "SELECT_TWITTER_USER", "data": ""}))
        print "sending"

    def handleClose(self):
        global clients, clientsData
        myIndex = self.getClientIndex()
        clients = clients[:myIndex] + clients[myIndex + 1:]
        clientsData = clientsData[:myIndex] + clientsData[myIndex + 1:]
        print(self.address, 'closed')


server = SimpleWebSocketServer('', 8888, SimpleEcho)
server.serveforever()
