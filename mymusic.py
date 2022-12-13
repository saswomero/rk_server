from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

song_s = []

music = [
    {"name": "Queen",
     "info": "Британская рок-группа, добившаяся широчайшей известности в середине 1970-х годов, и одна из наиболее успешных групп в истории рок-музыки. Средства массовой информации называют группу «культовой» и пишут, что она и по сей день имеет сотни миллионов поклонников",
     "style": "Рок",
     "songs": ["We Will Rock You", "I Want to Break Free", "We Are the Champions"],
     "foto": "queen.jpg"
     },
    {"name": "Adele",
     "info": "Британская певица, автор-исполнитель и поэтесса, лауреат 15 премий Грэмми и первый музыкант, сумевший выиграть в номинациях «Альбом года» (21 и 25), «Запись года» и «Песня года» дважды.",
     "style": "Поп",
     "songs": ["Skyfall", "Hello", "I Miss You"],
     "foto": "adele.jpg"
     },
    {"name": "Пицца",
     "info": "Российская музыкальная группа, основанная в 2010 году Сергеем Приказчиковым, который является автором, композитором и аранжировщиком песен группы.",
     "style": "Поп",
     "songs": ["Фары", "Романс", "Улыбка"],
     "foto": "пицца.jpg"
     },
    {"name": "Ёлка",
     "info": "Украинская и российская поп-певица. Начанала музыкальную карьеру в составе ужгородской группы B&B",
     "style": "Поп",
     "songs": ["Прованс", "Не сдамся на полпути", "Нарисуй мне небо"],
     "foto": "ёлка.jpg"
     },
    {"name": "Земфира",
     "info": "Российская рок-певица, музыкант, композитор, продюсер, поэт и автор песен. Лидер группы «Zемфира»",
     "style": "Рок",
     "songs": ["Хочешь?", "Искала", "Ариведерчи"],
     "foto": "земфира.jpg"
     }
]


@app.route("/", methods=['GET'])
def root():
    return render_template('index.html')


@app.route("/artists", methods=['GET'])
def artists():
    names = []
    for musics in music:
        names.append(musics["name"])
    infos = []
    for musics in music:
        infos.append(musics["info"])

    print(names)
    return render_template('mym3.html',
                           names=names)


@app.route("/name/<m_name>/", methods=['GET'])
def by_name(m_name):
    for musics in music:
        if musics["name"] == m_name:
            print("Нашли", m_name)
            return render_template("mym.html",
                                   name=musics["name"],
                                   info=musics["info"],
                                   style=musics["style"],
                                   songs=musics["songs"],
                                   foto=musics["foto"])
    return "Никого не нашли с таким именем"


@app.route("/style/<m_style>/", methods=['GET'])
def by_style(m_style):
    names = []
    for musics in music:
        if musics["style"] == m_style:
            names.append(musics["name"])
            print("Нашли", names)

    return render_template('mym2.html',
                           style=m_style,
                           names=names)


@app.route("/new_artist", methods=['GET'])
def new_artict():
    name = request.args.get('name')
    style = request.args.get('style')
    songs = request.args.get('song')
    music.append({
        "name": name,
        "info": "",
        "style": style,
        "songs": songs,
        "foto": ""
    })
    return "Добавили артиста <br>" + str(music)


@app.route("/playlist/<song_name>/", methods=['GET'])
def playlist(song_name):
    for musics in music:
        for songs in musics["songs"]:
            if songs == song_name:
                song_s.append({"name": musics["name"],
                               "song": songs})
    print(song_s)

    return render_template("playlist.html",
                               name=song_s)


if __name__ == "__main__":
    app.run(debug=True)