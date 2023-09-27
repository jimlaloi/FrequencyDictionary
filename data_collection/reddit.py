import os, praw

# SUPPLY YOUR APP'S INFO
reddit = praw.Reddit(client_id= 'SnfpmlK7WdT9wZ5lqsZw9g',  # 14-character code
                     client_secret='ejQ3cWCSMA5gXuYq7rfnGSqrmdPT_A',  # 27-character code
                     user_agent= 'Jim Law',  # your app's name
                     username='macnfleas',  # your reddit username
                     password='Slughorn6')  # your reddit password


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
                        'Bourgogne',
                        'Bretagne',
                        'Caen',
                        'Cherbourg',
                        'Clermontfd',
                        'Franchecomte',
                        'GrandSud',
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
                        'martinique',
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
                        'Quebec',
                        'metaquebec',
                        'montreal',
                        'expatriation',
                        'Cuisine',
                        'BellePatisserie',
                        'anglais',
                        'Breton',
                        'FrancaisCanadien',
                        'francophonie',
                        'GrosMots',
                        'banalites',
                        'CajunFrench',
                        'Franglish',
                        'QuestionsDeLangue',
                        'philosophie',
                        'ExpressionEcrite',
                        'Livres',
                        'nouvelles',
                        'OCPoesie',
                        'mangafr',
                        'BDFrancophone',
                        'EcouteCa',
                        'frenchelectro',
                        'frenchrap',
                        'frenchrock',
                        'musiquefrancaise',
                        'vendredimusique',
                        'cinemacinema',
                        'FilmsFR',
                        'guessthefrenchmovie',
                        'ParlonsSerie',
                        'ivrevirgule',
                        'paslegorafi',
                        'jememarre',
                        'gifsuryvette',
                        'unexpectedgwennhadu',
                        'alimentation',
                        'vosfinances',
                        'transgenre',
                        'besoindeparler',
                        'santementale',
                        'PasDeQuestionIdiote',
                        'plusunegoutte',
                        'AddictionsFR',
                        'ParentingFR',
                        'conseiljuridique',
                        'CoeursBrisesDeFrance',
                        'sexualitefr',
                        'SocialParis',
                        'TinderFrance',
                        'AJEstUnCon',
                        'AJEstUnConLibre',
                        'BestOfFrance',
                        'bussiere',
                        'commeDitLaJeuneMariee',
                        'ConnardsDeParisiens',
                        'EnculesDeProvinciaux',
                        'EnTouteModestie',
                        'FanclubDeChefVautour',
                        'Franceboule',
                        'redditarou',
                        'franse',
                        'franselibre',
                        'jesuistresintelligent',
                        'lafamilledechapalyn',
                        'nouvelletaglinedusub',
                        'pariscirclejerk',
                        'rance',
                        'ranse',
                        'SansDecPoirot',
                        'lestaxissontdescons',
                        'UberCestDesGrosPedes',
                        'Malaise',
                        'OracleJDBC/',
                        'Bellygareth/',
                        'Perry75',
                        'JeSuisEnCPEtCestDrole/',
                        'mecsfous',
                        'franceUltraLibre',
                        'jeuairfrance',
                        'dota2france',
                        'jdr',
                        'jeuxvideo',
                        'esportfr',
                        'GuidesJV',
                        'leagueoflegendsFR',
                        'TableVirtuelle',
                        'asmonaco',
                        'GolfenFrancais',
                        'Ligue1',
                        'pedale',
                        'smcaen',
                        'SquaredCircle_FR',
                        'FitnessFrance/',
                        'mangerbouger',
                        'grimpe',
                        'BitcoinFrance',
                        'entraideinformatique',
                        'FrenchTech',
                        'GentilsVirus',
                        'PodcastFrancais',
                        'programmation',
                        'ScienceFr',
                        'zetetique',
                        'AutoHebergement',
                        'arduino_raspPi_FR/',
                        'anarchisme',
                        'FrontdeGauche',
                        'nuitdebout',
                        'Politique',
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
                        'voitures',
                        'conspiration',
                        'forumlibre',
                        'jailu',
                        'truefrance',
                        'renseignement',
                        'effondrement/',
                        'VideosFrancais',
                        'Eveil',
                        'vieuxcons',
                        'videosderepas/',
                        'prepaHEC',
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
                        'leagueoflegendsFR',
                        'BonneBouffe',
                        'FranceDigeste',
                        'actualite',
                        'LetsNotMeetFR',
                        'placeFR',
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
                        'Giscardpunk'
                        ]

# SPECIFY THE MAXIMUM NUMBER OF COMMENTS TO SCRAPE
max_comments = 1000
os.chdir(r"C:\Users\lawj2\OneDrive - BYU\Research\3 - Projects in writing stage\French frequency dictionary\Corpus\Reddit scrape")

for s in subreddits_to_search:
    with open(s + ".txt", "w", encoding="utf-8") as fout:
        print("Working on subreddit:", s)
        subreddit = reddit.subreddit(s)

        top_subs = subreddit.top(limit = max_comments)

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
            submission.comments.replace_more(limit= 0)
            for comment in submission.comments.list():
                fout.write(comment.body + "\n")