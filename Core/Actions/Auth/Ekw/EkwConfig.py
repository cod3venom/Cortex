
class EkwConfig:
    Gate: str = "https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW"
    First_code_css: str = "#kodWydzialuInput"
    Second_code_css: str = "#numerKsiegiWieczystej"
    Third_code_css: str = "#cyfraKontrolna"
    Form_submit_css: str = "#wyszukaj"
    Report_view_css: str = "#przyciskWydrukZupelny"

    Pages_count_xpath: str = "count(/html/body/table[1]/tbody/tr/td/form)"
    Page_selector_xpath: str = "/html/body/table[1]/tbody/tr/td[$]/form/input[@type='submit']"

    wrong_third_number = 'Nieprawidłowa cyfra kontrolna!'
    record_not_found = 'nie została odnaleziona'
