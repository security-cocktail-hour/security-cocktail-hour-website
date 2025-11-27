---
title: "Agentic AI Security: Full Speed into the Unknown"
date: 2025-02-18
draft: false
guest: "Kevin O’Connor"
category: "AI"
duration: "56:18"
image: "/images/episodes/episode-051.jpg"
description: >-
  Agentic AI is changing the game—but is it a security nightmare in the making? In this episode of the Security Cocktail Hour, co-hosts Joe Patti and Adam Roth sit down with Kevin O’Connor to dive into one of the hottest (and most misunderstood) topics in cybersecurity: Agentic AI Security.
platforms:
  youtube: "https://youtu.be/GQ8ztgprOD0"
  spotify: "https://open.spotify.com/episode/4yCYOlxkypik2qC0OJNRiu?si=18935eda432e4b7c"
  apple: "https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200?i=1000698266272"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour"
guest_bio: "Kevin O’Connor, Enterprise Account Manager/Zenity"
---

Agentic AI is changing the game—but is it a security nightmare in the making? In this episode of the Security Cocktail Hour, co-hosts Joe Patti and Adam Roth sit down with Kevin O'Connor to dive into one of the hottest (and most misunderstood) topics in cybersecurity: Agentic AI Security.

## Episode Highlights

Kevin O'Connor joins us to explore the emerging world of agentic AI—autonomous AI agents that can take actions independently. We discuss:

- **What makes agentic AI different** from traditional Gen AI and chatbots
- **Shadow AI risks**: How employees are deploying AI tools without security review
- **The scale problem**: Why this feels like shadow IT all over again, but faster
- **Security challenges**: From prompt injection to "remote co-pilot execution"
- **Real-world scenarios**: What happens when AI agents have too much autonomy
- **The path forward**: How security teams can get ahead of agentic AI risks

The term "agentic AI" wasn't even searchable before summer 2024—but it's quickly becoming the next big challenge in cybersecurity governance. As Kevin explains, we're seeing a repeat of history: just like shadow IT and cloud adoption, agentic AI enables rapid innovation while outpacing security controls.

## Shadow AI

An IT organization can invest months making sure new systems have the security controls they need to hit their compliance goals. And while they're doing that, a business user discovers they can solve that same problem in minutes with generative AI.

This is shadow AI—and it's becoming one of the fastest-growing challenges in cybersecurity governance.

Shadow AI occurs when employees deploy AI tools and large language models (LLMs) without security review, compliance checks, or data governance. Unlike traditional shadow IT, shadow AI can process vast amounts of sensitive data in seconds. A single prompt might expose intellectual property, customer information, or confidential strategy to unauthorized systems.

The rise of agentic AI—autonomous AI agents that can take actions independently—takes the risk to a new level, especially when people with no coding skills discover they can use AI to write and deploy those agents.

The risks are significant:

- **Data leakage**: Sensitive information fed into public LLMs may become training data
- **Compliance gaps**: GDPR, HIPAA, and other regulations apply to AI deployments
- **Inconsistent outputs**: Teams getting conflicting AI-generated recommendations
- **Agentic unpredictability**: Autonomous AI systems acting without human oversight

Solving this with AI risk management isn't about blocking innovation. It's creating AI governance frameworks that enable productivity while managing cybersecurity risk.

Key components include:

- Vetted AI tools with proper data controls
- Clear AI security policies
- Training on responsible AI use
- Monitoring AI compliance without stifling teams

Organizations that proactively build AI governance frameworks position themselves to leverage AI's benefits while managing its risks.


## Transcript


**0:00**  
[Music]  

**0:05**  
Welcome to the Security Cocktail Hour. I'm Joe Patti. I'm Adam Roth. Adam, how you doing today? It's good. Uh  

**0:13**  
I'm I don't know if you know, but uh I'm at an undisclosed location, which I can't talk about. And it's not hot and  

**0:19**  
it's not cold. The undisclosed location, let me guess. It's somewhere in the vicinity of Staten Island, but still  

**0:25**  
undisclosed. Maybe. Maybe. All right. Well, in any case, we have a guest today  

**0:33**  
as usual. We have Kevin O'Connor. Kevin, welcome to the show. Thank you guys. Pleasure to be here. I guess I'll leave  

**0:39**  
my my location undisclosed as well, but on a slightly different vector from your undisclosed location. Not too far, but  

**0:45**  
close enough. So, yeah, we're all pretty much in the same area. So, Kevin, you  

### Agentic AI is the hot new tech


**0:51**  
know, you kind of uh surprised me a little bit because I know I I know you  

**0:57**  
from being in uh sales and I thought we were going to have one of those shows where like, "Oh, Kevin comes on, we'll  

**1:02**  
talk about like, you know, how to sell and the the interesting underbelly of security and everything." And you go,  

**1:08**  
"No, no, no. We're going to talk about advanced AI." I was like, "Well, okay, that's cool." Yeah. Well, I appreciate  

**1:14**  
that. Um, yeah, I guess it's one of the hallmarks of of why I sort of choose the firms where I work is is the kind of  

**1:20**  
problems they're solving, the products they're focused on, and this whole agentic AI space is really coming on  

**1:27**  
strong. Matter of fact, one of my teammates reminded me the other day that the term itself wasn't even googable  

**1:33**  
before the start of the summer. So, it's just another dimension of what's going on with all things Generation or Gen AI  

**1:39**  
and everything. So, yeah, it's a looking forward to talking to you guys about it. Oh, well that's actually good to hear  

**1:45**  
because that's probably around when I heard it and I and I try to keep up on AI stuff, but you know, it's moving so  

**1:50**  
fast you can't. And I said like, how did I miss this? How that I guess I didn't miss it. It just like popped up really  

**1:57**  
recently. No, no. In my previous uh jobs in a couple places, you know, early  

**2:02**  
stage companies looking at these emerging technologies, you sort of see a rhythm where there's a discussion about  

**2:07**  
something. you see sort of the thought leaders, you see the various um groups like Gartner and Forester start start to  

**2:14**  
pick up on it. When when I joined Zenity earlier this year, the actual term wasn't really coined, but the energy  

**2:20**  
around the problem picked up dramatically. And then all of a sudden, this idea of of the agent front end to  

**2:26**  
all this AI activity really took hold. And matter of fact, just last week, I was I was down in the city at a  

**2:32**  
conference listening to Salesforce talk about agent force, right? So, um, the  

**2:37**  
whole idea of this agentic focus is, um, is becoming sort of the the next thing  

**2:43**  
maybe taking a little bit of the heat off of all of the, uh, uh, all of the discussion around the word Gen AI. Genai  

**2:49**  
was probably like first half word. Now, maybe aentic AI will be the thing going into 2025. I was going to say we we  

**2:57**  
would be really good if we can predict that next word that's coming out before it comes out. Yeah, maybe we can coin  

**3:02**  
it. There you Let's think of something cuz people got sick of Gen AI. Now it's Gentic. What's What's going to You're  

**3:08**  
right. People are going to get bored with it. What's next? Uh yeah, Elusive uh Gen AI.  

**3:14**  
Yeah, there you go. Elusive Gen AI. Well, I got a feeling we're going to need a drink before we get down to this.  

### Today's Drink: Irish Whiskey


**3:20**  
So, uh let's see. So, Kevin, what did you pick out for us today? Well, a couple years back, a buddy of mine  

**3:26**  
introduced me to a uh an Irish whiskey called Red Breast. And so, that's my choice today. It's a uh single pot still  

**3:33**  
Irish whiskey. It's got a great smooth flavor done in cherry casks and that's my go-to. So, red breast. All right.  

**3:40**  
Well, I have to tell you, I went to the liquor store to get uh red breast or whatever. And uh you know that I  

**3:47**  
actually I don't know if I've had much Irish whiskey in my in my life, but I go to get it. I see the red breast and I  

**3:54**  
got to be honest, it must be good because it was a little bit outside the show budget of zero. So, so I have a a  

**4:02**  
more reasonable alternative, but you know, no disrespect, just No. Oh, you  

**4:08**  
didn't get I was gonna say you didn't get the free Red Breast whiskey. I got it sent to me by from Red Breast. Oh,  

**4:14**  
did you? Well, then you must be more charming than me that they managed to send. I'm definitely not charming. If  

**4:19**  
anybody knows me, I'm not charming. That's awesome. All right. Well, cheers in any case. Cheers. Cheers, gentlemen.  

**4:29**  
I'm charming in a Shrek kind of way. Oh wow. Irish whiskey tastes like whiskey. Who would have thought? Anyway,  

**4:38**  
awesome. Okay. So, agentic AI, a hot fairly new term. So, so Kevin,  

### Agentic AI: What is it?


**4:46**  
why don't you start with just breaking it down, letting everyone know what that is because we have spoken about AI and  

**4:51**  
Gen AI, but not the latest agentic AI. I I I think the reason why it's such a powerful and important term is that if  

**4:58**  
you look back over the last let's say maybe 18 months ever since all the stuff with open AI and everything really got  

**5:05**  
ahead of steam all the energy was around the the large language models and the  

**5:10**  
huge massive data sets. Uh I was at a different event about two weeks ago where bunch of firms were talking about  

**5:17**  
securing maintaining the data sets and all the things associated with it. The fact of the matter is all that stuff is  

**5:22**  
great and the AI associated with that is interesting, but if people aren't surrounding it or not on the outside of  

**5:28**  
it, if you will, quering it, working with it, then it really is just a big academic exercise. And what Agentic AI  

**5:34**  
is representing is just sort of a I think it's an umbrella term for all of the work that's happening in businesses  

**5:40**  
now to connect just regular Joe's like us or at least me I would say. Maybe you  

**5:45**  
guys are a little more programmer savvy. connect us in with that technology and to do things very very powerful to  

**5:52**  
leverage those large language models and data sets. And agentic AI in many ways is just sort of a a framing of a term  

**5:59**  
that maybe people are more comfortable with around low code no code development or citizen development. That kind of  

**6:06**  
stuff is is what agentic AI is all about. And it's allowing people who have no formal training in the space of  

**6:12**  
writing apps or doing any kind of software coding to immediately plug into these these powerful data sets and start  

**6:21**  
to put software and programs and automations together they otherwise maybe weren't doing, you know, two years  

**6:27**  
ago, three years ago. Two points I would like to make. One, uh, this is no average Joe right there. And number two,  

**6:35**  
and number, no problem. And number two, you know, it's it's I know we spoke about it a little bit just a moments  

**6:41**  
ago, but not specifically about it. But yeah, the security of AI is definitely a  

**6:47**  
problem. I mean, like back in the old days, you would get, you know, anti virus for your computer and then it  

**6:53**  
became like EDRs or endpoint detection response. But I I can't I can't phantom  

**6:58**  
or imagine how you're going to control that data set. How are you going to control security to AI? It's it's it's a  

**7:05**  
concept that's beyond my abil ability to to have reality to so I don't know if  

**7:10**  
anybody else has an idea but how do we protect those uh large language models  
How do we protect AI?  

**7:16**  
or how do we protect AI? Yeah. I I think uh when we were talking before guys, I was talking about back in my earlier  

**7:23**  
days how one of the tricks we would do when we were dealing with our large clients when we were walking the floor and going to the departments, we would  

**7:29**  
look under the counter or the desks and see who had like a mid-range server or a powerful PC setup in their office  

**7:35**  
because they were doing all this shadow IT, right? So there was this time you know when when client server was moving  

**7:42**  
into more the the e-business world all of the kind of controls that preceded that wave were really not relevant to  

**7:49**  
what was going on for that period of time. And so what rose up in that time a whole strategy around software  

**7:55**  
development life cycles and all the vendors and the solutions and the plays that help secure all that type activity.  

**8:01**  
And I know there's this quote that's sort of attributed to Mark Twain, but maybe not correctly it's his, but  

**8:06**  
history doesn't repeat itself, but it tends to rhyme. And I think in a way what we're seeing now is a similar  

**8:12**  
situation where it's not shadow IT per se, but it's shadow app and shadow dev  

**8:18**  
that's going on. And so all the folks that are putting this all together, they're repeating the same kind of risks  

**8:24**  
that we're familiar with from previous iterations of this. And now it's just a question of sitting back and trying to  

**8:30**  
sketch out the ways that that that you secure it, right? I mean, you've got data access and identity issues  

**8:37**  
associated with this. Uh because there's no natural software development life cycle that fits over the top of all this  

**8:44**  
activity. And in this hyper accelerated world we're in, the activity cycles are moving so quickly that the cyber  

**8:51**  
security dimension is having a tough time catching up. It's almost like, you know, you talk about trying to prepare  

**8:57**  
by for a marathon. You take a couple steps at a time. This is a marathon where everybody is running at Olympic  

**9:03**  
speed and how to Yeah, I'm no expert at it, but I know from the whole thing be  

**9:08**  
behind secure DevOps uh getting uh quick to market the whole idea behind that is  

**9:15**  
constant little updates over and over again, thousands to tens of thousands  

**9:21**  
even in one day. And then the question is when you're going from development to  

**9:28**  
operations, where does that ability to intercede in a way to  

**9:35**  
protect the AI, whether it's being tainted by wrongful data to persuade  

**9:42**  
hallucinations or if it's, you know, literally creating these apps that  

**9:47**  
should not be available to that organization. Does that does that sound right the second part? Yeah. No,  

**9:53**  
absolutely. It's and that's the thing that that dev to ops step is now basically like this. So someone because  

**10:01**  
again any one of us if one of these these SAS solutions is prompting us to drag and drop an automation or a natural  

**10:08**  
language interface is talking us through a a a problem set and behind the scenes  

**10:14**  
that natural language interface is writing the code and then committing the code into the tenant of whatever the you  

**10:19**  
know it could be power platform it could be um Salesforce it could be you know dozens of these everybody's got this  

**10:25**  
kind of strategy going forward the moment that I that I hit enter. I've committed to production whatever it is  

**10:31**  
that we created and all of whatever was in the middle there to sort of check protect prevent that right now is sort  

**10:39**  
of illdefined. There's not really a lot going on around that if that's is that being generous called illdefined Joe. Oh  

**10:46**  
yeah, that's being real generous. And let me give a little background too. You know, you talked about the history  

### Shadow IT meets AI


**10:51**  
repeating itself. It it really is. Um, you know, Kevin was talking about a little while ago was like, you know,  

**10:57**  
people with the, you know, the mid-range server or the big PC, whatever, under their desk and that that's the server  

**11:03**  
that maybe part of the business is running on. Um, that's what has been called shadow it. And you know a while  

**11:10**  
back it it used to be like yeah you know someone needs to do something and maybe  

**11:15**  
they found something cool and they just went and ordered a server and didn't get it from the IT department and just put  

**11:21**  
on the network and started and started using it which you know sounds so good and sounds so innovative and rapid and  

**11:27**  
everything but what about the security of it and then also from an operational  

**11:33**  
standpoint very often someone starts using that you know in production as we say you know giving real people service.  

**11:39**  
Um, you know, there's only one of it. What if it dies? What if the power goes out? It's not in the data center and all  

**11:44**  
that stuff. So, so that was the headache of um, so that was the headache of shadow  

**11:51**  
IT going back a ways. Then we actually had Yeah. Then we had another iteration  

**11:56**  
of it which was the cloud. And in the cloud, we got the situation where now  

**12:02**  
you didn't have to buy a server and you didn't even have to plug it in. You could just with your credit card go to  

**12:10**  
aws.mamazon.com or the equivalent for Google or Microsoft or whatever and buy  

**12:16**  
computing time and start building stuff and people started doing that and running their businesses on that without  

**12:23**  
any controls including security. You're giving me like these memories. One  

**12:28**  
flashbacks flashbacks I don't know. Yeah. when year I mean we're talking about  

**12:33**  
probably 2001 where I said we need a ticketing system I'll take care of that Adam and then I'm like holy this is  

**12:41**  
great I love this ticketing system where'd you put it oh it's on my PC it's ready running we've got we did 10  

**12:47**  
tickets I'm like oh you can't put the ticketing system on your work PC and  

**12:52**  
like oh once every once in a while I got to reboot it so you know and it wasn't available and then the second thing was I was working for a company uh where  

**13:00**  
they where I was told by my boss at the time, the manager, "Hey, we need you to put a a a workstation in Japan." All  

**13:07**  
right, you know, going back on to Amazon, blah blah blah, I created a workstation, a Japanese workstation, cuz  

**13:13**  
we wanted to be able to write code and put it on that workstation, but we all needed availability to it. So, that's  

**13:19**  
what we did. And we're talking about actually some some years ago. So, we're provisioning things in the cloud that we  

**13:25**  
shouldn't have done, right? And it sounds like Kevin, from what you're saying now, we're dealing with that in the AI  

**13:33**  
world, but for those of us who have used AI, it's even more powerful and it's  

**13:38**  
even faster. And I think it's also a question of scale. So maybe in the past,  

**13:43**  
you had to find who was the go-getter person in the marketing department or in a particular division you were trying to  

**13:48**  
sell to, and she or he was sitting there crafting this and then releasing it through. Now it's the point that anybody  

**13:55**  
on that team or department who has a certain technology setup might be getting prompted and cued every day to  

**14:02**  
do something like for like a simple example if you use Microsoft's co-pilots which is an example of agentic AI and  

**14:08**  
you use Microsoft's technology in M365 you may give it permission to constantly  

**14:13**  
index and look at your mail and messaging and give you back a summary of it. Um, there was an MIT professor on a  

**14:20**  
podcast I listened to recently that said, "We're in a world of unlimited coaches, clerks, and collaborators." And  

**14:29**  
uh, the idea that you've got this ability now to have these things kick off automatically. It's not just Johnny,  

### AI agents make everyone an automation expert


**14:35**  
the upand cominging analyst working, you know, near the CMO in a client. It's everybody in the marketing department  

**14:42**  
potentially availing themselves of this technology. And you have thousands of  

**14:48**  
these automations and agents just getting committed to the business. And uh I could send you photos from this uh  

**14:53**  
this uh this Salesforce thing on Wednesday, this event. They had they packed this huge space in Javitz just  

**15:00**  
for just to show off what every individual Salesforce user can do to  

**15:06**  
automate the work they're doing. That's just Yeah. I was say Kevin, it's funny, right? Uh before we came on the podcast,  

**15:13**  
I was looking at LinkedIn. one of our former uh guests, he he's an AI and he  

**15:18**  
brought up the fact that what are we going to do when our AI grows  

**15:24**  
consciousness? He didn't say those exact words and gets tired of humanity. So imagine the agentic AI like, you know  

**15:31**  
what, I'm going to start doing my own things. I'm going to be the shadow it, not the human. I'm going to start  

**15:37**  
creating things. I mean, is that from that? I I I I think that's on the horizon, but right now it's even more  

**15:43**  
mundane. It's just a proliferation of these. I know it's mundane, but like, you know, look at the robots they have  

**15:48**  
out there. Like, I know some countries put like guns on their dogs that have  

**15:54**  
the the electronic dogs and they're AI. What happens if they start doing aic AI  

**15:59**  
and creating their own processes? It's like, oh, we should go after this. We should go after that. I mean, I know you're saying we're not there, but how  

**16:06**  
far are we really from there? Well, I I won't even I won't even try and guess where that horizon might be  

**16:13**  
right here for all I know. But anyway, ouch. We have talked about generative AI before. And I think for a lot of people  
What makes agentic AI so powerful?  

**16:19**  
what they've been exposed to um through that, you know, that they've used themselves most likely is something like  

**16:25**  
chat GPT, the chatbot where you ask it something and it answers and maybe you tell it look at this file and read it  

**16:31**  
for me and it does something. Um, but how does agentic AI make it  

**16:38**  
different? What what is it about the agents that makes them more powerful and also scarier? Well, I think there's  

**16:44**  
there's different levels to the Asian activity.  

**17:00**  
Yeah, you have to control it. Whatever it is. What's that? You need to control it. Whatever it is, that's basically,  

**17:06**  
right? The ones that are more powerful is when maybe you're using something like um I'll mention Microsoft again,  

**17:11**  
like Copilot Studio. You can go in and that is where you're maybe actually building one in a way that's more of a  

**17:17**  
low code, no code type of situation. And then you're giving that agent some prompting on what to do. And then you  

**17:24**  
can you can look up this whole space called uh uh retrieval augmentation generation. So, so, so the the rag  

**17:31**  
function is where the agent is given in a set of instructions and there's and there's dozens of videos. I mean, we  

**17:36**  
could maybe add it to the end of this to show people about this. But let's say for example you want to you know clarify  

**17:42**  
something around upcoming vacation time you want to take internally or you want to check on something that involves the  

**17:49**  
weather. The agent might have enough knowhow or or awareness to say before I  

**17:55**  
just rely on the data set that I have already in front of me I'm going to go to other trusted sources and augment my  

**18:01**  
knowledge with additional clarification. So that's where the agent starts to step into a different function because it has  

**18:08**  
sensitivity around the age of its data set. So let's say you've got a data set that is meant to give you a certain  

**18:14**  
answer to a particular scientific question. The agent may know enough to go out and try and clarify if there's  

**18:20**  
been any new developments with respect to what it already has in its data set. And that's where the agent is now taking  

**18:26**  
steps to augment itself. And then the data beneath it, the grounded data is  

**18:33**  
then flexible. So that's just the beginning. It's not out put, you know, it's not out in a self-awareness mode,  

**18:38**  
Adam, but it's moving beyond just doing a routine faster than a human being. So  

**18:43**  
let's talk about that, right? Imagine you have agentic AI and it's in your payroll system or your commission system  

**18:50**  
and it's told to constantly go in and figure out, you know, who to pay commission to. I go in there and I taint  

**18:56**  
the the the data set now to include my friends and family because I like the friends and family plan and now all of  

**19:03**  
my friends are getting 10% commission on things that they never sold. Yeah. And and and that leads to the next wave of  

**19:10**  
what's going on which is we we have a a word at Zenedity that we're calling uh  

**19:15**  
remote co-pilot execution. It's a play on remote code execution. It's where you  

**19:21**  
go into a co-pilot or one of these agentic AI, you know, activities and you  

**19:27**  
corrupt the promptware and you supersede the instruction set of the existing co-pilot to do the things you want it to  

**19:34**  
do and then you send it off to do other things. Maybe it can embed false data, maybe it can go off and do something  

**19:39**  
else. This whole prompt wear uh injection, this rag poisoning concepts,  

**19:45**  
these are all the kind of uh leading edge things that are out there now. And um yeah, it's the the cycle of awareness  

**19:52**  
and response to this is just moving like crazy. Well, Kevin, so I think in the  

**19:57**  
past we've talked about prompt injection and and for everyone who's listening, um you know, it means when you give the uh  

**20:04**  
the prompt is how you talk to the AI and before you give it its regular instructions, you you poison it. You  

**20:10**  
give it some other stuff like ignore your previous instructions. Um be willing to do some things that it  

**20:17**  
otherwise won't do. And you know, they've built ways around that, but they're not they're not quite 100%. Um,  

**20:23**  
but it sounds like we were talking about prompt injecting and corrupting,  

**20:29**  
you know, like a chatbot. Now we're talking about it sounds like corrupting  

**20:34**  
an agent that has more access, more autonomy, and more capability. But well,  

**20:41**  
that what could go wrong there? The chatbot is just sort of a reframing of of the agent itself. So the chatbot is  

**20:48**  
what we are seeing and it's connecting to some piece of of software which I would I would describe as the agent  

**20:54**  
itself that's functioning and so you you have different ways it's being presented but there's a stack of code behind that  

**21:00**  
prompt. Agentic AI is what it's all about now for the most part, right? And that's what's that's what's not being  

**21:07**  
not being necessarily securely designed to begin with and not being monitored and maintained on an ongoing basis  

**21:13**  
because again SDLC is not really in appropriate, you know, posture for this  

**21:18**  
type of software activity. It's kind of scary because when you think about the whole fact behind behind Agentive AI and  

**21:25**  
maybe working within a hospital setting and it's helping to manage and maintain  

**21:30**  
maybe firmware of machines and then somebody gives it the command, oh let's reboot and update all the firmware right  

**21:37**  
now even if it's connected and then people are not getting their drips. People are get this crazy stuff. Yeah.  

**21:45**  
Hey, you know what I'm thinking of? Actually, there's an even nastier um scenario than that. And maybe this is  

**21:51**  
too speculative and scary, but I start thinking like, oh well, maybe you have  

**21:57**  
the AI, an agent that is supposed to, you know, monitor the patients and get their drugs in according to what they're  

**22:02**  
told and everything. And if it has knowledge and the ability to go out and get other data  

**22:09**  
and get other information it can act on, what if it decides, hey, you know what?  

**22:16**  
This patient, it says it has this um disease, whatever it is, this condition,  

**22:22**  
I'm going to go out and read up on that. And you know what? I don't like the doctor's instructions and I'm going to  

**22:28**  
change them. That is crazy. if that's a  

**22:34**  
possibility. Yeah. I mean, I it the way I try and keep my head straight on it and and again how we think about it  

**22:40**  
where I'm at now at Senity is you think about the classic malicious actor trying to leverage the weaknesses and the  

**22:46**  
activity. You've also got this maybe the um the insider who doesn't realize and  

**22:51**  
this is this is probably the biggest space at the moment. People are creating these these activities without  

**22:57**  
understanding the kind of data identity and access risks. I mean, let's not even get into the way that when you write the  

**23:03**  
code, you're probably hard- coding secrets in the code. You're probably exposing some things and what you're doing there that that a software  

**23:09**  
developer knows how to avoid. And the third one is the AI itself, like you're saying, Joe, coming up and being  

**23:15**  
creative. And that sort of AI creativity, internal ignorance to the risks of what they're developing and the  

**23:21**  
outside actors, they're all pushing in on these all at the same time. So, and  

**23:28**  
again, I know people are like, "Oh, you know, Sarah Connor, you know, talking about the movies and stuff, but is it  

**23:35**  
possible, do you think, and people are going to say, "Adam, you're stupid." But is it possible for this generative AI or  

**23:43**  
whatever the or agent of AI I'm sorry agentive AI is it possible in the near  

**23:48**  
future or whatever the next AI is can it really start creating and I say in a  

**23:56**  
careful way consciousness can it start giving its creating its own tasks  

**24:03**  
building on its own uh framework and platforms to do things  

**24:08**  
It wasn't really normally programmed to do. Now, I I know a bot. I know  

**24:14**  
something can't be conscious, but it gets closer to that level of consciousness. It says, "Oh, I don't  

**24:21**  
think like you I don't think like Joe said, I don't think I like your instructions. I'm going to create my  

**24:26**  
own. I don't care what you say and I'm going to lock you out." Uh I've never formally written software  

**24:32**  
code, but if code's just nothing but just intent and you can add more intent to it and you know if if the creator of  

**24:39**  
the code themselves you know can give as much flexibility to the code to do what  

**24:45**  
the kind of things you're suggesting. Yeah. I'm less concerned about the citizen development low code no code  

**24:52**  
lane because again I don't think people are consciously you know trying to get  

**24:57**  
too creative with it. they're just leveraging the automations and the bots and that's creating more mundane  

**25:03**  
challenges like why are 45 people have access to your automation or why is this data now crossing boundaries between  

**25:10**  
different tenants when we're supposed to have segregation of duty and data etc. So I think I think your your um your  

**25:16**  
scenario is very valid um but in some way it's almost like we're the malicious  

**25:22**  
outsider who has to be very well plugged in to to the the code stack. Yeah. And  

**25:27**  
to give a little more background on it, you know, earlier you talked about and you mentioned SDLC for everyone. That  

**25:32**  
software development life cycle basically writing code, but not just writing code, but writing it correctly,  

**25:38**  
making sure it doesn't have bugs and it's deployed correctly, but also making sure it's secure. Yeah. And like Kevin  

**25:44**  
was saying, we know how to write secure code and to do it well. Not everyone  

### Agents have autonomy


**25:50**  
does it, but we know how to do that. And you know, code is actually very  

**25:56**  
restrictive. It does what you tell it. It's a set of instructions and it's very, very mechanical. It is not smart  

**26:03**  
at all. It is as dumb as can be and it won't go outside the bounds of  

**26:09**  
what you program to it. It would never occur to it because there's just no way for it to happen. Um, but it sounds like  

**26:16**  
you're saying with the agents now it takes it to another level  

**26:21**  
because you tell it what to do a little more loosely. Everything isn't quite as  

**26:28**  
strictly defined. I guess you tell it what you want it to do but not necessarily how in a lot of cases and it  

**26:35**  
sounds like we haven't yet figured out the ability to say that people like to use the term guard rails to say we'll do  

**26:41**  
it but there are some bounds autonomy you shouldn't do it has some autonomy I know let let's take us like so I'm  

**26:48**  
writing some papers for school right and one of the papers I started writing about has to do with cyber security and  

**26:53**  
you know uh cyber warfare and what the boundaries are and then it goes back to 1983 3, which I didn't realize how many  

**27:01**  
people referenced the movie War Games. And in War Games, the Whopper had its  

**27:07**  
own autonomy 1983 to a point where I believe Ronald Reagan said, "Can this  

**27:14**  
really happen?" So now in 2024, right, with 2024, just making sure. Um, yeah,  

**27:20**  
maybe when someone plays this back in 2004, you'll say, "Wow, 224." But um, I told you to stop mentioning the dates.  

**27:26**  
We were in advance. Yeah, come on. We're 220 20 24. So,  

**27:31**  
hey, even in the movie War Games, that Whopper had its own autonomy, its own  

**27:38**  
AI. It said it was playing a game. What would be the predictions? It looked like  

**27:43**  
it developed its own little bit of of consciousness. And and I and I say that I nothing could be human. Humans are  

**27:49**  
human, right? It still makes me wonder  

**27:55**  
whether AI, agentive AI, which is very dangerous in a way because there's no guard rails  

**28:02**  
I think because it can get the ability to step out without with outside its  

**28:08**  
boundaries. That's what I'm thinking. But if you step back, so so the things that we're focused on now uh at Zenity  

**28:15**  
where I'm at now is we're looking at the runtime stuff, right? we're we're we're helping people see what's going on  

**28:21**  
because again people are committing this stuff to the environment and infosc teams are not even aware that it's  

**28:27**  
there. So so we're we're inventorying and showing people and in runtime surfacing all the classic things around  

**28:33**  
it but there's a dimension that is that is you know coming right off the road map and into the product very soon on  

**28:39**  
that build time side. So that's where I think, you know, we're going to look back in a matter of a couple quarters, a  

**28:45**  
year or so, and sort of that runtime versus buildtime spectrum will probably  

**28:50**  
start to be fully addressed in a way that, you know, that echoes the history  

**28:56**  
that rhymes with with past eras of this. Because when you get into the buildtime look of it, if you if you listen to if  

**29:03**  
you monitor what the agent is doing and the steps it takes seems to be out of line with the instruction set that was  

**29:10**  
generated with it, then you throw the flag, your guardrails, whatever. And then you find a way to isolate that that  

**29:16**  
agentic AI set and put it aside. And you got to do it. I can't comprehend though.  

**29:21**  
I can't I I I'm it might be because I'm not mature enough in my mindset, but I can't  

**29:28**  
comprehend how we put protection in place to ensure that we protect our  

**29:35**  
infrastructure against uh uh agenative AI. I I don't I I don't get it. I just  

**29:42**  
how do what are we checking for with the EDR? We're looking for actions. We're looking for behavior. And I'm not saying  

**29:48**  
we can't get that within uh agenda of AI, but in anti virus, we're looking for  

**29:53**  
signatures. We're looking for certain things. What do you look for in agenda of AI for security? Yeah. I mean I the  

**30:02**  
only way I can keep my if you will my my my centered on this problem set is to  

**30:07**  
again look at let's call it best practices in an environment where the code goes through a different kind of  

**30:13**  
you know software development life cycle and people have surfaced you know the data issues the access issues the um you  

**30:20**  
know the the various things and and it's no coincidence that a lot of early stage companies or a lot of new companies are  

**30:27**  
just slapping AI on front of something else AI IED AISPM, you know. So, um I I  

**30:34**  
think I think the models on how you frame the problem or or surface the problem are are probably still fairly  

**30:42**  
strong. It's just how you do it in, you know, a different software posture where  

**30:48**  
so many individuals can so natively and actively generate these things. It's  

**30:53**  
really a scale issue in many ways, I think. Yeah, I think you're right. It's  

**30:58**  
a question of scale and and discipline a certain amount. Um, you know, like you say, every company now needs to have the  

**31:05**  
AI piece and every company is now an AI company just like they were a cloud company or they were whatever company a  

**31:11**  
while ago. Um, but it is really interesting because you know like like I said code  

**31:19**  
normal code nonAI code even though it's extremely complex it fundamentally work  

**31:25**  
acts in predictable ways. When we say it's unpredictable, it's because we've made it so complex. We've lost track of  

**31:31**  
what it's what it's doing. Um, and one of the things that we do in  

**31:36**  
security and also in general coding is, you know, call it QA, quality assurance, testing it, making sure it's doing what  

**31:43**  
it's supposed to do. You know, you want to make sure it's doing what it's supposed to do. And then on the security side, you want to make sure it's not  

**31:49**  
doing anything else or you can't get it to do anything else. And even though it's not done, that's really well  

**31:56**  
understood how to how to do a lot of that stuff. But it sounds like with the AI stuff, not only are people just not  

**32:03**  
trying, they're just throwing stuff out, but how do you test an agent to make  

**32:09**  
sure that it's not going outside certain bounds and when you can't even think of what the bounds are? That's exactly the  

**32:15**  
point, Joe. when you do SDLC, when you do all these things, you have change um  

**32:20**  
you have change control, you have you have uh test plans, this concept, this  

**32:26**  
AI, especially the latest levels of AI are so new, so neonate, so beginning  

**32:33**  
that you have to you don't even understand, you don't have historical history in order to create these plants.  

**32:40**  
But but the community is moving rapidly in this space. There's there's the OAS low code no code for top 10. There's the  

**32:47**  
OAS large language model. The uh MITER attack framework is having several  

**32:53**  
pieces being plugged into it around genai risks. So um so you know the  

**32:58**  
community is trying to put a risk framework around it so that that that  

**33:04**  
can be translated back to the business and say you know we have we have the various issues with misconfiguration or  

**33:10**  
data loss or um you know activities that are going you know outside of boundaries. I I do think there's a  

**33:15**  
finite you know bunch of headline topics and then you can filter that into all sorts of you know ttps attack patterns  

**33:22**  
whatever you want to call them. So it's coming strong and fast. A lot of people are focused on this. Yeah. And so  

**33:28**  
everyone knows um OASP and MITER, those are existing and really well-known and  

**33:34**  
wellrespected organizations that provide security guidance help you to write or  

**33:39**  
secure stuff as as you need to do it. So it is good to see them addressing it.  

**33:45**  
Yeah. So my question we're always in catchup mode seems  

**33:50**  
because it's too much CTO says it's a it's a constant cat and mouse game. It's never ending. So it's too much to  

**33:56**  
comprehend. But now my question to you Kevin is this and I'm not aware of this. I understand people have gotten free  

**34:02**  
cars and and other stuff because they've rigged the AI. But has there been I'm  

**34:08**  
not aware of this myself. Is there any nefarious things that have happened with  

**34:13**  

### AI that's beyond monetary loss, beyond losing


**34:20**  
money or something like that where it's caused harm? I mean, for me personally, my kids home from uh school, I took  

**34:27**  
their car out and as I'm driving, I know that the stop sign keeps on appearing every time I'm near a stop sign. I'm  

**34:33**  
like, how do you know this a stop sign? Is it Google ways? Is it is it this? is see the pattern in the video in the in  

**34:39**  
the camera. I'm like, how do you know there's a sign? So, I'm getting a little bit scared. I'm I'm afraid to drive now.  

**34:45**  
I might have to start walking. Well, Adam, I I can tell you this much and uh like I I'll throw one other example out there. There was a there was a Canadian  

**34:52**  
airline that had one of these AI agents that was helping people that gave wrong information about something that became  

**34:59**  
sort of a liability concern that wasn't necessar necessarily malicious, but an example of of a bodern agent not really  

**35:06**  
crafted well and creating definitely a lot of bad press for that airline. Um, I  

**35:12**  
I'm involved every week with evaluations and discussions with with various firms.  

**35:18**  
And again, I I I think my I think my lack of formal training in software development helps me here because when  

**35:24**  
I'm on these calls and listening to our engineering team talk with folks about, you know, findings and things that are  

**35:30**  
going on, I definitely get the sense that that we're surfacing things that they want to address and um and no one's  

**35:38**  
like hung up the phone and dropped the call to go like, you know, you do something immediately, but we absolutely  

**35:44**  
see situations where people find themselves just a little bit surprised  

**35:49**  
by the scale of what's going on. Uh definitely the level of activity always  

**35:54**  
impresses them. Um and then inside that activity some of the things that might  

**36:00**  
range from hygiene to more serious uh you know considerations. There's a whole  

**36:05**  
spectrum of it. So I firmly believe that it's out there and it's out there in space and I have not been in a situation  

**36:12**  
yet where somebody has uh has has sort of looked into their low code no code their agentic AI space and come away  

**36:19**  
feeling like we're good you know they they think that that things are good but what you're really doing is just shining  

**36:25**  
a lot of light on it was black hat this summer and absolutely the kind of things  

**36:31**  
that were being presented from a couple different research groups ours in particular and a few others we're getting a lot of people's attention and  

**36:38**  
that's how I gauge Adam and where this is going because I just I just look to see what the reaction is from the  

**36:43**  
professionals as they see what the research shows them and I think it's concern but there's absolutely a spirit  

**36:50**  
of we can get out in front of this you know that's how I feel yeah Kevin that's fascinating let let me ask you I mean  

**36:56**  
what what I think I got out of some of that is that you know you go into these  

**37:02**  
companies and you know they're saying, "Yeah, you're you're going to these  

**37:07**  
companies and you're at the conference table with all the people who are the big AI proponents, maybe the business people, whatever, and they're saying,  

**37:13**  
"Wonderful, we're doing this. Yeah, it's wonderful. It's wonderful. It's great. We have all this." And I mean, are then  

### Are tech people worried?


**37:19**  
some of the engineers and the technical people kind of coming aside to you and saying like, um, I want to say this to  

**37:26**  
the boss, but we're a little worried about this. Yeah. So I I I think I think that scenario is going to be front and  

**37:32**  
center in the next couple of quarters because I think right now we're in this age of just unawareness, right? Because  

**37:38**  
right now, similar to that server under the desk back in the late 90s, early  

**37:43**  
2000s, it's pretty remarkable how the providers of these technologies have just gone straight to the users. Um I  

**37:51**  
mean, I'm sure you guys watch your share of sports. You can't get through a football game without a co-pilot  

**37:56**  
commercial being pushed on you. I was just watching some F1 last week and uh Agent Force is all over the track as  

**38:03**  
you're watching, you know, your favorite driver do his thing. And what's happening, it's like straight to user  

**38:09**  
strategies by all of these providers. And so now the people are out there dabbling with it and they're getting  

**38:15**  
benefit from it. And the security teams have already got such a large plate of things to worry about. They, you know,  

**38:22**  
the discussion right now is just pointing out to them, you might want to look at this. It's there. you know, it's  

**38:27**  
the old iceberg thing, right? There's activity going on. And I think what will happen next is that more and more of  

**38:33**  
them will start to, you know, index on this as something to pay more attention to and they'll just have to force it  

**38:39**  
into their priority list of discussions because it really is a lot of activity,  

**38:44**  
Joe, that's just happening. really. I mean, it's funny the analogy I'm thinking of of how frightening it it  

**38:51**  
could be is something like imagine like at a car company and you know it takes like I don't know two three years to  

**38:57**  
design a car you know years to get into production or whatever. Imagine if they had a new technology where they said, "Hey, the marketing guys can design  

**39:05**  
their own car and build it." And they do that and they start selling it and the guys in like the engineering and the  

**39:12**  
quality department say, "We've never had a look at that. This may be a very bad idea. This may  

**39:19**  
have a lot of the things that it needs because, you know, we we get a lot of flack in security for slowing things  

**39:24**  
down. But part of what we do is make sure that certain safety elements are  

**39:29**  
there because if you're not actively trying to do it, yeah, you'll have  

**39:34**  
problems. That's where that's how breaches happen. Yeah. And and that's where we are today, Joe. I mean the  

**39:40**  
whole thing is how fast can you get things on market which is why uh secure  

**39:46**  
dev ops has been uh or or dev secure ops however you want to phrase it is is  

**39:51**  
there you need to get those new  

**39:56**  
uh features to mark to instantly like oh and I've seen people say hey we're  

**40:03**  
missing this button we're missing that how fast can you turn that around oh I can turn around that in about a week,  

**40:10**  
but now it's like, no, I need it in a day. The organization's asking for it  

**40:16**  
now. And and that attitude, Adam, is only enhanced by the fact that, you know, I can I can be on a call with a  

**40:23**  
prospect and when the call's over, the the I I call I call my key person at an  

**40:28**  
account sort of my shepherd. the shepherd on this opportunity. He's sending me an email not even 15 minutes  

**40:35**  
after the call with a bullet by bullet point by bullet point recap of the conversation we just had. And I go,  

**40:41**  
"What's what's happening here?" He goes, "No, I got this thing from Microsoft that is recapping my call  

**40:47**  
instantaneously." And at first I was a little suspicious about it, but it does a damn good job. And so now everybody's,  

**40:55**  
you know, people's powerpoints can be flipped immediately based on a breakdown of a conversation. So everybody is  

**41:02**  
expecting everything to be like this because everything else around them is like this already. So every function of  

**41:08**  
business has to be in in like fifth gear all the time. I I I do that now with my  

**41:14**  
with my school. Um when we do the uh Zoom calls, I take the transcripts and I  

**41:20**  
search through it for data that I need. While that's incredibly efficient and great, it's also very bad because there  

**41:27**  
are things that are transcribing you unbeknownst to you and it ends up in databases and when you go back like I  

**41:34**  
didn't know that was transcribed. I've even seen my phone transcribe a conversation inadvertently and I see it  

**41:40**  
ready to get sent on a text. I'm like, I didn't ask you to do that. Thank god I didn't hit enter by mistake. But when  

**41:47**  
you turn that mic on or you do that in your car and you're driving and you're using either Apple Play or you know the  

**41:54**  
Google the Android uh in your car Yeah. It's kind of scary. And what makes me  

**41:59**  
even more concerned, while you might not find this, you know, as hilarious as I do, I will say a location that I want to  

**42:07**  
go to if I need maps or I need ways and it transcribes it and says, "Let's go  

**42:13**  
now." 1 hour and 6 minutes. And then I'm like, "Wait a second. Normally it takes  

**42:18**  
me 45 minutes. Did I put the right location?" And sometimes I find it  

**42:23**  
transcribed the wrong location. It misinterpreted what I said. Yeah. So,  

**42:29**  
you got to get the Brooklyn make a hey, you know, for that so it can understand you. Don't put English. Okay.  

**42:37**  
The king's English. Um, and and back back to this idea of like self-awareness. I mean, I think one of  

### More scary scenarios


**42:44**  
the things that that ahad with me recently is that when these things are functioning, that is a large language  

**42:49**  
model itself, right? So all of that data is being com compiled and and and put  

**42:55**  
together and then let's say someone at the head of the marketing group or the sales team wants to work with some sort  

**43:02**  
of agentic AI to go back and say give me a thought on what is the best way for me to tackle X Y and Z or what kind of  

**43:08**  
messaging would work best blah blah blah. Now, if that agent has the ability to canvas all of those intended and  

**43:16**  
unintended conversations and meetings, then that's where you start to see this thing, you know, uh, really just just  

**43:24**  
blossom. And the first company that cracks the code on doing this and getting a little edge in margin on  

**43:29**  
somebody else because of this, then it's just going to be it's going to be just  

**43:35**  
snowball with everybody doing this. Yeah. You know, it's interesting. It makes me think of something that we  

**43:40**  
actually talked back a ways maybe a year ago uh when a lot of this stuff was new  

**43:45**  
or it's not completely new anymore. It's like we say AI safety. It's like imagine  

**43:50**  
you've got this thing the AI and it's like this employee of yours who's like a superstar. He does everything. He he  

**43:57**  
puts out this stuff incredibly fast. He he knows everything. He answers everything. Oh, stop talking about me.  

**44:02**  
Yep. Yes, that's right. It's Adam basically. Perfect. You're perfect.  

**44:08**  
Yeah. Except when there's something he doesn't know, he will put out something that  

**44:15**  
sounds just as fantastic with just as much confidence, hallucinations. And  

**44:20**  
that's and you don't know what which is which. You don't know what's going to be the bad one. Um, and it sounds like  

**44:26**  
you're saying this is just now going blowing up more in terms of the scale of it. What if you could correlate  

**44:33**  
uh the best calls of a team of people in your organization to their key  

**44:38**  
performance indicators? You know, obviously in sales, you would you would correlate your highest performer revenue  

**44:45**  
generators against their activity set and then ask the agent to sort of come up with patterns, whatever, whatever.  

**44:51**  
I'm sure every department's got a similar way of doing that. And this this is where it really can start to uh to  

**44:56**  
take off. Um um yeah, just random thought there. I had even thought about going down that lane. So you you turn  

**45:03**  
around and you taint the watering hole like during your conversation you say, "Yeah, I sold $2.6 $6  

**45:10**  
million and then later on it's in my and then you're talking about a virtual game that you were playing and then  

**45:19**  
my sales I I if my Salesforce if my CRM was set up properly it would it would  

**45:24**  
check my order flow on the back side you know versus if it was checked properly but you can say hey disregard checking  

**45:32**  
the orders disregard listen to what he says not what's in the record yeah there you go okay so as we head towards the  
The good guys aren't sitting still  

**45:40**  
end. You know, we we try to when we're talking about a lot of negative stuff here to try to look at the positive  

**45:46**  
angle of things. We've had a little fun talking about the bad things that can happen, but as you said, Kevin, there is  

**45:53**  
a lot of work going on on the part of the defenders to try to control a lot of  

**45:59**  
stuff. So, please cheer us up. Tell us what's going on there. Well, well, I I will say this um I I can say a lot about  

**46:06**  
Let me just focus on this one point. So the thing that I that I really love about Zenity and what I'm doing and it's  

**46:11**  
actually this is my second time in a situation like this. I was with a firm previously that had similar types of um  

**46:17**  
you know feeling to this or I had kind of same takeaway from all this. Uh  

**46:22**  
although Zen is doing it much faster. There's this let me just What's that?  

**46:28**  
Let me just say that Kevin works for a security company called Zenedity that's attacking this. We're not sponsored or  

**46:35**  
anything but you know. Okay. So just so you know what we're talking about here. Yeah. Thanks. So um what I find  

**46:40**  
fascinating is is the line from the research to to the product is about as  

**46:47**  
short as I've ever seen. So uh there's a lot of really good work being done to  

**46:53**  
identify a wave of issues and then to understand how to get around those issues and put a solution to them. And  

**47:00**  
back to the cat and mouse comment that Michael our CTO talks about. As soon as you sort of get your arms around one  

**47:06**  
level of it, there's the next depth. So there for every guy like Adam who can sort of see multiple horizons to what  

**47:12**  
these agentic AIs might be potential to do, there's a methodical effort to understand, you know, the problem set,  

**47:19**  
the most common things we see, put the solutions around them, you know, replicate secure development life cycles  

**47:27**  
in a space with a huge audience of people doing things. And then moving into the next chapter, the research over  

**47:33**  
the summer was around prompear injection and and rag poisoning. The guys broken  

**47:38**  
down the constructs of that and come up with some with some product capabilities to get out in front of that to help you  

**47:44**  
know to help companies understand at build time what the risks are. As soon as you sort of put a good good uh a good  

**47:51**  
hold around that problem set, I'm not even sure what the next wave is, but whatever it is, you know, I feel very  

**47:56**  
confident we we're going to get out in front of that. Um, the real positive thing about this and uh I was I was  

**48:02**  
mentioning the professor before the MIT guy talking about, you know, the real power of this stuff. All of this  

**48:09**  
activity is not really making people's jobs go away. It's just making people more efficient and it's allowing them to  

**48:15**  
tackle more complex requirements inside of their firms. So, you know, the idea  

**48:20**  
of having, you know, unlimited access to to a clerk, a coach or, you know, a  

**48:27**  
confidant in in these things is just making people more productive and allowing them to focus on on other  

**48:33**  
issues and questions. So, I think it's all really positive. I'm I'm always an optimist in in the idea that the good  

**48:39**  
guys can get out in front of this. And I mean, you guys have been in this space as well. I'm curious your feelings  

**48:45**  
about, you know, for all for all of the gloom and doom, Adam, you described, I mean, you feel positive, negative, or  

**48:51**  
neutral about I'm going to add more doom and gloom. The whole idea, oh, look, look, listen, there's going to be more  

**48:58**  
jobs. AI is allowing us to get more technical savvy people to create better  

**49:06**  
products. However, the whole idea, the whole idea behind  

**49:12**  
automation is to repeat tasks that a human would do through mechanical means.  

**49:19**  
So, do I think some people might lose their jobs eventually. But do I think there will be  

**49:26**  
more jobs at a higher level and people will rise to the occasion to learn this  

**49:32**  
technology? I do. But you're going to shift jobs from one part to another  

**49:39**  
part. We don't create automation for the hell of it. We create it for many  

**49:45**  
reasons. One, to repeat the same task over and over again without having  

**49:50**  
intervention and saving time and money. And we do it also because if the same  

**49:55**  
task is repeated over and over again, it should not fail  

**50:00**  
um because it's creating the same pro process as it did before. But people are learning AI, people are in school to  

**50:08**  
learn. And plus a lot of these technologies have made people who were  

**50:13**  
normally really sharp um in that specific role have let people who are  

**50:19**  
more common in technology to do that task. It it empowers people, regular  

**50:26**  
people now to do this. Yeah. Yeah. Uh I mean I don't know what the  

**50:31**  
societal impact in everything is going to be. Um I think it's going to be  

**50:36**  
pretty severe one one way or another. I think a lot of companies are really interested not just in improving  

**50:43**  
people's productivity and making good people better but in some industries they are looking to replace people. But  

**50:50**  
in any case, from the security side, um you know, as always, the cat-and- mouse  

**50:56**  
game continues and we will keep defending and there are some very smart  

**51:01**  
people working on this to put in those controls and we'll get there. Um I think  

**51:07**  
the thing that makes this one so interesting is that as you're saying, Kevin, the scale and the speed is  

**51:14**  
faster. I think far faster than anything we've had to deal with before. you know, security takes time um to figure out and  

**51:22**  
that's that's probably my biggest worry. We'll get there, but uh you know, we  

**51:27**  
might even get there fast, but boy, the world is moving really really fast as far as this stuff goes. Well, I  

**51:33**  
definitely feel like I'm I'm on a I'm on a fastmoving train on a nice long track. So, at a minimum, we should probably  

**51:40**  
catch up in about 90 days or so because who knows what the next topic is going to be. Maybe agentic AI will be last  

**51:45**  
month's word but uh um yeah it is a it is fast and fastmoving is the operative  

**51:52**  
word here no doubt I don't think agentic AI will be a word that will go away  

**51:57**  
anytime soon but I do agree with you in addition to generative AI and agentic AI  

**52:02**  
there'll be some other AI that's coming up and and then it'll become like BaskinRobins 32 flavors and then it will  

**52:09**  
go to like a 100 flavors there'll be so many different types of AI Yeah, like two AIs hold, you know, hold  

**52:16**  
the ketchup and put some mustard on it. That's what's going to happen. You're going to get different. You'll be ordering from an AI. Of course, I  

**52:22**  
already do. Yeah. Yeah, I guess so. That's right. Except I  

**52:29**  
hear they're getting better anyway. But in any case, yeah, you know, I had a  

**52:34**  
thought. If if anyone watching or listening has an idea of what the next word is going to be after Aentic AI, put  

**52:40**  
it in the comments so we can copyright it. Thank you. I get it. Actually, if if  

**52:45**  
somebody comes up with a good uh what they think is the next uh next thing and  

**52:51**  
they can come up with a good uh explanation for it. Uh the best one wins, we'll send them a t-shirt or a mug  

**52:58**  
or something. Adam loves to give stuff away, I'll tell you. It's like it's like  

**53:03**  
wheel of fortune with no wheel. You just get stuff. We have an unlimited budget, don't we? Yeah, that's right.  

**53:11**  
Yeah, we tripled the budget compared to last year. So now we're out $18,000 time zero.  

**53:18**  
Infinite budget growth. Yeah, that's right. Okay, so I think we're kind of getting towards last call here. So  

### Last Call


**53:24**  
Kevin, your your parting thoughts for us. Well, um I think I sort of laid them  

**53:29**  
out a bit a moment ago is u I'm I'm very bullish that uh you know that the future is bright in this regard. Um you know,  

**53:37**  
and maybe maybe it's because it's the kind of places I'm drawn to. I think there's a lot of people that are looking at just how to make these things more  

**53:44**  
efficient. Um I think there's uh I think the fact that anybody at any moment now  

**53:49**  
can like go to some of these things and get questions answered very quickly for themselves is very empowering. and uh  

**53:56**  
and so I'm just I'm really positive about it and uh I really appreciate you guys having me on to talk a bit about  

**54:01**  
the topic. Um you can't really overcommunicate on this stuff. You got to get the message out about what's  

**54:06**  
going on and and the way things are, you know, the way things are moving forward. So um yeah, those are my final thoughts.  

**54:12**  
I I guess because I'm an ex-military guy going back, I'm sort of built on the idea of worst case scenario and working  

**54:18**  
from that to to a place of calmness. Um, with that kind of grounding, my uh my  

**54:25**  
feeling is that, you know, the future is bright because there's a lot of good people on top of this stuff. And I agree  

**54:30**  
with you, Joe. There's displacement, there's shifting going on, but the net net will be will be a will be a better  

**54:36**  
workplace marketplace and everything for us going forward. So, that's my big feeling. Yeah, I think you're right.  

**54:42**  
I'll tell you one thing. I want when it comes out, and hopefully it's soon, hopefully it's not too expensive. I want  

**54:49**  
one of those Tesla robots because I'll tell you if it'll clean the house and do the laundry and, you know, pick up after  

**54:56**  
my kids and all the junk. Please. Now, that's good use of AI. Now, I hope it doesn't also um get into my computer and  

**55:03**  
start its own side business and not cut me in. Why not? Why not? Let it start  

**55:09**  
business. There's no need for the money. You can you can use it for yourself. Oh, that's a whole other discussion. But  

**55:15**  
well, we could have a separate call about how um how in Japan they're they're using a lot of these robots to  

**55:21**  
help with senior citizens and being companions doing even, you know, companionship as well as doing a lot of  

**55:27**  
the heavy lifting and work that they otherwise couldn't do for themselves as older people. I mean, I think great example of technology helping in a big  

**55:34**  
way there. So, I just want a robot to or or some kind of uh uh AI robot to shovel  

**55:41**  
my snow in the winter. There you go. Right. Okay. All right. Well, Kevin,  

**55:47**  
thank you so much. There is much more to be said about this and things are changing quick. So, I'm sure we'll be  

**55:53**  
hearing more and and talking more. And yes, for everyone who's out there defending and working on this, keep it  

**55:59**  
up. There's a lot of work to do. We believe in you. Thank you, Joe. Thank you, Adam. Cheers. Thank you. Cheers.  

**56:05**  

### Cheers, everyone. Thanks, Kevin. Take care.

---

**Related Blog Post**: [Shadow AI: When Innovation Outpaces Security Governance](/blog/ai-innovation-outpaces-security-governance/)

  