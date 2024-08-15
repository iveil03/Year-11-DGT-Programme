#Maori Myths and Legends Quiz Game
#Author: Levi Pearce
#Version 1.1



intructions = ("""                                             
               
                                                         Welcome to my Maori Myths and Legends quiz
                                               game. This is a multi choice quiz based on various Maori Myths
                                                  and Legends. It has three levels: Easy, Medium and Hard. Each 
                                              level has five questions, and the first two levels have four possible 
                                                 answers per question and the third has five possible answers per 
                                                 question. Every time you get a question correct, your score 
                                                         increases by one. Try and beat the high score!  """)



#LVL 1
Questions_1= [{"question_text": "1. According to Maori Mythology, What is a Taniwha?",
              "options": ["a) A serpentine like monster that dwells in deep waterways", "b) A fiery bird that lives in the sky", "c) A tree dwelling creature that waatches over the forest", "d) None of the above, it doesn't exist"],
              "correct_answer": "a"},
             
             {"question_text": "2. Why did Maui and his Brothers Slow the Sun?",
               "options": ["a) Because it was beating down too fast, causing their crops to die", "b) It was moving too fast through the sky, not giving them enough time to complete their chores", "c) It was going too high, causing the days to be long and cold", "d) It was rising too quickly, not giving them enough time to rest"],
               "correct_answer": "b"},
             
             
             {"question_text": "3. Who is Tane Mahuta?",
               "options": ["a) The God of wind", "b) One of Maui's brothers", "c) The first Maori Chief", "d) The God of Forests and Birds"],
               "correct_answer": "d"},    
             
             
             {"question_text": "4. According to Maori Mythology, who is Matariki?",
               "options": ["a) The daughter of Maui", "b) The eldest daughter of the six sister stars that rise on the Maori New Year", "c) The Mother of the six sister stars that rise on the Maori New Year", "d) Noone, it is the name of a Maori holiday"],
               "correct_answer": "c"}, 
             
             
             {"question_text": "5. Maui Fished up the North Island by:",
               "options": ["a) Reeling in a giant underground rock, leftover from an erruption", "b) Disturbing an underground monster tha stirred up silt, creating a landmass", "c) Fishing a large peice of land that was deep in the ocean", "d) Pulling in a giant fish that became the North Island, after becoming hard and rigid"],
               "correct_answer": "d"},
             ]   

#LVL 1
score_1 = 0


#LVL 2
Questions_2= [{"question_text": "1. What is the primary point of Maori Myths and Legends?",
              "options": ["a) To tell extraordinairy stories with their villages", "b) To pass on their history and past to the next generation", "c) To tell and inform other cultures about their own culture and story", "d) To act as substitutes to books and the written language"],
              "correct_answer": "b"},
             
             {"question_text": "2. According to Maori Mythology, who is responsible for the separation of the Earth mother (Papatuanuku) and the Sky Father (Ranginui)?",
               "options": ["a) Maui, as they were trapping humans between their grasp", "b) Humans, as they arrived in between them, forcing them apart", "c) Tane Mahuta, as he and his brothers wanted space", "d) Tumatauenga, the god of war and human activity was sick of being confined, so he pushed them apart"],
               "correct_answer": "c"},
             
             
             {"question_text": "3. According to Maori Mythology how did the first woman (Hineahuone) come to be?",
               "options": ["a) In the beginning, stars collided, creating man and woman, that populated the earth by breathing life into every being", "b) After they got separated Ranginui wanted a woman for his sons, so he created one out of the sky and stars and delivered it to his sons", "c) Io Matua Kore - the supreme being; personification of light and the world of the living and the forest, created the men, then a woman to pair", "d) After separating his parents, Tane Mahuta convinced the other gods to create a woman to populate the earth"],
               "correct_answer": "d"},    
             
             
             {"question_text": "4. According to Maori Mythology what is Maui Known as?",
               "options": ["a) A trickster, known for his cleverness,  as well as possessing superhuman strength", "b) The God of the people and mankind, who protected his people, existing among them", "c) The Grandson of Tane Mahuta, who gave Maui the task of protecting his people", "d) All of the above"],
               "correct_answer": "a"}, 
             
             
             {"question_text": "5. How did Maui create fire?",
               "options": ["a) He was given a special fish jawbone, that had the properties to bring fire to the people", "b) He used sticks from a burnt down tree, and rubbed the dry sticks against each other, creating fire", "c) When he visited his father in the underworld, his father showed him how to create a fire with the bones of a Moa, using special incantations", "d) He didn’t create fire, Ranginui, the sky father did, after cursing his sons for separating him and Papatuanuku the earth mother, he threw it down on them, burning them"],
               "correct_answer": "b"},
             ] 

#LVL 2
score_2 = 0

#LVL 3           
Questions_3= [{"question_text": "1. Who are Maui's parents?",
              "options": ["a) Makeatutara and Taranga", "b) Tane Irawaru and Hineahuone Urangi", "c) Manwhaia and Turianga", "d) Hukainga and Maniaka", "e) Wairuanga and Kaitiangi"],
              "correct_answer": "a"},
             
             {"question_text": "2. According to Maori Mythology how was was the milky way created?",
               "options": ["a) Io-matua-kore, the 'supreme God' created the stars to give him and the other Gods light", "b) They are the dry, solid tears of the Sky Father (Ranginui), who wept for his beloved (Earth Mother) after being separated", "c) It is a shark, sent up to the sea of the sky by the Demigod Maui to watch over and protect the Maori tribes on earth", "d) They are fragments from an explosion, caused by the God Tūmatauenga, who was jealous of his brother, Tane", "e) The Sky Father put them in the sky so that his beloved, the Earth mother, could see them on earth, and think of him at night"],
               "correct_answer": "c"},
             
             
             {"question_text": "3. What happened to Maui when he was a baby?",
               "options": ["a) He was blessed by the Sky Father (Ranginui) with a special Karakia, which gave him superhuman strength and courage", "b) He was cast into the ocean by his mother, as he was premature", "c) He was abandoned in the bush, eventually being found by his siblings", "d) He as taken by his father, who hid him in the underworld", "e) Nothing, as he had a protective spell over him as soon as he formed in his mother's womb"],
               "correct_answer": "b"},    
             
             
             {"question_text": "4. How many brothers did Tane Mahuta have?",
               "options": ["a) 14", "b) 7", "c) 5", "d) 0", "e) It is unknown how many siblings Tane Mahuta had, as over years, the number has become varied"],
               "correct_answer": "b"}, 
             
             
             {"question_text": "5. How many brothers did Maui have?",
               "options": ["a) 7", "b) 3", "c) 4", "d) 2", "e) None, he was the only male offspring in his family"],
               "correct_answer": "c"},
             ] 

score_3 = 0

  
keep_going = ""
while keep_going == "":
    #Creating a variable that allows user to enter an input.

    play_screen = input ("""                                                            Maori Myths and Legends Quiz Game
                                                                 Press <enter> to begin! """)
    #If user presses <enter> button, ask for their name and give them instructions. Done using 'if' statements.
    if play_screen == "":
        
        name = input ("""                                                               
                    
                                                                 Please enter your name: """)
        
        print ("""                                 
                                                              Alright""" + ' ' + name + ',' + ' ' + """Here's your instructions:""")
        print (intructions)
        
        if name != "":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            

            for question in Questions_1:
                print(question["question_text"])


                for option in question["options"]:
                    print (option)
                print()


                user_input = input("Enter your answer: ")
                question["user_input"] = user_input 


            for index, question in enumerate(Questions_1):
                if question["user_input"] == question["correct_answer"]:
                    score_1 += 1
                    print(f"{index + 1}. Correct Answer")
                else:
                    print(f"{index + 1}. Wrong Answer, the correct answer was {question['correct_answer']}")


            print()

            round_1_result = score_1 / len(Questions_1)
            print (f"You got {score_1} / {len(Questions_1)} questions correct!")
            print("")
            print("")
            print("")
            print("")
            print("""                                                       That was level one, time for level two! 
                                                           This level is harder, good luck!""")
            print("")
            print("")
            print("")
            print("")

            for question in Questions_2:
                print(question["question_text"])


                for option in question["options"]:
                    print (option)
                print()


                user_input = input("Enter your answer: ")
                question["user_input"] = user_input 


            for index, question in enumerate(Questions_2):
                if question["user_input"] == question["correct_answer"]:
                    score_2 += 1
                    print(f"{index + 1}. Correct Answer")
                else:
                    print(f"{index + 1}. Wrong Answer, the correct answer was {question['correct_answer']}")


            print()

            round_2_result = score_2 / len(Questions_2)
            print (f"You got {score_2} / {len(Questions_2)} questions correct!")

            print()
            print()
            print()
            print()
           
            print()
            print()
            print("That was level 2")
            print("It is now time for the hardest and last level; level 3")
            print("You will have five possible answers per questions, with the questions being the hardest of all three levels")
            print()
            print()
            print("Good Luck")
            print()
            print()

            for question in Questions_3:
                print(question["question_text"])


                for option in question["options"]:
                    print (option)
                print()


                user_input = input("Enter your answer: ")
                question["user_input"] = user_input 


            for index, question in enumerate(Questions_3):
                if question["user_input"] == question["correct_answer"]:
                    score_3 += 1
                    print(f"{index + 1}. Correct Answer")
                else:
                    print(f"{index + 1}. Wrong Answer, the correct answer was {question['correct_answer']}")


            print()

            round_3_result = score_3 / len(Questions_3)
            print (f"You got {score_3} / {len(Questions_3)} questions correct!")


        

        


#'Else' statement to print an error message if user does not enter the <enter> key for an input.
        
        else:
          print("                                                                That is not a valid input.")
    
          keep_going = input("                                                 Press <enter> to play the game or any other key to quit: ")



  
