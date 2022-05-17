import funcs

def algorithm(text):
    # Receive the text line from the user.
    # Initialize variables.
    found_func = False
    count = 0
    start_string = 0
    end_string = len(text)
    the_func = None
    count2 = 0
    key_words = {("open",): funcs.Sites_and_Apps().do_open,("search",):funcs.Sites_and_Apps().do_search, ("and",): print,("wiki","wikipedia",):funcs.Sites_and_Apps().wiki,("what","who","where","when","solve","equation",):funcs.Sites_and_Apps().questions_and_answers,("play","video","song",):funcs.Sites_and_Apps().play_videos,("record",):funcs.Audio.do_record,("file",):funcs.Audio.play_file,("picture","capture","pic",):funcs.Extra.camera,("funny","joke","laugh",):funcs.Extra.joke,("pause","stop",):funcs.Extra.pause,("game","gaming",):funcs.Extra.games,("note",):funcs.Note.do_note,("read",):funcs.Note.read_note,("write",):funcs.Note().write1,("delete",):funcs.Note.delete_notes,("is my name",):funcs.User.username,("change my name",):funcs.User.change_name,("time",):funcs.Time.time,("day","date",):funcs.Time.day } #Create dictionary of key words for every function and the correlating functions

    for l in range(0, len(text)+1):#iterate over text
        texty = text[start_string:l:1]
        for k in key_words.keys():#iterate over set of key words
            for i in k: #Iterate over individual words
                length = len(" " + i + " ") - 1
                if i in texty:# count the place that the keyword is in
                    count+=1
                    count2+=1
                    if not found_func: # The first time a key word appears within the part of the text we ran through.
                        found_func = True
                        the_func = key_words[k]
                        start_string = l+1
                    else: #If a second or more key word appeared
                        end_string = l-length

                if count< count2*2 and ((count != 0 and count % 2 == 0 ) or (l == end_string and found_func != False)): # if we found two new key word, pass the text between the start and end to the function
                    the_func(text[start_string:end_string])
                    the_func = key_words[k]
                    start_string = end_string+length+1
                    end_string = len(text)
                    count+=1
while True:
    try:
        text = funcs.Ai_Listening().takeCommand().lower()
        algorithm(text)
    except:
        pass
