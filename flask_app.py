from flask import Flask, render_template, request, send_file,redirect,url_for, Response, redirect

app = Flask(__name__,static_folder="static", template_folder="templates")
import sys
import os

@app.route('/', methods=['GET','POST'])



def Menu_func():
    import os
    #capitalLet = os.environ['AWS_PASS']
    #smallLet = os.environ['aws-pass']
    

    #if request.method == 'POST':
    
        #Request form 3.0 hvis:
        #Request form 2.0 hvis:

        #Input_str = str(request.form['GoogleSearch'])
        #Input_str.replace(' ','+')
        
        #return redirect(google_url_1+Input_str+google_url_2,code=302)
    
    return render_template('Frontpage.html')



@app.route('/Quizpage', methods=['GET','POST'])
def Quizpage():

    Soeren_datascience = ["1_3","1_4","1_6","2_1","2_3","2_6","5_2","5_3","5_5","3_2","4_1","4_2"]
    Isabel_datascience = ["1_3","1_4","1_5","2_1","2_6","5_1","5_3","3_3","4_5","4_4",]
    
    Linnea_UX = ["1_2","1_4","1_9","2_1","2_4","2_6","5_1","5_3","3_2","4_3","4_11","4_1"]
    Jens_UX = ["1_2","1_5","1_9","2_2","2_6","2_3","5_1","5_2","3_2","4_1","4_11"]

    Daniel_udvikler = ["1_1","1_6","1_10","2_1","2_2","2_6","5_3","5_6","3_1","4_1","4_2","4_3"]
    Cathrine_udvikler = ["1_2","1_6","1_9","2_3","2_6","5_3","5_6","3_3","4_4","4_7"]

    Niklas_management = ["1_3","1_5","1_9","2_2","2_6","5_1","5_2","5_5","3_5","4_1","4_2"]
    Jeppe_management = ["1_4","1_5","1_9","2_3","2_6","5_5","3_5","4_3","4_8"]
    
    Sebastian_Industry = ["1_4","1_11","1_5","2_6","2_2","2_4","5_1","5_5","3_5","4_3","4_8"]
    Rasmus_Indsutry = ["1_4","1_11","1_5","2_3","2_1","2_4","5_1","5_4","3_4","4_5","4_11"]

    Nicolaj_automation = ["1_1","1_2","1_4","1_10","2_1","2_2","2_6","5_1","5_3","3_1","4_1","4_3"]
    Morten_automation = ["1_10","2_1","2_6","5_1","5_6","3_2","4_2","4_8",]

    Yasmin_graduate = ["1_5","1_9","1_10","2_1","2_6","5_1","5_6","3_2","4_7","4_11","4_10"]
    Philip_management = ["1_1","1_5","1_9","2_3","2_6","5_1","5_2","3_5","4_2","4_6"]

    Peter_automation = ["1_4","1_5","1_10","2_1","2_4","5_1","5_2","5_5","3_5","4_1","4_10",""]




    if request.method == 'POST':

        #--------------Request filled form-----------------#

        q0_1 = request.form["opt1radio"]
        q1_1 = request.form.getlist('question1_1')
        q2_1 = request.form.getlist('question2_1')
        q3_1 = request.form.getlist('question3_1')
        q4_1 = request.form.getlist('question4_1')
        q5_1 = request.form.getlist('question5_1')


        result_list = []
        Peter_score = 0
        Philip_score = 0
        Yasmin_score = 0
        Morten_score = 0
        Nicolaj_score = 0
        Soeren_score = 0
        Isabel_score = 0
        Linnea_score = 0
        Jens_score = 0
        Daniel_score = 0
        Cathrine_score = 0
        Niklas_score = 0
        Jeppe_score = 0
        Sebastian_score = 0
        Rasmus_score = 0
        Final_result = ""

        #-----Loop through & collect list answers----------#        

        for i in q1_1:
            result_list.append(i)
        for s in q2_1:
            result_list.append(s)
        for d in q3_1:
            result_list.append(d)
        for a in q4_1:
            result_list.append(a)
        for c in q5_1:
            result_list.append(c)

        #--------Match score with candidates--------------#

        for a in result_list:
            if a in Soeren_datascience:
                Soeren_score = Soeren_score + 1
        
        for a in result_list:
            if a in Isabel_datascience:
                Isabel_score = Isabel_score + 1
        
        for a in result_list:
            if a in Linnea_UX:
                Linnea_score = Linnea_score + 1
        
        for a in result_list:
            if a in Jens_UX:
                Jens_score = Jens_score + 1

        for a in result_list:
            if a in Daniel_udvikler:
                Daniel_score = Daniel_score + 1
            
        for a in result_list:
            if a in Cathrine_udvikler:
                Cathrine_score = Cathrine_score + 1

        for a in result_list:
            if a in Niklas_management:
                Niklas_score = Niklas_score + 1

        for a in result_list:
            if a in Jeppe_management:
                Jeppe_score = Jeppe_score + 1
        
        for a in result_list:
            if a in Sebastian_Industry:
                Sebastian_score = Sebastian_score + 1
        
        for a in result_list:
            if a in Rasmus_Indsutry:
                Rasmus_score = Rasmus_score + 1

        for a in result_list:
            if a in Nicolaj_automation:
                Nicolaj_score = Nicolaj_score + 1

        for a in result_list:
            if a in Morten_automation:
                Morten_score = Morten_score + 1

        for a in result_list:
            if a in Yasmin_graduate:
                Yasmin_score = Yasmin_score + 1

        for a in result_list:
            if a in Philip_management:
                Philip_score = Philip_score + 1

        for a in result_list:
            if a in Peter_automation:
                Peter_score = Peter_score + 1
        

        ##Add extra point to practice
        if q0_1 == "Software":
            Daniel_score = Daniel_score + 3
            Cathrine_score = Cathrine_score + 3
            Nicolaj_score = Nicolaj_score + 2

        elif q0_1 == "Design":
            Linnea_score = Linnea_score + 3
            Jens_score = Jens_score + 3

        elif q0_1 == "Management":
            Jeppe_score = Jeppe_score + 3
            Niklas_score = Niklas_score + 3
            Yasmin_score = Yasmin_score + 3
            Philip_score = Philip_score + 3
            Peter_score = Peter_score + 3
            
            
        elif q0_1 == "Datascience":
            Soeren_score = Soeren_score + 3
            Isabel_score = Isabel_score +3

        elif q0_1 == "Robotics":
            Sebastian_score = Sebastian_score + 3
            Rasmus_score = Rasmus_score + 3
        

        


        print(Daniel_score,Soeren_score,Jens_score,Cathrine_score,Jeppe_score,Niklas_score,Sebastian_score,Morten_score,Philip_score,Yasmin_score,Peter_score,Rasmus_score,Isabel_score)

        score_list = []

        score_list.append(Linnea_score)
        score_list.append(Jens_score)
        score_list.append(Daniel_score)
        score_list.append(Cathrine_score)
        score_list.append(Niklas_score)
        score_list.append(Jeppe_score)
        score_list.append(Soeren_score)
        score_list.append(Rasmus_score)
        score_list.append(Sebastian_score)
        score_list.append(Isabel_score)
        score_list.append(Nicolaj_score)
        score_list.append(Morten_score)
        score_list.append(Yasmin_score)
        score_list.append(Philip_score)
        score_list.append(Peter_score)


        max = 0

        for i in score_list:
            if i > max:
                max=i        
                winner = score_list.index(max)
                if winner == 0:
                    Final_result = "Linnea"
                    Img_Result = "Linnea.png"
                    disc_result = "You remind me of me! My name is Linnea, and I am a UX Designer at IBM Client Innovation Center. I have a bachelor's degree in Information Management and a master's in Service Design. My role is to be the users' ambassador and design concepts and solutions that provide value for people. I conduct research, facilitate workshops, create wireframes, and perform user testing. My hobbies include ceramics and other creative projects, as well as walking in nature with my dog. In my work, I value a strong social community, innovative frameworks, and the fact that each day can look completely different."
                elif winner == 1:
                    Final_result = "Jens"
                    Img_Result = "Jens.png"
                    disc_result = "My name is Jens, and I am a UX Designer. I have a bachelor's degree in Communication and Digital Media and a master's in Information Studies. In my project, I am involved in many different tasks. I design solutions for our clients' users, based on their needs, so my work primarily involves user research, prototyping, and user testing. I love almost all sports—both watching and participating—and I enjoy good food in great company. I highly value my colleagues and the camaraderie we have in the CIC. People are always willing to help, and there is a strong social engagement in the center. Additionally, I appreciate the variety of projects and the close collaboration with high-profile individuals such as partners, where you can really soak up learning."
                elif winner == 2:
                    Final_result = "Daniel"
                    Img_Result = "Daniel.png"
                    disc_result = "You remind me of me! My name is Daniel, and I am a Software Developer at IBM Client Innovation Center. I graduated as a computer scientist from KEA and work daily as a developer on various monitoring projects for our clients. I love to develop and spend much of my free time on it—besides lifting heavy weights from time to time. One of the things I value most in my daily life is the collaboration with my colleagues and our community—it’s top-notch!"
                elif winner == 3:
                    Final_result = "Cathrine"
                    Img_Result = "Cathrine.png"
                    disc_result = "You remind me of me! My name is Cathrine, and I am a Frontend Developer at IBM Client Innovation Center. I have a bachelor's degree in Business Administration (Communication) from CBS and a master's in Software Development from ITU. I work daily developing in React, JavaScript, HTML, and CSS, where we regularly hold product demos with the client. In my free time, I enjoy being active and participate in running (including in the CIC's running club), CrossFit, and other yoga/pilates-inspired training. I greatly appreciate being able to combine my technical skills with my communication background as a consultant at IBM Client Innovation Center."
                elif winner == 4:
                    Final_result = "Niklas"
                    Img_Result = "Niklas.png"
                    disc_result = "You remind me of me! My name is Niklas, and I am a Project Manager at IBM Client Innovation Center. I have a master's degree in Information Management from Aarhus University BSS and also work as a Scrum Master and Agile Coach. My job mainly involves networking and facilitating transformations for our various clients. In my free time, I spend a lot of time gaming, working out, and relaxing with my loved ones. What I value most about my work is the young, ambitious camaraderie, which also places a strong emphasis on a fun and stress-free workplace."
                elif winner == 5:
                    Final_result = "Jeppe"
                    Img_Result = "Jeppe.png"
                    disc_result = "You remind me of me! My name is Jeppe, and I am an IT Business Consultant at IBM Client Innovation Center. I hold a master’s degree in Digital Transformation from Aarhus University BSS. In my daily work, I am a Product Owner, leading a cross-functional team of developers, business people, and testers in a Scaled Agile Framework setup. My primary task is to bridge business and IT so the team delivers maximum value. In my free time, I play a lot of tennis. The best part of my job is my amazing colleagues—we have an incredible amount of fun. In my current role, I get to drive the innovation agenda and am also involved in digital strategy work, which I find really exciting."
                elif winner == 6:
                    Final_result = "Søren"
                    Img_Result = "Soeren.png"
                    disc_result = "You remind me of me! My name is Søren, and I am a Data Scientist at IBM Client Innovation Center. I hold a master’s degree in Quantitative Economics from Aarhus University and help our clients use their data more intelligently by leveraging the latest technologies in AI and Machine Learning. In my free time, I enjoy spending time with my friends, food, and golf—preferably all at once! The best part of my job is working with the coolest people and contributing innovative solutions."
                elif winner == 7:
                    Final_result = "Rasmus"
                    Img_Result = "Rasmus.png"
                    disc_result = "You remind me of me! My name is Rasmus, and I am an Industry 4.0 Consultant at IBM Client Innovation Center. I have a background as a civil engineer in Operations and Innovations Management, primarily focused on process optimization and business strategy. Currently, I am focused on building our team, developing strategies, and creating products. Outside of work, I have a great passion for sports and film production. What I enjoy most about my job is the opportunity to work on things I am passionate about, alongside fantastic people."
                elif winner == 8:
                    Final_result = "Sebastian"
                    Img_Result = "Sebastian.png"
                    disc_result = "You remind me of me! My name is Sebastian, and I am an Industry 4.0 Consultant at IBM Client Innovation Center. I have a degree in Manufacturing Technology from Aalborg University, focusing on Digital Manufacturing and artificially intelligent robots. I’m the sporty gamer type who can easily lock myself away for an entire weekend to hold a LAN party with the guys—but I can also get really upset if I miss a workout. I spend a lot of time with family and friends, often engaging in activities that include physical exercise, like padel tennis. I love spending money on trips to warm destinations and ski vacations—life isn’t just about work, and there’s room for that here."
                elif winner == 9:
                    Final_result = "Isabel"
                    Img_Result = "Isabel.png"
                    disc_result = "You remind me of me! My name is Isabel, and I am a combined Data Scientist and Project Manager at IBM Client Innovation Center. I have a degree in Biomedical Engineering from DTU and handle a wide range of tasks daily—from setting up sensors for the Watson IoT Platform and modeling data to facilitating daily stand-ups in the project team and discussions with clients. In my free time, I play handball and sail when the weather is nice. I love that every day is different at IBM Client Innovation Center and that I get to meet many diverse clients and companies. Additionally, I enjoy my (young and fun) colleagues. Innovation and creativity are at the forefront of my projects, and I work with new, exciting technologies."
                elif winner == 10:
                    Final_result = "Nicolaj"
                    Img_Result = "Nikolaj.png"
                    disc_result = "I’m a bit like you! My name is Nicolaj, and I’m an Automation Developer at IBM Client Innovation Center. I have a bachelor’s degree in IT Product Development, and I spend my days developing automation solutions to free up valuable customer resources. In my free time, I enjoy gaming and spending time with my friends. The best part of my job is that I get to challenge myself and work with new, customer-relevant technologies."
                elif winner == 12:
                    Final_result = "Yasmin"
                    Img_Result = "Yasmin.png"
                    disc_result = "I’m a bit like you! My name is Yasmin, and I’m an Automation Associate at IBM. I have a master's degree in IT Management, and I work in a coordinating and facilitating role, acting as the link between IT and the business—kind of like a mini project manager. I work with process mapping and gather knowledge from various sources, which is analyzed to inform decisions and initiate projects. In my free time, I spend time with my friends and family—and maybe a bit too much time on Instagram. One of the things I value most at IBM is the feedback culture. There is a strong focus on both personal and professional development. It’s AMAZING to have that opportunity, as not all companies prioritize it. Additionally, there are great opportunities for training in both Denmark and abroad—the possibilities are endless, and you can acquire all the knowledge you desire. You have colleagues who are highly skilled and willing to share their expertise."
                elif winner == 13:
                    Final_result = "Philip"
                    Img_Result = "Philip.png"
                    disc_result = "I’m a bit like you! My name is Philip, and I’m a Cognitive Process Transformation Consultant at IBM, where I started in our Associate program in 2015. I have a background in Human Resource Management from CBS, and I work daily in project management closely with clients to deliver IT solutions that support their business transformation—we're part of a large international team of functional and technical experts. In my free time, I enjoy sailing, skiing, and doing triathlons—all as hobbies to foster social connections and maintain my energy levels in a busy everyday life."
                elif winner == 14:
                    Final_result = "Peter"
                    Img_Result = "Peter.png"
                    disc_result = "I’m a bit like you! My name is Peter, and I’m an IT Business Consultant at IBM. I have a master's degree in Information Management from Aarhus University BSS, and I work daily as a business analyst on an automation project. Here, I uncover the business's critical processes with stakeholders and coordinate with the automation team. In my free time, I’m really into good coffee, delicious food, and movies—especially Oscar films and Hitchcock. What I value most about my job is the freedom to achieve my goals, the variety of tasks, and the opportunity to create my own work with new projects and roles."
                else:
                    Final_result = "Wow! You have a wealth of skills—you’ve matched with several of our profiles!"


        return render_template("Result.html",result = Final_result, img_Result=Img_Result, Disc_result = disc_result) 

    return render_template('Quizpage.html')




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8001)