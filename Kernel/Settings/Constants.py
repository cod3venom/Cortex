class Constants:
    SOFTWARE_NAME_UPPER = 'CORTEX'
    SETTINGS_FILE = '/usr/share/cortex/settings.json'

    """
        SOME STRING CONTANTS
    """
    EMPTY = ''
    SPACE = ' '
    NEWLINE = '\n'
    ZERO = 0
    START = 'Start'
    SPIDER = 'spider'

    """
        BOT AUTH KEYWORDS
        {'USER_ID': '', 'CLIENT_ID': '', 'CLIENT_IDENTIFIER': '','CLIENT_PASSWORD':'', 'CLIENT_LEVEL': ''}
    """

    BOTAUTH = "BotAuth"
    USER_ID = 'USER_ID'
    CLIENT_ID = 'CLIENT_ID'
    CLIENT_IDENTIFIER = "CLIENT_IDENTIFIER"
    Client_identifier = "Client_identifier"
    CLIENT_PASSWORD = "CLIENT_PASSWORD"
    Client_password = "Client_password"
    CLIENT_LEVEL = 'CLIENT_LEVEL'

    """
        AUTH FLAGS
    """
    LOGGED_IN = "LOGGED IN SUCCESSFULLY"
    WRONG_CREDENTIALS = "WRONG CREDENTIALS"
    LOGOUT = "Logged_out"
    LOGGED_OUT = "LOGGED OUT SUCCESSFULLY"

    """
        BOT LAUNCHER CONSTANTS
    """
    BOT_LAUNCHER = "gnome-terminal --title=MACHINE_NR_#{} -- python3 {}/Start.py {} {} {}"
