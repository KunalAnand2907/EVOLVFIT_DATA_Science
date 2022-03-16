#1.) Importing Libraries
import cv2
import mediapipe as mp
import numpy as np
import time
import math
import calculate_angle
from parameters import parameters
import pose_estimate

mp_drawing = mp.solutions.drawing_utils # mp_drawing - visualizing the landmarks
mp_holistic = mp.solutions.holistic  # Mediapipe Solutions - - renders the 4 module pipeline

# Double - Arm Doumbell
counter=0
stage="Up"

# Overhead Press
press=0
stage_o="Up"

# VIDEO FEED - oNLY USING THE POSE MODULE OUT OF 4 MODULES IN m HOLISTIC MODULE
parameters()

#5.)  Curl-Counter Code for All Exercises
Class = ['Single_arm_Dumbell','OH-Press','Neutral'] # Add on the Exercise names in this List
cap = cv2.VideoCapture(r"curls.mp4")
## Setup mediapipe instance
with mp_holistic.Holistic(min_detection_confidence=0.2, min_tracking_confidence=0.2) as holistic: #
    while cap.isOpened():
        timer=cv2.getTickCount()
        ret,frame = cap.read()
        frame = cv2.resize(frame,(1280,720))
        
        #Recolor image
        image =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image.flags.writeable = False # False as we can read as well as write w.r.t image
        
        # Make detections
        results =holistic.process(image)
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        if condition_0 == "Angle":
            if condition_1 == 0:
                    try: 
                            landmarks = results.pose_landmarks.landmark
                            print(landmarks)
                            shoulder_1 = [landmarks[cond_angle[0]].x,landmarks[cond_angle[0]].y]
                            elbow_1 = [landmarks[cond_angle[1]].x,landmarks[cond_angle[1]].y]
                            wrist_1 = [landmarks[cond_angle[2]].x,landmarks[cond_angle[2]].y]
                            
                            shoulder_2 = [landmarks[12].x,landmarks[12].y]
                            elbow_2 = [landmarks[14].x,landmarks[14].y]
                            wrist_2 = [landmarks[16].x,landmarks[16].y]
                            
                            angle = calculate_angle(shoulder_1, elbow_1, wrist_1,shoulder_2, elbow_2, wrist_2)
                            
                            per = np.interp(angle[0],(20,160),(100,0)) # LEFT
                            bar = np.interp(angle[0],(30,160),(600,200))
            
                            cv2.putText(image, str(round(angle[0],2)), 
                            tuple(np.multiply(elbow_1, [1280, 720]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                
                            cv2.putText(image, str(round(angle[1],2)), 
                            tuple(np.multiply(elbow_1, [1280, 720]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                            
                            #print(landmarks)
                            
                            #fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer) # Get frames per second
                            # Curl Counter Logic
                            color =(255,0,255)
                            if Signs[0]=="<" or Signs[1]==">":
                                if angle[0]>Angle_para[1]:
                                    stage = "Down"
                                    if per ==0:
                                        color =(0,255,0)
                                if angle[0]<Angle_para[0] and stage =="Down": # Count when we moves from down to up , >160 is full flat so down
                                    stage="Up"
                                    if per ==100:
                                        color=(0,255,0)
                                    counter+=1
                                    print(counter)
                            
                            
                            
            
                    except:
                         pass
                            
                            # Render curl counter and status box
                    cv2.rectangle(image,(5,5),(270,80),(245,117,66),-1)
        
                            # fps
                            #cv2.putText(image,str(fps),(90,19),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 1, cv2.LINE_AA)
        
                            # Draw Bar
                    cv2.rectangle(image,(1000,200),(1055,600),color,3)
                    cv2.rectangle(image,(1000,int(bar)),(1055,600),color,cv2.FILLED)
                    cv2.putText(image,f'{int(per)}%',(1000,170),cv2.FONT_HERSHEY_PLAIN, 2,color, 3)
        
       
                            # Rep data
                    cv2.putText(image,'REPS',(17,25),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 1, cv2.LINE_AA)
                    cv2.putText(image,str(counter),(20,72),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
                            #Stage Data
                    cv2.putText(image,'STAGE',(120,25),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 1, cv2.LINE_AA)
                    cv2.putText(image,stage,(120,65),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2, cv2.LINE_AA)
        
                            # Render Class Name
                    cv2.putText(image,Class[0],(500,45),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), 2, cv2.LINE_AA)
        
               
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )   
                            
                    if results.pose_landmarks !=None:
                                    face_res, pose_res, full_frame_res, angle_res, elbow_flat_angle, elbow_straight_angle, hand_straight_angle = pose_estimate(
                                    results.pose_landmarks, image)
                    if full_frame_res == 0:
                                          cv2.rectangle(image, (0,0), (1280,697), (0, 255, 0), 10) # green
                    else:
                                          cv2.rectangle(image, (0,0), (1280,697), (0, 0 ,255), 10) #red
                                    
    
            
                    cv2.imshow("Mediapipe Feed",image)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                            break
            elif condition_1==1:
                    try: 
                            landmarks = results.pose_landmarks.landmark
                            print(landmarks)
                            shoulder_1 = [landmarks[cond_angle[0]].x,landmarks[cond_angle[0]].y]
                            elbow_1 = [landmarks[cond_angle[1]].x,landmarks[cond_angle[1]].y]
                            wrist_1 = [landmarks[cond_angle[2]].x,landmarks[cond_angle[2]].y]
                            
                            shoulder_2 = [landmarks[cond_angle[3]].x,landmarks[cond_angle[3]].y]
                            elbow_2 = [landmarks[cond_angle[4]].x,landmarks[cond_angle[4]].y]
                            wrist_2 = [landmarks[cond_angle[5]].x,landmarks[cond_angle[5]].y]
                            
                            angle = calculate_angle(shoulder_1, elbow_1, wrist_1,shoulder_2, elbow_2, wrist_2)
                            
                            #per = np.interp(angle[0],(20,160),(100,0)) # LEFT
                            #bar = np.interp(angle[0],(30,160),(600,200))
            
                            cv2.putText(image, str(round(angle[0],2)), 
                            tuple(np.multiply(elbow_1, [800, 720]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                
                            cv2.putText(image, str(round(angle[1],2)), 
                            tuple(np.multiply(elbow_1, [800, 720]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                            
                            #print(landmarks)
                            
                            #fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer) # Get frames per second
                            # Curl Counter Logic
                            color =(255,0,255)
                            if Signs[0]=="<" and Signs[1]==">":
                                # 2.) Oh- Press Curl Counter    
                                    if angle[0]<70:
                                           stage_o = "Down"
                                    if angle[0]>120 and stage_o=="Down":
                                            stage_o="Up"
                                            press+=1
                                            print(press)
                            
                    except:
                         pass
                            
                            # Render curl counter and status box
                    cv2.rectangle(image,(5,5),(270,80),(245,117,66),-1)
        
                            # fps
                            #cv2.putText(image,str(fps),(90,19),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 1, cv2.LINE_AA)
        
                            # Draw Bar
                    #cv2.rectangle(image,(1000,200),(1055,600),color,3)
                    #cv2.rectangle(image,(1000,int(bar)),(1055,600),color,cv2.FILLED)
                    #cv2.putText(image,f'{int(per)}%',(1000,170),cv2.FONT_HERSHEY_PLAIN, 2,color, 3)
        
       
                            # Rep data
                    cv2.putText(image,'REPS',(17,25),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 1, cv2.LINE_AA)
                    cv2.putText(image,str(press),(20,72),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
                            #Stage Data
                    cv2.putText(image,'STAGE',(120,25),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 1, cv2.LINE_AA)
                    cv2.putText(image,stage_o,(120,65),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2, cv2.LINE_AA)
        
                            # Render Class Name
                    cv2.putText(image,Class[1],(500,45),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), 2, cv2.LINE_AA)
        
               
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )   
                            
                    if results.pose_landmarks !=None:
                                    face_res, pose_res, full_frame_res, angle_res, elbow_flat_angle, elbow_straight_angle, hand_straight_angle = pose_estimate(
                                    results.pose_landmarks, image)
                                    if full_frame_res == 0:
                                          cv2.rectangle(image, (0,0), (800,720), (0, 255, 0), 10) # green
                                    else:
                                          cv2.rectangle(image, (0,0), (800,720), (0, 0 ,255), 10) #red
            
            
                    cv2.imshow("Mediapipe Feed",image)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                            break
        
                
                
            else:
                    cv2.putText(image,Class[2],(500,45),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), 2, cv2.LINE_AA)
                    cv2.imshow("Mediapipe Feed",image)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                           break
                
        #elif condition_0 ==:Angle_Ground
                   
    cap.release()
    cv2.destroyAllWindows()
                    