from person import Person


class Staff(Person):
    """
    The Staff class is also a sub-class of the 'Person'
    class meaning it inherits characteristics such as
    'name' and 'p_id'.
    """
    roomCapacity = 4
    wants_accomodation = False

    def get_all_staff(self):
        pass

    def get_office_allocated(self):
            pass
