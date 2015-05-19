# This script should be kept in the same folder as the files which has to be renamed
import os
# This is the name of the anime/THINGY and season number
name = "Bakuman S03E"
total_number_of_episodes = 25
# we take all the files in the directory the script has been placed
for filename in os.listdir("."):
    # Here the code will vary depending on what the files are originally named
    # I download all my anime with IDM and it names the anime -> videoplayback.mp4, videoplayback_2.mp4, videoplayback_3.mp4 ...  and so on
    # taking the first episode as a special case (strip .mp4 from filename)
    if(filename[:-4:] == "videoplayback"):
        print filename+"  -->> "+ name+"0"+str(1)+".mp4"+"\n\n"
        #os.rename(filename, name+"0"+str(1)+".mp4") UNCOMMENT THIS
    # the remaining files of mine have the episode no in its title
    for epno in range(total_number_of_episodes,0,-1):
        if(not(filename[:-4:].find(str(epno))== -1)):
            # for episodes's 1 to 9, make it 01 - 09
            if(epno/10 == 0):
                print filename+"  -->> "+ name+"0"+str(epno)+".mp4"+"\n\n"
                #os.rename(filename, name+"0"+str(epno)+".mp4") UNCOMMENT THIS
                break
            else:
                print filename+"  -->> "+ name+str(epno)+".mp4"+"\n\n"
                #os.rename(filename, name+str(epno)+".mp4") UNCOMMENT THIS
                break

# the actual code for renaming have been commented out, remove the # and run script
