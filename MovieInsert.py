from ActorInsert import *

movies = LikeDict()
movies["The Room"] = Movie(
    "The Room",
    "Johnny is a successful banker who lives happily in a San Francisco townhouse with his fiancée, Lisa. One day, inexplicably, she gets bored with him and decides to seduce his best friend, Mark. From there, nothing will be the same again.",
    "https://ia.media-imdb.com/images/M/MV5BMTg4MTU1MzgwOV5BMl5BanBnXkFtZTcwNjM1MTAwMQ@@._V1_.jpg",
    [
        Character(
            "Johnny",
            "Johnny is a successful banker who lives happily in a San Francisco townhouse with his fiancée, Lisa.",
            actors["tommy"]
        ),
        Character(
            "Mark",
            "Mark is that man who be stealin' yo girl.",
            actors["greg"]
        ),
        Character(
            "Lisa",
            "Lisa's that girl that get stolen from you by people like Mark",
            actors["juli"]
        )
    ]
)

movies["Best F(r)iends"] = Movie(
    "Best F(r)iends",
    "When a drifter befriends a quirky mortician, an unlikely business partnership is formed. Paranoia soon develops, however, and both men are forced to come to terms with the fragility of friendship and loyalty.",
    "https://ia.media-imdb.com/images/M/MV5BNDAxNzNhODEtZmUxMC00YjM1LWI4MDAtYzQ4NDY1ZDY0MTBiXkEyXkFqcGdeQXVyNzM0MTY5NTE@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
    [
        Character(
            "Harvey Lewis",
            "That creepy guy that does stuff to corpses.",
            actors["tommy"]
        ),
        Character(
            "Jon Kortina",
            "That guy that knows that creepy guy that does stuff to corpses.",
            actors["greg"]
        )
    ]
)

movies["Sherlock Holmes (TV Series)"] = Movie(
    "Sherlock Holmes (TV Series)",
    "A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.",
    "https://ia.media-imdb.com/images/M/MV5BMWY3NTljMjEtYzRiMi00NWM2LTkzNjItZTVmZjE0MTdjMjJhL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTQ4NTc5OTU@._V1_.jpg",
    [
        Character(
            "Sherlock Holmes",
            "A crazy drug addicted genius detective.",
            actors["benedict c"]
        ),
        Character(
            "Dr. John Hudson",
            "A Doctor who takes care of his constantly high and delusional patient Mr. Holmes by indulging his detective fantasies whilst he is on shrooms.",
            actors["freem"]
        )
    ]
)