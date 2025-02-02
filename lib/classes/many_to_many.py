class Band:
    def __init__(self, name, hometown):
        # Initialize band with name, hometown, and an empty concert list
        self.name = name  # Calls setter to validate input
        self.hometown = hometown  # Calls setter to validate input
        self._concerts = []  # Stores concerts associated with the band

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, new_name):
        # Ensure name is a non-empty string; default to 'Unknown' if invalid
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        elif not hasattr(self, "_name"):  
            self._name = "Unknown"

    @property
    def hometown(self):
        return self._hometown 

    @hometown.setter
    def hometown(self, new_hometown):
        # Ensure hometown is a non-empty string; default to 'Unknown' if invalid
        if not hasattr(self, "_hometown"):  
            if isinstance(new_hometown, str) and len(new_hometown) > 0:
                self._hometown = new_hometown
            else:
                self._hometown = "Unknown"

    def add_concert(self, concert):
        """Adds a concert to the band's list if it belongs to this band."""
        if isinstance(concert, Concert) and concert.band == self:
            self._concerts.append(concert)

    def concerts(self):
        """Returns a list of concerts the band has played."""
        return self._concerts

    def venues(self):
        """Returns a list of unique venues where the band has performed."""
        return list(set(concert.venue for concert in self._concerts if concert.venue))

    def play_in_venue(self, venue, date):
        """Creates and returns a new Concert instance for this band at a venue on a given date."""
        if isinstance(venue, Venue) and isinstance(date, str) and len(date) > 0:
            return Concert(date, self, venue)
        return None  # Return None if inputs are invalid

    def all_introductions(self):
        """Returns a list of introduction messages for all the band's concerts."""
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = []  # Class attribute to store all concert instances

    def __init__(self, date, band, venue):
        # Initialize concert with date, band, and venue
        self.date = date  # Calls setter to validate input
        self.band = band  # Calls setter to validate input
        self.venue = venue  # Calls setter to validate input

        # Automatically associate this concert with the band and venue
        if isinstance(band, Band):
            band.add_concert(self)
        if isinstance(venue, Venue):
            venue.add_concert(self)

        Concert.all.append(self)  # Add instance to the global concert list

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        # Ensure date is a non-empty string
        if isinstance(new_date, str) and len(new_date) > 0:
            self._date = new_date  

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, new_band):
        # Ensure band is a valid Band instance
        if isinstance(new_band, Band):
            self._band = new_band

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, new_venue):
        # Ensure venue is a valid Venue instance
        if isinstance(new_venue, Venue):
            self._venue = new_venue  

    def hometown_show(self):
        """Checks if the concert is in the band's hometown."""
        return self.band and self.band.hometown == self.venue.city

    def introduction(self):
        """Generates an introduction message for the concert."""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        # Initialize venue with name, city, and an empty concert list
        self.name = name  # Calls setter to validate input
        self.city = city  # Calls setter to validate input
        self._concerts = []  # Stores concerts associated with the venue
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        # Ensure name is a non-empty string; default to 'Unknown' if invalid
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        elif not hasattr(self, "_name"):  
            self._name = "Unknown"  # Only set to "Unknown" during initialization

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, new_city):
        # Ensure city is a non-empty string; default to 'Unknown' if invalid
        if isinstance(new_city, str) and len(new_city) > 0:
            self._city = new_city
        elif not hasattr(self, "_city"):
            self._city = "Unknown"

    def add_concert(self, concert):
        """Adds a concert to the venue's list."""
        if isinstance(concert, Concert):
            self._concerts.append(concert)

    def concerts(self):
        """Returns a list of concerts held at the venue."""
        return self._concerts

    def bands(self):
        """Returns a list of unique bands that have performed at the venue."""
        unique_bands = list(set(concert.band for concert in self._concerts if concert.band))
        return unique_bands

    def concert_on(self, date):
        """Returns the concert happening on a specific date at the venue, if any."""
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
