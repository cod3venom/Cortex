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
    STOP = 'Stop'
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

    '''
        BOT OPTIONS CONSTANTS
    '''
    GET_BOT_OPTIONS = 'GetBotOptions'
    OPTIONS_ID = 'Option_id'


    """
        BOT LAUNCHER CONSTANTS
    """
    MACHINE_PREFIX = 'MACHINE_#'
    #/home/venom/Desktop/DEV/Cortex1.1/Kernel/TermContainer/out/artifacts/TermContainer_jar
    #java -jar ./TermContainer.jar
    # BOT_LAUNCHER = "gnome-terminal --title=MACHINE_NR_#{} -- python3 {}/Start.py {} {} {}"
    #BOT_LAUNCHER = '''exec java -jar /home/venom/Desktop/DEV/Cortex1.1/Kernel/TermContainer/out/artifacts/TermContainer_jar/TermContainer.jar {} {} {} {}  '''
    #BOT_LAUNCHER = '''gnome-terminal fg  -- xpanes -t  -d -c "python3 {}/Start.py {} {} {}"  '''

    #BOT_LAUNCHER = '''gnome-terminal --disable-factory --title=MACHINE_NR_#{} -- python3 "{}/Start.py" {} {} {} '''
    BOT_LAUNCHER = '''gnome-terminal fg  -- xpanes -t  -d -c "python3 {}/Start.py {} {} {}" {}  '''


    '''
        SOME ALERT CONSTANTS
    '''
    JSON_WRONG_FORMAT = '[JSON.class] GOT WRONG JSON FORMAT'
    JSON_WRONG_KEY = '[JSON.class] GOT WRONG KEYWORD : {}'