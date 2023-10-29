import os, praw, time

# SUPPLY YOUR APP'S INFO
reddit = praw.Reddit(client_id= '',  # 14-character code
                     client_secret='',  # 27-character code
                     user_agent= '',  # your app's name
                     username='',  # your reddit username
                     password='')  # your reddit password


# SPECIFY THE SUBREDDIT COMMUNITIES YOU WANT TO SCRAPE
# Pulled subreddits from the r/france "annuaire des subreddits de la francophonie" https://www.reddit.com/r/france/wiki/annuaire/
# As well as other subreddits suggested in response to a question on r/French about French subreddits https://www.reddit.com/r/French/comments/7oqcwo/french_subreddits/
# Some subreddits suggested by those sources are conceivably French-language, but actually most posts are in English, so I checked and removed those.
# I also removed any subreddits specifically for anglophones learning French (like r/french), because they're full of English and non-native-like French.
# Finally I searched "français" on Reddit communities and added any over 5k subscribers that fit the above criteria.
subreddits_to_search = ['france', 
                        'rance', 
                        'moi_dlvv', 
                        'quebec', 
                        'montreal', 
                        'jeuxvideo', 
                        'FrancaisCanadien', 
                        'jardin', 
                        'nouvelles', 
                        'musique', 
                        'sante_bien_etre',
                        'aixmarseille',
                        'alsace',
                        'Aquitaine',
                        'Auvergne',
                        'Bordeaux',
                        'Bretagne',
                        'Caen',
                        'Cherbourg',
                        'Clermontfd',
                        'Franchecomte',
                        'Grenoble',
                        'JustMarseilleThings',
                        'Lehavre',
                        'Lille',
                        'limousin',
                        'lorraine',
                        'Lyon',
                        'JustLyonThings',
                        'Montpellier',
                        'Nancy',
                        'Nantes',
                        'nicefrance',
                        'Normandie',
                        'Paris',
                        'picardie',
                        'provence',
                        'Reims',
                        'Rennes',
                        'rouen',
                        'savoie',
                        'Strasbourg',
                        'toulouse',
                        'Tours',
                        'guadeloupe',
                        'lareunion',
                        'reunionisland',
                        'Tahiti',
                        'nouvelle_caledonie',
                        'FrancePics',
                        'geographie',
                        'Histoire',
                        'belgique',
                        'Wallonia',
                        'suisse',
                        'Algerie',
                        'Cameroon',
                        'Cameroun',
                        'Cotedivoire',
                        'Madagascar',
                        'maroc',
                        'acadie',
                        'metaquebec',
                        'expatriation',
                        'Cuisine',
                        'BellePatisserie',
                        'anglais',
                        'FrancaisCanadien',
                        'francophonie',
                        'GrosMots',
                        'banalites',
                        'CajunFrench',
                        'Franglish',
                        'QuestionsDeLangue',
                        'philosophie',
                        'ExpressionEcrite',
                        'nouvelles',
                        'OCPoesie',
                        'mangafr',
                        'BDFrancophone',
                        'EcouteCa',
                        'frenchelectro',
                        'frenchrap',
                        'vendredimusique',
                        'cinemacinema',
                        'FilmsFR',
                        'guessthefrenchmovie',
                        'ParlonsSerie',
                        'ivrevirgule',
                        'paslegorafi',
                        'gifsuryvette',
                        'unexpectedgwennhadu',
                        'alimentation',
                        'vosfinances',
                        'transgenre',
                        'besoindeparler',
                        'santementale',
                        'PasDeQuestionIdiote',
                        'AddictionsFR',
                        'ParentingFR',
                        'conseiljuridique',
                        'CoeursBrisesDeFrance',
                        'sexualitefr',
                        'SocialParis',
                        'TinderFrance',
                        'BestOfFrance',
                        'commeDitLaJeuneMariee',
                        'EnculesDeProvinciaux',
                        'Franceboule',
                        'redditarou',
                        'franse',
                        'franselibre',
                        'jesuistresintelligent',
                        'nouvelletaglinedusub',
                        'pariscirclejerk',
                        'SansDecPoirot',
                        'lestaxissontdescons',
                        'Malaisetopie',
                        'OracleJDBC',
                        'Bellygareth',
                        'JeSuisEnCPEtCestDrole',
                        'mecsfous',
                        'franceUltraLibre',
                        'jeuairfrance',
                        'dota2france',
                        'jdr',
                        'esportfr',
                        'GuidesJV',
                        'leagueoflegendsFR',
                        'TableVirtuelle',
                        'asmonaco',
                        'GolfenFrancais',
                        'Ligue1',
                        'pedale',
                        'smcaen',
                        'FitnessFrance',
                        'mangerbouger',
                        'grimpe',
                        'BitcoinFrance',
                        'FrenchTech',
                        'PodcastFrancais',
                        'programmation',
                        'ScienceFr',
                        'zetetique',
                        'AutoHebergement',
                        'arduino_raspPi_FR',
                        'anarchisme',
                        'FrontdeGauche',
                        'nuitdebout',
                        'Politiquefrancaise',
                        'politiquedumonde',
                        'politiquequebec',
                        'quefaitlapolice',
                        'Justicedeclasse',
                        'ranm',
                        'seddit',
                        'melenchon',
                        'HamonPourPresident',
                        'Feminisme',
                        'LgbtqiEtPlus',
                        'taule',
                        'DiscussionPolitique',
                        'islamophobie',
                        'FranceInsoumise',
                        'Ruffin',
                        'petitpain',
                        'painauchocolat',
                        'chocolatine',
                        'jardin',
                        'jardinage',
                        'jardinageQc',
                        'voitures',
                        'conspiration',
                        'forumlibre',
                        'truefrance',
                        'renseignement',
                        'effondrement',
                        'VideosFrancais',
                        'vieuxcons',
                        'videosderepas',
                        'fonctionpublique_fr',
                        'causerie',
                        'MemeFrancais',
                        'FranceDetendue',
                        'FrenchMemes',
                        'ChatGPT_FR',
                        'AskFrance',
                        'trouduction',
                        'QuebecLibre',
                        'Netflixfr',
                        'WriteStreak',
                        'chiens',
                        'penseesdedouche',
                        'Montreal_Francais',
                        'TwitchFR',
                        'france6',
                        'BonneBouffe',
                        'FranceDigeste',
                        'actualite',
                        'LetsNotMeetFR',
                        'placeFR',
                        'placefrance',
                        'ecologie',
                        'EnculerLesVoitures',
                        'rienabranler',
                        'Sysadmin_Fr',
                        'CineSeries',
                        'economie',
                        'SportsFR',
                        'AujourdhuiJaiAppris',
                        'LeGifFrancais',
                        'BruxellesMaBelle',
                        'ScienceFiction_FR',
                        'okcopainattard',
                        'bonjour',
                        'Giscardpunk',
                        'FranceRugby',
                        'FranceFIRE',
                        'ProvenceFrance'
                        ]

os.chdir("/Reddit scrape")

# set number of seconds to sleep between each request for more comments
# If you get "Too many requests" errors, increase the sleep time
t = 3

for s in subreddits_to_search:
    with open(s + ".txt", "w", encoding="utf-8") as fout:
        print("Working on subreddit:", s)
        subreddit = reddit.subreddit(s)

        top_subs = subreddit.top(limit = None)

        topics_dict = {}
        topics_dict["title"] = []
        topics_dict["id"] = []

        for i in top_subs:
            topics_dict["title"].append(i.title)
            topics_dict["id"].append(i.id)

        for v in topics_dict["title"]:
            fout.write(v + "\n")

        ids = topics_dict["id"]

        print(f"There are {len(ids)} posts gathered from the '{s}' subreddit")

        for index,id in enumerate(ids):
            print("Working on id #" + str(index + 1) + ":", id)
            submission = reddit.submission(id)
            submission.comments.replace_more(limit= None)
            for comment in submission.comments.list():
                fout.write(comment.body + "\n")
            time.sleep(t)
