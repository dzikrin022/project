biodata = {}
biodata['Dzikri'] = {
    "name" : "Dzikri Nursyaban",
    "age" : 19,
    "address" : "Kp. Cipari Ds. Sukatani Kec. Cilawu Kab. Garut",
    "hobbies" : ["reading","play sudoku"],
    "is_married" : False,
    "list_school" : [
        {
        "name" : "SMKN 10 Garut",
        "level" : "High School",
        "year-in" : "2015",
        "year-out" : "2018",
        "major" : "TKJ"
        },
        {
        "name" : "MTs Miftahul Huda",
        "level" : "Junior High School",
        "year-in" : "2012",
        "year-out" : "2015",
        "major" : None
        },
        {
        "name" : "SDN Mekarsari III",
        "level" : "Elementary",
        "year-in" : "2006",
        "year-out" : "2012",
        "major" : None
        }
    ],
    "Skills" : [
        {
        "skill_name" : "Python",
        "level" : "Beginner"
        },
        {
        "skill_name" : "MikroTik",
        "level" : "Advanced"
        },
        {
        "skill_name" : "Cisco",
        "level" : "Advanced"
        }
        ],
    "interest_in_coding" : True
}
import json
s = json.dumps(biodata)
with open("D:\\biodata.json","w") as f:  #yang ini merupakan lokasi dimana file json akan disimpan
    f.write(s)

