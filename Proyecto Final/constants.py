#Constantes que voy a usar en mi programa.

class Constants:
    #-- Constants de Main Menu --#
    MENU = """
                        Select an Option:

                        1. User Session List.
                        2. User Session List by Date.
                        3. Total User Session Time.
                        4. User MAC.
                        5. All User MACs.
                        6. User conected by AP.
                        7. User Traffic.
                        8. List AP (Ordered by Total Traffic).

                        """

    ANSWER = """Option: """

    P_TO_C = "Press a key to Continue.."

    WANT_QUIT = """
                        Are you sure you want to go out? 
                        1.Yes
                        2.No
                        """

    EXITING = "Exiting.."

    RETURNING = "Returning.."

    INV_OP = "Invalid Option"

    INV_OP2 = "Enter a Correct Option!, Try again.."

    SPACE = "\n"


    #-- Constants de REGEXs--#

    REGEX_ID = ("""^(?=.*[a-z])(?=.*[0-9]).{16,16}$""")

    REGEX_DATE = ("""^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$""")

    REGEX_HOUR = ("""^(((([0-1][0-9])|(2[0-3])):?[0-5][0-9]:?[0-5][0-9]+$))""")

    REGEX_MACAP = ("""^(04|DC)(\-)(18|9F)(\-)(DB|D6)(\-)([0-9]{2})(\-)([A-F0-9]{2})(\-)([A-F0-9]{2})(\:)(UM)$""")

    REGEX_MAC = ("""^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$""")

    