from models import PersonalHistory, Event
from datetime import datetime

class FormUtil:
    def __init__(self):
        pass

    @staticmethod
    def today_date_str():
        return FormUtil.date_to_str(datetime.now())

    @staticmethod
    def date_to_str(date):
        return date.strftime("%m/%d/%Y")

    @staticmethod
    def dob_str(ph, event):
        """
        :type ph: PersonalHistory
        :type event: Event
        """

        dob = event.listed_dob if event.listed_dob else ph.rap_sheet.dob
        return FormUtil.date_to_str(dob)

    @staticmethod
    def event_to_name_as_charged(ph, event):
        """
        :rtype : Name
        :type ph: PersonalHistory
        :type event: Event
        """
        return ph.rap_sheet.names_as_charged[event.arrest_info.name_as_charged_id]

    @staticmethod
    def attorney_or_party_without_attorney(ph, event):
        """
        :type ph: PersonalHistory
        :type event: Event
        """
        return ph.name + " AKA " + FormUtil.event_to_name_as_charged(ph, event) + "\n" + ph.address.to_str_one_line()

    @staticmethod
    def short_case_name(ph, event):
        """
        :rtype : str
        :type ph: PersonalHistory
        :type event: Event
        """
        return "People v. " + FormUtil.event_to_name_as_charged(ph, event).last

    @staticmethod
    def cr_180_header(ph, event):
        """
        :type ph: PersonalHistory
        :type event: Event
        """
        return [
            ("1a", FormUtil.attorney_or_party_without_attorney(ph, event)),
            ("1b", ph.phone_number),
            ("1c", ph.email),
            ("1d", "Self-Represented"),
            ("1e", ""),  # Fax number
            ("2a", FormUtil.event_to_name_as_charged(ph, event)),
            ("2b", FormUtil.dob_str(ph, event)),
            ("3", event.associated_cases[0].case_id),
        ]

    @staticmethod
    def cr_180_header_2(ph, event):
        """
        :type ph: PersonalHistory
        :type event: Event
        """
        return [
            ("7", FormUtil.event_to_name_as_charged(ph, event)),
            ("8", event.associated_cases[0].case_id),

        ]

    @staticmethod
    def case_date(event):
        return FormUtil.date_to_str(event.associated_cases[0].date)
