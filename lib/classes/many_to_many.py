class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(hometown, str) or len(hometown) == 0:
            raise ValueError("Hometown must be a non-empty string")
        
        self._name = name
        self._hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self] or None

    def venues(self):
        return list(set([concert.venue for concert in Concert.all_concerts if concert.band == self])) or None

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()] or None


class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(city, str) or len(city) == 0:
            raise ValueError("City must be a non-empty string")
        
        self._name = name
        self._city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("City must be a non-empty string")
        self._city = value

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.venue == self] or None

    def bands(self):
        return list(set([concert.band for concert in Concert.all_concerts if concert.venue == self])) or None


class Concert:
    all_concerts = []

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or len(date) == 0:
            raise ValueError("Date must be a non-empty string")
        if not isinstance(band, Band):
            raise ValueError("Band must be an instance of Band class")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be an instance of Venue class")

        self._date = date
        self.band = band
        self.venue = venue
        Concert.all_concerts.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Date must be a non-empty string")
        self._date = value

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    @classmethod
    def concert_on(cls, date):
        return next((concert for concert in cls.all_concerts if concert.date == date), None)
