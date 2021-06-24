"""
__description__ = "Standardises downloaded Wikipedia article to a consistent format that can be 
processed better such as making punctuation fixes, stripping end-sections, etc."
__author__ = "Guy Keogh"
__license__ = "BSD 2-Clause"
"""

def space_after_punctuation(data):
    """Add spaces after . and ,"""
    prior_elem_was_punctuation = False
    elemcount = 0
    for elem in data:
        if prior_elem_was_punctuation:
            if elem != " ":
                data = data[:elemcount] + ' ' + data[elemcount:]
                elemcount+=1 #Added element before us, putting us 1 ahead of original. Compensate.
        if elem in ('.', ','):
            prior_elem_was_punctuation = True
        else:
            prior_elem_was_punctuation = False
        elemcount+=1
    return data

def strip_end_sections(text):
    """Strip useless parts at end (refs, see also, etc)"""
    References_start = text.rfind("References")
    See_also_start = text.rfind("See also")
    External_links_start = text.rfind("External links")
    Further_reading_start = text.rfind("Further reading")

    end_of_document = References_start
    if See_also_start < end_of_document and See_also_start != -1:
        end_of_document = See_also_start
    if External_links_start < end_of_document and External_links_start != -1:
        end_of_document = External_links_start
    if Further_reading_start < end_of_document and Further_reading_start != -1:
        end_of_document = Further_reading_start

    if end_of_document != -1:
        text = text[:end_of_document]

    return(text)
def detect_headings(text):
    """Detect locations of headings within text, and their start and end locations"""
    title_indexes = []
    slash_n_in_row = 0
    title_index = 0 #How many characters into current title
    index = 0
    if_title = False
    for letter in text:
        if letter == "\n":
            slash_n_in_row += 1
            if slash_n_in_row == 3:
                if_title = True
            else:
                if if_title:
                    end = index
                    start = index - title_index
                    #print("Start: ",start," end: ",end)
                    title_indexes.append(tuple((start,end)))
                if_title = False
        else:
            slash_n_in_row = 0
            if if_title:
                title_index+=1
            else:
                title_index = 0
        index+=1
    return title_indexes
