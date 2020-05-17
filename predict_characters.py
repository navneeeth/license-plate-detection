import segment_characters
import joblib
import sys
import colorama
print(colorama.Fore.WHITE+"Currently in file: "+str(sys.argv[2]))
fileNo = int(str(sys.argv[3]))
dirSize = int(str(sys.argv[4]))
percentageCompleted = fileNo * 100 / dirSize
percentageCompleted = round(percentageCompleted, 2)
print(colorama.Fore.GREEN+"Completed " + str(percentageCompleted) + "% out of 100.")
if(len(segment_characters.characters) > 0):
    print(colorama.Style.DIM+colorama.Fore.WHITE+"Loading model...")
    filename = './svc.sav'
    #model = pickle.load(open(filename, 'rb'))
    model = joblib.load(filename, 'r')
    
    print(colorama.Style.DIM+colorama.Fore.WHITE+'Model loaded. \nPredicting characters of number plate...')
    classification_result = []
    for each_character in segment_characters.characters:
        # converts it to a 1D array
        each_character = each_character.reshape(1, -1);
        result = model.predict(each_character)
        classification_result.append(result)
    
    #print('Classification result')
    #print(classification_result)
    
    plate_string = ''
    for eachPredict in classification_result:
        plate_string += eachPredict[0]
    
    print(colorama.Fore.WHITE+'Predicted License Plate:')
    print(colorama.Fore.CYAN+plate_string)
    
    # it's possible the characters are wrongly arranged
    # since that's a possibility, the column_list will be
    # used to sort the letters in the right order
    
    column_list_copy = segment_characters.column_list[:]
    segment_characters.column_list.sort()
    rightplate_string = ''
    for each in segment_characters.column_list:
        rightplate_string += plate_string[column_list_copy.index(each)]
    
    print(colorama.Fore.WHITE+'Sorted License Plate:')
    print(colorama.Fore.GREEN+rightplate_string)